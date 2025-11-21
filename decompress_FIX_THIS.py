
'''
Original text:
'''
original = "the forest trail was quiet as the hikers walked along the narrow path. the trail curved gently around trees and rocks, and the hikers admired the tall trees. as the trail continued, the forest grew darker, but the hikers stayed close together along the trail."
#TODO: Print length of compressed text
print("original: ")


#TODO: Fill out the rest of this dictionary based on original text, above.
#(Hint: the word for 5 is trees)
# Dictionary from the activity
dictionary = {
    "1": "the",
    "2": "trail",
    "3": "hikers",
    "4": "forest",
    "5": "was",
    "6": "quiet",
    "7": "walked",
    "8": "along",
    "9": "narrow",
    "10": "path",
    "11": "curved",
    "12": "gently",
    "13": "around",
    "14": "trees",
    "15": "and",
    "16": "rocks",
    "17": "admired",
    "18": "tall",
    "19": "grew",
    "20": "darker",
    "21": "but",
    "22": "stayed",
    "23": "close",
    "24": "together",
    "25": "as",
}

#TODO: Fill out the rest of this compressed_text string with numbers and values, based on the dictionary
#(Hint: The next number is 6)
# Words that aren't repeated should just be written (like 'quiet' already is). 
# Punctuation should also be just written. Also spaces.
compressed_text = """
1 4 2 5 6 25 1 3 7 8 1 9 10. 1 2 11 12 13 14 15 16, 15 1 3 17 1 18 14. 25 1 2 continued, 1 4 19 20, 21 1 3 22 23 24 8 1 2.
"""

def decompress(text, dictionary):
    tokens = text.split() #returns list of substrings. By default, splits on spaces & other whitespace
    output_words = []
    
    #TODO Complete the for loop in line 53, which should iterate over the tokens list just created
    for token in tokens:
        word = token
        punctuation = ""
        
        # If the token ends with punctuation, separate it
        if not token[-1].isalnum():
            word = token[:-1]
            punctuation = token[-1]
        
        # Replace numeric codes with dictionary words
        if word in dictionary:
            decompressed = dictionary[word]
        else:
            decompressed = word
        
        # Reattach any punctuation
        #TODO: Add the *end* of the output variable the decompressed word plus any punctuation:
        output_words.append(decompressed + punctuation)
    
    return " ".join(output_words)

#TODO: Assign to the following variable the result of calling the decompress function with the appropriate variables 
decompressed_output = decompress(compressed_text, dictionary)
print("\n" + decompressed_output + "\n")