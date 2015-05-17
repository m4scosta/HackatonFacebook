import requests
import json
from bs4 import BeautifulSoup


class TudoGostosoCrawler():

	def __init__(self):
		self.recipes = []

	def crawl(self, urls):
		success = 0
		while success < 100:
			success += int(self._crawl_url(next(urls)))

	def _crawl_url(self, url):
		response = requests.get(url)

		if response.status_code != 200:
			print("\nerr\n")
			return 0

		soup = BeautifulSoup(response.content.decode("utf-8"))

		ingredients_html, instructions_html = soup.findAll("div", {"class": 'recipelist'})
		img = soup.find("img", {"class": 'photo pic'})

		picture_url = img["src"].strip().replace("thumb", "gallery") if img else None
		name = soup.find("div", {"class": "page-title item"}).text.strip()
		prep_time = soup.find("span", {"class": "preptime"}).text.strip()
		portions = soup.find("span", {"class": 'yield'}).text.strip()
		ingredients = [ingr.text.strip() for ingr in ingredients_html.findAll("span")]
		instructions = [instr.text.strip() for instr in instructions_html.findAll("span")]

		self._add_recipe(
			name=name, prep_time=prep_time, picture_url=picture_url,
			portions=portions, ingredients=ingredients, instructions=instructions)
		return 1

	def _add_recipe(self, **recipe):
		self.recipes.append(recipe)


def urls_to_crawl():
	n = 100
	while True:
		url = "http://www.tudogostoso.com.br/receita/{}-whatever.html".format(n)
		print("{} generated".format(url))
		n += 1
		yield url


if __name__ == "__main__":
	crawler = TudoGostosoCrawler()
	crawler.crawl(urls_to_crawl())

	json_string = json.dumps(crawler.recipes, indent=4, sort_keys=True)

	with open("../recipes.json", "w") as json_file:
		json_file.write(json_string)

	print(json_string)
