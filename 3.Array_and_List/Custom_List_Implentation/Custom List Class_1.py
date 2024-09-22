
import ctypes

class CustomList:
    def __init__(self):
        initialcapacity = 1
        self.capacity = initialcapacity
        self.size = 0
        self.array = self.__create_array(self.capacity)


    def __create_array(self,capacity):
        #Create a new Refernatial array with capacity
        return (capacity * ctypes.py_object)()        
    
    def __resize(self,new_capacity):
        new_array = self.__create_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array #Replace the old array
        self.capacity = new_capacity
           
    def append(self,item):
        if(self.size == self.capacity):
            self.__resize(2 * self.capacity)


    def __len__(self):
        #print("Give me the logice and i will tell the size")
        return self.size
    def __str__(self):
        output = ''
        for i in range(self.size):
            output = output + str(self.array[i]) + ','
        return '['+output[:-1] +']'  

    def pop(self):
        if(self.size == 0):
            return 'Empty List,IndexError: pop from empty list'
        popped_item = self.array[self.size - 1]
        self.size = self.size - 1
        return popped_item
    def clear(self):
        self.size=0

    def insert(self,position,element):
        # Position will  be inside only
        if(self.size == self.capacity):
            self.__resize(2*self.capacity)
        
        for index in range(self.size,position,-1): 
            self.array[index] = self.array[index-1]
        
        self.array[position] = element
        self.size +=1

    def remove(self,element):
        pass




########################################3            
my_list = CustomList()
my_list.append(1)
my_list.append(2)
print(my_list)
print(len(my_list))
my_list.append(3)
print(my_list)


print(my_list)
print(my_list.pop())
print(my_list)
print(my_list.pop())







