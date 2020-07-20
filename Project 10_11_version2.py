import os, re
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

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

    #Create a window for findings
    findings = Tk()
    findings.title("Matches")
    findings_frame = Frame(findings)
    findings_frame.pack(fill=BOTH, expand=1, pady=80)

    #Create a Treeview widget and scrollbar
    tv = ttk.Treeview(findings_frame)
    scrollbar = ttk.Scrollbar(findings_frame, orient="vertical", command=tv.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    #Create headings and columns in the widget
    tv['columns'] = ('pre_words', 'match', 'post_words')
    tv.heading('pre_words', text='Previous words')
    tv.column('pre_words', anchor='e', width=200)
    tv.heading('match', text='Match')
    tv.column('match', anchor='center')
    tv.heading('post_words', text='Following words')
    tv.column('post_words', anchor="w", width=200)
    tv.pack(fill=BOTH, expand=1)

    tv.configure(yscrollcommand=scrollbar.set)

    #create a counter for matches
    counter = 0

    #Open/read files
    for file in filenames:
        with open(file, encoding="utf-8") as fin:
            words = fin.read().strip().split()
        for i in range(len(words)):
            #Search the word that user provided
            if re.search(entry, words[i], flags=re.I):
                counter += 1
                #Create a string of previous words
                pre_wds = " ".join(words[i-5:i])
                #Create a string of following words
                post_wds = " ".join(words[i+1:i+6])
                #Insert the matches in the Treeview windget
                tv.insert('', "end", text=counter, values=(pre_wds, words[i], post_wds))

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



