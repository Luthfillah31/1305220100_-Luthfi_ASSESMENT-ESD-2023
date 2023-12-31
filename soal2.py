def isPalindrome(word):
    word = word.lower()
    return (word == word[::-1])
i = input()
if isPalindrome(i):
    print("eureeka!")
else:
    print("suka blyat")
