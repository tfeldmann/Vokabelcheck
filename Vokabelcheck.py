# -*- coding: utf-8 -*-

from Tkinter import *
import string


def get_words(text):
    words = []
    for char in ["\n","\t","\r","!","-",".",",","?","'",'"',";","_","*","/",":"]:
        text = text.replace(char, " ")
    for word in string.split(text, " "):
        stripped = string.strip(word)
        stripped = stripped.lower()
        if (stripped != "" and not stripped in words):
            words.append(stripped)
    return words


def missing_vocabulary(t, v):
    words = get_words(t)
    vocs = get_words(v)

    missing = []
    for word in words:
        if (word in vocs):
            continue;
        else:
            missing.append(word)

    return missing


def show_missing_vocabulary(text, vocabulary):
    mv = missing_vocabulary(text, vocabulary)

    rw = Tk()
    rw.bind_class("Text","<Control-a>", selectall)
    rw.bind_class("Text","<Command-a>", selectall)
    result = Text(rw)
    resultScroll = Scrollbar(rw)
    result.configure(yscrollcommand = resultScroll.set)
    resultScroll.configure(command = result.yview)
    result.pack(side = LEFT, fill = BOTH)
    resultScroll.pack(side = RIGHT, fill = Y)
    result.insert(END, 'Unbekannte Vokabeln:\n\n')

    for word in mv:
        result.insert(END, word+"\n")


def selectall(event):
    event.widget.tag_add("sel","1.0","end")


def main():
    root = Tk()
    root.bind_class("Text","<Control-a>", selectall)
    root.bind_class("Text","<Command-a>", selectall)

    upperFrame = Frame(root)

    textFrame = Frame(upperFrame)
    latinText = Text(textFrame, border = 10)
    latinTextScroll = Scrollbar(textFrame)
    latinText.pack(side = LEFT, fill = BOTH, expand = 1)
    latinTextScroll.pack(side = RIGHT, fill = Y)
    latinText.config(yscrollcommand = latinTextScroll.set)
    latinTextScroll.config(command = latinText.yview)
    latinText.insert(END, 'Ich bin ein:kleiner, "feiner, feiner, "feiner Text. Nichts besonderes.\nJepp.')

    vocabFrame = Frame(upperFrame)
    vocabs = Text(vocabFrame, width = 25)
    vocabsScroll = Scrollbar(vocabFrame)
    vocabs.pack(side=LEFT, fill=BOTH, expand = 1)
    vocabsScroll.pack(side=RIGHT, fill=Y)
    vocabs.config(yscrollcommand = vocabsScroll.set)
    vocabsScroll.config(command = vocabs.yview)
    vocabs.insert(END, 'kleiner\nbesonderes\nein\nIch\nNichts')

    textFrame.pack(side = LEFT, expand = 1, fill = BOTH)
    vocabFrame.pack(side = RIGHT, expand = 1, fill = BOTH)
    upperFrame.pack(side=TOP, expand = 1, fill = BOTH)

    controlFrame = Frame(root)
    start = Button(controlFrame, text = 'Analyse starten', command = lambda: show_missing_vocabulary(latinText.get(1.0, "end"), vocabs.get(1.0, "end")))
    start.pack(side = RIGHT, padx = 14, pady = 14)
    copyright = Label(controlFrame, text = '(c)2012 feldmann.thomas@googlemail.com', fg = 'gray')
    copyright.pack(side = LEFT, padx = 14, pady = 14)
    controlFrame.pack(fill = X)

    root.mainloop()


if __name__ == "__main__":
    main()
