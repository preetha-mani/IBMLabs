mystr=input(("Enter a String:")) #string input can be directly got
mystr=mystr.casefold() #casefold()-It does not consider whether it is upper or lower case
revstr=reversed(mystr) #recersed()-directly reverse the string
if list(mystr) == list(revstr): #it checks like a list
    print("IT IS A PALINDROME")
else:
    print("IT IS NOT A PALINDROME")