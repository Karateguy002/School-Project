import random
import time
from multiprocessing import Process, Queue


def producer(queue, N):
    for i in range(N):
        number = random.randint(1, 100)
        queue.put(number)
        print(f"Producer sent: {number}")
        time.sleep(random.uniform(0, 1))
    queue.put(-1)


def consumer(queue):
    while True:
        number = queue.get()
        if number == -1:
            break
        print(f"Consumer received: {number}")


if __name__ == '__main__':
    queue = Queue()
    N = random.randint(5, 20)

    producer_process = Process(target=producer, args=(queue, N))
    consumer_process = Process(target=consumer, args=(queue,))

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()
