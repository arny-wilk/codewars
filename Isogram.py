''' An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case 

example: (input -> output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)

'''

def is_isogram(string):
    #your code here
    
    # Convert the word or sentence in lower case letters.
    clean_word = string.lower()
    
    # Make an empty list to append unique letters to
    letter_list = []
    
    for letter in clean_word :
        # If letter is an alphabet then only check
        if letter.isalpha():
            if letter in letter_list :
                return False
            letter_list.append(letter)
            
    return True

if __name__ == '__main__':
    print(is_isogram("Machine"))
    print(is_isogram("isogram"))                        
    print(is_isogram("GeeksforGeeks"))                    
    print(is_isogram("Alphabet "))
    print(is_isogram("Dermatoglyphics"))
    
# Other methods:

# with set :
def is_isogram(string):
    return len(string) == len(set(string.lower()))

# with count :

def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True


    