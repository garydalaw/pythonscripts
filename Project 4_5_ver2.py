import re, os

#Defining functions
def normalized_count(tFind, tWord):
    nom_count = (tFind / tWord) * 1000
    return round(nom_count, 2)

'''This function takes five arguments, so that all the features found 
    from a register can be written into the output file in the meantime
'''
def find_pattern(register, feature1, feature2, feature3, type):
    lineCounter = 0
    tWcount = 0
    F1count = 0
    F2count = 0
    F3count = 0
    print("Finding patterns on " + type)

    #The following will open files and identify the features
    for file in register:
        ofile = open(file)
        for line in ofile:
            lineCounter += 1
            if lineCounter < 8:
                continue
            else:
                line = re.sub(r"^\<[hp]\>", "", line)
                split_word = line.lower().split()
                for f_pattern in split_word:
                    if len(f_pattern) > 1:
                        tWcount += 1
                        f_pattern = f_pattern.strip()
                        if re.findall(feature1, f_pattern):
                                F1count += 1
                        elif f_pattern in feature2:
                                F2count += 1
                        elif f_pattern in feature3:
                                F3count += 1

    #The following calculates the normalized count by utilize the function normalized_count
    nom1 = normalized_count(F1count, tWcount)
    nom2 = normalized_count(F2count, tWcount)
    nom3 = normalized_count(F3count, tWcount)

    #The following output the csv file
    with open("C:\\Users\\DaLaw\\Documents\\Mini-CORE_new\\result.csv", "a") as f_out:
        f_out.write(type + "\t" + str(nom1) + "\t" + str(nom2) + "\t" + str(nom3) + "\n")

#-----------------------------------------------------------------------------------------------------------------------

#The following sets up variables and lists
pronouns = ["I", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them"]
love_words = ["honey", "love", "sweetheart", "baby", "darling", "sweetie", "heart", "loves", "forever", "smile", "feel",
              "touch", "loving", "cute", "kiss", "kissing", "kisses", "kissed", "hug"]
contraction = r"([\'\’][msdt|ll|ve|re|all])"

#Change the directory
os.chdir("C:\\Users\\DaLaw\\Documents\\Mini-CORE_new")

#Read all the file in the current directory
file_in = [i for i in os.listdir() if re.search(r"\.txt$", i, flags=re.I)]

#Create a csv file
with open("C:\\Users\\DaLaw\\Documents\\Mini-CORE_new\\result.csv", "w") as f_out:
    f_out.write("Register\tContraction\tPronouns\tLove Words\n")

#Store each register into a list
print("Reading and categorizing files to different lists...please wait...")
for file_name in file_in:

    HIregister = [HI for HI in os.listdir() if re.search(r"^1\+HI+", HI)]
    IDregister = [ID for ID in os.listdir() if re.search(r"^1\+ID+", ID)]
    INregister = [IN for IN in os.listdir() if re.search(r"^1\+IN+", IN)]
    IPregister = [IP for IP in os.listdir() if re.search(r"^1\+IP+", IP)]
    LYregister = [LY for LY in os.listdir() if re.search(r"^1\+LY+", LY)]
    NAregister = [NA for NA in os.listdir() if re.search(r"^1\+NA+", NA)]
    OPregister = [OP for OP in os.listdir() if re.search(r"^1\+OP+", OP)]
    SPregister = [SP for SP in os.listdir() if re.search(r"^1\+SP+", SP)]

#Find features by using the find_pattern function defined above
find_pattern(HIregister, contraction, pronouns, love_words, "HI")
find_pattern(IDregister, contraction, pronouns, love_words, "ID")
find_pattern(INregister, contraction, pronouns, love_words, "IN")
find_pattern(IPregister, contraction, pronouns, love_words, "IP")
find_pattern(LYregister, contraction, pronouns, love_words, "LY")
find_pattern(NAregister, contraction, pronouns, love_words, "NA")
find_pattern(OPregister, contraction, pronouns, love_words, "OP")
find_pattern(SPregister, contraction, pronouns, love_words, "SP")


print("Finished!")

'''
------------------------Report----------------------------
I looked for contractions, pronouns, and words that are 
used when talking about love.

Accuracy calculation is based on the file: 
1+LY+SL+LY-LY-LY-LY+OL-SL-SL-SL+NNNN+0003397.txt

Total findings for feature 1 = 42
Total findings for feature 2 = 5
Total findings for feature 3 = 14

Actual findings that are correct for feature 1 = 21
Actual findings that are correct for feature 2 = 4
Actual findings that are correct for feature 3 = 13
----------------------------------------------------------
          |      Precision        |         Recall        |
----------------------------------------------------------
Feature 1 |      21/21 = 100%      |      21/42 = 50%     |
Feature 2 |      4/4 = 100%        |      4/5 = 80%       |
Feature 3 |      13/13 = 100%      |      13/14 = 93%     |
----------------------------------------------------------

Hypothesis: all features tend to occur more in song lyrics.

Result: my hypothesis seems to be true based on the data set.

'''