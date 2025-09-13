'''
Create a new file named task5.py and inside create a list of your favorite books, including book
titles and authors. Use list slicing to print the first three books in the list. Create a dictionary that
represents a basic student database, including student names and their corresponding student IDs.
Implement pytest test cases to verify the correctness of your code for each data structure.
'''


# List of books and Authors
bookList = [
    'Audie Murphy: To Hell and Back',
    'F. Scott Fitzgerald: The Great Gatsby',
    'William Shakesphere: MacBeth',
    'Authur Miller: The Cruicible',
    'Harper Lee: To Kill a Mocking Bird'
]

# Fake student database from chatGPT with ID as keys and Names as Values
gptDatabase = {
    101 : 'Alice Johnson',
    102 : 'Brandon Lee',
    103 : 'Chloe Martinez',
    104 : 'Daniel Kim',
    105 : 'Emily Carter',
}

print(f'First 3 authors in the list {bookList[0:3:1]}')