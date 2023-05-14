year = int(input())

while True:
    year += 1

    a = int(year / 1000)  # 1st
    b = int(year / 100 % 10)  # 2nd
    c = int(year / 10 % 10)  # 3rd
    d = int(year % 10)  # 4th

    if a != b and a != c and a != d and b != c and b != d and c != d:
        print(year)
        break
