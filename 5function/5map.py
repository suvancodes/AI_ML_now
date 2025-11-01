# MAP FUNCTION IN PYTHON -> the map function applied a given function to all in an input list(or any other iterable ) and return a map object 

# map  take a function and a list then it call the function and work for it 

# SYNTAX-> map(function_name,list_name)

# Example

# def squre(x):
#     return x*x
# lis = [1,2,3,4,5]
# print(list(map(squre,lis)))



# map using lambda function

# example

# num = [1,2,3,4,5,6]
# print(list(map(lambda x: x*x,num)))


# map with multipal iterable

# num1 = [1,2,2,3]
# num2 = [1,2,3,4]
# print(list(map(lambda x,y:x+y,num1,num2)))

#more example 

# Example 1 -> convart str to int and print using map

# st = ['1','2','3','4']
# int_num = list(map(int,st))
# list(map(print,int_num))

# Example->2 lower case to upper case

# word=["apple","subho","dustu"]
# upper = list(map(str. upper,word))
# print(upper)

# Example-3 list of dict

# def get_name(persion):
#     return persion['name']

# people = [{'name':'subho','age':19,},{'name':'susmita','age':38,}]
# name = list(map(get_name,people))
# print(name)

