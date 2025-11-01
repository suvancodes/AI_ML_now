import multiprocessing
import time

def square():
    for i in range(6):
        time.sleep(2)
        print(f"Square of {i} is {i**2}")

def cube():
    for i in range(6):
        time.sleep(2)
        print(f"Cube of {i} is {i**3}")

if __name__ == '__main__':
    # create two processes
    p1 = multiprocessing.Process(target=square)
    p2 = multiprocessing.Process(target=cube)

    t = time.time()
    
    # start both processes
    p1.start()
    p2.start()

    # wait for both to complete
    p1.join()
    p2.join()

    et = time.time() - t
    print(f"Execution Time: {et:.2f} seconds")

