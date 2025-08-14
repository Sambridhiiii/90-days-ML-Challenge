from multiprocessing import Process
import time

def cpu_bound_task():
    x = 0
    for _ in range(10**7):
        x += 1

if __name__ == "__main__":
    start = time.time()

    processes = []
    for _ in range(2):
        p = Process(target=cpu_bound_task)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    end = time.time()
    print(f"Time taken with processes: {end - start:.2f} seconds")