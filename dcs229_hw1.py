#question 1  
import string
import random


# question 1 

def randomString(min_num: int = 0, max_num: int = 10) -> str:  
    ''' definition: this function accepts a min and max string value 
        and prints a random string with a length in between the 
        specified numbers
        
    Parameters: 
        min_num: integer of minimum string length
        max_num: integer of maximum string length
    Returns: 
        new_string: a randomly generated string
    ''' 
    new_string = "" 
    for i in range(random.randint(min_num, max_num)):
        index = random.randint(0, len(string.ascii_letters) - 1) 
        new_string += string.ascii_letters[index] 
    return new_string 

# question 2  
def countNucleotides(dna_sequence: str) -> dict[str, int]:  
    ''' definition: this function accepts a DNA sequence and 
        returns a dictionary where every key is a character in 
        the sequence and every value is the amount of times 
        it appears in the sequence
        
    Parameters: 
        dna_sequence: string of the dna sequence to be used
    Returns: 
        dict: dictionary with characters as keys and appearances 
        as values
    '''
    count_A = 0  
    count_C = 0 
    count_G = 0 
    count_T = 0
    for nucleotide in dna_sequence: 
        if nucleotide.upper() == "A":
            count_A += 1
        elif nucleotide.upper() == "C":
            count_C += 1
        elif nucleotide.upper() == "G":
            count_G += 1
        else:
            count_T += 1  
    dict = {"A": count_A, "C": count_C, "G": count_G, "T": count_T} 
    return dict


#question 3  

def countWords(list_of_strings: list) -> dict[str, int]:  
    ''' definition: this function accepts a list of strings 
        and returns a dictionary where every key is a unique 
        word (ignoring capitalization) and every value is the 
        amount of times the word appears
        
    Parameters: 
        list_of_strings: a list consisting of submitted words
    Returns: 
        dict: a dictionary where keys are unique words and values 
        are the amount of times they appear
    ''' 
    dict = {} 
    for word in list_of_strings:   
        if word not in dict: 
            dict[word] = 1
        else: 
            dict[word] += 1  
    return dict

#question 4 

def readWords(filename: str) -> list[str]:  
    ''' definition: this function accepts and reads a filename  
        and returns a list of all words present in the file  
    
    Parameters: 
        filename: string of txt file with words and lines
    Returns: 
        word_list: list of all words present in the file 
    ''' 
    word_list = []   
    with open(filename, "r") as infile: 
        line = infile.readline() 
        while line != "": 
            line_items = line.strip().split() 
            word_list.extend(line_items)   
            line = infile.readline()  
    infile.close()
    return word_list 

def main() -> None:   
    
    #################### test 1 - Q1 ####################
    min_length1 = input("what is the minimum possible string length you would like? ")
    max_length1 = input("what is the maximum possible string length you would like? ") 
    randomString(min_length1, max_length1)

    #################### test 2 - Q1 ####################
    min_length2 = input("what is the minimum possible string length you would like? ")
    max_length2 = input("what is the maximum possible string length you would like? ") 
    randomString(min_length2, max_length2)
    
    #################### test 3 - Q1 ####################
    min_length3 = input("what is the minimum possible string length you would like? ")
    max_length3 = input("what is the maximum possible string length you would like? ") 
    randomString(min_length3, max_length3)
    
    #################### test 1 - Q2 ####################
    sequence1 = input("what DNA sequence would you like to use? *must only contain A,C,G,T* ")
    print(countNucleotides(sequence1)) 
    
    #################### test 2 - Q2 ####################
    sequence2 = input("what DNA sequence would you like to use? *must only contain A,C,G,T* ")
    print(countNucleotides(sequence2)) 
    
    #################### test 3 - Q2 ####################
    sequence3 = input("what DNA sequence would you like to use? *must only contain A,C,G,T* ")
    print(countNucleotides(sequence3)) 
    
    #################### test 1 - Q3 ####################  
    new_list1=[]  
    i = 1
    num_of_words = input("how many words would you like in the list? ")
    while i <= (int(num_of_words)): 
        word = input("input word " + str(i) + ": " )
        new_list1.append(word)
        i += 1  
    print(countWords(new_list1))  
    
    #################### test 2 - Q3 ####################  
    new_list2=[]  
    i = 1
    num_of_words = input("how many words would you like in the list? ")
    while i <= (int(num_of_words)): 
        word = input("input word " + str(i) + ": " )
        new_list2.append(word)
        i += 1  
    print(countWords(new_list2))  
    
    #################### test 3 - Q3 ####################  
    new_list3=[]  
    i = 1
    num_of_words = input("how many words would you like in the list? ")
    while i <= (int(num_of_words)): 
        word = input("input word " + str(i) + ": " )
        new_list3.append(word)
        i += 1  
    print(countWords(new_list3))  
    
    #################### test 1 - Q4 ####################  
    result1 = readWords("hw_test1.txt")  
    print(f"Result  :{result1}") 
    print(f"Expected:['hello', 'class!', 'This', 'is', 'test', '1', 'of', 'the', 'homework', 'I', 'am', 'a', 'slice', 'of', 'bologna!']") 
    print('\t')

    #################### test 2 - Q4 #################### 
    result2 = readWords("hw_test2.txt") 
    print(f"Result  :{result2}") 
    print(f"Expected:['Hi', 'again', 'class!', 'This', 'is', 'test', '2', 'of', 'the', 'homework.', 'do', 'you', 'like', 'fruit?']")
    print('\t')

    #################### test 3 - Q4 ####################  
    result3 = readWords("hw_test3.txt") 
    print(f"Result  :{result3}") 
    print(f"Expected:['Goodbye', 'class!', 'This', 'is', 'test', '3', 'of', 'the', 'homework.', 'It', 'was', 'fun', 'working', 'with', 'you', 'all!']")
    print('\t')
    
    
    

if __name__ == "__main__": 
    main()