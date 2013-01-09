# -*- coding: utf-8 -*-
'''
Vokabelcheck 1.1

(c)2012 Thomas Feldmann
feldmann.thomas@gmail.com
'''

from Tkinter import *
import tkMessageBox
import tkFileDialog
import webbrowser
import time
import model

PROJECT_URL = 'http://tfeldmann.github.com/Vokabelcheck'
TEXT_SETTINGS = {'undo': True, 'padx': 10, 'pady': 10, 'exportselection': 0}

class App():
    def __init__(self, root):
        self.root = root
        root.title('Vokabelcheck')

        upperframe = Frame(root)

        textframe = Frame(upperframe)
        self.latintext = Text(textframe, TEXT_SETTINGS)
        latintext_scrollbar = Scrollbar(textframe)
        self.latintext.pack(side=LEFT, fill=BOTH, expand=1)
        latintext_scrollbar.pack(side=RIGHT, fill=Y)
        self.latintext.config(yscrollcommand=latintext_scrollbar.set)
        latintext_scrollbar.config(command=self.latintext.yview)

        vocabframe = Frame(upperframe)
        self.vocabstext = Text(vocabframe, TEXT_SETTINGS, width=30)
        vocabs_scrollbar = Scrollbar(vocabframe)
        self.vocabstext.pack(side=LEFT, fill=BOTH, expand=1)
        vocabs_scrollbar.pack(side=RIGHT, fill=Y)
        self.vocabstext.config(yscrollcommand=vocabs_scrollbar.set)
        vocabs_scrollbar.config(command=self.vocabstext.yview)

        textframe.pack(side=LEFT, expand=1, fill=BOTH)
        vocabframe.pack(side=RIGHT, expand=1, fill=BOTH)
        upperframe.pack(side=TOP, expand=1, fill=BOTH)

        controlframe = Frame(root)
        start = Button(controlframe, text='Unbekannte Vokabeln zeigen',
            command = self.push_show_missing_vocabulary)
        start.pack(side=RIGHT, padx=14, pady=14)
        controlframe.pack(fill=X)

        self.latintext.insert(END, 'Lateinischer Text')
        self.vocabstext.insert(END, 'Vokabelliste')

        # menu
        menubar = Menu(root, tearoff=0)
        textmenu = Menu(menubar)
        textmenu.add_command(label='Text öffnen',
            command=self.push_text_open)
        textmenu.add_command(label='Vokabelliste öffnen',
            command=self.push_vocabs_open)
        textmenu.add_separator()
        textmenu.add_command(label='Text speichern',
            command=self.push_text_save)
        textmenu.add_command(label='Vokabelliste speichern',
            command=self.push_vocabs_save)
        textmenu.add_separator()
        textmenu.add_command(label='Beenden',
            command=lambda: root.destroy())
        menubar.add_cascade(label='Programm', menu=textmenu)
        helpmenu = Menu(menubar)
        helpmenu.add_command(label='Über Vokabelcheck',
            command=lambda: tkMessageBox.showinfo('Info', __doc__))
        helpmenu.add_command(label='Projektseite',
            command=lambda: webbrowser.open(PROJECT_URL))
        menubar.add_cascade(label='Hilfe', menu=helpmenu)
        root.config(menu=menubar)

    def load_endings(self, filename='Endungen.txt'):
        try:
            with open(filename, 'rb') as f:
                file_content = f.read()
                lines = file_content.split('\n')
                endings = []
                for line in lines:
                    # remove whitespace, lowercase
                    line = line.strip()
                    # don't append when line is comment or emtpy
                    if line[:1] != '#' and line.strip() != '':
                        endings.append(line)
                return endings

        # 'Endungen.txt' does not exist
        except IOError as e:
            tkMessageBox.showinfo('Keine Endungen gefunden!',
                'Konnte die Datei Endungen.txt nicht finden.')


    def load_text(self, textfield):
        try:
            with open(tkFileDialog.askopenfilename(), 'rb') as f:
                file_content = f.read()
                textfield.delete(1.0, END)
                textfield.insert(1.0, file_content)
        except: pass

    def save_text(self, textfield, filename, title='Speichern'):
        try:
            filename = tkFileDialog.asksaveasfilename(
                initialfile=filename, title=title)
            f = open(filename, 'wb')
            f.write(textfield.get(1.0, END))
            f.close()
        except: pass

    def push_text_open(self):
        self.load_text(self.latintext)

    def push_text_save(self):
        self.save_text(self.latintext, 'Text.txt', 'Text speichern')

    def push_vocabs_open(self):
        self.load_text(self.vocabstext)

    def push_vocabs_save(self):
        self.save_text(self.vocabstext, 'Vokabeln.txt', 'Vokabeln speichern')

    def push_show_missing_vocabulary(self):
        root = self.root

        # GUI
        rw = Toplevel(root)
        rw.title('Unbekannte Vokabeln')
        result_text = Text(rw, TEXT_SETTINGS, width=30)
        result_scroll = Scrollbar(rw)
        result_text.configure(yscrollcommand=result_scroll.set)
        result_scroll.configure(command=result_text.yview)
        result_scroll.pack(side=RIGHT, fill=Y)
        result_text.pack(side=LEFT, fill=BOTH, expand=1)

        # show missing vocabulary
        text = self.latintext.get(1.0, 'end')
        text = model.words_from_text(text)
        vocabs = self.vocabstext.get(1.0, 'end')
        vocabs = model.words_from_text(vocabs)
        endings = self.load_endings()

        t0 = time.clock()
        missing = model.missing_vocabulary(text, vocabs, endings)
        t = time.clock() - t0

        if missing:
            for vocab in missing:
                result_text.insert(END, vocab + '\n')
        else:
            result_text.insert(END, 'Keine unbekannten Vokabeln')

        # show measured time
        result_text.insert(END, '\nErmittelt in %.4fs' % t)


def main():
    root = Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
