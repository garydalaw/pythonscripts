import re

counter = 0

# The following list is to filter out those are not real nominalization. However, it only provides several examples.
non_nom = ["sentence", "instance", "Romance"]

# The following is an empty list.
nom_list = []

print("\n<< Nominalization Detecter >> Ver.1.0\n")

in_text = input("Please paste a short text here:\n")

split_text = in_text.split()

for texts in split_text:
    # The following regex should match nominalizaiton mentioned on the website.
    if re.findall(r"\w+[st]ions?\b|\w+ments?\b|\w+[ae]nces?\b|\w+ees?\b|\w+^f[eo]rs?\b|\w+ing\b", texts):

        # The following if statement checks fake nominalizations if they are in the list non_nom. If they are, then skip it and continue.
        if texts in non_nom:
            continue
        # The following will append each matching to a new list called nom_list.
        nom_list.append(texts)

        # When there is a match, the counter will add one.
        counter += 1

print(nom_list)
print("Identified nominalization in total: " + str(counter))

