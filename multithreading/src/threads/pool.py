import time
import concurrent.futures as futures


def worker(seconds: float) -> str:
    print(f"Worker sleeping for {seconds} seconds")
    time.sleep(seconds)
    print(f"Worker finished sleeping for {seconds} seconds")
    return f"Done after {seconds} seconds"


def main() -> None:
    """_summary_
        Here we create 3 threads that sleep for different amount of time.
        Thread 1 sleeps for 3 seconds
        Thread 2 sleeps for 2 seconds
        Thread 3 sleeps for 1 second
    """

    with futures.ThreadPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = [executor.submit(worker, sec) for sec in secs]

        for f in futures.as_completed(results):
            print(f.result())

    with futures.ThreadPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(worker, secs)

        for result in results:
            print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    print(f"Time taken: {round(time.time() - start, 2)} seconds")
