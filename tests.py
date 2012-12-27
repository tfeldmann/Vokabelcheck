# -*- coding: utf-8 -*-
import unittest
import model

class WordsFromText(unittest.TestCase):
    def test_parsing(self):
        x = model.words_from_text("!Abc &§$def,gh   iL..m\r\n\tx")
        self.failUnlessEqual(x, {'Abc', 'def', 'gh', 'iL', 'm', 'x'})

    def test_char_only(self):
        x = model.words_from_text("!.%)(%/&(/!§)=)")
        self.failUnlessEqual(x, set())

    def test_empty_text(self):
        x = model.words_from_text("")
        self.failUnlessEqual(x, set())

    def test_duplicates(self):
        words = model.words_from_text("A A A B C")
        self.failUnlessEqual(words, {"A", "B", "C"})


class WordWithEndings(unittest.TestCase):
    def test_connecting(self):
        word = 'abc'
        x = model.word_with_endings(word, {'', 'b', 'aBc'})
        self.failUnlessEqual(x, {'abc', 'abcb', 'abcaBc'})

    def test_empty_wordlist(self):
        x = model.word_with_endings(set(), {"a", "b"})
        self.failUnlessEqual(x, set())

    def test_empty_endings(self):
        x = model.word_with_endings("x", set())
        self.failUnlessEqual(x, {"x"})

    def test_duplicates(self):
        word = "abc"
        x = model.word_with_endings(word, {"x", "x", "y"})
        self.failUnlessEqual(x, {"abcx", "abcy"})


class WordsWithEndings(unittest.TestCase):
    def test_basic(self):
        words = ['a', 'b', 'ABC']
        x = model.words_with_endings(words, {'', 'x', 'XX'})
        self.failUnlessEqual(x, {'a', 'ax', 'aXX', 'b', 'bx', 'bXX',
            'ABC', 'ABCx', 'ABCXX'})

    def test_empty_wordlist(self):
        x = model.words_with_endings(set(), {"a", "b", "c"})
        self.failUnlessEqual(x, set())

    def test_empty_endings(self):
        x = model.words_with_endings({"a", "b", "c"}, set())
        self.failUnlessEqual(x, {"a", "b", "c"})

    def test_duplicates(self):
        x = model.words_with_endings(["a", "b", "b"], ["1", "2"])
        self.failUnlessEqual(x, {"a1", "a2", "b1", "b2"})


class MissingVocabulary(unittest.TestCase):
    def test_basic(self):
        x = model.missing_vocabulary({"a1", "a2", "a3"}, {"a", "b"}, {"1", "2"})
        self.failUnlessEqual(x, {"a3"})

    def test_empty_words(self):
        x = model.missing_vocabulary(set(), {"a", "b"}, {"1", "2"})
        self.failUnlessEqual(x, set())

    def test_empty_basicforms(self):
        x = model.missing_vocabulary({1, 2, 3, 4}, set(), {1, 2})
        self.failUnlessEqual(x, {1, 2, 3, 4})

    def test_empty_endings(self):
        x = model.missing_vocabulary({1, 2, 3, 4}, {3, 4}, set())
        self.failUnlessEqual(x, {1, 2})


import os
class ParsingTests(unittest.TestCase):
    def setUp(self):
        model.save_endings(['abc', '# def', '', '  ', 'test'],
            'test_endings.txt')

    def test_load_endings(self):
        e = model.load_endings('test_endings.txt')
        self.failUnlessEqual(e, ['abc', 'test'])

    def tearDown(self):
        os.remove('test_endings.txt')


if __name__ == '__main__':
    unittest.main()
