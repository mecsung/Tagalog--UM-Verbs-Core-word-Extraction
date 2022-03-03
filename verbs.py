import os, os.path
import nltk
import nltk.data
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from PIL import ImageTk, Image
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

mypath = os.path.expanduser('~/nltk_data')
var = mypath in nltk.data.path
# print(var)

um = nltk.data.load('corpora/um_fil_corpus/um.txt')
root = nltk.data.load('corpora/um_fil_corpus/ugat.txt')
# print(um)

tokenizer = RegexpTokenizer("(um)")
tokens = word_tokenize(um)
words = word_tokenize(root)

# translation = {117: None, 109: None}
affix = 'um'

# ******************** FUNCTIONS *****************************************
def convert():
    val = entry.get("1.0", END).lower()
    
    output.insert(END, "\n********************* FILIPINO -UM VERB CHECKER ******************** \n")
    if tokenizer.tokenize(val):         # check regex if um is present
        su = val.replace(affix, '')
        output.insert(END, (su))
        # print(su)                     # print salitang ugat
 
        if su[:2] == su[2:4]:              # if first two letter is duplicated
            output.insert(END, (su[2:]))
            # print(su[2:])

        elif su[:1] == su[1:2]:             # if first letter is duplicated
            output.insert(END, (su[1:]))
            # print(su[1:])
              
    else:
        output.insert(END, "unknown value\n")
        # print("unknown value")
        
    # output.insert(END, (val))
    
def corpus():
    ctr, count = 0, 0
    output.insert(END, "\n***************** -UM AFFIX REMOVAL AND RULE BASED ***************** \n")
    
    for token in tokens:
        if tokenizer.tokenize(token):
            output.insert(END, (token) + "\t=\t")
            # print(token, end='  \t')
            new_token = token.replace(affix, '')
            
            # print(token.replace(affix, ''))
            # print(token.translate(translation))
            if new_token[:2] == new_token[2:4]:
                output.insert(END, (new_token[2:]) + "\n")

            elif new_token[:1] == new_token[1:2]:
                output.insert(END, (new_token[1:]) + "\n")

            else:
                output.insert(END, (new_token) + "\n")
                    
            count = count + 1
            for word in words:
                if word == token.replace(affix, ''):
                    ctr = ctr + 1

    stats = (ctr / count) * 100
    format_stats = "{:.2f}".format(stats)
    
    # print("\nAccuracy : " + str(format_stats) + " %")
    output.insert(END, "\nTotal Words : " + (str(ctr)))
    output.insert(END, "\nAccuracy : " + (str(format_stats) + " %"))

def delete(): 
    entry.delete('1.0', END)
    output.delete('0.0', END)

# ************************** GUI ******************************************
win = tk.Tk()
win.title("Lemmatization of Tagalog - UM Verbs using Affix Removal and Rule-based Method")
win.configure(bg="#263D42")
win.geometry("750x620")

panel = Label(win, text="Tagalog -UM Lemmatizer", bg="#263D42",
              height=2, font=("Bradley Hand ITC", 20), fg='#fff'
              ).pack()

# Insert textbox
entry = Text(win, height = 2, width = 70)
entry.insert(END, "Mag-enter ng salita")
entry.pack()

button_frame = tk.Frame(win)
button_frame.pack(side="bottom", fill="x", expand=False)
# Insert button
entry_button = tk.Button(button_frame, height = 2, width = 25,
                      text = "Magpatuloy",cursor="mouse",
                      bg="green", fg="white",
                      command = convert).pack()
# Corpus button
corpus_button = tk.Button(button_frame, height = 2, width = 25,
                      text = "Suruin ang corpus",cursor="mouse",
                      bg="#263D42", fg="white",
                      command = corpus).pack()
# Delete button
delete_button = tk.Button(button_frame, height = 2, width = 25,
                      text = "Burahin",cursor="mouse",
                      command = delete).pack()

# Output textbox
output = scrolledtext.ScrolledText(win, height = 20, width = 68,
              bg = "lightyellow")
output.bind("<Key>", lambda a: "break")
# output.configure(state="disabled")
output.pack()

panel = Label(button_frame, text="Developed by: Legaspi | Carpio | San Juan | Recto | Rufino",
              font=("Arial", 10), fg='#969696'
              ).pack()

win.mainloop()



# ***************************** BACKEND TEST ********************************
while True:
    count, ctr = 0, 0
    print("\nA. -um Corpus\n"
          "B. User Input\n"
          "... Exit\n")

    select = (input("Select a task : "))
    if select.upper() == "A":
        print("\n************** -UM AFFIX REMOVAL ************** \n")
        
        for token in tokens:
            if tokenizer.tokenize(token):
                print(token, end='  \t')
                su = token.replace(affix, '')
                
                # print(token.translate(translation))

                if su[:2] == su[2:4]:
                    s2 = su[2:]
                    print(su[2:])

                elif su[:1] == su[1:2]:
                    s1 = su[1:]
                    print(su[1:])
                else:
                    print(su)

                count = count + 1
                for word in words:
                    if word == su:
                        ctr = ctr + 1

        stats = (ctr / count) * 100
        format_stats = "{:.2f}".format(stats)
        print("\n" + str(ctr))
        print(count)
        print("Accuracy : " + str(format_stats) + " %")
        
    elif select.upper() == "B":
        print("\n********** FILIPINO -UM VERB CHECKER ********** \n")
        while True:
            verb = input("Enter a verb : ")
            if tokenizer.tokenize(verb):        # check regex if um is present
                su = verb.replace(affix, '')
                print(su)                       # print salitang ugat
 
                if su[:2] == su[2:4]:           # if first two letter is duplicated
                    print(su[2:])

                elif su[:1] == su[1:2]:            # if first letter is duplicated
                    print(su[1:])
                
            else:
                print("unknown value")
    else:
        break;











