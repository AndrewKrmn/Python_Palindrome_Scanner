pypok = 1

while pypok == 1:
    print("============================Palindrome scanner==========================")

    sentance = input("Write word :")

    if sentance.lower() == sentance.lower()[::-1]:
        print("This word is a palindrome!")
    else:
        print("This word is not a palindrome!")
