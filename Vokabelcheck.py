# -*- coding: utf-8 -*-
"""Vokabelcheck
(c)2012, Thomas Feldmann

Questions, ideas:
feldmann.thomas@gmail.com

Project page:
http://tfeldmann.github.com/Vokabelcheck
"""

import string
import re
from Tkinter import *
import tkMessageBox

text_settings = {"undo": True, "padx": 10, "pady": 10, "exportselection": 0}

# latin grammar definitions
conjugations = set(['am', 'amini', 'amur', 'amus', 'ant', 'antur', 'ar', 'aris', 'as', 'at', 'atis', 'atur', 'bam', 'bamini', 'bamur', 'bamus', 'bant', 'bantur', 'bar', 'baris', 'bas', 'bat', 'batis', 'batur', 'beris', 'bimini', 'bimur', 'bimus', 'bis', 'bit', 'bitis', 'bitur', 'bo', 'bor', 'bunt', 'buntur', 'ebam', 'ebamini', 'ebamur', 'ebamus', 'ebant', 'ebantur', 'ebar', 'ebaris', 'ebas', 'ebat', 'ebatis', 'ebatur', 'em', 'emini', 'emur', 'emus', 'ent', 'entur', 'er', 'erim', 'erimus', 'erint', 'eris', 'erit', 'eritis', 'ero', 'erunt', 'es', 'et', 'etis', 'etur', 'i', 'iam', 'iamini', 'iamur', 'iamus', 'iant', 'iantur', 'iar', 'iaris', 'ias', 'iat', 'iatis', 'iatur', 'iebam', 'iebamini', 'iebamur', 'iebamus', 'iebant', 'iebantur', 'iebar', 'iebaris', 'iebas', 'iebat', 'iebatis', 'iebatur', 'iemini', 'iemur', 'iemus', 'ient', 'ientur', 'ieris', 'ies', 'iet', 'ietis', 'ietur', 'imini', 'imur', 'imus', 'io', 'ior', 'is', 'isti', 'istis', 'it', 'itis', 'itur', 'iunt', 'iuntur', 'm', 'mini', 'mur', 'mus', 'nt', 'ntur', 'o', 'or', 'r', 'ris', 's', 't', 'tis', 'tur', 'unt', 'untur', 'verunt'])
declinations = set(['a', 'ae', 'am', 'arum', 'as', 'e', 'ebus', 'ei', 'em', 'erum', 'es', 'i', 'ia', 'ibus', 'im', 'is', 'ium', 'o', 'orum', 'os', 's', 'u', 'ui', 'um', 'us', 'uum'])

def conjugate(base):
    return set([base + conjugation for conjugation in conjugations])
def declinate(base):
    return set([base + declination for declination in declinations])

def get_words(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.rstrip('\r\n\t')
    words = set(string.split(string.lower(text), " "))
    return words


def missing_vocabulary(t, v):
    t = get_words(t) # words from the text
    v = get_words(v) # words from vocabs

    # remove known vocabulary by subtracting sets
    missing = t - v
    for vocab in v:
        c = conjugate(vocab)
        d = declinate(vocab)
        missing = missing - c
        missing = missing - d

    return missing


def show_missing_vocabulary(text, vocabulary):
    rw = Tk()
    rw.title("Unbekannte Vokabeln")
    result = Text(rw, text_settings, width = 30)
    resultScroll = Scrollbar(rw)
    result.configure(yscrollcommand = resultScroll.set)
    resultScroll.configure(command = result.yview)
    resultScroll.pack(side = RIGHT, fill = Y)
    result.pack(side = LEFT, fill = BOTH, expand = 1)

    mv = missing_vocabulary(text, vocabulary)
    if (mv):
        for word in mv:
            result.insert(END, word+"\n")
    else:
        result.insert(END, "Keine unbekannten Vokabeln.")


def main():
    root = Tk()
    root.title("Vokabelcheck")

    upperFrame = Frame(root)

    textFrame = Frame(upperFrame)
    latinText = Text(textFrame, text_settings)
    latinTextScroll = Scrollbar(textFrame)
    latinText.pack(side = LEFT, fill = BOTH, expand = 1)
    latinTextScroll.pack(side = RIGHT, fill = Y)
    latinText.config(yscrollcommand = latinTextScroll.set)
    latinTextScroll.config(command = latinText.yview)

    vocabFrame = Frame(upperFrame)
    vocabs = Text(vocabFrame, text_settings, width = 30)
    vocabsScroll = Scrollbar(vocabFrame)
    vocabs.pack(side = LEFT, fill = BOTH, expand = 1)
    vocabsScroll.pack(side = RIGHT, fill = Y)
    vocabs.config(yscrollcommand = vocabsScroll.set)
    vocabsScroll.config(command = vocabs.yview)

    textFrame.pack(side = LEFT, expand = 1, fill = BOTH)
    vocabFrame.pack(side = RIGHT, expand = 1, fill = BOTH)
    upperFrame.pack(side = TOP, expand = 1, fill = BOTH)

    controlFrame = Frame(root)
    start = Button(controlFrame, text = 'Analyse starten',
        command = lambda: show_missing_vocabulary(latinText.get(1.0, "end"), vocabs.get(1.0, "end")))
    start.pack(side = RIGHT, padx = 14, pady = 14)
    controlFrame.pack(fill = X)

    latinText.insert(END, "Lateinischer Text")
    vocabs.insert(END, "Vokabelliste")


    # Menu
    menubar = Menu(root)
    textmenu = Menu(menubar)
    textmenu.add_command(label="Text öffnen")
    textmenu.add_command(label="Vokabelliste öffnen")
    textmenu.add_command(label="Endungen öffnen")
    textmenu.add_separator()
    textmenu.add_command(label="Text speichern")
    textmenu.add_command(label="Vokabelliste speichern")
    textmenu.add_command(label="Endungen speichern")
    textmenu.add_separator()
    textmenu.add_command(label="Beenden")
    menubar.add_cascade(label="Programm", menu=textmenu)

    helpmenu = Menu(menubar)
    helpmenu.add_command(label="Projektseite")
    helpmenu.add_command(label="Über das Programm",
        command=lambda: tkMessageBox.showinfo("Über das Programm", __doc__))
    menubar.add_cascade(label="Hilfe", menu=helpmenu)

    root.config(menu=menubar)

    root.mainloop()


if __name__ == "__main__":
    main()
