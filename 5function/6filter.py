# FILTER() FUNCTION -> filter function construct an iterator form elements of an iterable for which a function return true .it is used filer out item form a list
 
# filter take a functino and a list it filter element accoding to the given function condition 

# Example 1 print even number

# def even(x):
#     if(x%2==0):
#         return True
# lst =[1,2,3,4,5,6,7,8,10,111,112,9,222]
# even = list(filter(even ,lst))
# print(even)

# Example-2 print number even and greater then 5 using lambda function

# lis = [1,2,3,4,5,6,7,8,9]
# print(list(filter(lambda x:x>5 and x%2==0,lis)))

# filter in dict
# ckack age is 18+ or not

people = [{'name':'subho','age':19,},{'name':'susmita','age':38,}]
def age_find(persion):
    return persion['age']>18

print(list(filter(age_find,people)))
    