def checkPaliandrome(word):

    if word == word[::-1]:
        print(f"{word} is paliandrome")
    else:
        print(f"{word} is not a paliandrome")
       

word =input("enter the word")
checkPaliandrome(word)