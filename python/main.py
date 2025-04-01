from curl_cffi import requests
from bs4 import BeautifulSoup
import json


def write_to_file(data: list, file_name: str):
    '''
    Write the data into a json file

    Args:
        data - list of dictionary
        file_name - string of the file name

    Returns:
        None
    '''
    print(f'Writing into {file_name}')
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def main():
    chicken_url = 'https://panlasangpinoy.com/categories/recipes/chicken-recipes/page/'
    pork_url = 'https://panlasangpinoy.com/categories/recipes/pork-recipes/page/'
    beef_url = 'https://panlasangpinoy.com/categories/recipes/beef-recipes/page/'
    vegy_url = 'https://panlasangpinoy.com/categories/recipes/vegetable-recipes/page/'
    fish_url = 'https://panlasangpinoy.com/categories/recipes/fish-recipes-recipes/page/'


if __name__ == '__main__':
    main()
