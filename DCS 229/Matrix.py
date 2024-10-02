from __future__ import annotations #to use Matrix as type in type hints


#! I used stack overflow, geeksforgeeks, and W3 schools for a decent 
#! portion of this project this includes the zip function, pop function, 
#! and the rjust function I did also consult the CAT tutor Rafay a few 
#! times as well as receiving help from Britton briefly for touch-ups 
#! and other functionalities of the code I did not understand. 

class Matrix: 
    __slots__ = ("_num_rows", "_num_cols", "_data") 
    
    def __init__(self, num_rows = None, num_cols = None, data = None, *, filename = None) -> None:   
        self._num_rows = num_rows 
        self._num_cols = num_cols
        self._data = data   
        if num_rows is not None:    
            self._readMatrix(num_rows, num_cols, data)
        else:            
            self._readFile(filename)

    def _readFile(self, filename: str) -> Matrix: 
        with open(filename, "r") as infile:   
            line = infile.readline()  
            self._data = []  
            regular_data = []
            self._num_rows = -1 
            while line != '': 
                line_items = line.strip().split()  
                regular_data.append(line_items) 
                line = infile.readline()  
                self._num_rows += 1   
        regular_data.pop(0) 
        if len(regular_data) % self._num_rows != 0:  
            print(regular_data) 
            print(len(regular_data))
            raise ValueError("inconsistent number of integers per line")  
        else:  
            for lists in regular_data: 
                int_list = [] 
                for element in lists: 
                    new_element = int(element) 
                    int_list.append(new_element) 
                self._data.append(int_list)
            self._num_cols = int(len(self._data)/self._num_rows)  
            f_matrix = Matrix(self._num_rows, self._num_cols, self._data)
            return f_matrix
    
    def _readMatrix(self, num_rows, num_cols, data) -> Matrix:  
        self._num_rows = num_rows
        self._num_cols = num_cols  
        self._data = data  
        self._data = []  
        for i in range(num_rows): 
            row_values = [] 
            for x in range(num_cols): 
                row_values.append(data[num_cols*i + x])
            self._data.append(row_values)   
        
    def getNumRows(self) -> int:  
        ''' 
            definition: this function uses self to find and return the number of 
            rows in the matrix that is inputted 
        
            parameters: 
                self: the matrix that is inputted 
        
            returns:   
                self._num_rows: the number of rows in the matrix

        '''
        return self._num_rows 
    
    def getNumCols(self) -> int:
        ''' 
            definition: this function uses self to find and return the number of 
            columns in the matrix that is inputted 
        
            parameters: 
                self: the matrix that is inputted 
        
            returns:   
                self._num_cols: the number of columns in the matrix

        '''
        return self._num_cols 
    
    def __str__(self) -> str:   
        ''' 
            definition: this function uses self to identify the matrix data inputted 
            and then returns the data as a string that will be printed as the desired 
            matrix class form.
        
            parameters: 
                self: the matrix that is inputted.
        
            returns:   
                my_string: the string form of the matrix that will print as the desired form 
                when returned
        '''
        my_string = '' 
        i = 0   
        just_width = 0
        for lists in self._data:  
            for element in lists:  
                if len(str(element)) > just_width: 
                    just_width = len(str(element))    
                else: 
                    just_width = just_width  
        if just_width == 1:  
            just_width = 0
        for lists in self._data: 
            if (self._data.index(self._data[i])) == 0: 
                my_string += '|'   
                i += 1
            else: 
                my_string += '|\n|'   
                i += 1 
            for element in lists:   
                my_string += '  ' + (str(element)).rjust(just_width) + '  ' 
        my_string += '|' 
        return my_string
    
    
    def __getitem__(self, row_col: tuple[int]) -> int:   
        ''' 
            definition: this function uses self to identify the matrix data inputted 
            and a tuple that represents the indices (row and column number) of the 
            location of a matrix element.
            
            parameters: 
                self: the matrix that is inputted. 
                row_col: a tuple containing integers corresponding with the location 
                of the desired matrix element
        
            returns:   
                self._data[row][col]: the element (integer) at the corresponding row and 
                column 
        '''
        row = int(row_col[0])
        col = int(row_col[1]) 
        if row+1 <= self._num_rows and col+1 <= self._num_cols: 
            return self._data[row][col]
        else: 
            raise IndexError("the specified tuple has invalid indices, please choose values smaller than the number of rows and columns ***remember to use python indices, so the first element would have an index of 0***")
        
    def __eq__(self, other: Matrix) -> bool:  
        ''' 
            definition: this function uses self and other to identify if 
            two properly inputted matricies are the same, in terms of the
            number of rows and columns, and the data, and returns a boolean 
            value based on if all the information is matching.
            
            parameters: 
                self: the first matrix that is inputted 
                other: the second matrix that is inputted
        
            returns:   
                boolean: either True or False depending on if the 
                construction of the matricies are the exact same. 
        '''
        
        if type(other) != Matrix: 
            raise TypeError("the second matrix is not of type matrix, please make sure you are using the correct types!")
        else: 
            if (self._num_rows == other._num_rows and self._num_cols == other._num_cols and self._data == other._data): 
                return True 
            else: 
                return False
        
    def __add__(self, other: Matrix) -> Matrix:  
        ''' 
            definition: this function uses self and other to identify the 
            sum of two properly inputted matricies, then returns a new 
            matrix that consists of all the summed up values that 
            correspond to the same position in the matricies.
        
            parameters: 
                self: the first matrix that is inputted.
                other: the second matrix that is inputted. 
        
            returns:   
                a_matrix: a matrix object with the same dimensions 
                as both inputted matricies and their combined data.
        '''
        if self._num_rows != other._num_rows or self._num_cols != other._num_cols: 
            raise ValueError("the dimensions of the matricies do not match")   
        if type(other) != Matrix: 
            raise TypeError("the second matrix is not of type matrix, please make sure you are using the correct types!")
        else:     
            new_cols = self._num_cols
            new_rows = self._num_rows
            new_data = [] 
            for listsa in self._data:    
                index1 = self._data.index(listsa) 
                for listsb in other._data: 
                    index2 = other._data.index(listsb)
                    if index2 == index1:  
                        value = [x + y for x, y in zip(listsa, listsb)]  
                        for number in value: 
                            new_data.append(number) 
            a_matrix = Matrix(new_cols, new_rows, new_data)  
            return a_matrix

    def __mul__(self, other: Matrix) -> Matrix:  
        ''' 
            definition: this function uses self and other to identify the 
            product of two properly inputted matricies, then returns a new 
            matrix that consists of the correct dot products between the 
            two matricies in their corresponding positions.
        
            parameters: 
                self: the first matrix that is inputted. 
                other: the second matrix that is inputted.
        
            returns:   
                m_matrix: a matrix object with updated dimensions based on 
                the first two matricies, and the correct data.
        '''
        if self._num_cols != other._num_rows: 
            raise ValueError("dimensions are not suitable for multiplying, the number of columns in the first matrix must be equal to the number of rows in the second matrix") 
        if type(other) != Matrix: 
            raise TypeError("the second matrix is not of type matrix, please make sure you are using the correct types!")
        else:   
            new_rows = self._num_rows 
            new_cols = other._num_cols   
            new_data = []
            for m in range(new_rows): 
                for n in range(new_cols): 
                    value = 0 
                    total = 0
                    for k in range(self._num_cols):  
                        value = self._data[m][k]*other._data[k][n] 
                        total += value
                    new_data.append(total) 
            m_matrix = Matrix(new_rows, new_cols, new_data) 
            return m_matrix 
            
    def transpose(self) -> Matrix:  
        ''' 
            definition: this function uses self to identify the 
            data of a matrix, and then returns the a new matrix 
            which is the transpose of the original matrix, which 
            in shorter terms flips the data corresponding to each 
            column and row, as well as the number of rows and columns.
        
            parameters: 
                self: the matrix that is inputted. 
        
            returns:   
                t_matrix: a matrix object with updated dimensions 
                based on the inputted matrix, and with the data in 
                the new order.
                
        '''
        new_cols = self._num_rows 
        new_rows = self._num_cols   
        t_data = []
        new_data = list(map(list, zip(*self._data)))  
        for lists in new_data: 
            for element in lists:  
                t_data.append(element)
        t_matrix = Matrix(new_rows, new_cols, t_data)
        return t_matrix
         
            
