# palindrome checker: verify a string is the same spelled frontwards and backwards
# extra comment added for class demonstration
from string import punctuation

word = input("Input a word to see if it's a palindrome: ").lower().replace(" ", "")
for i in punctuation:
    word = word.replace(i, "")

count_beginning = 0
count_ending = -1

a = word[count_beginning]
b = word[count_ending]
s = len(word)

for letter in word:
    if a == b:
        count_beginning += 1
        count_ending -= 1
        if s == count_beginning:
            print("Yes, that is a palindrome")
            break
        a = word[count_beginning]
        b = word[count_ending]
    else:
        print("No, that is not a palindrome.")
        break

