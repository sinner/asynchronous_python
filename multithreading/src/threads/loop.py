import time
import threading


def worker(seconds: int) -> int:
    print(f"Worker sleeping for {seconds} seconds")
    time.sleep(seconds)
    print(f"Worker finished sleeping for {seconds} seconds")
    return seconds


def main() -> None:
    """_summary_
        Here we create 3 threads that sleep for different amount of time.
        Thread 1 sleeps for 3 seconds
        Thread 2 sleeps for 2 seconds
        Thread 3 sleeps for 1 second
    """
    threads: list[threading.Thread | None] = []

    for _ in range(10):
        t = threading.Thread(target=worker, args=(1.5,))
        t.start()
        # Append the thread to the list. We can't join the thread here because
        # it will wait for the thread and block the main thread and won't be
        # able to start the next thread
        threads.append(t)

    # Wait for the threads to finish. Without this,
    # the main thread will finish before the worker threads
    for t in threads:
        if t:
            t.join()


if __name__ == "__main__":
    start = time.time()
    main()
    print(f"Time taken: {round(time.time() - start, 2)} seconds")
