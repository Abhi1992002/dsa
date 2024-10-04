## Implementing dynamic arrays in Python
# class Array
# pushback - last postion insertion
# resize - double the size of the array
# popback - remove the last element
# get - get the element at a given index
# insert - insert an element at a given index
# print - print the array

class Array:
    def __init__(self):
        self.capacity = 2
        self.length = 0 # Number of elements in the array
        self.arr = [0] * self.capacity

    def pushback(self,n):
        # if my array is full, resize it
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1

    def resize(self):
        # create a new a array of double size
        capacity = self.capacity * 2
        print("Increased the capacity from ",self.capacity , " to ", capacity)
        new_arr = [0] * capacity

        # copying old element in new array
        for i in range(0,self.length):
            new_arr[i] = self.arr[i]

        print("New Array", new_arr )
        self.arr = new_arr
        self.capacity = capacity

    def popback(self):
        last_element = self.arr[self.length-1]
        self.arr[self.length-1] = 0
        return last_element

    def get(self,i):
        if i > self.length-1:
            return None
        element = self.arr[i]
        return element

    def insert(self,i,n):
        if self.length > self.capacity:
            self.resize()

        for index in range(self.length-1,-1,-1):
            if index == i:
                self.arr[index] = n
                break
            self.arr[index+1] = self.arr[index]

    def print(self):
            print("My current array : ", self.arr)

my_arr = Array()
my_arr.pushback(10)
my_arr.pushback(20)
my_arr.pushback(30)
my_arr.pushback(40)
my_arr.pushback(50)
my_arr.pushback(60)
my_arr.pushback(70)
my_arr.print()
print(my_arr.get(3))
my_arr.popback()
my_arr.print()
my_arr.insert(3,69)
my_arr.print()
