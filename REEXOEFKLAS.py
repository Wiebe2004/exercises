import re
import requests

def extract_urls(url):
    response = requests.get(url)
    html = response.text

    url_pattern = 'https?:\/\/[^\s]+\.(?:jpg|jpeg|png|gif|bmp|webp|svg)'
    urls = re.findall(url_pattern, html)
    return urls

def main():
    url = "https://www.bol.com"
    urls = extract_urls(url)
    for url in urls:
        print(url)

main()