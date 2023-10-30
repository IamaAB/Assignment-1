def anagrams(string1,string2):
    return  sorted(string1) == sorted(string2)


input1= input("Enter String 1 : ")
input2= input("Enter String 2 : ")

result = anagrams(input1,input2)
if result:
    print(f"{input1} and {input2} are anagrams")
else:
    print(f"{input1} and {input2} are not anagrams")