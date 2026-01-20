def consonne_vowels(text): 
    consonnes = 'ZRTPQSDFGHJKLMWXCVBNnbvcxwmlkjhgfdsqptrz'
    count = 0
    for char in text :
        if char in consonnes : 
            count += 1
    return count
input_text = input("Enter a text: ")
consonne_vowels(input_text) 
print("The number of consonnes in the text is:", consonne_vowels(input_text))