import hash_table as ht
import dynamic_hash_table as dt
# letter_codes = {chr(i): i - 97 for i in range(97, 123)}  # a-z: 0-25
# letter_codes.update({chr(i): i - 65 + 26 for i in range(65, 91)})  # A-Z: 26-51
class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    
class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    
    def __init__(self, book_titles, texts):
        book_titles_copy = book_titles[:]
        texts_copy = [text[:] for text in texts]
        self.mergesort(book_titles_copy,texts_copy,0,len(book_titles)-1)
        for j1 in range(len(texts_copy)): 
            self.mergesort(texts_copy[j1],None,0,len(texts_copy[j1])-1)
        list1 = []
        for i in texts_copy:
            li =[]
            prev =-1
            j =0
            while j<(len(i)):
                while(prev !=-1 and j<len(i) and i[j] == i[prev]):  
                    # print("test")
                    j +=1 

                if(j == len(i)):
                    continue 
                # print(i[j],"app")                                                                    
                li.append(i[j])
                prev = j
                # print(prev,"check")
            list1.append(li)

        self.books = book_titles_copy
        self.texts = list1
        # print(self.texts)
     



    def distinct_words(self, book_title):
        end = len(self.books)-1
        start = 0
        mid = 0
        while(start<=end):
            mid = (start+end)//2
            if(self.books[mid] == book_title):
                return self.texts[mid]
            elif(self.books[mid] >book_title):   
                end = mid-1
            else:
                start = mid+1
        if(self.books[start] == book_title): 
            return self.texts[start]
        else:
            return []          





    
    def count_distinct_words(self, book_title):
        end = len(self.books)-1
        start = 0
        mid = 0
        while(start<=end):
            mid = (start+end)//2
            if(self.books[mid] == book_title):
                return len(self.texts[mid])
            elif(self.books[mid] >book_title):   
                end = mid-1
            else:
                start = mid+1
        if(self.books[start] == book_title): 
            return len(self.texts[start])
        else:
            return 0
    
    def search_keyword(self, keyword):
        req =[]
        for i in range(len(self.books)):
                end = len(self.texts[i])-1
                start = 0
                mid = 0
                while(start<=end):
                    mid = (start+end)//2
                    if(self.texts[i][mid] == keyword):
                        req.append(self.books[i])
                        break
                    elif(self.texts[i][mid] >keyword): 
                        end = mid-1
                    else:
                        start = mid+1
                # if(self.books[start] == keyword): 
                #     req.append(self.books[i])
        return req            


    
    def print_books(self):
        for i in range(len(self.books)):
            print(self.books[i],end=": ")
            for i1,j in enumerate(self.texts[i],1):
                if(i1 == len(self.texts[i])):
                    print(j,end="") 
                else:    
                    print(j,end=" | ")  
            print()        



    # def custom_comparator(self,s1, s2):
    # # Compare the strings based on their letter codes
    #     for i in range(min(len(s1), len(s2))):
    #         code1 = letter_codes.get(s1[i], float('inf'))  # Use inf for missing letters
    #         code2 = letter_codes.get(s2[i], float('inf'))
    #         # print(code1,code2,i)
    #         if code1 != code2:
    #             return code1 - code2  # Return the difference if codes are different
    #     return len(s1) - len(s2) 

    def merge(self, books, letters, mid, low, high):
        i = low
        j = mid + 1
        new_books = []
        new_letters = []

        # Merge the two halves while maintaining correspondence
        while i <= mid and j <= high:
            if books[i]<= books[j]:
                new_books.append(books[i])
                if(letters != None):
                    new_letters.append(letters[i])
                i += 1
            else:
                new_books.append(books[j])
                if(letters != None):
                    new_letters.append(letters[j])
                j += 1

        # Copy the remaining elements of the left half (if any)
        while i <= mid:
            new_books.append(books[i])
            if(letters != None):
                    new_letters.append(letters[i])
            i += 1

        # Copy the remaining elements of the right half (if any)
        while j <= high:
            new_books.append(books[j])
            if(letters != None):
                    new_letters.append(letters[j])
            j +=1         

        # Copy the merged subarray back into the original arrays
        for idx in range(len(new_books)):
            # print(len(books))
            books[low + idx] = new_books[idx]
            if(letters != None):
                letters[idx+low] = new_letters[idx]

    def mergesort(self, books, letters, low, high):
        if low < high:
            mid = (low + high) // 2
            self.mergesort(books, letters, low, mid)
            self.mergesort(books, letters, mid + 1, high)
            self.merge(books, letters, mid, low, high)


