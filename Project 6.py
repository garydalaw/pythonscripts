import os, re, codecs, operator

#The following define two functions
def create_funWd ():
    with codecs.open("function_words.txt", encoding="ASCII") as fin:
        fun_wds = [wd for wd in fin]
    for line in fun_wds:
        #re_char = re.sub(r"ufeff", "", line)
        split_words = line.lower().strip().split()
    return split_words


def create_wdFlist(register, type):

    line_counter = 0
    funWd = create_funWd()
    cur_dict = dict()

    for file in register:
        ofile = codecs.open(file, encoding="ASCII")
        for line in ofile:
            line_counter += 1
            if line_counter < 8:
                continue
            else:
                line = re.sub("\<[hp]\>|[\^\*\(\)\$*]|", "", line)
                sp_wd = line.lower().strip().split()
                for wd in sp_wd:
                    if wd in funWd:
                        continue
                    else:
                        if len(wd) > 1:
                            if wd not in cur_dict:
                                cur_dict[wd] = 1
                            else:
                                cur_dict[wd] += 1

    with open("C:\\Users\\DaLaw\\Documents\\Mini-CORE_new\\" + type + "_wordfrequencylist.csv","a") as fout:
        fout.write("Word\tFrequency\n")
        for k, v in sorted(cur_dict.items(), key=lambda x: x[1], reverse=True):
            fout.write(str(k) + "\t" + str(v) + "\n")


#-------------------------------------------------------------------------------------------------------------------#

#Change the current directory
os.chdir("C:\\Users\\DaLaw\\Documents\\Mini-CORE_new")

#Read all the files
file_in = [f for f in os.listdir() if re.search(r"\.txt$", f, flags=re.I)]

#Save all files into a list
for file_name in file_in:

    HIregister = [HI for HI in os.listdir() if re.search(r"^1\+HI+", HI)]

create_wdFlist(HIregister, "HI")

print("Finished!")