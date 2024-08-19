import time
import threading


def worker(seconds: int) -> None:
    print(f"Worker sleeping for {seconds} seconds")
    time.sleep(seconds)
    print(f"Worker finished sleeping for {seconds} seconds")


def main() -> None:
    """_summary_
        Here we create 3 threads that sleep for different amount of time.
        Thread 1 sleeps for 3 seconds
        Thread 2 sleeps for 2 seconds
        Thread 3 sleeps for 1 second
    """
    t1 = threading.Thread(target=worker, args=(3,))
    t2 = threading.Thread(target=worker, args=(2,))
    t3 = threading.Thread(target=worker, args=(1,))

    # Start the threads. Without this, the threads will not run
    t1.start()
    t2.start()
    t3.start()

    # Wait for the threads to finish. Without this,
    # the main thread will finish before the worker threads
    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    start = time.time()
    main()
    print(f"Time taken: {round(time.time() - start, 2)} seconds")
