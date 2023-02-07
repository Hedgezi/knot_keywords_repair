def findKeywordsTag(filename):
    with open(filename, 'r') as f:
        for line in f:
            if '<keywords>' in line.strip(' \t\n'):
                if '</keywords>' in line.strip(' \t\n'):
                    return False
                alltags = []
                nextline = f.readline().strip(' \t\n')
                while nextline != '</keywords>':
                    alltags.append(nextline)
                    nextline = f.readline().strip(' \t\n')
                return [keyword.removeprefix('<term>').removesuffix('</term>') for keyword in alltags]
    return False

def deleteHyphen(keywords):
    keywords[0] = keywords[0].removeprefix('-').removeprefix('—')

def wordKeywordsRemainCase(keywords: list[str]) -> list[str]:
    for kwnum, keyword in enumerate(keywords):
        if keyword.lower().find('keywords:') != -1: # case, where it wrongly parsed and there is word Keywords after which written all keywords; maybe try a 'keyword' pattern to find?
            onlykeywordslist = keywords[kwnum:]
            onlykeywordslist[0] = onlykeywordslist[0][onlykeywordslist[0].lower().find('keywords:')+10:]
            trueterms = []
            for wnum, word in enumerate(onlykeywordslist):
                while onlykeywordslist[wnum].find(',') != -1:
                    trueterms.append(onlykeywordslist[wnum][:onlykeywordslist[wnum].find(',')])
                    onlykeywordslist[wnum] = onlykeywordslist[wnum][onlykeywordslist[wnum].find(',')+1:].lstrip() # cut off term that we already added to trueterms
                if word[-1].rstrip == ',':
                    trueterms.append(onlykeywordslist[wnum][:-1])
                elif word[-1] == '-':
                    onlykeywordslist[wnum+1] = onlykeywordslist[wnum][:-1] + onlykeywordslist[wnum+1]
                else:
                    if len(onlykeywordslist) == wnum+1:
                        trueterms.append(onlykeywordslist[wnum])
                    else:
                        onlykeywordslist[wnum+1] = '{0} {1}'.format(onlykeywordslist[wnum][:].rstrip(), onlykeywordslist[wnum+1])
            return trueterms
    return False

print(findKeywordsTag('file1.xml'))
print(wordKeywordsRemainCase(findKeywordsTag('file1.xml')))