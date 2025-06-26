from bs4 import BeautifulSoup
import requests

url = "https://timesofindia.indiatimes.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

headline = soup.find("figcaption").get_text()
#print(headline)

with open("headlines.txt", "a") as file:
    file.write(f"{headline}\n")
print("Headline saved to headlines.txt")
