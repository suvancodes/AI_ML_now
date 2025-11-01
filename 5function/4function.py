# define a function and calling it

# def x(name):
#     print("hello", name)
#     return name

# x("subho")
# print(x("suvankar"))

            # squre of a number

# def sq(a):
#     return a**2
# print(sq(12))

            
            # max btw two number
            
# def mx(a,b):
#     if(a>b):
#         return a
#     else:
#         return b
# print(mx(12,13))


            # odd or even
            
# def isodd(a):
#     if(a%2==0):
#         return "even"
#     else:
#         return "odd"
# print(isodd(12))

            # power of a number
            
# def power(a,b):
#     return a**b
# print(power(2,2))


            # BMI calculater
            
# def bmi(h,w):
#     return w/(h**2)
# print(bmi(1.62,50))

            #factorial of a number 
            
# def fact(a):
#     fact =1
#     for i in range(1,a+1):
#         fact *= i
#     return fact
# print(fact(5))


                # chack a number prime of not 
                
# def isprime(a):
#     for i in range(2,a):
#         if(a%i != 0):
#             return True
#         return False
# print(isprime(3))

                # 
                    # *arg -> it take multipale value as a tuple
                                       
# def a(*arg):
#     return sum(arg)

# arg = (1,2,3)
# print(a(*arg))

                    # **kwarg -> it take a value as a dictionary 
             
# def a(**arg):
#     return arg

# arg = {
#     "name" : "subho",
#     "age":19,
# }
# print (a(**arg))


                # LAMBDA function 
                
                # suure of two using lambda function
                
# squar = lambda x:x*x
# print(squar(2))

                # cube of a number 
                
# cube = lambda x:x**3
# print(cube(3))

            # squre of each term in am list
            
# sq = lambda x:x**2
# l = [1,2,3,4,5]
# for i in range(5):
#     l[i] = sq(l[i])
# print(l)

                # recursion 
                
                # factorial of a number

# def fect(a):
#     if(a == 0):
#         return 1

#     return a*fect(a-1)
# print(fect(5))

            # product of a array except it self
            
# arr=[1,2,3,4,5]
# mul=1
# for i in range(5):
#     mul*=arr[i]
# for i in range(5):
#     ans = mul//arr[i]
#     arr[i]=ans
# print(arr)





