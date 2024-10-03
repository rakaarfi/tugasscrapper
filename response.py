import requests
from bs4 import BeautifulSoup as bs

HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

def get_request(url:str, session:requests.Session):
  response = session.get(url, headers=HEADERS)
  url = url + '?single=1'
  if response.status_code == 200:
    print(f"Getting requests from {url}")
    soup = bs(response.content, 'html.parser')
  else:
    soup = None
    print(f"Failed to get response from {url}, status code: {response.status_code}")

  return soup, response.status_code
  
if __name__ == '__main__':
  url = 'https://news.detik.com/'
  soup, status = get_request(url=url)
  print(f"Status code: {status}")
  # print(get_request(url=url))