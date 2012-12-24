# -*- coding: utf-8 -*-
import re

def words_from_text(text):
    text = re.sub('[^a-zA-Z]', " ", text)
    text = text.rstrip('\r\n\t')
    words = text.split(" ")
    words = [word for word in words if word != ""]
    return words

def word_with_endings(word, endings):
    return [word + ending for ending in endings]

def words_with_endings(words, endings):
    _words = []
    for word in words:
        variations = word_with_endings(word, endings)
        for v in variations:
            _words.append(v)
    return _words

def save_endings(endings, filename="endings.txt"):
    f = open(filename, 'wb')
    for ending in endings:
        f.write(ending + "\n")
    f.close()

def load_endings(filename="endings.txt"):
    with open(filename, 'rb') as f:
        file_content = f.read()
        lines = file_content.split("\n")

        endings = []
        for line in lines:
            if line[:1] != "#" and line.strip() != "":
                endings.append(line)
        return endings
