import time, os, codecs, re
from selenium import webdriver

#Change the directory
os.chdir("C:\\Users\\LawTheFamily\\Desktop\\GC_talks\\")

#Locate the Chrome driver
driver = webdriver.Chrome("C:\\Users\\LawTheFamily\\Downloads\\chromedriver_win32\\chromedriver.exe")

#Define a fucntion to download talks
def download_talks(year, month, language):

    #Open the GC_titles file and store the titles in a list
    with open("C:\\Users\\LawTheFamily\\Desktop\\GC_talks\\GC_titles_" + str(year) + "_" + str(month) + ".txt") as fin:
        iDlist = fin.read()
        iDlist = iDlist.split()
        # print(iDlist)

    #Loop the titles, open Chrome driver, download the talks
    for read_titles in iDlist:
        print("I'm working on ID: " + read_titles + " right now!")

        driver.get("https://www.lds.org/general-conference/" + str(year) + "/" + str(month) +
                   "/" + read_titles + "?lang=" + language)

        #Wait 3 second for loading the website
        time.sleep(3)

        #Grab the main text area by using xpath
        conf_text = driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/div')

        #Get the text and split it by each new line
        get_text = conf_text.text
        get_text = re.split(r"\n", get_text)

        #Output the talks into a text file encoded in utf-8
        with codecs.open("C:\\Users\\LawTheFamily\\Desktop\\GC_talks\\" + str(year) + "_" +
                                 str(month) + "_" + read_titles + "_" + language + ".txt", "w", encoding="utf-8") as fout:
            for text in get_text:
                # print(text)
                fout.write(text + "\n")

#----------------------------------------------------------------------------------------------------------------------#

###Main script###

#Run the function below. Needed arguments: year, month, and language codes (eng, jpn, etc...)

download_talks(2017,10,"jpn")

print("Completed! All downloaded!")

#Close the driver

driver.quit()