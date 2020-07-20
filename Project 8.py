import re, os, nltk
from collections import Counter

#6 file registers: JA_BI, JA_HI, PS_BI, PS_HI, TB_BI, TB_HI

#Define a function for normalized count
def normalized_count(tFind, tWord):
    nom_count = (tFind / tWord) * 1000
    return round(nom_count, 2)

#Define a function for a total word count for each register
def countS(string):
    wd_count = 0
    string = string.split()
    for i in string:
        wd_count += 1
    return wd_count

#Define a function to output a NN sequence file
def nn_sequence(register, type):

    bString = ""
    nn_freq = {}
    print("Finding N+N sequence in a register " + type + "...")

    for file in register:
        #line_counter = 0
        with open(file) as fOpen:
            string = fOpen.read()
            string = re.sub(r"[\<\>\%]", "", string)
            string = string.lower().strip()
            bString += string   #save all the files of the current register as big string

    wd_count = countS(bString)  #Perform the total word count here
    #print(wd_count)

    token = nltk.word_tokenize(string)  #Tokenize words

    pos = nltk.pos_tag(token)   #POS tagging

    #The following for loop extracts NN sequence and export to a csv file
    for i in range(len(pos)):
        try:
            if re.search(r"NN|NNS|NP|NNPS", pos[i][1]) and re.search(r"NN|NNS|NP|NNPS", pos[i+1][1]):
                n1 = pos[i][0]
                n2 = pos[i+1][0]
                nn = n1 + "\t" + n2
                nn_freq[nn] = nn_freq.get(nn, 0) + 1    #Push the findings into an empty dictionary
        except IndexError:
            print("There is a single noun at the end.")

    nn_tuple = [t for t in nn_freq.items()]     #Convert the dictionary into a list of tuple

    new_dict = {}   #This new dictionary is used in the following for loop

    for n in range(len(nn_tuple)):
        #Get each value of each tuple from the list and run the normalized count
        nom = normalized_count(nn_tuple[n][1], wd_count)
        #Push each tuple key and the nom count (as value) into a new dictionary
        new_dict[nn_tuple[n][0]] = nom


    # Output frequency CSV file in descending order using the new dictionary
    with open("C:\\Users\\DaLaw\\Documents\\AWE_untagd\\" + type + "_nn_sequences.csv", "w") as fout:
        fout.write("Noun 1\tNoun2\tNom count\n")
        for k, v in sorted(new_dict.items(), key=lambda x: x[1], reverse=True):
            fout.write(str(k) + "\t" + str(v) + "\n")


#----------------------------------------------------------------------------------------------------------------------#

#Change the directory
os.chdir("C:\\Users\\DaLaw\\Documents\\AWE_untagd")

print("Reading and categorizing files to different lists...")

#Read all of the files
readFile = [f for f in os.listdir() if re.search(r"\.txt$", f, flags=re.I)]

print("Creating a list for each register...")
#Create a list for each register

for fName in readFile:
    JA_BI = [JB for JB in os.listdir() if re.search(r"JA_BI", JB, flags=re.I)]
    JA_HI = [JH for JH in os.listdir() if re.search(r"JA_HI", JH, flags=re.I)]
    PS_BI = [PB for PB in os.listdir() if re.search(r"PS_BI", PB, flags=re.I)]
    PS_HI = [PH for PH in os.listdir() if re.search(r"PS_HI", PH, flags=re.I)]
    TB_BI = [TB for TB in os.listdir() if re.search(r"TB_BI", TB, flags=re.I)]
    TB_HI = [TH for TH in os.listdir() if re.search(r"TB_HI", TH, flags=re.I)]


nn_sequence(JA_BI, "JA_BI")
nn_sequence(JA_HI, "JA_HI")
nn_sequence(PS_BI, "PS_BI")
nn_sequence(PS_HI, "PS_HI")
nn_sequence(TB_BI, "TB_BI")
nn_sequence(TB_HI, "TB_HI")

print("Finished")

'''
**********************************************************************************************************************
There are some errors in terms of the accuracy of the POS tagger.
It seems like the pos tagger treats some punctuations and single "s" as nouns. This may be due the segmentation of a 
possessive noun, for instance "avatar's storyline." It is possible that the tagger considers the possessive "s" and 
apostrophe as part of the noun.
I was not quite sure about what the acronyms (JA, PS, and TB) stand for, but I observed that in JA_BI and JA_HI the 
total N+N compounds have a higher frequency than other registers. For those registers related to biology, we can find
words like "cell," "treatment," or "prototype", names of body parts, and so forth, but not "government," "laws," names 
of states as in HI files. Overall, most of the N+N compounds in each register seems to appear once only.
**********************************************************************************************************************
'''

