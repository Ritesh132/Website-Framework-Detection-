from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Add your scraping logic here
        # For example, extracting all the links on the page:
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return render_template('result.html', url=url, links=links)
    except requests.exceptions.RequestException as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
