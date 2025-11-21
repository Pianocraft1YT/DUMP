
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
    "5": "",
    "6": "",
    "7": "",
    "8": "",
    "9": "",
    "10": "",
    "11": "",
    "12": "",
    "13": "",
    "14": "",
    "15": "",
    "16": "",
    "17": "",
    "18": "",
    "19": "",
    "20": "",
    "21": "",
    "22": "",
    "23": "",
    "24": ""
}

#TODO: Fill out the rest of this compressed_text string with numbers and values, based on the dictionary
#(Hint: The next number is 6)
# Words that aren't repeated should just be written (like 'quiet' already is). 
# Punctuation should also be just written. Also spaces.
compressed_text = """
1 4 2 8 quiet .
"""

def decompress(text, dictionary):
    tokens = text.split() #returns list of substrings. By default, splits on spaces & other whitespace
    output_words = []
    
    #TODO Complete the for loop in line 53, which should iterate over the tokens list just created
    for ? in ?
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
        output_words.?
    
    return " ".join(output_words)

#TODO: Assign to the following variable the result of calling the decompress function with the appropriate variables 
decompressed_output = ?
print("\n" + decompressed_output + "\n")