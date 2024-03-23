def remove_vowels(text):
    vowels = "AEIOUaeiou"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result
    
text = input("Enter tweet: ")
text = remove_vowels(text)
print(f"You tweet: {text}")    