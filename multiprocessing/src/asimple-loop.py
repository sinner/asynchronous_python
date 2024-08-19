import multiprocessing
import time


def do_something(seconds: float) -> str:
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


def main() -> None:
    start = time.perf_counter()

    # p1 = multiprocessing.Process(target=do_something, args=[1.5])
    # p2 = multiprocessing.Process(target=do_something, args=[1.5])

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    processes = []

    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)  # type: ignore

    for process in processes:  # type: ignore
        process.join()  # type: ignore

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')


if __name__ == '__main__':
    main()