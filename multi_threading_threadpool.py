from concurrent.futures import ThreadPoolExecutor
from time import sleep


def worker(num):
    print(f"calculating the {num}")
    sleep(1)
    return num**2



pool=ThreadPoolExecutor(max_workers=6)

work1=pool.submit(worker,5)

work2=pool.submit(worker,101)

work3=pool.submit(worker,5)

work4=pool.submit(worker,101)
work5=pool.submit(worker,5)

work6=pool.submit(worker,101)

work7=pool.submit(worker,5)

work8=pool.submit(worker,101)


pool.shutdown()

work6=pool.submit(worker,800)