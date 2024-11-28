from prime_generator import get_next_size
letter_codes = {chr(i): i - 97 for i in range(97, 123)}  # a-z: 0-25
letter_codes.update({chr(i): i - 65 + 26 for i in range(65, 91)})  # A-Z: 26-51
class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        self.type = collision_type
        self.params = params
        self.size = params[-1]
        self.no_slots   = 0
        self.table = [0]*self.size
        self.store = []

    
    def insert(self, x):
        pass
    
    def find(self, key):
        pass
    
    def get_slot(self, key):
        pass
    
    def get_load(self):
        req = self.no_slots/self.size
        return req
    
    def __str__(self):
        pass
    
    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        pass

    def __hash__(self,key,param = 0) -> int:
        req = 0 
        z = 1
        use = self.params[0]
        if( param) != 0:
            use = self.params[1]
        for i  in range(len(key)):
            req +=  letter_codes.get(key[i], 1)*z
            z *= use  
        return req
    
# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF, 
# YOU WOULD NOT NEED TO WRITE IT TWICE
    
class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type,params)
        self.table = [False]*self.size
        if(self.type == "Chain"):
            self.table = [[False] for _ in range(self.size)]
            
    
    def insert(self, key):
        index = self.__hash__(key) % self.size
        self.no_slots +=1
        if(self.type == "Chain"):
            self.table[index][0] = True 
            if(len(self.table[index])==1):
                self.store.append(index) 
            else:  
                for i  in self.table[index]:
                    if(i == key):
                        self.no_slots-=1
                        return
                     

            self.table[index].append(key) 


                

        elif(self.type == "Linear"): 
            # print(key)
            if(self.table[index] != False):
                ret = index
                # index = (index+1)%self.size
                while(self.table[index] != False):
                    if(self.table[index] == key):
                        self.no_slots-=1
                        return
                    index = (index+1)%self.size
                    if(index == ret):
                        raise Exception("Table is full")
                    
                self.table[index] = key 
                self.store.append(index) 
            else:
                self.table[index] = key 
                self.store.append(index) 
        else:
            if(self.table[index] != False):
                
                ret = index
                
                range = self.params[2] - (self.__hash__(key,2)) % self.params[2]
                # index = (index+range)%self.size
                while(self.table[index] != False):
                    if(self.table[index] == key):
                        self.no_slots-=1
                        return
                    index = (index+range)%self.size
                    if(index == ret):
                        raise Exception("Table is full")           
                    
                self.table[index] = key 
                self.store.append(index) 
            else:
                self.table[index] = key 
                self.store.append(index)         

                    
    def find(self, key):
        

        index = self.__hash__(key) % self.size
        if(self.type == "Chain"):
            if(self.table[index][0]!= False):
                for i  in range(1,len(self.table[index])):
                    if(self.table[index][i] == key):
                        return True
            return  False
        elif(self.type == "Linear"):
            if(self.table[index]!= False):
                while(self.table[index]!= key and self.table[index]!= False):
                    index = (index+1)%self.size
                if(self.table[index] == False):
                    return False
                return True    


            return  False
        else:
            if(self.table[index]!= False):
                ranges = self.params[2] - self.__hash__(key,2) % self.params[2]
                while(self.table[index]!= key and self.table[index]!= False):
                    index = (index+ranges)%self.size
                if(self.table[index] == False):
                    return False
                return True    


            return  False
        
    
    
    def get_slot(self, key):
        return self.__hash__(key) % self.size    

    
    def get_load(self):
        return super().get_load()
        
    def __str__(self):
        result = []
        table_size = len(self.table)
        
        if self.type == "Chain":
            for k, i in enumerate(self.table, 1):
                if len(i) == 1:
                    result.append("<EMPTY>")
                else:
                    for j in range(1, len(i)):
                        result.append(str(i[j]))  # Convert to string if needed
                        if j < len(i) - 1:
                            result.append(" ; ")
                if k < table_size:
                    result.append(" | ")  # Add '|' between entries but not after the last one
                    
        else:
            for k, i in enumerate(self.table, 1):
                if not i:  # Use `not` to check for False or None
                    result.append("<EMPTY>")
                else:
                    result.append(str(i))  # Convert to string if needed
                if k < table_size:
                    result.append(" | ")  # Add '|' between entries but not after the last one

        return ''.join(result)  # Join the list into a single string

              


    def __hash__(self,key,param = 0) -> int:
        return super().__hash__(key,param)
        
    
