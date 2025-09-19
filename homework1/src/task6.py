'''
Create two new files named task6.py and task6_read_me.txt. Inside of task6_read_me.txt
Then write a program inside task6.py of that reads task6_read_me.txt and counts the number
of words in it. Include pytest test cases that verify the word count for each text file.
'''

import re

def  count_text(text):

    with open(text, 'r') as file:
        content = file.read()
    
    # re.findall will clean the text and leave only words and no puncuations
    words = re.findall(r'\b\w+\b', content)
    num_words = len(words)

    return num_words
