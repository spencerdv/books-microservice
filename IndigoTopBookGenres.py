# This application scrapes data presented by Indigo.com
# URL: https://www.indigo.ca/en-ca/books/best-books-of-the-year/top-10-books-by-genre/
# Accessed: 2/22/24

import requests
import json
import re
#from bs4 import BeautifulSoup

# Indigo Scrape
search_url = 'https://www.indigo.ca/en-ca/books/best-books-of-the-year/top-10-books-by-genre/'

valid_genres = ['cookbooks', 'fantasy', 'fiction', 'historical-fiction', 'horror', 'mystery', 'non-fiction',
                'queer-voices', 'romance', 'thrillers']


while True:
    print('Please enter a genre you are most interested in.\nYou may select from: cookbooks, romance, fantasy, horror, historical-fiction, mystery, non-fiction, thrillers or queer-voices. \nYou may enter "q" to quit.')

    # Obtains input from user
    genre_selected = input()
    genre_selected = genre_selected.lower()
    if genre_selected == 'q':
        break

    
    # Validates input from user
    while genre_selected not in valid_genres:
        print("That genre was not valid. \nPlease enter a genre you are most interested in.\nYou may select from: cookbooks, romance, fantasy, horror, historical-fiction, mystery, non-fiction, thrillers or queer-voices.")
        genre_selected = input()
        genre_selected = genre_selected.lower()

    # Gets data from Indigo.com
    response = requests.get(f'{search_url}{genre_selected}/')

    response.json
    #print(response)
    text = response.text
    # print(text)
    book_list = []

    # Uses Regex expressions to parse through data
    search_list = re.findall('data-home-product-title=.*', text)

    for collection in search_list:
        result = collection[25:]
        book_list.append(result)

    title_list = []

    for book in book_list:
        match_object = (re.search('data', book))
        title_list.append(book[:match_object.start() - 2])

    # Formats the text to handle title add-ons from Indigo.com
    for book in range(len(title_list)):
        if ': A Novel' in title_list[book]:
            index = int(title_list[book].index(':'))
            title_list[book] = title_list[book][:index]
        if 'Indigo Exclusive Edition' in title_list[book]:
            index = int(title_list[book].index('Indigo')) - 2 
            title_list[book] = title_list[book][:index]
        
    # Presents data to the user
    print(f"The current top selling books of the {genre_selected} genre are:\n")
    num = 1
    for book in title_list:
        print(f'{num}: {book}')
        num += 1
    print('\n')
    
# Farewell message
print("Thank you for using our service!")