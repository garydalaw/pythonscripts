import os, re, json, datetime


def get_cap(list):
    counter = 0
    string_comments = []
    allCap = []
    for s in list:
        string_list = re.split(r"\s", s)
        string_comments.append(string_list)

    for listoflist in string_comments:
        for string in listoflist:
            if re.search(r"^[A-Z]{2,}", string):
                counter += 1
                allCap.append(string)

with open("C:\\Users\\LawTheFamily\\Documents\\BYU Fall 2017\\Ling 360\\yelp_100K_2017.json", encoding="utf-8") as fin:

    # string_comments = []
    oneStar_comments = []
    oneStar_allCap = []
    oneStar_allCap_counter = 0
    fiveStar_comments = []
    fiveStar_allCap = []
    fiveStar_allCap_counter = 0

    for review in fin:
        review = json.loads(review)
        if review["stars"] == 1:
            oneStar_comments.append(review["text"])
        elif review["stars"] == 5:
            fiveStar_comments.append(review["text"])
    #
    # for s in oneStar_comments:
    #     string_list = re.split(r"\s", s)
    #     string_comments.append(string_list)
    #
    # for listoflist in string_comments:
    #     for string in listoflist:
    #         if re.search(r"^[A-Z]{2,}", string):
    #             oneStar_allCap.append(string)
    #
    # for aC in oneStar_allCap:
    #     print(aC)
