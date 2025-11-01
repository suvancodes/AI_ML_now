        ## swap two number with out a third variable
        
# def swap(a,b):
#     a=a+b
#     b = a - b
#     a = a - b
#     return(a,b)

# a=10
# b=20
# print(a,b)
# a,b = swap(a,b)
# print(a,b)

#smallest btw 3 number

# a= input("enter 1st") 
# b=input("enter 2nd") 
# c= input("enter 3rd") 
# if(a<b and a<c):
#     print(a)
# elif(b<a and b<c):
#     print(b)
# else:
#     print(c)



        # reverse number
        
# a = 123
# ans =0
# while(a>0):
#     dig = a%10
#     ans = ans*10+dig
#     a=a//10
# print(ans)

            # invart traingle
            
            
# n = int(input("enter n "))
# for i in range(0,n,1):
#     for j in range(n-i,0,-1):
#         print("*",end=" ")
#     print()


            #palidrom

# def ispal(str):
#     n = len(str)
#     for i in range(0,len(str)//2,1):
#         if(str[i]!=str[n-i-1]):
#             return False
#     return True

# str="racecar"
# if(ispal(str)):
#     print("true")
# else:
#     print("false")
    
    # reversed a string
    
# str = "subho"
# n = len(str)
# r=""
# for i in range(n-1,-1,-1):
#     r+=str[i]
    
# print(r)

            # reverse a list
            
# lst = [1,2,2,4,5]
# n = len(lst)
# st = 0
# end = n-1
# while(st<end):
#     lst[st],lst[end] = lst[end],lst[st]             # swap
#     st+=1
#     end-=1
    
# print(lst)

# rotate a list form 2nd position

# lst = [1,2,3,4]
# st = 1
# n = len(lst)
# end = n - 1

# while(st<end):
#     lst[st],lst[end] = lst[end],lst[st]
#     st+=1
#     end-=1
# print(lst)

# make a list of n number value of n^2

# n = int(input("enter n"))
# lst = [x**2 for x in range(n+1)]
# print(lst)

# string to list

# st = "abcd"
# n = len(st)
# lst=[]
# for i in range(n):
#     lst.append(st[i])
# print(lst)

        # count of vowels
        
# s = input("enter a")
# ct = 0
# for i in range(len(s)):
#     if(s[i]=='a' or s[i]=='e' or s[i]=='o' or s[i]=='u' or s[i]=='i'):
#         ct+=1
# print(ct)

                    # remove all punctuation in a given string

import string

s = input("enter s-> ")
for i in string.punctuation:
    s = s.replace(i, "")
print(s)


