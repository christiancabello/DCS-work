########## HW 2 ########## -- used geeksforgeeks for max key recognition

import string

def readText(filename: str) -> list[str]: 
    ''' 
    definition: this function accepts and reads a filename and 
    returns a list of all words present in the file without punctuation

    Parameters: 
        filename: txt file with words and lines
    Returns: 
        word_list: list of all words present in the file
    ''' 
    word_list = []   
    with open(filename, "r") as infile: 
        line = infile.readline() 
        while line != "": 
            line_items = line.strip().split() 
            for item in line_items: 
                word = str(item)  
                for punctuation in string.punctuation: 
                    word = word.replace(punctuation, '')  
                if word == '': 
                    pass 
                else: 
                    word_list.append(word)   
            line = infile.readline() 
    return word_list  

def findMostFrequentWord(words: list[str]) -> tuple: 
    ''' 
        definition: this function builds a dictionary of unique words 
        and returns a tuple with the largest count word

    Parameters: 
        words: list of strings 
    Returns: 
        max_word: tuple of word with highest count
    ''' 
    result_dict = {}  
    for word in words:  
        if word in result_dict: 
            result_dict[word] += 1 
        else: 
            result_dict[word] = 1   
    max_value = max(result_dict, key=result_dict.get)  
    result_tuple = (max_value, result_dict[max_value])
    return result_tuple

def main() -> None:  
    #################### test 1   
    filename = "randomwords.txt"  
    result = findMostFrequentWord(readText(filename))  
    print(f"Actual: {result}") 
    print(f"Expected:('hi', 7)") 
    print('\n')

    #################### test 2   
    filename = "randomwords2.txt"
    result2 = findMostFrequentWord(readText(filename)) 
    print(f"Actual: {result2}") 
    print(f"Expected:('correspond', 3)")
    print('\n')

    #################### test 3    
    filename = "randomwords3.txt" 
    result3 = findMostFrequentWord(readText(filename)) 
    print(f"Actual: {result3}") 
    print(f"Expected:('dried', 6)")
    print('\n')

if __name__ == "__main__": 
    main() 
