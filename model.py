# -*- coding: utf-8 -*-
import re


def words_from_text(text):
    """
    returns an unordered set of words that are contained in the text.
    Duplicates are removed
    """
    text = re.sub('[^a-zA-Z]', " ", text)
    text = text.strip('\r\n\t')
    words = text.split()
    words = {word for word in words if word != ""}
    return words


def word_with_endings(word, endings):
    if not word:
        return set()
    if not endings:
        return {word}
    return {word + ending for ending in endings}


def words_with_endings(words, endings):
    result = set()
    for word in words:
        for variation in word_with_endings(word, endings):
            result.add(variation)
    return result


def missing_vocabulary(words, basicforms, endings):
    """
    connect the basic forms with endings and check whether the words in the
    "words" list are known. Returns a set of words that are missing.

    words, basicforms and endings must be sets
    """
    words = {x.lower() for x in words}
    basicforms = {x.lower() for x in basicforms}
    endings = {x.lower() for x in endings}
    return words - basicforms - words_with_endings(basicforms, endings)
