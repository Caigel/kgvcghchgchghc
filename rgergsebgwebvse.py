import multiprocessing
import time
import random
from datetime import datetime

def worker():
    """Each worker waits a random time, prints the current time, then exits."""
    wait_time = random.uniform(0, 1)  
    time.sleep(wait_time)
    print(f"Process {multiprocessing.current_process().name} - Time: {datetime.now().strftime('%H:%M:%S.%f')}")

if __name__ == "__main__":
    processes = []
    
    for i in range(3):
        p = multiprocessing.Process(target=worker, name=f"Worker-{i+1}")
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
