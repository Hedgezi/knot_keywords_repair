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
        allterms = [i.strip() for i in word.split(',') if i != '']
        trueterms += allterms[:-1]
        # allterms[-1][-1] - last symbol of last word in a row
        if len(allterms) == 0: # example: 6189781.tei.xml
            continue
        elif allterms[-1][-1] == '-': # example: 260371.tei.xml in folder 2
            keywords[wnum+1] = allterms[-1][:-1] + keywords[wnum+1]
        else: # example: 1337244.tei.xml or 260347.tei.xml in folder 2
            trueterms.append(allterms[-1])
    return trueterms

def deleteHyphen(keyword: str) -> str:
    return keyword.lstrip(' —-')

def deleteAmps(keyword: str) -> str:
    return keyword.replace('&apos;', '').replace('&quot;', '').replace('&amp;', '')

def colon_in_keywords(keywords: list[str]) -> list[str]:
    true_terms = []
    for wnum, word in enumerate(keywords[::-1]):
        if word.find(':'):
            true_terms = keywords[:len(keywords)-wnum-2]
    return true_terms

def checkForProblems(keywords: list[str]) -> dict[str, list[int]]:
    problems = {'commas': [], 'keyword_word': [], 'hyphen': [], 'pseudo_ampersand': [], 'one_number': [], 'random_short_letters': [], 'some_colon': []}
    for kwnum, keyword in enumerate(keywords):
        if keyword.find(',') != -1:
            problems['commas'].append(kwnum)
        if keyword.lower().find('keyword:') != -1: # case, where it wrongly parsed and there is word Keywords after which written all keywords; maybe try a 'keyword' pattern to find?
            problems['keyword_word'] = [keyword.lower().find('keyword:')]
        if keyword.find('—') != -1: # it is primarily can be found only in first word, so we can extract this to check only first word
            problems['hyphen'].append(kwnum)
        if keyword.find('&apos;') or keyword.find('&quot;') or keyword.find('&amp;') != -1:
            problems['pseudo_ampersand'].append(kwnum)
        if keyword.isdigit(): # example: 260404.tei.xml in folder 2
            problems['one_number'] = [kwnum]
        if len(keyword) <= 2: # example: 260882.tei.xml in folder 2
            problems['random_short_letters'] = [kwnum]
        if keyword.find(':') != -1: # as in 260105.tei.xml and 260347.tei.xml in folder 2
            problems['some_colon'].append(kwnum) # я могу поставить этот кейс выше, потому что (по идее) если мы итак находим двоеточие (не со словом keywords), то мы сразу бракуем весь документ, следовательно нам и не приходится исследовать его на другие ошибки 
    return problems

def repairPossibleProblems(keywords: list[str], problems: dict[str, list[int]]) -> list[str]:
    # deletion of strange characters is trivial
    if problems['hyphen']:
        for i in problems['hyphen']:
            keywords[i] = deleteHyphen(keywords[i])
    if problems['pseudo_ampersand']:
        for i in problems['pseudo_ampersand']:
            keywords[i] = deleteHyphen(keywords[i])
    # some other easy cases
    if problems['keyword_word']:
        onlykeywordslist = keywords[problems['keyword_word'][0]:]
        onlykeywordslist[0] = onlykeywordslist[0][onlykeywordslist[0].lower().find('keyword:')+9:]
        return keywordsDividedByCommas(onlykeywordslist)
    if problems['one_number']:
        onlykeywordslist = keywords[:problems['one_number'][0]]
        return keywordsDividedByCommas(onlykeywordslist)
    if problems['random_short_letters']:
        onlykeywordslist = keywords[:problems['random_short_letters'][0]]
        return keywordsDividedByCommas(onlykeywordslist)
    if problems['some_colon']:
        onlykeywordslist = colon_in_keywords(keywords)
        return keywordsDividedByCommas(onlykeywordslist)
    return keywords

if __name__ == '__main__':
    keywords = extractKeywordsAsList("1337244.tei.xml", PREFIX)
    allproblems = checkForProblems(keywords)
    print(repairPossibleProblems(keywords, allproblems))