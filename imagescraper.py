from bs4 import BeautifulSoup
import requests
from flask import Flask
from flask import jsonify

app = Flask(__name__)

#Take in a name of a wikipedia page from user by receiving a GET
#Go to the Wikipedia page, scrape the image found at the top right
#Return image to user as a string
@app.route('/<string:keyword>/')
def scrape_image(keyword):
  url = 'https://en.wikipedia.org/wiki/' + keyword
  res = requests.get(url)
  if res.status_code == 200:
    soup = BeautifulSoup(res.content)
    image = soup.select('table.infobox a.image img[src]')
    response = jsonify({'imageLink':image[0]['src']})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, 200
  else:
    return "Error, action unsuccessful", 404

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=31598)