import os, re, json


# reviews = ["I LOVE that so much", "I love SEQUIOA trees", "I LIKE this restaurant SO MUCH.", "RESTAURANT CRAZY WAITER"]
#
# for review in reviews:
#     matches = re.findall(r"[A-Z]{2,}", review)
#     num_matches = len([i for i in matches])
#     print(num_matches)
#     for match in matches:
#         print(match)

import json, re
with open("C:\\Users\\LawTheFamily\\Documents\\BYU Fall 2017\\Ling 360\\yelp_100K_2017.json", encoding="utf-8") as fin:
    with open("C:\\Users\\LawTheFamily\\Desktop\\review_data.csv", "w") as fout:
        fout.write('Business ID\tStars\tCap words\tVery\n')
        for review in fin:
            review = json.loads(review)
            matches_1 = re.findall(r"[A-Z]{2,}", review["text"])
            matches_2 = re.findall(r"very", review["text"], flags=re.I)
            num_matches_1 = len([i for i in matches_1])
            num_matches_2 = len([j for j in matches_2])

            fout.write(review['business_id'] + '\t' + str(review['stars']) + '\t' +
                       str(num_matches_1) + "\t" + str(num_matches_2) + '\n')

