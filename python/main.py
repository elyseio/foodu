from curl_cffi import requests
from bs4 import BeautifulSoup
import json


def make_request(url: str):
    '''
    Make the request to the url to parse the data

    Args:
        url - link string

    Returns:
        recipe_data - list of dictionary containing recipe name, url, img link
    '''

    # pagination
    page = 1

    # create a session
    s = requests.Session()

    # store parsed data
    recipe_data = []

    while True:
        domain = f'{url}{page}'
        print(domain)

        req = s.get(domain, impersonate='chrome')

        soup = BeautifulSoup(req.text, 'lxml')
        recipes = soup.select('.category-recipes')

        # checks if there are recipe, if none, break out of the loop and return data
        if recipes:
            for recipe in recipes:
                recipe_name = recipe.select_one('.entry-title-link')
                link = recipe_name.get('href', None)
                img = recipe.select_one('.aligncenter.post-image.entry-image')
                if img:
                    img_link = img.get('data-src', None)
                else:
                    img_link = None
                data = {
                    'recipe': recipe_name.text,
                    'url': link,
                    'img': img_link
                }
                recipe_data.append(data)
        else:
            break

        # iterate pages
        page += 1

    return recipe_data


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
    '''
    Contains the url for scraping data, after scraping writes it to a json file
    '''
    chicken_url = 'https://panlasangpinoy.com/categories/recipes/chicken-recipes/page/'
    pork_url = 'https://panlasangpinoy.com/categories/recipes/pork-recipes/page/'
    beef_url = 'https://panlasangpinoy.com/categories/recipes/beef-recipes/page/'
    vegy_url = 'https://panlasangpinoy.com/categories/recipes/vegetable-recipes/page/'
    fish_url = 'https://panlasangpinoy.com/categories/recipes/fish-recipes-recipes/page/'

    # Chicken Recipes
    chicken_recipes = make_request(chicken_url)

    # Pork Recipes
    pork_recipes = make_request(pork_url)

    # Beef Recipes
    beef_recipes = make_request(beef_url)

    # Vegetable Recipes
    vegy_recipes = make_request(vegy_url)

    # Fish Recipes
    fish_recipes = make_request(fish_url)

    # Write to file
    write_to_file(chicken_recipes, 'chicken_recipes.json')
    write_to_file(pork_recipes, 'pork_recipes.json')
    write_to_file(beef_recipes, 'beef_recipes.json')
    write_to_file(vegy_recipes, 'vegy_recipes.json')
    write_to_file(fish_recipes, 'fish_recipes.json')


if __name__ == '__main__':
    main()
