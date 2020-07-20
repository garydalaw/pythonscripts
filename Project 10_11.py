import os, re
from tkinter import *
from tkinter import filedialog

#Create an empty window widget
root = Tk()

#Create a browse function. When the button is pressed, it asks for a directory
#Then show the directory in the widget and create a list of filenames
def browse_pressed():

    file = filedialog.askdirectory()    #ask for directory
    show_dir["text"] = file #print the directory on the widget
    os.chdir(file)  #change the directory
    # Here, I use global to make the following list global, so that I can use it in different function
    global filenames
    filenames = [i for i in os.listdir() if re.search(r"\.txt$", i, flags=re.I)]

#Create a search function so that it will show matches with pre-/post words in a new window widget
def search_function():
    global filenames    #Use the list created in the function above
    entry = user_entry.get()    #get the user entry for the keyword/regular expression

    # Create a window for findings
    findings = Tk()
    findings.title("Findings")
    findings_frame = Frame(findings)

    findings_frame.grid_rowconfigure(0, weight=1)

    #Create a scrollbar (using grid)
    scrollbar = Scrollbar(findings_frame)
    scrollbar.grid(row=0, column=3, sticky=N + S)

    # Create a window for text results (using grid)
    left_concordance = Listbox(findings_frame, width=50)
    left_concordance.grid(row=0, column=0, sticky=E)
    core_text = Listbox(findings_frame, width=20)
    core_text.grid(row=0, column=1, sticky="")
    right_concordance = Listbox(findings_frame, width=50, yscrollcommand=scrollbar.set)
    right_concordance.grid(row=0, column=2, sticky=W)

    scrollbar.config(command=core_text.yview)
    findings_frame.pack(padx=100, pady=100)

    #Open/read files
    for file in filenames:
        with open(file, encoding="utf-8") as fin:
            words = fin.read().strip().split()
        for i in range(len(words)):
            # Search the word that user provided
            if re.search(entry, words[i], flags=re.I):
                # Create a string of previous words
                pre_wds = " ".join(words[i - 5:i])
                # Create a string of following words
                post_wds = " ".join(words[i + 1:i + 6])
                # Insert the matches into different Listbox
                left_concordance.insert(END, pre_wds + "\n")
                core_text.insert(END, words[i] + "\n")
                right_concordance.insert(END, post_wds + "\n")

#----------------------------------------------------------------------------------------------------------------------#

#Create a main frame
main_frame = Frame(root)

#Create labels, buttons, etc. in the widget
label_1 = Label(main_frame, text="Please select a directory first")
browse_button = Button(main_frame, text="Browse", command=browse_pressed)
show_dir = Label(main_frame, text="No file is selected")
label_2 = Label(main_frame, text="Type a word/regular expression")
user_entry = Entry(main_frame)
search_button = Button(main_frame, text="Search", command=search_function)

label_1.grid(row=0, column=1)
browse_button.grid(row=1, column=1)
show_dir.grid(row=2, column=1)
label_2.grid(row=3, column=1)
user_entry.grid(row=4, columnspan=2)
search_button.grid(row=5, column=1)

main_frame.pack(padx=50, pady=20)

#Execute GUI
root.mainloop()








