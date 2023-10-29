cin = input("Enter a String: ")

count_vowel=0
count_consonant=0

cin = cin.lower()
for letter in cin:
    if letter.isalpha():
        if letter in "aeiou":
            count_vowel +=1
        else:
            count_consonant +=1

print("Total Vowels are: ", count_vowel)
print("Total Consonants are: ", count_consonant)
