# This application scrapes data presented by Indigo.com
# URL: https://www.indigo.ca/en-ca/books/best-books-of-the-year/top-10-books-by-genre/
# Accessed: 2/22/24

import requests
import json
import re
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/genre/<genre_selected>')
def genre_response(genre_selected):

    # Indigo Scrape
    search_url = 'https://www.indigo.ca/en-ca/books/best-books-of-the-year/top-10-books-by-genre/'

    valid_genres = ['cookbooks', 'fantasy', 'fiction', 'historical-fiction', 'horror', 'mystery', 'non-fiction',
                    'queer-voices', 'romance', 'thrillers']

    # Obtains input from user
    genre_selected = genre_selected.lower()

    # Validates input from user
    if genre_selected not in valid_genres:
        return ("That genre you entered was not valid. \nPlease enter a genre you are most interested in.\nYou may select from: cookbooks, romance, fantasy, horror, historical-fiction, mystery, non-fiction, thrillers or queer-voices.")

    # Gets data from Indigo.com
    response = requests.get(f'{search_url}{genre_selected}/')

    response.json
    text = response.text
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
        elif 'indigo exclusive edition' in title_list[book]:
            index = int(title_list[book].index('indigo')) - 2 
            title_list[book] = title_list[book][:index]
        elif 'INDIGO EXCLUSIVE EDITION' in title_list[book]:
            index = int(title_list[book].index('INDIGO')) - 2 
            title_list[book] = title_list[book][:index]
        
    # Presents data to the user
    return title_list

app.run(debug=True)
