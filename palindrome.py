def isPalindrome(word):
    word = word.lower()
    for index in range(len(word)//2):
        if(word[index] != word[len(word)-index - 1]):
            return False
    return True


word = input("Worteingabe: ")
palindromeBool = isPalindrome(word)

if(palindromeBool):
    print(word + " ist ein Palindrom")

else:
    print(word + " ist kein Palindrom")