# -*- coding: utf-8 -*-
"""
Vokabelcheck 1.1

(c)2012 Thomas Feldmann
feldmann.thomas@gmail.com
"""

from Tkinter import *
import tkMessageBox
import tkFileDialog
import webbrowser


PROJECT_URL = "http://tfeldmann.github.com/Vokabelcheck"

class App():
    def __init__(self, root):
        root.title("Vokabelcheck")
        upperframe = Frame(root)

        textframe = Frame(upperframe)
        self.latintext = Text(textframe, text_settings)
        latintext_scrollbar = Scrollbar(textframe)
        self.latintext.pack(side = LEFT, fill = BOTH, expand = 1)
        latintext_scrollbar.pack(side = RIGHT, fill = Y)
        self.latintext.config(yscrollcommand = latintext_scrollbar.set)
        latintext_scrollbar.config(command = self.latintext.yview)

        vocabframe = Frame(upperframe)
        self.vocabstext = Text(vocabframe, text_settings, width = 30)
        vocabs_scrollbar = Scrollbar(vocabframe)
        self.vocabstext.pack(side = LEFT, fill = BOTH, expand = 1)
        vocabs_scrollbar.pack(side = RIGHT, fill = Y)
        self.vocabstext.config(yscrollcommand = vocabs_scrollbar.set)
        vocabs_scrollbar.config(command = self.vocabstext.yview)

        textframe.pack(side = LEFT, expand = 1, fill = BOTH)
        vocabframe.pack(side = RIGHT, expand = 1, fill = BOTH)
        upperframe.pack(side = TOP, expand = 1, fill = BOTH)

        controlframe = Frame(root)
        start = Button(controlframe, text = 'Analyse starten',
            command = lambda: show_missing_vocabulary(self.latintext.get(1.0, "end"), self.vocabstext.get(1.0, "end")))
        start.pack(side = RIGHT, padx = 14, pady = 14)
        controlframe.pack(fill = X)

        self.latintext.insert(END, "Lateinischer Text")
        self.vocabstext.insert(END, "Vokabelliste")

        # creating the menu
        menubar = Menu(root, tearoff=0)
        textmenu = Menu(menubar)
        textmenu.add_command(label="Text öffnen",
            command=self.push_text_open)
        textmenu.add_command(label="Vokabelliste öffnen",
            command=self.push_vocabs_open)
        textmenu.add_command(label="Endungen öffnen",
            command=self.push_endings_open)
        textmenu.add_separator()
        textmenu.add_command(label="Text speichern",
            command=self.push_text_save)
        textmenu.add_command(label="Vokabelliste speichern",
            command=self.push_vocabs_save)
        textmenu.add_command(label="Endungen speichern",
            command=self.push_endings_save)
        textmenu.add_separator()
        textmenu.add_command(label="Beenden",
            command=lambda: root.destroy())
        menubar.add_cascade(label="Programm", menu=textmenu)
        helpmenu = Menu(menubar)
        helpmenu.add_command(label="Über Vokabelcheck",
            command=lambda: tkMessageBox.showinfo("Über Vokabelcheck", __doc__))
        helpmenu.add_command(label="Projektseite",
            command=lambda: webbrowser.open(PROJECT_URL))
        menubar.add_cascade(label="Hilfe", menu=helpmenu)
        root.config(menu=menubar)

    def load_text(self, textfield):
        with open(tkFileDialog.askopenfilename(), 'rb') as f:
            file_content = f.read()
            textfield.delete(1.0, END)
            textfield.insert(1.0, file_content)

    def save_text(self, textfield, filename, title="Speichern"):
        filename = tkFileDialog.asksaveasfilename(
            initialfile=filename,
            title=title)
        f = open(filename, 'wb')
        f.write(textfield.get(1.0, END))
        f.close()

    def push_text_open(self):
        self.load_text(self.latintext)

    def push_text_save(self):
        self.save_text(self.latintext, "Text.txt", "Text speichern")

    def push_vocabs_open(self):
        self.load_text(self.vocabstext)

    def push_vocabs_save(self):
        self.save_text(self.vocabstext, "Vokabeln.txt", "Vokabeln speichern")

    def push_endings_open(self):
        pass

    def push_endings_save(self):
        pass



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
    v = get_words(v) # words from self.vocabstext

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
    result_Scroll = _Scrollbar(rw)
    result.configure(yscrollcommand = result_Scroll.set)
    result_Scroll.configure(command = result.yview)
    result_Scroll.pack(side = RIGHT, fill = Y)
    result.pack(side = LEFT, fill = BOTH, expand = 1)

    mv = missing_vocabulary(text, vocabulary)
    if (mv):
        for word in mv:
            result.insert(END, word+"\n")
    else:
        result.insert(END, "Keine unbekannten Vokabeln.")


def main():
    root = Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
