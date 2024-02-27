from bs4 import BeautifulSoup
from urllib.parse import urljoin

class CssSelectorParser:
    
    def _parse_book(self, root):
        result = {}
        title_elem = root.select_one('title')
        if title_elem is not None:
            title_text = title_elem.text
            result['title'] = title_text.strip()
        description = root.select_one('meta[description]')
        if description is not None:
            description_text = description.attrs['content']
            result['description'] = description_text.strip()
        price_elem = root.select_one('.product_main p.price_color')
        if price_elem is not None:
            price_text = price_elem.text
            result['price'] = price_text.strip()

        return result
    
    def _parse_next(self, root, base_url):
        links = root.select('.product_pod a')
        to_return = []
        for link in links:
            url = link.attrs['href']
            to_return.append(urljoin(base_url, url))
        next_page = root.select_one('li.next')
        if next_page is None:
            url = link.attrs['href']
            to_return.append(urljoin(base_url, url))
        return to_return
            
    
    def parse(self, content, base_url):
        soup = BeautifulSoup(content)
        element = soup.select_one('article.product_page')
        if element is not None:
            result = self._parse_book(soup)
            return result, []
        next_links = self._parse_next(soup, base_url)
        return None, next_links
        