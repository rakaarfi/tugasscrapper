from response import get_request
import requests

# Extract link
def get_link(soup):
  article = soup.find('div', class_='grid-row content__bg')

  content = article.find_all('a', class_='media__link')

  # Extract link from content
  link_list = []
  for i in content:
    href = i.get('href')

    if len(href) > 50 and "https://20.detik.com/" not in href and "https://news.detik.com/foto-" not in href:
      link_list.append(href)

  # Delete duplicate alternatif set
  unique_links = [i for n, i in enumerate(link_list) if i not in link_list[:n]]
  print(f"Total unique links found: {len(unique_links)}")

  return unique_links

# Extract img URL, Title, Content, author, date
def link_content(links):
  session = requests.Session()
  #links = links + '?single=1'
  response, check_status = get_request(url=links, session=session)
  print(f"Getting image, title, content, author, date from {links}")

  datas ={}
  if check_status == 200:
    article = response.find('article', class_='detail')

    # img = None
    # author = None
    # date = None
    # title = None
    # content = None

    try:
      img = article.find('img', class_='p_img_zoomin').get('src')
    except AttributeError as e:
      img = None
      print(f"An exception occurred: {e}")

    author = validate_datas(tag='div', classes='detail__author', article=article).get_text(strip=True)
    date = validate_datas(tag='div', classes='detail__date', article=article).get_text(strip=True)
    title = validate_datas(tag='h1', classes='detail__title', article=article).get_text(strip=True)
    
    # validate content in tag p
    contents = [
          p.get_text() for p in article.find_all('p') 
          if 'para_caption' not in p.get('class', []) 
          and 'Simak Video' not in p.get_text() 
          and "Gambas" not in p.get_text()
      ]
    content = " ".join(contents)
    print(f"Datas added")

    datas['Author'] = author
    datas['Date'] = date
    datas['Title'] = title
    datas['Image'] = img
    datas['Content'] = content
  return datas

def validate_datas(tag, classes, article):
  try:
    data = article.find(tag, class_=classes)
  except AttributeError as e:
    data = None
    print(f"An exception occurred: {e}")
  return data

def get_detail_link_content(links):
  all_data = []
  for link in links:
    data = link_content(links=link)
    all_data.append(data)
  
  print(f"Getting all data from each link content")
  return all_data

if __name__ == '__main__':
  #get_link(soup)
  print(link_content(links='https://news.detik.com/berita/d-7568026/tampang-mr-tersangka-baru-kasus-pembubaran-diskusi-di-kemang'))