import bs4
import requests
import lxml
import json
import re
from pprint import pprint


def data(url):
    # list of abusive words
    info = requests.get("https://www.cs.cmu.edu/~biglou/resources/bad-words.txt")
    soup = bs4.BeautifulSoup(info.text, "lxml")

    abusive_words = []
    abusive_words = soup.text.split()
    #print(abusive_words)

    # data from the website we will scrape 
    info_url = requests.get(url)
    soup_url = bs4.BeautifulSoup(info_url.text, "lxml")
    my_data = []
    my_data = soup_url.text.split()
    #print(my_data)

    count = 0
    mal_words = []
    for word in range(len(my_data)):
        for abusive_word in range(len(abusive_words)):
            if my_data[word] == abusive_words[abusive_word]:
                mal_words.append(abusive_words[abusive_word])
                count += 1
    if count == 0:
        return "this website is safe"
    else:
        return f"contains {count} malicious words"

    #return [count, mal_words]

print(data("https://lowvelder.co.za/424505/advantages-time-management/#:~:text=Time%20management%20helps%20children%20prioritize,decisions%20and%20work%20more%20efficiently."))
#data("https://www.dictionary.com/browse/fuck")

    my_data = ""
    my_data += soup.text
    data = my_data.split()
    for i in range(len(data)):
        if(profanity.contains_profanity(data[i])):
            return False
    return True


#Counts the Number of vulgar words in the url
def getNumOfBadWords(url):
    num_of_bad_words = 0
    info = requests.get(url)
    soup = bs4.BeautifulSoup(info.text, "lxml")
    my_data = ""
    my_data += soup.text
    data = my_data.split()
    for i in range(len(data)):
        if profanity.contains_profanity(data[i]):
            print(data[i])
            num_of_bad_words += 1

    return num_of_bad_words

