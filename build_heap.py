import heapq

def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        current, left_child, right_child = i, 2*i+1, 2*i+2
        while left_child < n:
            smallest_child = left_child if (right_child >= n or data[left_child] < data[right_child]) else right_child
            if data[current] > data[smallest_child]:
                swaps.append((current, smallest_child))
                data[current], data[smallest_child] = data[smallest_child], data[current]
                current, left_child, right_child = smallest_child, 2*smallest_child+1, 2*smallest_child+2
            else:
                break
    return swaps


def main(): 
    Input = input() 
    if "I" in Input:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n

    if "F" in Input:  
        filepath = "tests/" + input() 
        with open(filepath, 'r') as file:
            n = int(file.readline().strip())
            data = list(map(int, file.readline().strip().split()))
            assert len(data) == n
            
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
