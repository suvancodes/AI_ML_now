### multithreading with ThreadPoolExecutor

# from concurrent.futures import ThreadPoolExecutor
# import time

# def printn(num):
#     time.sleep(1)
#     return f"number : {num}"
# number = [1,2,3,4,5,6,7,8,9]
# with ThreadPoolExecutor(max_workers=3) as ex:
#     result = ex.map(printn,number)
    
# for res in result:
#     print(res)


from concurrent.futures import ProcessPoolExecutor
import time

def printn(num):
    time.sleep(1)
    return f"number : {num}"
num = [1,2,3,4,5]
if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as ex:
        result = ex.map(printn,num)
        
    for res in result:
        print(res)
    