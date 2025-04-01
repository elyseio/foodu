from curl_cffi import requests
from bs4 import BeautifulSoup
import json


def write_to_file(data: list, file_name: str):
    print(f'Writing into {file_name}')
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def main():
    pass


if __name__ == '__main__':
    main()
