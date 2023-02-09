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
        if allterms[-1][-1].rstrip == ',': # example: 18933.tei.xml in folder 2
            trueterms.append(allterms[-1])
        elif allterms[-1][-1] == '-': # example: 260371.tei.xml in folder 2
            keywords[wnum+1] = allterms[-1][:-1] + keywords[wnum+1]
        else: # example: 1337244.tei.xml or 260347.tei.xml in folder 2
            trueterms.append(allterms[-1])
    return trueterms

def deleteHyphen(keywords: list[str]) -> list[str]:
    keywords[0] = keywords[0].lstrip(' —-')

def deleteAmps(keywords: list[str]) -> list[str]:
    for kwnum, keyword in enumerate(keywords):
        if keyword.find('&apos;') != -1:
            keywords[kwnum] = keyword.replace('&apos;', '')

def oneNumberRemainCase(keywords: list[str]) -> list[str]: # example: 260404.tei.xml in folder 2
    for kwnum, keyword in enumerate(keywords):
        if keyword.isnumeric():
            onlykeywordslist = keywords[:kwnum]
            return keywordsDividedByCommas(onlykeywordslist)
    return False

def randomLettersWasIncluded(keywords: list[str]) -> list[str]: # example: 260882.tei.xml in folder 2
    for kwnum, keyword in enumerate(keywords):
        if len(keywords) <= 2:
            onlykeywordslist = keywords[:kwnum]
            return keywordsDividedByCommas(onlykeywordslist)
    return False

def otherColonWasIncludedCase(keywords: list[str]) -> list[str]: # as in 260105.tei.xml and 260347.tei.xml in folder 2
    for kwnum, keyword in enumerate(keywords): # think i can't fix those keywords, so i'll better just tell that they are wrong
        if keyword.find(':') != -1:
            return True
    return False

def wordKeywordsRemainCase(keywords: list[str]) -> list[str]:
    for kwnum, keyword in enumerate(keywords):
        if keyword.lower().find('keywords:') != -1: # case, where it wrongly parsed and there is word Keywords after which written all keywords; maybe try a 'keyword' pattern to find?
            onlykeywordslist = keywords[kwnum:]
            onlykeywordslist[0] = onlykeywordslist[0][onlykeywordslist[0].lower().find('keywords:')+10:]
            return keywordsDividedByCommas(onlykeywordslist)
    return False

def checkCycle(keywords: list[str]) -> list[str]: # order is important
    if wordKeywordsRemainCase(keywords) != False:
        return wordKeywordsRemainCase(keywords)
    elif oneNumberRemainCase(keywords) != False:
        return oneNumberRemainCase(keywords)
    elif randomLettersWasIncluded(keywords) != False:
        return randomLettersWasIncluded(keywords)
    elif otherColonWasIncludedCase(keywords) != False:
        return otherColonWasIncludedCase(keywords)
    else:
        return keywordsDividedByCommas(keywords)

if __name__ == '__main__':
    keywords = extractKeywordsAsList("1337244.tei.xml", PREFIX)
    print(checkCycle(keywords))