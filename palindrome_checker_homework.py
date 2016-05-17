from string import punctuation

word = input("What is your word or sentence? ").lower().replace(" ", "")

for i in punctuation:
    word = word.replace(i, "")

reverse_word = (word[::-1])

if word == reverse_word:
    print("Yes! That is a palindrome!")
else:
    print("No! That is not a palindrome!")