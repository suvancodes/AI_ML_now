# exception handling-> Exception handling in Python allows you to handle errors gracefully and take corrective actions without
# stopping the execution of the program.

# exception-> Exception handling in Python allows you to handle errors gracefully and take corrective actions without
# stopping the execution of the program.

# common exception->
# 1.zero division error.
# 2.file not find error
# 3. value error 
# 4. type error

# example -> 1. -> name error

# try:
#     # write block of code 
#     a=b
# except:
#     print('variable is not been asigned')

# it write error as it is. 

# try:
#     # write block of code 
#     a=b
# except NameError as ex:
#     print(ex)


# example->2   ZeroDivisionError

# try:
#     res = 1/0
# except ZeroDivisionError as ex:
#     print(ex)


# example 3-> prant of all error 

# try:
#     rs = 1/2
#     a=b
# except ZeroDivisionError as ex:
#     print(ex)
# except Exception as ex:             # we should use this as a last exception block
#     # this is the prant of all error  
#     print(ex)

# example->3

# try:
#     num = int(input("enter number->"))
#     rs = 10/num
#     print(rs)
# except ValueError as v:
#     print(v)
#     print('it is not a valid number')
# except ZeroDivisionError as z:
#     print(z)
#     print("you can't enter 0")
# except Exception as ex:
#     print(ex)


# use of else block 
    
# try:
#     num = int(input("enter number->"))
#     rs = 10/num
# except ValueError as v:
#     print(v)
#     print('it is not a valid number')
# except ZeroDivisionError as z:
#     print(z)
#     print("you can't enter 0")
# except Exception as ex:
#     print(ex)
# else:
#     # if no exception will came then this will run 
#     print(rs)


# finally -> the error came or not it will be run 

# try:
#     num = int(input("enter number->"))
#     rs = 10/num
# except ValueError as v:
#     print(v)
#     print('it is not a valid number')
# except ZeroDivisionError as z:
#     print(z)
#     print("you can't enter 0")
# except Exception as ex:
#     print(ex)
# else:
#     # if no exception will came then this will run 
#     print(rs)
# finally:
#     print('hey')


# file handling and exception 

# try:
#     file = open('example.txt','r')
#     content = file.read()
#     print(content)
# except Exception as ex:
#     print(ex)
# finally:
#     if 'file' in locals() or not file.closed():
#         file.close()
#         print('file closed')
    
    
    
                        # all error -> https://chatgpt.com/share/68827eda-e3f4-8013-b737-1dbb97cf7b10