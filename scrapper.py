import requests
import json
import time
from bs4 import BeautifulSoup

with open("./codes.json", 'r') as j:
     ids = json.loads(j.read())

with open('results.csv', 'a') as the_file:
    for elem in ids["ids"]:

        time.sleep(1)

        URL = "https://epicov.org/epi3/epi_set/EPI_SET_20220616yx?detail=" + elem
        #test = "https://epicov.org/epi3/epi_set/EPI_SET_20220616yx?detail=EPI_ISL_452634/e3470fbb68c543069cb52d22ad0c1dd8"

        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")
        datadiv = soup.find("div", id="popup-content")
        children = datadiv.findChildren("div")

        try:
            line = children[0].text + ";" + \
                children[1].text.split(": ")[1] + ";" + \
                children[2].text.split(": ")[1] + ";" + \
                children[3].text.split(": ")[1] + ";" + \
                children[4].text.split(": ")[1] + ";" + \
                children[5].text.split(": ")[1] + '\n'

            #print(line)
            the_file.write(line)
        except:
            print("Error while processing " + elem)


