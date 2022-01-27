from multiprocessing import Pool
from time import perf_counter

def fib(n):
        if n <= 2:
                return 1
        elif n == 0:
                return 0
        else:
                return fib(n-1)+fib(n-2)

if __name__ == '__main__':
        n = 40
        start = perf_counter()
        with Pool(20) as p:
                print(p.map(fib, list(range(n+1))))
        time_full = perf_counter() - start
        print(f"Time work program : {time_full}")
