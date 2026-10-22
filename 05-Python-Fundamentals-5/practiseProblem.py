with open("/Users/devanshshah/Developer/PrimeLab/05-Python-Fundamentals-5/sampleTextForPractiseProblem.txt", "r") as f:
    sampleText = f.read()
    print(sampleText)
    print("Enter the word you want to find from sampleTextForPractiseProblem file :")
    searchString = input()
    if(searchString in sampleText):
        print("Word Found!")
    else:
        print("No the word doesnt exist")