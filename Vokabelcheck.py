import string
from Tkinter import *
import latin_grammar as grammar


def get_words(text):
    for char in ["\n","\t","\r","!","-",".",",","?","'",'"',";","_","*","/",":"]:
        text = text.replace(char, " ")
    words = set(string.split(string.lower(text), " "))

    return words


def missing_vocabulary(t, v):
    t = get_words(t) # words from the text
    v = get_words(v) # words from vocabs

    # remove known vocabulary
    missing = t - v
    for vocab in v:
        c = grammar.conjugate(vocab)
        d = grammar.declinate(vocab)
        missing = missing - c
        missing = missing - d

    return missing


def show_missing_vocabulary(text, vocabulary):
    mv = missing_vocabulary(text, vocabulary)

    rw = Tk()
    rw.focus_set()
    result = Text(rw, width = 25)
    resultScroll = Scrollbar(rw)
    result.configure(yscrollcommand = resultScroll.set)
    resultScroll.configure(command = result.yview)
    resultScroll.pack(side = RIGHT, fill = Y)
    result.pack(side = LEFT, fill = BOTH)
    result.insert(END, 'Unbekannte Vokabeln:\n\n')

    for word in mv:
        result.insert(END, word+"\n")


def main():
    root = Tk()
    upperFrame = Frame(root)

    textFrame = Frame(upperFrame)
    latinText = Text(textFrame)
    latinTextScroll = Scrollbar(textFrame)
    latinText.pack(side = LEFT, fill = BOTH, expand = 1)
    latinTextScroll.pack(side = RIGHT, fill = Y)
    latinText.config(yscrollcommand = latinTextScroll.set)
    latinTextScroll.config(command = latinText.yview)

    vocabFrame = Frame(upperFrame)
    vocabs = Text(vocabFrame, width = 25)
    vocabsScroll = Scrollbar(vocabFrame)
    vocabs.pack(side=LEFT, fill=BOTH, expand = 1)
    vocabsScroll.pack(side=RIGHT, fill=Y)
    vocabs.config(yscrollcommand = vocabsScroll.set)
    vocabsScroll.config(command = vocabs.yview)

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
