import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from multiprocessing import Pool

def get_download_list(url, destination_folder):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    a_tags = soup.findAll('a')

    return [(url + link['href'], destination_folder + link['href']) for link in a_tags]

def download_file(file_tuple):
    try:
        print(file_tuple[0] +  file_tuple[1])
        urllib.request.urlretrieve(file_tuple[0], file_tuple[1].replace(' ', ''))
    except:
        print(f'unable to download file: \'{file_tuple[0]}\' into folder: \'{file_tuple[1]}\'...')

if __name__ == '__main__':
    files_url = 'http://vizzed.net/gba/files/'
    destination_folder = 'Z:\\gba\\roms\\'
    download_list = get_download_list(files_url, destination_folder)

    with Pool(5) as p:
        p.map(download_file, download_list)

    print('success!')
