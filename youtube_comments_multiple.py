import time, codecs, os
from selenium import webdriver

os.chdir("C:\\Users\\DaLaw\\Desktop\\CCYC")

with open("C:\\Users\\DaLaw\\Desktop\\CCYC\\YT_ID_list_test.txt") as fin:
    # for line in fin:
    iDlist = fin.read()
    iDlist = iDlist.split()

driver = webdriver.Chrome("C:\\Users\\DaLaw\\Downloads\\chromedriver_win32\\chromedriver.exe")

for readID in iDlist:
    print("I'm working on ID:" + readID + " right now!")

    driver.get("https://www.youtube.com/watch?v=" + readID)

    driver.execute_script('window.scrollTo(1, 500);')

    #now wait to load the comments
    time.sleep(12)
    height = 500
    prev_len = 0
    # comment_div = []
    comments = []
    while True:
        driver.execute_script("window.scrollTo(0, " + str(height) + ");")
        height += 3000
        print("Scrolling...")
        time.sleep(5)
        # comment_div = driver.find_element_by_xpath('//*[@id="contents"]')
        comments = driver.find_elements_by_xpath('//*[@id="content-text"]')
        if prev_len == len(comments):
            break
        prev_len = len(comments)

    with codecs.open("C:\\Users\\DaLaw\\Desktop\\CCYC\\comments_for_" + readID + ".txt", "w", encoding="utf-8") as fout:
        for comment in comments:
            # print(comment.text)
            fout.write(comment.text + "\n")

    # print("Done working on" + readID)

print("Comments download completed!")

driver.quit()