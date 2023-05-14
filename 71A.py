"""
A. Way Too Long Words
"""

n = int(input())

for i in range(n):

    w = input()
    lowerC = w.lower()
    wordlen = len(lowerC)

    if wordlen <= 10:
        print(lowerC)
    else:
        firstWord = lowerC[0]
        ithWord = wordlen - 2
        lastWord = lowerC[-1]

        print(firstWord, ithWord, lastWord, sep="")
