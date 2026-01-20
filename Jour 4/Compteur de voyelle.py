def count_vowels(text):
    vowels = "aeuioyAEYUIO"
    count = 0
    for char in text:
        if char in vowels:
            count = count + 1
    return count
input_text = input("Enter a text: ")
count_vowels(input_text)
print("The number of vowels in the text is:", count_vowels(input_text))
