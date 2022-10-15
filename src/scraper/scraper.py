import requests
from bs4 import BeautifulSoup
from time import sleep


class SaladScraper:
    def __int__(self):
        pass

    def fetch_raw_recipes(self, url, headers):
        html = None
        print("Calling fetch raw information from recipes")
        try:
            req = requests.get(url, headers=headers)
            if req.status_code == 200:
                html = req.text
        except Exception as e:
            print(f"Exception while getting raw recipes {e}")
        finally:
            return html.strip()

    def get_all_recipes(self, headers):
        recipes = []
        url = "https://www.allrecipes.com/recipes/96/salad/"
        try:
            req = requests.get(url=url, headers=headers)
            if req.status_code == 200:
                html = req.text
                soup = BeautifulSoup(html, "html.parser")
                links = soup.findAll("a", {"class": "taxonomy-nodes__link"})
                idx = 0
                for link in links:
                    sleep(2)
                    if idx >= 9:
                        return
                    recipe = self.fetch_raw_recipes(link["href"], headers)
                    recipes.append(recipe)
                    idx += 1

        except Exception as e:
            print(f"Exception while getting all recipes {e}")
        finally:
            return recipes

    def scrape(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
            "Pragma": "no-cache",
        }
        return self.get_all_recipes(headers)
