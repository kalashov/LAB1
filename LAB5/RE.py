import re

while True:
    test = int(input("Enter test case number: "))

    if test == 0:
        break

    if(test == 1):
        s1 = input()
        if re.match(r"^ab*$", s1):
            print("Matched")
        else:
            print("Not matched")

    if(test == 2):
        s2 = input()
        if re.match(r"^ab{2,3}$", s2):
            print("Matched")
        else:
            print("Not matched")

    if(test == 3):
        s3 = input()
        if re.match(r"[a-z]+_[a-z]+", s3):
            print("Matched")
        else:
            print("Not matched")

    if(test == 4):
        s4 = input()
        if re.match(r"[A-Z][a-z]+", s4):
            print("Matched")
        else:
            print("Not matched")

    if(test == 5):
        s5 = input()
        if re.match(r"^a.*b$", s5):
            print("Matched")
        else:
            print("Not matched")

    if(test == 6):
        s6 = input()
        print(re.sub(r"[ ,.]", ":", s6))

    if(test == 7):
        s7 = input()
        print("".join(x.title() for x in s7.split("_")))

    if(test == 8):
        s8 = input()
        print(re.split(r"(?=[A-Z])", s8))

    if(test == 9):
        s9 = input()
        print(re.sub(r"(\w)([A-Z])", r"\1 \2", s9))

    if(test == 10):
        s10 = input()
        print(re.sub(r"(?<!^)(?=[A-Z])", "_", s10).lower())

