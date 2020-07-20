import re, random
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup as bs

#Define a function to retrive body text from a website
def getBodyText(url):
    try:
        open_page = urlopen(url)    #open the url
        read_page = bs(open_page, "lxml")   #read the url
    except HTTPError and AttributeError:    #check if there is any error
        return None

    #Create a list of links from the website provided
    links = [i.attrs["href"] for i in read_page.find_all("a")]
    #Exclude all of the internal links
    links = [i for i in links if re.search(r"^http", i)]

    #This counter uses for numbering a file below
    counter = 1

    #The for loop will run 5 times, which means to scrape the website 5 times
    for n in range(5):
        random_num = random.randint(0, len(links) - 1)  #generate a random number
        url = links[random_num] #pass an index into the variable url
        print(url)
        o_link = urlopen(url) #open the url
        r_link = bs(o_link, "lxml") #read the url

        #The following will output the body text to a .txt file
        with open("C:\\Users\\DaLaw\\Desktop\\webscraping" + str(counter) + ".txt", "w", encoding="UTF-8") as fout:
            fout.write(urlparse(url).netloc + "\n")
            for i in r_link.find("body").find_all("p"): #find the p tag only within the body tag
                fout.write(i.get_text() + "\n") #output all of the text found inside the body tag
        counter += 1

"""
-----------------------------------------------------------------------------------------------------------------------
"""
#Call the function getBodyText
print(getBodyText("https://www.yahoo.com/news/"))
print("Finished!")

'''
Note:
The content of the body text in the output files may vary depending on the random num inside the function.
This will affect which website to be read every time it runs.
'''

