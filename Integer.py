from Number import Number

######################################################################
class Integer(Number):
    def __init__(self, value: int) -> None:
        ''' initializer method for Integer class
        Parameter:
            value: an integer
        Raises:
            ValueError if value cannot be converted to int
        '''
        # simply call the super class initializer
        super().__init__(int(value))

    def __add__(self, other: Number | int | float) -> Number:
        ''' method to add an Integer object with any object of type
            Integer, Float, int, or float
        Parameters:
            other: an Integer, Float, int, or float object
        Returns:
            a Float object if other is of type Float or float, or
            an Integer object otherwise
        Raises:
            TypeError if the type of other is not one of Integer, Float,
                int, or float
        '''
        # import Float only when needed to avoid circular import
        # (see https://bit.ly/488rlWX)
        from Float import Float
        self.checkType(other, [Integer, Float, int, float])

        if isinstance(other, Float):
            return Float(self._value + other._value)
        if isinstance(other, float):
            return Float(self._value + other)
        if isinstance(other, int):
            return Integer(self._value + other)
        return Integer(self._value + other._value)

    def __mul__(self, other: Number | int | float) -> Number:
        ''' method to multiply an Integer object with any object of type
            Integer, Float, int, or float
        Parameters:
            other: an Integer, Float, int, or float object
        Returns:
            a Float object if other is of type Float or float, or
            an Integer object otherwise
        Raises:
            TypeError if the type of other is not one of Integer, Float,
                int, or float
        '''
        from Float import Float
        
        self.checkType(other, [Integer, Float, int, float])

        if isinstance(other, Float):
            return Float(self._value * other._value)
        if isinstance(other, float):
            return Float(self._value * other)
        if isinstance(other, int):
            return Integer(self._value * other)
        return Integer(self._value * other._value)
         # your code instead


def main() -> None:
    
    #!#################### Test 1 ####################!#   
    num_1 = Integer(3) 
    num_2 = Integer(5) 
    print(f" Actual  : {num_1 + num_2}")  
    print(f" Expected: 8")
    print('\t')
    
    
    #!#################### Test 2 ####################!#
    num_3 = Integer(-14)
    print(f" Actual  : {num_1*num_3}") 
    print(f" Expected: -42")
    print('\t')
     
     
    #!#################### Test 3 ####################!#
    num_4 = Integer(12) 
    num_5 = Integer(23)  
    print(f" Actual  : {num_4*num_5}") 
    print(f" Expected: 276")
    print('\t')
    
    
    
#todo in this case we do not have to override the __str__ method in Number since it returns the value of self._value

if __name__ == "__main__":  # don't execute main when Integer is imported
    main()