class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type,params)
        self.table = [(None,None)]*self.size
        if(self.type == "Chain"):
            self.table = [[(None,None)] for _ in range(self.size)]
        
    
    def insert(self, x):
        # x = (key, value)
        key = x[0]
        index = self.__hash__(key) % self.size
        self.no_slots +=1
        if(self.type == "Chain"):
            if(self.table[index][0] == (None,None)):
                self.table[index].pop() 
                self.store.append(index)
            else:
                for i in  self.table[index]:
                    if(i[0] == key):
                        self.no_slots-=1
                        return      
            self.table[index].append(x) 
            

        elif(self.type == "Linear"): 
            # print(key)
            if(self.table[index] != (None,None)):
                ret = index
                # index = (index+1)%self.size
                while(self.table[index] != (None,None)):
                    if(self.table[index][0] == key):
                        self.no_slots-=1
                        return
                    index = (index+1)%self.size
                    if(index == ret):
                        raise Exception("Table is full")
                    
                self.table[index] = x
                self.store.append(index)
            else:
                self.table[index] = x
                self.store.append(index)
        else:
            if(self.table[index] != (None,None)):
                
                ret = index
                
                range = self.params[2] - self.__hash__(key,2) % self.params[2]
                # index = (index+range)%self.size
                while(self.table[index] != (None,None)):
                    if(self.table[index][0] == key):
                        self.no_slots-=1
                        return
                    index = (index+range)%self.size
                    if(index == ret):
                        raise Exception("Table is full")
                    
                self.table[index] = x
                self.store.append(index)
            else:
                
                self.table[index] = x
                self.store.append(index)
    
    def find(self, key):
        index = self.__hash__(key) % self.size
        if(self.type == "Chain"):
            for k in self.table[index]:
                if(k[0]==key):
                    return k[1]
            return  self.table[index][0][1]
        elif(self.type == "Linear"):
            if(self.table[index][0] != key and self.table[index][0]!= None):
                while(self.table[index][0] != key and self.table[index][0]!= None):
                    index = (index+1)%self.size

            return  self.table[index][1]
        else:
            range = self.params[2] - self.__hash__(key,2) % self.params[2]
            if(self.table[index][0] != key and self.table[index][0]!= None):
                while(self.table[index][0] != key and self.table[index][0]!= None):
                    index = (index+range)%self.size

            return  self.table[index][1]
       

    def get_slot(self, key):
        return self.__hash__(key) % self.size
    
    def get_load(self):
        return super().get_load()
    
    def __str__(self):
        result = []
        table_size = len(self.table)
        
        if self.type == "Chain":
            for k, i in enumerate(self.table, 1):
                if len(i) == 1 and i[0][0] is None:
                    result.append("<Empty>")
                else:
                    for j in range(len(i)):
                        str1 = i[j][0]
                        result.append(f"({str1},{i[j][1]})")
                        if j < len(i) - 1:
                            result.append(";")
                if k < table_size:
                    result.append(" | ")  # Add '|' between entries but not after the last one
                    
        else:
            for k, i in enumerate(self.table, 1):
                if i == (None, None):
                    result.append("<Empty>")
                else:
                    str1 = i[0]
                    result.append(f"({str1},{i[1]})")
                if k < table_size:
                    result.append(" | ")  # Add '|' between entries but not after the last one

        return ''.join(result)  # Join the list into a single string


    def __hash__(self,key,param=0) -> int:
        return super().__hash__(key,param)





# hi =HashMap("Double",[23,5,7,10])
# # # hi =HashMap("Linear",[23,10])
# hi.insert(("apple",40))
# hi.insert(("b",401))
# hi.insert(("lol",40))
# hi.insert(("lol",40))
# hi.insert(("lol",40))
# hi.insert(("lola",40))

# def find(self, key):
#         index = self.__hash__(key) % self.size
#         if(self.type == "Chain"):
#             for k in self.table[index]:
#                 if(k[0] == key):
#                     return k[1]
#         else:
#             if(self.table[index][0] == key):
#                 return self.table[index][1]
#             else:
#                 while(self.table[index][0] != key):
#                     index = (index+1)%self.size
#             return self.table[index][1]




# print(hi.__hash__("apple"))
# print(hi.find("b"))
# print(hi.get_slot("b"))
# print(hi.get_load())
# print(hi)
# print(hi.store)