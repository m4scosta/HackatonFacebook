import requests
import json
from bs4 import BeautifulSoup


class TudoGostosoCrawler():

	def __init__(self):
		self.recipes = []

	def crawl(self, urls):
		for url in urls:
			self._crawl_url(url)

	def _crawl_url(self, url):
		response = requests.get(url)

		if response.status_code != 200:
			print("err")
			return

		soup = BeautifulSoup(response.content.decode("utf-8"))

		ingredients_html, instructions_html = soup.findAll("div", {"class": 'recipelist'})
		img = soup.find("img", {"class": 'photo pic'})

		picture_url = img["src"].strip() if img else None
		portions = soup.find("span", {"class": 'num yield'}).text.strip()
		ingredients = [ingr.text.strip() for ingr in ingredients_html.findAll("span")]
		instructions = [instr.text.strip() for instr in instructions_html.findAll("span")]

		self._add_recipe(picture_url=picture_url, portions=portions,
			ingredients=ingredients, instructions=instructions)

	def _add_recipe(self, **recipe):
		self.recipes.append(recipe)


def urls_to_crawl():
	for n in range(100, 200):
		url = "http://www.tudogostoso.com.br/receita/{}-whatever.html".format(n)
		print("{} generated".format(url))
		yield url


if __name__ == "__main__":
	crawler = TudoGostosoCrawler()
	crawler.crawl(urls_to_crawl())

	json_string = json.dumps(crawler.recipes, indent=4, sort_keys=True)

	with open("../recipes.json", "w") as json_file:
		json_file.write(json_string)

	print(json.loads(json_string))
