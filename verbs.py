import os, os.path
import nltk
import nltk.data
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from PIL import ImageTk, Image
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
import array as arr
import numpy

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
    if tokenizer.tokenize(val):             # check regex if um is present
        su = val.replace(affix, '', 1)
        output.insert(END, (su))
        
        length = int(len(su) - 1)
        if length == 2:                   
            pass
        
        if length == 3:                      
            if su[:1] == su[1:2]:       
                output.insert(END, (su[1:]))
            else:
                pass

        if length == 4:                        
            if su[:1] == su[1:2]:            
                output.insert(END, (su[1:]))
            else:              
                pass
            
            
        if length > 4:                       
            if length == 6:                     
                if su[:1] == su[1:2]:              
                    output.insert(END, (su[1:]))
                 
                elif su[:2] == su[2:4]:             
                    output.insert(END, (su[2:]))

                else:
                    pass
                    
            else:       
                if su[:1] == su[1:2]:
                    output.insert(END, (su[1:]))
                        
                elif su[:2] == su[2:4]: 
                    output.insert(END, (su[2:]))
                        
                elif su[:3] == su[3:6]:  
                    output.insert(END, (su[3:]))
                            
                else:               
                    pass
              
    else:
        output.insert(END, "unknown value\n")


    
def corpus():
    count, ctr = 0, 0
    a = 0
    root_words = []
    list_words = []
    
    output.insert(END, "\n***************** -UM AFFIX REMOVAL AND RULE BASED ***************** \n")
    for word in words:
        root_words.append(word)
        
    for token in tokens:
        if tokenizer.tokenize(token):
            output.insert(END, (token) + "\t=\t")
            # print(token, end='  \t')
            su = token.replace(affix, '', 1)

            length = int(len(su))
            if length == 2:                         # umoo --> oo
                output.insert(END, (su) + "\n")
                ctr = ctr + 1
                ugat = su
                if ugat in root_words:
                    a = a + 1
                else:
                    list_words.append(ugat)
                    
            elif length == 3:                      
                if su[:1] == su[1:2]:               # umooo --> ooo
                    output.insert(END, (su[1:]) + "\n")                  # ooo --> oo
                    ctr = ctr + 1
                    ugat = su[1:]
                    if ugat in root_words:
                        a = a + 1
                    else:
                        list_words.append(ugat)
                else:                               # umupo --> upo
                    output.insert(END, (su) + "\n")
                    ctr = ctr + 1
                    ugat = su
                    if ugat in root_words:
                        a = a + 1
                    else:
                        list_words.append(ugat)

            elif length == 4:                        
                if su[:1] == su[1:2]:               # umuupo --> uupo
                    output.insert(END, (su[1:]) + "\n")
                    ctr = ctr + 1
                    ugat = su[1:]
                    if ugat in root_words:
                        a = a + 1
                    else:
                        list_words.append(ugat)
                else:
                    output.insert(END, (su) + "\n")                     # bumaba --> baba, kumain --> kain, umutot --> utot
                    ctr = ctr + 1
                    ugat = su
                    if ugat in root_words:
                        a = a + 1
                    else:
                        list_words.append(ugat)

            elif length > 4:                        # bumababa --> bababa, kumakain --> kakain, umuusog --> uusog
                if length == 6:                     # dumaldal --> daldal
                    if su[:1] == su[1:2]:               # uusog --> usog
                        output.insert(END, (su[1:]) + "\n")
                        ctr = ctr + 1
                        ugat = su[1:]
                        if ugat in root_words:
                            a = a + 1
                        else:
                            list_words.append(ugat)
                     
                    elif su[:2] == su[2:4]:             # bababa --> baba, kakain --> kain
                        output.insert(END, (su[2:]) + "\n")
                        ctr = ctr + 1
                        ugat = su[2:]
                        if ugat in root_words:
                            a = a + 1
                        else:
                            list_words.append(ugat)
                    else:
                        output.insert(END, (su) + "\n")
                        ctr = ctr + 1
                        ugat = su
                        if ugat in root_words:
                            a = a + 1
                        else:
                            list_words.append(ugat)
                        
                else:       
                    if su[:1] == su[1:2]:               # uusog --> usog
                        output.insert(END, (su[1:]) + "\n")
                        ctr = ctr + 1
                        ugat = su[1:]
                        if ugat in root_words:
                            a = a + 1
                        else:
                            list_words.append(ugat)
                            
                    elif su[:2] == su[2:4]:             # bababa --> baba, kakain --> kain
                        output.insert(END, (su[2:]) + "\n")
                        ctr = ctr + 1
                        ugat = su[2:]
                        if ugat in root_words:
                            a = a + 1
                        else:
                            list_words.append(ugat)
                            
                    elif su[:3] == su[3:6]:            # ngingiti --> ngiti
                        output.insert(END, (su[3:]) + "\n")
                        ctr = ctr + 1
                        ugat = su[3:]
                        if ugat in root_words:
                            a = a + 1
                        else:
                            list_words.append(ugat)
                                
                    else:                               # umunawa --> unawa, tumalikod --> talikod
                        output.insert(END, (su) + "\n")
                        ctr = ctr + 1
                        ugat = su
                        if ugat in root_words:
                            a = a + 1
                        else:
                            list_words.append(ugat)
               
            else:
                output.insert(END, (su) + "Unknown Value\n")

            
            count = count + 1

    stats = (a / count) * 100
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
    a = 0
    root_words = []
    list_words = []
    
    print("\nA. -um Corpus\n"
          "B. User Input\n"
          "... Exit\n")

    select = (input("Select a task : "))
    for word in words:
        root_words.append(word)
    
    if select.upper() == "A":
        print("\n************** -UM AFFIX REMOVAL ************** \n")
        
        for token in tokens:
            if tokenizer.tokenize(token):
                print(token, end='  \t')
                su = token.replace(affix, '', 1)
                # print(token.translate(translation))

          
                length = int(len(su))
                if length == 2:                         # umoo --> oo
                    print(su)
                    ctr = ctr + 1
                    ugat = su
                    if ugat in root_words:
                        a = a + 1
                    else:
                        list_words.append(ugat)
                        
                elif length == 3:                      
                    if su[:1] == su[1:2]:               # umooo --> ooo
                        print(su[1:])                   # ooo --> oo
                        ctr = ctr + 1
                        ugat = su[1:]
                        if ugat in root_words:
                            a = a + 1
                        else:
                            list_words.append(ugat)
                    else:                               # umupo --> upo
                        print(su)
                        ctr = ctr + 1
                        ugat = su
                        if ugat in root_words:
                            a = a + 1
                        else:
                            list_words.append(ugat)

                elif length == 4:                        
                    if su[:1] == su[1:2]:               # umuupo --> uupo
                        print(su[1:])
                        ctr = ctr + 1
                        ugat = su[1:]
                        if ugat in root_words:
                            a = a + 1
                        else:
                            list_words.append(ugat)
                    else:
                        print(su)                       # bumaba --> baba, kumain --> kain, umutot --> utot
                        ctr = ctr + 1
                        ugat = su
                        if ugat in root_words:
                            a = a + 1
                        else:
                            list_words.append(ugat)

                elif length > 4:                        # bumababa --> bababa, kumakain --> kakain, umuusog --> uusog
                    if length == 6:                     # dumaldal --> daldal
                        if su[:1] == su[1:2]:               # uusog --> usog
                            print(su[1:])
                            ctr = ctr + 1
                            ugat = su[1:]
                            if ugat in root_words:
                                a = a + 1
                            else:
                                list_words.append(ugat)
                         
                        elif su[:2] == su[2:4]:             # bababa --> baba, kakain --> kain
                            print(su[2:])
                            ctr = ctr + 1
                            ugat = su[2:]
                            if ugat in root_words:
                                a = a + 1
                            else:
                                list_words.append(ugat)
                        else:
                            print(su)
                            ctr = ctr + 1
                            ugat = su
                            if ugat in root_words:
                                a = a + 1
                            else:
                                list_words.append(ugat)
                            
                    else:       
                        if su[:1] == su[1:2]:               # uusog --> usog
                            print(su[1:])
                            ctr = ctr + 1
                            ugat = su[1:]
                            if ugat in root_words:
                                a = a + 1
                            else:
                                list_words.append(ugat)
                                
                        elif su[:2] == su[2:4]:             # bababa --> baba, kakain --> kain
                            print(su[2:])
                            ctr = ctr + 1
                            ugat = su[2:]
                            if ugat in root_words:
                                a = a + 1
                            else:
                                list_words.append(ugat)
                                
                        elif su[:3] == su[3:6]:            # ngingiti --> ngiti
                            print(su[3:])
                            ctr = ctr + 1
                            ugat = su[3:]
                            if ugat in root_words:
                                a = a + 1
                            else:
                                list_words.append(ugat)
                                    
                        else:                               # umunawa --> unawa, tumalikod --> talikod
                            print(su)
                            ctr = ctr + 1
                            ugat = su
                            if ugat in root_words:
                                a = a + 1
                            else:
                                list_words.append(ugat)
                   
                else:
                    print('unkown value')

                
                count = count + 1
                           
               
        for lw in list_words:
            print(lw)
        
        stats = (a / count) * 100
        # print(a)
        format_stats = "{:.2f}".format(stats)
        # print("\n" + str(ctr))
        # print(count)
        print("Accuracy : " + str(format_stats) + " %")


    elif select.upper() == "B":
        print("\n********** FILIPINO -UM VERB CHECKER ********** \n")
        while True:
            verb = input("Enter a verb : ")
            if tokenizer.tokenize(verb):        # check regex if um is present
                su = verb.replace(affix, '', 1)
                
                print(su)                     
                length = int(len(su))
                if length == 2:                   
                    pass

                if length == 3:                      
                    if su[:1] == su[1:2]:          
                        print(su[1:])                   

                    else:                           
                        pass

                elif length == 4:                        
                    if su[:1] == su[1:2]:            
                        print(su[1:])
   
                    else:
                        pass

                elif length > 4:                       
                    if length == 6:                     
                        if su[:1] == su[1:2]:              
                            print(su[1:])
                         
                        elif su[:2] == su[2:4]:             
                            print(su[2:])

                        else:
                            pass
                            
                    else:       
                        if su[:1] == su[1:2]:
                            print(su[1:])
                                
                        elif su[:2] == su[2:4]: 
                            print(su[2:])
                                
                        elif su[:3] == su[3:6]:  
                            print(su[3:])
                                    
                        else:               
                            pass

            else:
                print("unknown value")
    else:
        break;











