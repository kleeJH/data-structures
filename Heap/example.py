from heap import MinHeap, MaxHeap

heap = MinHeap()
heap.create_heap(10, [6, 2, 3, 14, 11, 1, 6, 8, 12])
for i in range(len(heap)):
    print(heap.get_most_priotized())

print("-----------------------------------------------")

heap = MaxHeap()
heap.create_heap(10, [6, 2, 3, 14, 11, 1, 6, 8, 12])
for i in range(len(heap)):
    print(heap.get_most_priotized())