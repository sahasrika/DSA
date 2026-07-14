print("PALINDROME OR NOT ")
n=1221
nums=n
result=0
while nums>0:
    lastdigit=nums%10
    result=(result*10)+lastdigit
    nums=nums//10
if n==result:
    print("given number is palindrome")
else:
    print("number is non palindrome")