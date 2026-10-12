# Lab 6
# นักศึกษา: นายพชรพล ชนะศรี
# รหัสประจำตัว: 6901012610170

i = 0
def A(Word, Check):
    global i
    while i < len(Word):
        if Word[i] == Check:
            print(f"Found '{Check}' at index {i}")
        i += 1

def B(Word, Check):
    global i
    i = len(Word) - 1
    while i >= 0:
        if Word[i] == Check:
            print(f"Found '{Check}' at index {i}")
        i -= 1

def palindrome(Word):
    if Word == Word[::-1]:
        print(f"'{Word}' is a palindrome")
    else:
        print(f"'{Word}' is not a palindrome")

print("  A")
A("Hello World", "o")
print(" ")
print("  B")
B("Hello World", "l")
print(" ")
print(" Palindromes")
palindrome("25/8/52")
palindrome("25/8/58")
print("------------------------------")

def countChar(Word, Check):
    i = 0
    count = 0
    while i < len(Word):
        if Word[i] == Check:
            count += 1
        i += 1
    print(f"Character '{Check}' appears {count} times in '{Word}'")

def countVowels(Word): 
    vowels = "aeiouAEIOU"
    i = 0
    count = 0
    while i < len(Word):
        if Word[i] in vowels:
            count += 1
        i += 1
    print(f"Number of vowels in '{Word}': {count}")

def countWords(Word):
    words = Word.split()
    count = len(words)
    print(f"Number of words in '{Word}': {count}")
    

countChar("Hello World", "l")
countVowels("Hello World")
countWords("Hello World asd asdas ds")

