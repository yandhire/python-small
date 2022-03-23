# Program to check if a passed letter is a vowel or not
# Yazılan harf ünlü mü değil mi bulmak için bir program

vowels = "aeıioöuü"

def checker(ch):
    if ch in vowels:
        return "The character is a vowel."
    else:
        return "The character is not a vowel."
    
print(checker("a"))
print(checker("p"))