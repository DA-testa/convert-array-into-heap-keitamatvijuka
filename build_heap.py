import heapq

def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n//2-1, -1, -1):
        heapify_down(data, n, i, swaps)
    return swaps

def heapify_down(data, n, i, swaps):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and data[left] > data[largest]:
        largest = left
        
    if right < n and data[right] > data[largest]:
        largest = right
        
    if largest != i:
        swaps.append((i, largest))
        data[i], data[largest] = data[largest], data[i]
        heapify_down(data, n, largest, swaps)


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
