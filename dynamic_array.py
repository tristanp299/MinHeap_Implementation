# Name: Tristan Pereira
# OSU Email: pereirtr@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2 Dynamic Arrays and ADT Implementation
# Due Date:07/11/2022
# Description: dynamic_array.py is a Dynamic Array class that pulls from a StaticArray class. It has a multitude of functions that are regularly seen in dynamic arrays.
# This class is used by bag_da.py the Bag ADT class.


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index = self._index + 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------
    def pop(self):

        if self._size == 0:
            raise DynamicArrayException
        removed = self._data[self._size-1]
        self._data[self._size - 1] = None
        self._size-=1
        return removed

    def resize(self, new_capacity: int) -> None:
        """resize functions takes in a new_capacity and allocates old StaticArray elements into a new array with a new capacity.
        """
        if new_capacity<=0 or new_capacity<self._size:
            return
        else:
            new_arr = StaticArray(new_capacity)
            for i in range(self._size):
                new_arr[i] = self._data[i]
            self._capacity = new_capacity
            self._data = new_arr

    def append(self, value: object) -> None:
        """The append function takes in a object and adds it to the end of the self._data static array
        """
        if self._size == self._capacity:
            self.resize(self._capacity*2)
        self._data[self._size] = value
        self._size += 1


    def insert_at_index(self, index: int, value: object) -> None:
        """
        The insert_at_index function takes in an index and a value, allocates space for that object at that index, then places it there. If it is not within the index it will raise
        an Exception.
        """
        if index<0 or index>self._size:
            raise DynamicArrayException

        elif self._size == self._capacity:
            self.resize(self._capacity*2)
        new_arr = StaticArray(self._capacity)

        if index == 0:
            new_arr[0] = value
            for i in range(self._size):
                new_arr[i+1]=self._data[i]

        else:
            for i in range(0,index+1):
                new_arr[i] = self._data[i]

            new_arr[index] = value

            for i in range(index, self._size):
                new_arr[i+1] =self._data[i]

        self._size += 1
        for i in range(self._size):
            self._data[i] = new_arr[i]

    def remove_at_index(self, index: int) -> None:
        """
        remove_at_index takes an index as a parameter and removes the object at that location, while reallocating elements along the StaticArray. It raises an
        Exception if it is not within the index of the array.
        """
        if index<0 or index>=self._size:
            raise DynamicArrayException

        if self._capacity<10:
            self._capacity = self._capacity

        elif self._size*4 < self._capacity:
            self._capacity = self._size*2
            if self._size * 2 <= 10:
                self._capacity =10

        new_arr = StaticArray(self._capacity)

        for i in range(self._size-1):
            if i >= index:
                new_arr[i] = self._data[i+1]
            else:
                new_arr[i] = self._data[i]
        self._data = new_arr

        self._size-=1

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        The slice function takes a start index and a size as paramter, and returns a DynamicArray with those selected elements.
        """
        new_arr = DynamicArray()
        if start_index<0 or start_index>=self._size or start_index+size>self._size or size<0:
            raise DynamicArrayException
        if size ==0:
            return new_arr
        for i in range(start_index, start_index+size):
            new_arr.append(self._data[i])
        return new_arr

    def merge(self, second_da: "DynamicArray") -> None:
        """
        The merge function takes in a DynamicArray as a parameter and adds that array to the end of self._data
        """
        for i in range(second_da.length()):
            self.append(second_da[i])

    def map(self, map_func) -> "DynamicArray":
        """
        The map function takes a function as a parameter, and applies that to each element in the self._data array, the result it returned in a DynamicArray
        """
        new_arr = DynamicArray()
        for i in range(self._size):
            new_arr.append(map_func(self._data[i]))

        return new_arr

    def filter(self, filter_func) -> "DynamicArray":
        """
        The filter function takes a function as a parameter, which tests a condition for each element. It returns a DynamicArray of elements that tested True.
        """
        new_arr = DynamicArray()
        for i in range(self._size):
            if filter_func(self._data[i]) == True:
                new_arr.append(self._data[i])

        return new_arr

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        reduce function takes in a function and an initializer as parameters. It applies the function passed in Dynamic Array elements with the inititializer as
        an option to mutate the first element. It returns the resulting value.
        """
        if self._size == 0:
            return initializer
        else:
            if initializer is None:
                initializer = self._data[0]
                for i in range(1, self._size):
                    initializer = reduce_func(initializer, self._data[i])
            else:
                for i in range(self._size):
                    initializer = reduce_func(initializer, self._data[i])

            return initializer

def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    find_mode function takes in a Dynamic Array as a parameter and returns a tuple. The tuple contains the a DynamicArray of the modes of the inputted array,
    and the frequency of those modes.
    """
    lent = arr.length()
    mode = arr[0]
    frequency = 0
    overall_freq = 1

    new_arr = DynamicArray()
    for i in range(lent):
        # each element will be the mode once and frequency 1

        if arr[i] == mode:
            frequency += 1
            if i > 0 and frequency == overall_freq:
                new_arr.append(arr[i])

            # Since list is sorted the frequency will always be repeated values in the list
            if frequency > overall_freq:
                new_arr = DynamicArray()
                new_arr.append(arr[i])

                overall_freq += 1

        else:
            mode = arr[i]
            frequency = 1

    if overall_freq ==1:
        new_arr = DynamicArray()
        for i in range(lent):
            new_arr.append(arr[i])

    return (new_arr,overall_freq)
    

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":
    case = [1,1,2,3,4,4]
    case2 = [1,2,3,4,5]
    case3 = ['Apple', 'Banana', 'Banana', 'Carrot', 'Carrot', 'Date', 'Date', 'Date', 'Eggplant', 'Eggplant', 'Eggplant', 'Fig', 'Fig', 'Grape']
    da = DynamicArray(case2)
    mode, freq = find_mode(da)
    print(da)
    print(str(mode)+': frequency = '+str(freq))