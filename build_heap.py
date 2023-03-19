import heapq
from typing import List, Tuple

def parallel_processing(n: int, m: int, data: List[int]) -> List[Tuple[int, int]]:
    output = []
    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)

    for job_time in data:
        time, thread_index = heapq.heappop(threads)
        output.append((thread_index, time))
        heapq.heappush(threads, (time + job_time, thread_index))

    return output

def sift_down(data: List[int], n: int, i: int, swaps: List[Tuple[int, int]]) -> None:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] > data[largest]:
        largest = left

    if right < n and data[right] > data[largest]:
        largest = right

    if largest != i:
        swaps.append((i, largest))
        data[i], data[largest] = data[largest], data[i]
        sift_down(data, n, largest, swaps)

def build_heap(data: List[int]) -> List[Tuple[int, int]]:
    swaps = []
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(data, n, i, swaps)

    for i in range(n - 1, 0, -1):
        swaps.append((0, i))
        data[0], data[i] = data[i], data[0]
        sift_down(data, i, 0, swaps)

    return swaps


def main():
    # read input
    n = None
    data = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        if n is None:
            # read number of elements
            n = int(line)
        else:
            # read elements
            data += list(map(int, line.split()))

    # check input
    assert n is not None
    assert len(data) == n

    # call function to assess the data and give back all swaps
    swaps = build_heap(data)

    # output how many swaps were made (should be less than 4n)
    assert len(swaps) <= 4 * n
    print(len(swaps))

    # output all swaps
    for i, j in swaps:
        print(i, j)

    # sample usage of parallel_processing function
    result = parallel_processing(n, 2, data)
    for res in result:
        print(res[0], res[1])

if __name__ == "__main__":
    main()
