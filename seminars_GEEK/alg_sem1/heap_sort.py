import classes

def start():
    
    heap_list = classes.Heap(10, -5,5)
    print("rand generated array", heap_list)
    print("third element is: ", heap_list.get_elem(2))
    
    
    heap_list.heapSort()
    print("sorted class array is:", heap_list)
    
    # # Управляющий код для тестирования
    # my_list = list_gen(-2, 10, 100)
    # start = time.time()
    # print("unsorted array is: ", my_list)
    # heapSort(my_list)
    # n = len(my_list)
    # print ("Sorted array is")
    # for i in range(n):
    #     print ("%d" %my_list[i], end = ', ')

    # print()
    # print(f"sort lasted for {time.time() - start} ms ")
