from Number import Number

######################################################################
class Float(Number):
    __slots__ = ('_digits')

    def __init__(self, value: float | int, digits: int = 2) -> None: 
        
        ''' initializer method for Float class
        Parameter:
            value: a float or integer
            digits: an integer representing # of digits beyond
                decimal to be displayed when printing
        Raises:
            ValueError if value cannot be converted to float
        ''' 
        self._digits = digits 
        self._value = value
        # your code instead

    def __add__(self, other: Number | int | float) -> Number:
        from Integer import Integer 
        # you are likely to need Integer in here, so do a local-to-method
        # import (rather than global at the top) to avoid circular imports
        # (see Integer.py for an example that imports Float locally)
        self.checkType(other, [Integer, Float, int, float])

        if isinstance(other, Float):
            return Float(self._value + other._value)
        if isinstance(other, float):
            return Float(self._value + other)
        if isinstance(other, int):
            return Float(self._value + other) 
        return Float(self._value + other._value, self._digits) 

    def __mul__(self, other: Number | int | float) -> Number: 
        from Integer import Integer 
        # you are likely to need Integer in here, so do a local-to-method
        # import (rather than global at the top) to avoid circular imports
        # (see Integer.py for an example that imports Float locally)
        self.checkType(other, [Integer, Float, int, float])

        if isinstance(other, Float):
            return Float(self._value * other._value)
        if isinstance(other, float):
            return Float(self._value * other)
        if isinstance(other, int):
            return Float(self._value * other)
        return Float(self._value * other._value, self._digits)

    def changeFormat(self, digits: int) -> None:
        ''' for this object, sets the number of digits to appear after the
            decimal when printed
        Parameters:
            digits: integer number of digits to appear after the decimal
        Raises:
            ValueError if digits cannot be converted to int
        '''
        self._digits = input("how many decimal places would you like? ")
        if '.' in self._digits: 
             raise ValueError("digits cannot be converted to an integer")  
        else: 
            return self._digits
            

    def __str__(self) -> str:
        ''' returns a string representation of the Float object,
            formatted to the Float-object-specified digits of
            precision
        Returns:
            a string of the formatted Float, e.g., "3.1416"
            if the Float object's data contains 3.1415926535
            and the digits of precision had been changed to 4 
        '''
        # use f-string float formatting;
        # see https://realpython.com/how-to-python-f-string-format-float/  
        answer = input("would you like to change the number of decimals rounded to? (y: yes, n: no) ") 
        if answer == 'y':  
            self.changeFormat(self._digits) 
        if answer == 'n': 
            pass
        return f"Rounding float to {self._digits} decimal places: {self._value:.{self._digits}f}" 
    
def main() -> None:
        
    #!#################### Test 1 ####################!#  
    from Integer import Integer 
    num_1 = Float(3.3567387)
    num_2 = Float(5.67293984)  
    print(f" Actual  : {(num_1+num_2)}")  
    print(f" Expected: Rounding float to 3 decimal places: 9.030")
    print('\t')
    
    
    #!#################### Test 2 ####################!#
    num_3 = Float(3.14159)  
    num_int = Integer(5)
    print(f" Actual  : {num_3*num_int}") 
    print(f" Expected: Rounding float to 5 decimal places: 15.70795")
    print('\t')
    
     
    #!#################### Test 3 ####################!#
    num_4 = Float(1.23) 
    num_5 = Float(23.45)  
    print(f" Actual  : {num_4*num_5}") 
    print(f" Expected: Rounding float to 2 decimal places: 28.84")
    print('\t')
    
if __name__ == "__main__":  # don't execute main when Integer is imported
    main()

