import re

def  count_text(text):

    with open(text, 'r') as file:
        content = file.read()
    
    words = re.findall(r'\b\w+\b', content)
    num_words = len(words)

    return num_words
