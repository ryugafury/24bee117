import string

def ispangram(sentence):
    
    sentence_set = set(sentence.lower())
    
   
    alphabet_set = set(string.ascii_lowercase)
    
    
    return alphabet_set <= sentence_set

# Test cases
test_sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Crazy Fredrick bought many very exquisite opal jewels",
    "Hello world!"
]

for sentence in test_sentences:
    print(f"'{sentence}' is a pangram: {ispangram(sentence)}")