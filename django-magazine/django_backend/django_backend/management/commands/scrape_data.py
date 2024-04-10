from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from product.models import Product
import requests
import uuid
from django.core.files.base import ContentFile

class Command(BaseCommand):
    help = 'Scrapping data product'

    def handle(self, *args, **options):
        for i in range(1, 6):
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
                'Referer': 'https://www.sex.com/'
            }
            response = requests.get("https://www.atbmarket.com/catalog/322-zamorozheni-produkti?page="+str(i), headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                elements = soup.find_all(class_='catalog-item')

                for element in elements:
                    title_element = element.find(class_='catalog-item__title')
                    price_element = element.find(class_='product-price__top').get('value')
                    image_url = element.find(class_='catalog-item__img').get('src')
                    link_url = element.find(class_='catalog-item__photo-link').get('href')

                    if title_element.text and price_element and image_url and link_url:
                        img = requests.get(image_url)

                        new_product = Product(title=title_element.text.rstrip(), price=price_element, cat_id=4, slug=link_url.split("/")[-1])
                        image_data = ContentFile(img.content)
                        new_product.link_img.save(str(uuid.uuid4()) + '.jpg', image_data)

