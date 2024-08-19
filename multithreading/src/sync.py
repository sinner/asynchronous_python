import time


def worker(seconds: int) -> None:
    print(f"Worker sleeping for {seconds} seconds")
    time.sleep(seconds)
    print(f"Worker finished sleeping for {seconds} seconds")


def main() -> None:
    """_summary_
        Here the worker function is called three times with different
        sleep times synchronously.
    """
    worker(2)
    worker(3)
    worker(4)


if __name__ == "__main__":
    start = time.time()
    main()
    print(f"Time taken: {round(time.time() - start, 2)} seconds")
