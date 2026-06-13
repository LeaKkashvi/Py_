# Number palindrom or not with a list using while loop
L=[123,222,343,3432]
i=0
while i<len(L):
    num=L[i]
    temp=num
    r=0
    while temp>0:
        d=temp%10
        r=r*10+d
        temp=temp//10
    if num==r:
        print(num,"is a palindrome")
    else:
        print(num,"is not a palindrome")
    i+=1

