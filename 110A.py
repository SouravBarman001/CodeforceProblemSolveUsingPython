
userInput = input()
count = 0
for i in userInput:

    if i == '4' or i == '7':
        count +=1
    else:
        pass

if count == 4 or count == 7:
    print("YES")
else:
    print("NO")
