import re

#The following function calculate the normalized counts.
def normalized_count(tWord,tFind):
    count = (tFind / tWord) * 100
    return count

#The following sets up variables and lists
pronouns = ["I", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them"]
modals = ["must", "shall", "will", "should", "would", "can", "could", "may", "might"]

num_of_word_1 = 0
num_of_word_2 = 0

num_of_findings_1 = 0
num_of_findings_2 = 0

#The following prompts ask for two texts
text_1 = input("Please paste the first text here:\n")
text_2 = input("Please paste the second text here:\n")

#Split the texts
text_1 = text_1.lower().split()
text_2 = text_2.lower().split()

#Find the prnouns, contraction, and modals in the first text
#print("text 1 begins...")
for word_1 in text_1:
    word_1 = word_1.strip()
    num_of_word_1 += 1
    if re.findall(r"([\'\’][msdt|ll|ve|re|all])", word_1) or word_1 in pronouns or word_1 in modals:
        #print(word_1)
        num_of_findings_1 += 1

# Find the prnouns, contraction, and modals in the second text
#print("\ntext 2 begins...")
for word_2 in text_2:
    word_2 = word_2.strip()
    num_of_word_2 += 1
    if re.findall(r"([\'\’][msdt|ll|ve|re|all])", word_2) or word_2 in pronouns or word_2 in modals:
        #print(word_2)
        num_of_findings_2 += 1

#The following prints various results
print("The total number of words in the first text: " + str(num_of_word_1))
print("The total number of words in the second text: " + str(num_of_word_2))
print("The total number of findings in the first text: " + str(num_of_findings_1))
print("The total number of findings in the second text: " + str(num_of_findings_2))

#The following uses the normalized_count function
first_text = normalized_count(num_of_word_1,num_of_findings_1)
second_text = normalized_count(num_of_word_2,num_of_findings_2)

#Print out the normalized counts for each text
print("The normalized count for the first text: " + str(round(first_text,2)))
print("The normalized count for the second text: " + str(round(second_text,2)))

'''
------------------------Report----------------------------
Actual findings that are correct for text 1 = 44
Actual findings that are correct for text 2 = 35
----------------------------------------------------------
         |      Precision        |         recall        |
----------------------------------------------------------
1st text |      44/52 = 85%      |      44/44 = 100%     |
2nd text |      35/48 = 73%      |      35/35 = 100%     |
----------------------------------------------------------
'''