x = str(input("Enter a string : "))
temp = x
rev = x[::-1]

# while(x > 0):
#     digit = x % 10
#     rev = (rev * 10) + digit
#     x = x // 10
    
print("Reversed string is : ",rev)
if(temp == rev):
    print("It's a palindrome string!")
else:
    print("It's not a palindrome string!")