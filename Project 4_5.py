import re, os, codecs

def normalized_count(tFind,tWord):
    nom_count = (tFind / tWord) * 1000
    return nom_count

line_counter = 0
HI_wcount = 0
HI_p1_counter = 0
HI_p2_counter = 0
HI_p3_counter = 0
ID_wcount = 0
ID_p1_counter = 0
ID_p2_counter = 0
ID_p3_counter = 0
IN_wcount = 0
IN_p1_counter = 0
IN_p2_counter = 0
IN_p3_counter = 0
IP_wcount = 0
IP_p1_counter = 0
IP_p2_counter = 0
IP_p3_counter = 0
LY_wcount = 0
LY_p1_counter = 0
LY_p2_counter = 0
LY_p3_counter = 0
NA_wcount = 0
NA_p1_counter = 0
NA_p2_counter = 0
NA_p3_counter = 0
OP_wcount = 0
OP_p1_counter = 0
OP_p2_counter = 0
OP_p3_counter = 0
SP_wcount = 0
SP_p1_counter = 0
SP_p2_counter = 0
SP_p3_counter = 0


os.chdir("C:\\Users\\DaLaw\\Documents\\Mini-CORE_new")

file_in = [i for i in os.listdir() if re.search(r"\.txt$", i, flags=re.I)]
#print(file_in)

f_out = open("C:\\Users\\DaLaw\\Documents\\Mini-CORE_new\\result.csv", "w")
f_out.write("Register\tFeature 1\tFeature 2\tFeature 3\n")

#The following sets up variables and lists
pronouns = ["I", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them"]
modals = ["must", "shall", "will", "should", "would", "can", "could", "may", "might"]

for file_name in file_in:
    line_counter = 0
    if file_name[2:4] == "HI":
        o_file = open(file_name)
        for line in o_file:
            line_counter += 1
            if line_counter < 8:
                continue
            else:
                line = re.sub(r"^\<[hp]\>", "", line)
                split_word = line.lower().split()
                for f_pattern in split_word:
                    HI_wcount += 1
                    f_pattern = f_pattern.strip()
                    if re.findall(r"([\'\’][msdt|ll|ve|re|all])", f_pattern):
                        HI_p1_counter += 1
                        #print(f_pattern)
                    elif f_pattern in pronouns:
                        HI_p2_counter += 1
                        #print(f_pattern)
                    elif f_pattern in modals:
                        HI_p3_counter += 1
                        #print(f_pattern)

    elif file_name[2:4] == "ID":
        o_file = open(file_name)
        for line in o_file:
            line_counter += 1
            if line_counter < 8:
                continue
            else:
                line = re.sub(r"^\<[hp]\>", "", line)
                split_word = line.lower().split()
                for f_pattern in split_word:
                    ID_wcount += 1
                    f_pattern = f_pattern.strip()
                    if re.findall(r"([\'\’][msdt|ll|ve|re|all])", f_pattern):
                        ID_p1_counter += 1
                    elif f_pattern in pronouns:
                        ID_p2_counter += 1
                    elif f_pattern in modals:
                        ID_p3_counter += 1
    else:
        print("No such category!")

nc_for_HI_p1 = normalized_count(HI_p1_counter, HI_wcount)
nc_for_HI_p2 = normalized_count(HI_p2_counter, HI_wcount)
nc_for_HI_p3 = normalized_count(HI_p3_counter, HI_wcount)
print(HI_wcount)
print("p1 = " + str(HI_p1_counter))
print("p2 = " + str(HI_p2_counter))
print("p3 = " + str(HI_p3_counter))
print("nc1= " + str(nc_for_HI_p1))
print("nc2= " + str(nc_for_HI_p2))
print("nc2= " + str(nc_for_HI_p3))
nc_for_ID_p1 = normalized_count(ID_p1_counter, ID_wcount)
nc_for_ID_p2 = normalized_count(ID_p2_counter, ID_wcount)
nc_for_ID_p3 = normalized_count(ID_p3_counter, ID_wcount)
print(ID_wcount)
print("p1 = " + str(ID_p1_counter))
print("p2 = " + str(ID_p2_counter))
print("p3 = " + str(ID_p3_counter))
print("nc1= " + str(nc_for_ID_p1))
print("nc2= " + str(nc_for_ID_p2))
print("nc2= " + str(nc_for_ID_p3))
write_out_HI = os.path.basename("HI") + "\t" + str(nc_for_HI_p1) + "\t" + str(nc_for_HI_p2) + "\t" + str(nc_for_HI_p3) + "\n"
write_out_ID = os.path.basename("ID") + "\t" + str(nc_for_ID_p1) + "\t" + str(nc_for_ID_p2) + "\t" + str(nc_for_ID_p3) + "\n"

f_out.write(write_out_HI)
f_out.write(write_out_ID)


o_file.close()
f_out.close()
print("Finished!")