def main() -> None:  
#!################### __str__ Test 1 ###################!#
    m1 = Matrix(3, 2, [1,2,3,4,5,6])      
    print(m1) 
    print('\n')
    
#!################### __str__ Test 2 ###################!# 
    m2 = Matrix(4, 3, [5,4,12,455,6,7,8,9,5,133,9999,10000]) 
    print(m2) 
    print('\n')

#!################### __str__ Test 3 ###################!#  
    m3 = Matrix(1, 5, [55555, 5555, 555, 55, 5]) 
    print(m3)
    print('\n')

#!################### __getitem__ Test 1 ###################!#   
    print(f"Actual:   {m1[2,1]}")
    print(f"Expected: 6") 
    print('\n')
    
    
#!################### __getitem__ Test 2 ###################!#   
    print(f"Actual:   {m2[0,0]}")
    print(f"Expected: 5") 
    print('\n')
    

#!################### __getitem__ Test 3 ###################!#   
    print(f"Actual:   {m3[0,2]}")
    print(f"Expected: 5555") 
    print('\n')
    

#!################### __getitem__ Test FAIL ###################!#   
    try: 
        print(m3[2,2])   
    except:
        print(f"IndexError: the specified tuple has invalid indices, please choose values smaller than the number of rows and columns ***remember to use python indices, so the first element would have an index of 0***") 
        print('\n')
    

