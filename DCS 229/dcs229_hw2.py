import sys 
    
### 3 functions: 
''' 
1st: removes all words based on the green letters
2nd: removes all words based on the yellow letters 
3rd: removes all words based on the gray letters 

'''
#############################################################


'''
    definition: this function accepts each word in the
    file and a string containing the current wordle guess. It 
    then returns True or False based on whether or not the 
    word is a valid guess. 

    Parameters: 
        wordle_guess: string containing the current wordle guess 
        word: current possible wordle answer
    Returns: 
        True or False based on if the word can be used as 
        a possible wordle guess 
'''

def GreenLetters(wordle_guess: str, word: str) -> str:  
    let_num = 0  
    for letter_guess in wordle_guess: 
        if letter_guess == '.':  
            let_num += 1
        else: 
            i = let_num 
            if letter_guess == word[i]: 
                let_num += 1 
    if let_num != 5: 
        return False
    else: 
        return True 

#############################################################

# 2nd function: removes all words based on the yellow letters 
# change all_words to word: str 
'''
    definition: this function accepts each word left in the 
    file and a dictionary containing possible letters and 
    the positions they cannot have in the final word. It then 
    returns True or False based on whether the word is a 
    valid guess.

    Parameters: 
        my_dict: dictionary containing letter keys and 
        values corresponding to invalid positions 
        word: current possible wordle answer
    Returns: 
        True or False based on if the word can be used as 
        a possible wordle guess  
'''
def YellowLetters(my_dict: dict, word: str) -> dict[str, list[int]]:   
    i = 0  
    if my_dict == None: 
        return True
    for key in my_dict.items():  
        if key[0] in word:  
            char_num = key[0]    
            value = my_dict[char_num[i]] 
            for v in value:  
                if char_num == word[int(v)]:
                    return False  
        else: 
            return False    
    return True  

#############################################################

#3rd function: removes all words based on the gray letters  
'''
    definition: this function accepts each word left in the
    file and a set containing all invalid letters and returns 
    True or False based on whether or not the word is a valid 
    guess. 

    Parameters: 
        invalid_letters: set with all invalid letters 
        word: current possible wordle answer
    Returns: 
        True or False based on if the word can be used as 
        a possible wordle guess 
'''
def GrayLetters(invalid_letters: set, word: str) -> set | None: 
    if invalid_letters == None: 
        return True 
    else:  
        for invalid_letter in invalid_letters:    
            if invalid_letter in word:  
                return False  
    return True

#############################################################
''' 
    definition: this function accepts and reads a filename  
    and returns a list of all words present in the file 

    Parameters: 
        filename: txt file with words and lines
    Returns: 
        word_list: list of all words present in the file 
'''
     
def readText(filename: str) -> list[str]: 
    word_list = []   
    with open(filename, "r") as infile: 
        line = infile.readline() 
        while line != "": 
            line_items = line.strip().split() 
            word_list.extend(line_items)   
            line = infile.readline()  
    infile.close()
    return word_list ## the variable word_list will be called to words: list[str] in the function ## 


##########################################################################################################################
## main operating function

def showPossibleWords(words:   list[str], 
                        letters: str, 
                        also:    dict[str, list[int]] | None, 
                        gone:    set | None) -> None:  
    ''' 
    definition: this function accepts a list of all possible 
    wordle words, the current wordle guess, the possible wordle 
    letters, and letters that cannot be used in the word. It then 
    passes these parameters to separate functions based on the 
    color of each letter and removes inapplicable words accordingly. 

    Parameters: 
        words: txt file with all possible wordle answers
        letters: current wordle guess
        also: correct letters with incorrect position
        gone: letters than cannot be included in the word
    Returns: 
        words: updated file with all possible wordle guesses
    '''
    for word in reversed(words):  
        remove_list = [] 
        GreenLetters(letters, word) 
        if GreenLetters(letters, word) == False: 
            remove_list.append(word)
        if word in remove_list: 
            pass       
        else: 
            YellowLetters(also, word) 
            if YellowLetters(also, word) == False: 
                remove_list.append(word)     
        if word in remove_list: 
            pass
        else:  
            GrayLetters(gone, word) 
            if GrayLetters(gone, word) == False: 
                remove_list.append(word)   
        if word in remove_list: 
            words.remove(word)
    for word in words: 
        print(word)



##########################################################################################################################

# this is the function that calls the other green, yellow, and gray functions, and pass word as a parameter
# rather than all words 


def main() -> None:  
    words_result = readText("wordle_answers.txt") 
    sys.argv = ["wordle_answers.txt", "she..", "", "trnik"]  
    #filename = sys.argv[0]  
    #file_words = ReadText(filename)  
    my_dict = {}     
    if sys.argv[2] == None: 
        pass 
    else: 
        for element in sys.argv[2]:   
            if element in 'abcdefghijklmnopqrstuvwxyz':    
                letter = element 
                my_dict[letter] = 'a' 
                num = [] 
            else: 
                my_dict = my_dict   
                if element in '123456789':  
                    position = int(element) - 1
                    num += str(position) 
                    if my_dict[letter] == 'a':  
                        my_dict[letter] = num 
                    else: 
                        my_dict = my_dict  
    #arguments = sys.argv[1]    
    #possible_letters = sys.argv[2]  
    #my_word = 'hello'
    #invalid_letters = set(sys.argv[3])   
    while len(sys.argv[1]) != 5: 
        sys.argv[1] += '.'
    if len(sys.argv[1]) == 5:  
        if sys.argv[3] == None: 
            showPossibleWords(words_result, sys.argv[1], my_dict, None)  
        else:  
            showPossibleWords(words_result, sys.argv[1], my_dict, sys.argv[3])  
    #RemoveLetters(my_set)  
    #GrayLetters(invalid_letters, my_word) 
    #YellowLetters(possible_letters, my_word) 
    #GreenLetters(arguments, my_word)  


if __name__ == "__main__":
    main() 

