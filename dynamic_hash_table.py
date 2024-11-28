from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        memory = self.table
        self.size = get_next_size()
        self.no_slots =0
        self.table = [False]*self.size
        if(self.type == "Chain"):
            self.table = [[False] for _ in range(self.size)]
        for i in memory:   
            if(self.type == "Chain"):
                if(len(i)>1):
                    for k in range(1,len(i)):
                        self.insert(i[k])
            else:
                if(i != False):
                    self.insert(i)

               

        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        if self.get_load() >= 0.5:
            self.rehash()
            
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        memory = self.table
        self.size = get_next_size()
        self.no_slots =0
        self.table = [(None,None)]*self.size
        if(self.type == "Chain"):
            self.table = [[(None,None)] for _ in range(self.size)]
        for i in memory:   
            if(self.type == "Chain"):
                if(i[0][0] != None):
                    for k in range(len(i)):
                        self.insert(i[k])
            else:
                if(i[0] != None):
                    self.insert(i)
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        if self.get_load() >= 0.5:
            self.rehash()


# hi =DynamicHashSet("Double",[23,5,7,19])
# hi =DynamicHashSet("Chain",[23,29])
# # hi =HashMap("Linear",[23,10])
# hi.insert("apple")
# hi.insert("b")
# hi.insert("lol")
# hi.insert("lol")
# hi.insert("lol")
# hi.insert("lola") 
# hi.insert("lolap") 
# # hi.insert("lolapu") 
# print(hi.get_load())
# print(hi)    
 
   