#!################### __eq__ Test 1 ###################!#   
    print(f"Actual:   {(m1 == m2)}")
    print(f"Expected: False") 
    print('\n')
    

#!################### __eq__ Test 2 ###################!#  
    print(f"Actual:   {(m1 == m3)}")
    print(f"Expected: False") 
    print('\n')


#!################### __eq__ Test 3 ###################!#  
    m4 = Matrix(3, 2, [1,2,3,4,5,6])
    print(f"Actual:   {(m1 == m4)}")
    print(f"Expected: True") 
    print('\n')


#!################### __eq__ Test FAIL ###################!#  
    Fm = (2, 2, [1,2,3,4]) 
    try:
        print(m1 == Fm) 
    except:
        print(f"TypeError: the second matrix is not of type matrix, please make sure you are using the correct types!")  
        print('\n')


#!################### __add__ Test 1 ###################!#  
    print(m1+m4) 
    print('\n')


#!################### __add__ Test 2 ###################!#  
    m5 = Matrix(3, 2, [2,3,4,5,6,7]) 
    print(m1+m5)
    print('\n')


#!################### __add__ Test 3 ###################!#  
    m6 = Matrix(3, 2, [3,4,5,6,7,8]) 
    print(m1+m6)
    print('\n')


#!################### __add__ Test FAIL ###################!#   
    try: 
        print(m1+m4) 
    except:
        print(f"TypeError: the second matrix is not of type matrix, please make sure you are using the correct types!")  
    print('\n')


#!################### __add__ Test FAIL ###################!#   
    try: 
        print(m1+m2) 
    except:
        print(f"ValueError: the dimensions of the matricies do not match")
    print('\n')

    
#!################### __mul__ Test 1 ###################!#   
    m7 = Matrix(2, 3, [3,4,5,6,7,8]) 
    print(m1*m7)
    print('\n')


#!################### __mul__ Test 2 ###################!#   
    print(m5*m7)
    print('\n')
 
 
#!################### __mul__ Test 3 ###################!#   
    print(m6*m7)
    print('\n')


#!################### __mul__ Test FAIL ###################!#    
    try: 
        print(m3*m7) 
    except:  
        print(f"ValueError: dimensions are not suitable for multiplying, the number of columns in the first matrix must be equal to the number of rows in the second matrix")
        print('\n') 

#!################### __mul__ Test FAIL ###################!#    
    try:  
        print(Fm*m7)
    except:
        print(f"TypeError: the second matrix is not of type matrix, please make sure you are using the correct types!") 
        print('\n')   
        

#!################### transpose Test 1 ###################!#  
    print(m1.transpose()) 
    print('\n')


#!################### transpose Test 2 ###################!#  
    print(m2.transpose()) 
    print('\n')


#!################### transpose Test 3 ###################!#  
    print(m3.transpose()) 
    print('\n')


#!################### transpose Test FAIL ###################!#  
    try: 
        print(Fm.transpose()) 
    except: 
        print(f"TypeError: the second matrix is not of type matrix, please make sure you are using the correct types!")
        print('\n') 

#!################### getNumRows Test 1 ###################!#  
    print(f"Actual:  {m1.getNumRows()}")
    print(f"Expected: 3") 
    print('\n') 


#!################### getNumRows Test 2 ###################!#  
    print(f"Actual:  {m2.getNumRows()}")
    print(f"Expected: 4") 
    print('\n') 



#!################### getNumRows Test 3 ###################!#  
    print(f"Actual:  {m3.getNumRows()}")
    print(f"Expected: 1")          
    print('\n') 



#!################### getNumCols Test 1 ###################!#  
    print(f"Actual:  {m1.getNumCols()}")
    print(f"Expected: 2")  
    print('\n') 



#!################### getNumCols Test 2 ###################!#  
    print(f"Actual:  {m2.getNumCols()}")
    print(f"Expected: 3") 
    print('\n') 
 


#!################### getNumCols Test 3 ###################!#  
    print(f"Actual:  {m3.getNumCols()}")
    print(f"Expected: 5")  
    print('\n') 

main()