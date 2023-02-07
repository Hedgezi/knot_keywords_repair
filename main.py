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

def deletehyphen(keywords):
    keywords[0] = keywords[0].removeprefix('-').removeprefix('—')

# case, where some terms are numbers
def case1(keywords):
    for linenum, line in enumerate(keywords):


    

print(findKeywordsTag('file1.xml'))
print(case1(findKeywordsTag('file1.xml')))