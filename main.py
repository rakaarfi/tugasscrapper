from response import get_request
from parsing import get_link, get_detail_link_content
from export import exportPandas
import requests

def main(url):
  session = requests.Session()
  soup, check_status = get_request(url, session)
  link = get_link(soup)
  datas = get_detail_link_content(link)
  exportPandas(datas, 'datas_export')
  exportPandas(link, 'link_export')
  # tidak perlu
  return link, datas

if __name__ == '__main__':
  url = 'https://news.detik.com/'
  main(url=url)