import xml.etree.ElementTree as ET

PREFIX = "{http://www.tei-c.org/ns/1.0}"

def extractKeywordsAsList(filename, PREFIX):
    tree = ET.parse(filename)
    source = tree.getroot()

    profileDesc = source.find(f"{PREFIX}teiHeader/{PREFIX}profileDesc")
    keywordsTag = profileDesc.find(f'{PREFIX}textClass/{PREFIX}keywords')
    keywordsTerms = keywordsTag.findall(f'{PREFIX}term')

    keywords = [i.text for i in keywordsTerms]
    return keywords

def keywordsDividedByCommas(keywords: list[str]) -> list[str]:
    trueterms = []
    for wnum, word in enumerate(keywords):
        allterms = [i.strip() for i in word.split(',') if i != ''] # all words in a row, that was stripped by commas
        trueterms += allterms[:-1]
        # allterms[-1][-1] - last symbol of last word in a row
        if len(allterms) == 0: # example: 6189781.tei.xml
            continue
        elif allterms[-1][-1] == '-': # example: 260371.tei.xml in folder 2, last word is moved to next line
            keywords[wnum+1] = allterms[-1][:-1] + keywords[wnum+1]
        else: # example: 1337244.tei.xml or 260347.tei.xml in folder 2
            trueterms.append(allterms[-1])
    return trueterms

def deleteHyphen(keyword: str) -> str:
    return keyword.lstrip(' —-')

def deleteAmps(keyword: str) -> str:
    return keyword.replace('&apos;', '').replace('&quot;', '').replace('&amp;', '')

def colon_in_keywords(keywords: list[str]) -> list[str]:
    for wnum, word in enumerate(keywords):
        if word.find(':') != -1:
            return keywords[:wnum]
    return keywords

def checkForProblems(keywords: list[str]) -> dict[str, list[int, str]]:
    problems = {'commas': [], 'keyword_word': [], 'hyphen': [], 'pseudo_ampersand': [], 'one_number': [], 'random_short_letters': [], 'some_colon': []}
    keyword_word_variations =  ['keywords', 'keyword', 'key word', 'key-word']
    ampersand_replaced_variations = ['&apos;', '&quot;', '&amp;']

    if keywords[0].find('—') != -1: # it is primarily can be found only in first word, so we can extract this to check only first word
        problems['hyphen'].append(0)

    for kwnum, keyword in enumerate(keywords):
        if keyword.find(',') != -1:
            problems['commas'].append(kwnum)

        for keyvar in keyword_word_variations: # case, where it wrongly parsed and there is word Keywords (or variations) after which written all keywords
            kwindex = keyword.lower().find(keyvar)
            if kwindex != -1:
                problems['keyword_word'] = [kwnum, kwindex, keyvar]
                return problems

        if keyword.find(':') != -1: # as in 260105.tei.xml and 260347.tei.xml in folder 2
            problems['some_colon'].append(kwnum) # я могу поставить этот кейс выше, потому что (по идее) если мы итак находим двоеточие (не со словом keywords), то мы сразу бракуем весь документ, следовательно нам и не приходится исследовать его на другие ошибки 

        for amprep in ampersand_replaced_variations:
            if keyword.find(amprep) != -1:
                problems['pseudo_ampersand'].append([kwnum, amprep])

        if keyword.isdigit(): # example: 260404.tei.xml in folder 2
            problems['one_number'] = [kwnum]
        if len(keyword) <= 2: # example: 260882.tei.xml in folder 2
            problems['random_short_letters'] = [kwnum]
    return problems

def repairPossibleProblems(keywords: list[str], problems: dict[str, list[int]]) -> list[str]:
    # deletion of strange characters is trivial
    if problems['hyphen']:
        for i in problems['hyphen']:
            keywords[i] = deleteHyphen(keywords[i])
    if problems['pseudo_ampersand']:
        for i in problems['pseudo_ampersand']:
            keywords[i[0]] = deleteHyphen(keywords[i])
    # some other easy cases
    if problems['keyword_word']:
        onlykeywordslist = keywords[problems['keyword_word'][0]:]
        onlykeywordslist[0] = onlykeywordslist[0][problems['keyword_word'][1]+len(problems['keyword_word'][2])+1:].lstrip(' :') # +1 is for random s (it find 'keyword' not 'keywords')
        return keywordsDividedByCommas(onlykeywordslist)
    if problems['some_colon']:
        onlykeywordslist = keywords[:problems['some_colon'][0]]
        return keywordsDividedByCommas(onlykeywordslist)
    if problems['one_number']:
        onlykeywordslist = keywords[:problems['one_number'][0]]
        return keywordsDividedByCommas(onlykeywordslist)
    if problems['random_short_letters']:
        onlykeywordslist = keywords[:problems['random_short_letters'][0]]
        return keywordsDividedByCommas(onlykeywordslist)
    return keywords

if __name__ == '__main__':
    keywords = extractKeywordsAsList("examples/1.tei.xml", PREFIX)
    allproblems = checkForProblems(keywords)
    print(repairPossibleProblems(keywords, allproblems))