class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''
        req = "Chain"
        if(name == "Gates"):
            req = "Linear"
        elif(name == "Bezos"):
            req = "Double"    
        self.books = ht.HashMap(req,params)
    
    def add_book(self, book_title, text):
        use = ht.HashSet(self.books.type,self.books.params)
        for w in text:
            use.insert(w)
        req = use.store
        # for i in req:
        #     if self.books.type == "Chain":
        #         pass
        self.radixSort(use.store)         
        self.books.insert((book_title,use))
        
    
    def distinct_words(self, book_title):
        req = self.books.find(book_title)
        lis =[]
        for i in req.store:
            if(self.books.type == "Chain"):
               for k in range(1,len(req.table[i])):
                    book_title= req.table[i][k]
                    lis.append(book_title)
            else:
               book_title= req.table[i]
               lis.append(book_title)
        return lis       
        #store list of used indices and just visit them

    
    def count_distinct_words(self, book_title):
        #we can keep count of no of element inserted and that gives us required field
        req:ht.HashTable = self.books.find(book_title)
        return req.no_slots
    
    def search_keyword(self, keyword):
        lis = []
        # self.radixSort(self.books.store)   #unnecessary check  
        for i  in  self.books.store:
            if(self.books.type == "Chain"):
               for k in range(len(self.books.table[i])):
                    book_title= self.books.table[i][k][0]
                    text= self.books.table[i][k][1]
                    req = text.find(keyword)
                    if(req != False):
                        lis.append(book_title)
            else:
               book_title= self.books.table[i][0]
               text= self.books.table[i][1]
               req = text.find(keyword)
               if(req != False):
                   lis.append(book_title)

        return lis 

    
    

                   
            


        
    
    def print_books(self):
        for i in self.books.store:
            if(self.books.type == "Chain"):
                for k in range(len(self.books.table[i])):
                    req = self.books.table[i][k][1]
                    book = self.books.table[i][k][0]
                    print(book,end=": ")
                    print(req)
            else:
                req = self.books.table[i][1]
                book = self.books.table[i][0]
                print(book,end=": ")
                print(req)


    def getMax(self,arr):
        return max(arr)

# Counting sort based on the digit represented by exp (10^exp place)
    def countingSort(self,arr, exp):
        n = len(arr)
        output = [0] * n  # Output array to store the sorted result
        count = [0] * 10  # Since we're dealing with digits (0 to 9), the count array size is 10

        # Step 1: Store the count of occurrences of each digit (0 to 9)
        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1

        # Step 2: Change count[i] so that it contains the actual position of this digit in the output array
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Step 3: Build the output array
        i = n - 1
        while i >= 0:
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1

        # Step 4: Copy the sorted output array to arr[]
        for i in range(n):
            arr[i] = output[i]

    # Radix Sort function
    def radixSort(self,arr):
        # Step 1: Find the maximum number to know the number of digits
        max_val = self.getMax(arr)

        # Step 2: Perform counting sort for each digit. exp is 10^i, where i is the current digit position.
        exp = 1
        while max_val // exp > 0:
            self.countingSort(arr, exp)
            exp *= 10
        

# book_titles = ["book1", "book2"]
# texts = [["The", "name", "of", "this", "book", "contains", "a", "number","number","number","number","number","number"],
#              ["You", "can", "name", "this", "book", "anything","book","could"]]
# b = JGBLibrary("Gates",(10, 29))
# for i in range(2):
#     b.add_book(book_titles[i],texts[i])
# print(b.distinct_words("book1"))
# print(b.distinct_words("book2"))
# b.print_books()
# print(b.books)












# a = MuskLibrary(book_titles,texts)
# print(a.distinct_words("book1"))
# print(a.count_distinct_words("book1"))
# # a.print_books()
# print(a.search_keyword("number"))
# a.print_books()
# def distinct_words(self, book_title):
#         req = self.books.find(book_title)
#         shortcut = req.store
#         lis =[]
#         for i in req.store:
#             if(self.books.type == "Chain"):
#                for k in range(1,len(req.table[i])):
#                     book_title= req.table[i][k]
#                     lis.append(book_title)
#             else:
#                book_title= req.table[i]
#                lis.append(book_title)
#         return lis


    # def distinct_words(self, book_title):
    #     req = self.books.find(book_title)
    #     lis =[]
    #     for i in range(req.size):
    #         if(self.books.type == "Chain"):
    #            if(req.table[i][0] != False):
    #                 for k in range(1,len(req.table[i])):
    #                     book_title= req.table[i][k]
    #                     lis.append(book_title)
    #         else:
    #            if(req.table[i] != False):
    #                 book_title= req.table[i]
    #                 lis.append(book_title)
    #     return lis 

    
