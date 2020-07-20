
# The following functions convert singular into plural forms. (However, it does not cover all of the cases)

def adding_s(noun):
    print(noun + "s")

def adding_es(noun):
    print(noun + "es")

def adding_es_2(noun):
    print(noun[:-2] + "es")

def adding_ies(noun):
    print(noun[:-1] + "ies")

def adding_a(noun):
    print(noun[:-2] + "a")

def adding_e(noun):
    print(noun + "e")

def adding_ves(noun):
    if noun[-2:] == "fe":
        print(noun[:-2] + "ves")
    else:
        print(noun[:-1] + "ves")

def adding_ices(noun):
    print(noun[:-2] + "ices")

# The following function converts plural into singular.
# However, it only works for those pairs in the dictionary irr_singular_2 below and some other cases

def convert_plu_sing(noun):
    if noun in irr_singular_2:
        print(irr_singular_2[noun])

    elif noun[-3:] == "ies":
        print(noun[:-3] + "y")

    elif (noun[-2:] == "es") and not "houses" and not "horses":
        print(noun[:-2])

    elif noun[-1] == "s":
        print(noun[:-1])

    else:
        print(noun)

#---------------------main code below--------------------------------------------------------------------#

#The following variables contain a dictionary

irr_singular = {"fishes":"fish","sheep":"sheep","barracks":"barracks","foot":"feet","tooth":"teeth",
                "goose":"geese","child":"children","man":"men","woman":"women","person":"people",
                "mouse":"mice", "deer":"deer","gas":"gases","box":"boxes","bus":"buses","kiss":"kisses"
                }

irr_singular_2 = {"fishes":"fish","sheep":"sheep","barracks":"barracks","feet":"foot","teeth":"tooth",
                "geese":"goose","children":"child","men":"man","women":"woman","people":"person",
                "mice":"mouse", "deer":"deer","gases":"gas","boxes":"box","buses":"bus","kisses":"kiss"
                }

# The following list contains some words that end with o.

o_list = ["echo", "embargo", "hero", "potato", "tomato", "torpedo", "veto"]

# Opening

print("\nWelcome!\nThis is an English noun singular/plural converter.\n")

# Prompt user for input

user_input = input("Would you like to give me a singular noun? or a plural noun?\n"
                   "Type 1 for singular\n"
                   "Type 2 for plural\n")

# If the user wants to give a singular noun, then do run the following codes

if user_input == "1":
    noun_input = input("Now give me a singular noun here: ")

    # if the input matches those words in the dictionary, then run the following code

    if noun_input in irr_singular:
        print(irr_singular[noun_input])

    # if the input matches those words in the list, then run the following code

    elif noun_input in o_list:
        adding_es(noun_input)

    # if the input ends with "is", then run the following code

    elif noun_input[-2:] == "is":
        adding_es_2(noun_input)

    # if the input ends with "um" or "on", then run the following code

    elif (noun_input[-2:] == "um") or (noun_input[-2:] == "on"):
        adding_a(noun_input)

    # if the input ends with "ex" or "ix", then run the following code

    elif (noun_input[-2:] == "ex") or (noun_input[-2:] == "ix"):
        adding_ices(noun_input)

    # if the input ends with "fe" or "f", then run the following code

    elif (noun_input[-2:] == "fe") or (noun_input[-1] == "f"):
        adding_ves(noun_input)

    # if the input ends with "y" but not "boy", then run the following code

    elif (noun_input[-1] == "y") and (not "boy"):
        adding_ies(noun_input)

    # if the input ends with "a", then run the following code

    elif (noun_input[-1] == "a"):
        adding_e(noun_input)

    # if nothing applies, then do the following

    else:
        adding_s(noun_input)


# If the user wants to give a plural noun, then do run the following codes

elif user_input == "2":
    noun_input = input("Now give me a singular noun here: ")

    convert_plu_sing(noun_input)  # This will run the function convert_plu_sing() defined earlier.
