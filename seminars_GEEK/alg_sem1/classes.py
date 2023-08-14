from random import randint
import time

class Heap:
    def __init__(self, size: int, min: int, max: int):
        self.my_list = Heap.list_gen(min,max,size)
        self.size = size
        print("self size is ", self.size)
                

    
    def list_gen(min=-5, max=5, list_length=10):
        #print("temp = ", list_length ,[randint(min, max) for i in range(list_length)] )
        return [randint(min, max) for i in range(list_length)]

    def __str__(self) -> list:
        return f'{self.my_list}'
    
    def get_elem(self, i):
        return self.my_list[i]
        
        
    
    # Процедура для преобразования в двоичную кучу поддерева с корневым узлом i, что является индексом в arr[]. n - размер кучи
    def heapify(self, n, i):
        largest = i # Initialize largest as root
        l = 2 * i + 1   # left = 2*i + 1
        r = 2 * i + 2   # right = 2*i + 2

        # Проверяем существует ли левый дочерний элемент больший, чем корень
        if l < n and self.my_list[i] < self.my_list[l]:
            largest = l

        # Проверяем существует ли правый дочерний элемент больший, чем корень
        if r < n and self.my_list[largest] < self.my_list[r]:
            largest = r

        # Заменяем корень, если нужно
        if largest != i:
            self.my_list[i],self.my_list[largest] = self.my_list[largest],self.my_list[i] # свап

        # Применяем heapify к корню.
            Heap.heapify(self.my_list, n, largest)

# Основная функция для сортировки массива заданного размера
    def heapSort(self):
        #print("self size is ", self.size)
        n = self.size

    # Построение max-heap.
        for i in range(n, -1, -1):
            Heap.heapify(self, n, i)

    # Один за другим извлекаем элементы
        for i in range(n-1, 0, -1):
            self.my_list[i], self.my_list[0] = self.my_list[0], self.my_list[i] # сва
            Heap.heapify(i, 0)
