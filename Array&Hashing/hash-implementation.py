# we will store this Pair in out hashmap
class Pair:
    def __init__(self,key,val):
        self.key = key
        self.val = val

# We are trying to implement
# hash - to get index
# get - get value of a particular key
# put - put a key value pair in hash map
# remove - remove a key
# rehash - if capacity become filled half, just double the capacity and insert all the elments of previous map
# print
class HashMap:
    def __init__(self):
        self.size = 0 # This is the size of hashMap
        self.capacity = 2 # Capacity of array
        self.map = [None] * self.capacity    

    # Method to hash a string
    # we uses ord to get ASCII Code of an character
    def hash(self,key):
        # here key is a string, means collection of character
        integer = 0
        for c in key:
            integer += ord(c)
        return integer % self.capacity

    # getting the value of a particular key
    # Firslty we get the ket then search it in the map
    # then after getting the position, I will send user the value
    def get(self,key):
        # find the index of that key
        index  = self.hash(key)

        # If we have 10 keys, then the size of array is 16
        # 6 None position
        # Suppose when we have added the key, its postion is occupied, it goes to next
        # so we need to check for it as well
        # If i get a None, then our key can't be stored after that, because we are increasing index by 1

        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
 
            # circular transveral
            index += 1
            index = index % self.capacity

        return None

    ## adding the pair in hash map
    def put(self,pair : Pair):
        key = pair.key
        val = pair.val
        index = self.hash(key)

        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key,val)
                self.size += 1
                
                if self.size == self.capacity//2:
                    self.rehash()
                    return
                return
            elif self.map[index].key == key:
                self.map[index] = Pair(key,val)
                return 
          


            index += 1
            index = index % self.capacity        
                
            

    ## removing the Pair from hashmap using key
    def remove(self,key):
        # firtly check if key exist
        if not self.get(key):
           return 
        # get the index from the key 
        index = self.hash(key);        
           
        while True:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1 
                return 
            index += 1
            index = index % self.capacity

    ## If capacity of hash map filled half then we double its size
    # Create a hashmap of double capacity and add the previous hashmap element in it 
    def rehash(self):
        new_capacity = self.capacity*2
        new_hash = [None] * new_capacity
     
        old_map = self.map
        self.map = new_hash
        self.size = 0
        self.capacity = new_capacity
        # if we uses self.map instead of old_map, so as we insert the pair, it increases the size of map, resulting in wring index, basically it never stops

        for pair in old_map:
            if pair:
                self.put(pair) 
    

    def print(self):
         for pair in self.map:
             if pair:
                print(pair.key, pair.val);

pair1 = Pair("abhi",1)
pair2 = Pair("abhi2",2)
pair3 = Pair("abhi3",3)
pair4 = Pair("abhi4",4)
pair5 = Pair("abhi5",5)
pair6 = Pair("abhi6",6)
pair7 = Pair("abhi7",7)
pair8 = Pair("abhi8",8)

map = HashMap()       

map.put(pair1)
map.put(pair3)
map.put(pair2)
map.put(pair8)
map.put(pair7)
map.put(pair6)
map.put(pair5)
map.put(pair4)

map.remove(pair8.key)

map.print()
