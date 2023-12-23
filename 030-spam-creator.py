# As the assignment is so vague (just "spam creator"), there's many ways to approach this.
# Where to spam? Forums, site comments, specific social media profiles, reviews for a business, self-promotion, etc...
# I decided to harness "annoying phrases" from a NYT article: https://nypost.com/2022/10/23/annoying-people-say-these-75-things-according-to-reddit-users/
# Then you can enter a victim URL that the trash will be posted to.
# In 99% of cases, you will need to alter the post parameters, probably add cookies, stuff like that.  But ya know, an annoying and simple framework exists below.
import requests
from bs4 import BeautifulSoup
import random
import re

def get_random_sentences(url, num_sentences=2):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return []

    bs = BeautifulSoup(response.content, 'html.parser')
    text = bs.get_text()
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    sentences = [s.strip() for s in sentences if len(s.split()) > 5]
    randomcrap = random.sample(sentences, min(num_sentences, len(sentences)))

    return randomcrap

def post_garbage(sentences, endpoint):
    message = " ".join(sentences)
    response = requests.post(endpoint, data={'msg': message, 'user': 'guest', 'submit': 'Submit"})

    if response.status_code == 200:
        print("Spamming successful")
    else:
        print("plans have failed")

if __name__ == "__main__":
    url = "https://nypost.com/2022/10/23/annoying-people-say-these-75-things-according-to-reddit-users/"
    endpoint = input("Enter sad victim URL: ") 

    sentences = get_random_sentences(url)
    print("\nRandom trash:")
    for idx, sentence in enumerate(sentences, 1):
        print(f"{idx}. {sentence}")

    post_garbage(sentences, endpoint)
