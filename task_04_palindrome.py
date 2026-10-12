Word = input("Enter a word: ")
Word = Word.lower()
if Word == Word[::-1]:
    print(Word, "is a palindrome")
else:
    print(Word, "is not a palindrome")

