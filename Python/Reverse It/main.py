
def c_v_count(string): # returns a dictionary of the number of vowels and consonants
    vowels = 0
    consonants = 0
    string = string.lower();  
    for index in range(0,len(string)):   
        if string[index] in ('a',"e","i","o","u"): # vowels
            vowels = vowels + 1
        elif (string[index] >= 'a' and string[index] <= 'z'): # consonants
            consonants = consonants + 1
    return {"vowels": vowels, "consonants": consonants}


wordToReverse = input("What phrase or word would you like to be reversed? ")
if wordToReverse.find(" "):
    kind = "phrase"
else:
    kind = "word"
print(f"Your {kind} reversed: {wordToReverse[::-1]}")
print(f"Amount of vowels: {c_v_count(wordToReverse)['vowels']} \nAmount of consonants: {c_v_count(wordToReverse)['consonants']} ")