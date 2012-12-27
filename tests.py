# -*- coding: utf-8 -*-
import unittest
import model

class VocabFindingTests(unittest.TestCase):

    def test_words_from_text_parsing(self):
        words = model.words_from_text("!Abc &§$def,gh   iL..m\r\n\tx")
        self.failUnlessEqual(words, {'Abc', 'def', 'gh', 'iL', 'm', 'x'})

    def test_words_from_text_duplicates(self):
        words = model.words_from_text("A A A B C")
        self.failUnlessEqual(words, {"A", "B", "C"})

    def test_word_with_endings(self):
        word = 'abc'
        x = model.word_with_endings(word, ['', 'b', 'aBc'])
        self.failUnlessEqual(x, {'abc', 'abcb', 'abcaBc'})

    def test_word_with_endings_duplicates(self):
        word = "abc"
        x = model.word_with_endings(word, {"x", "x", "y"})
        self.failUnlessEqual(x, {"abcx", "abcy"})

    def test_words_with_endings(self):
        words = ['a', '', 'ABC']
        x = model.words_with_endings(words, {'', 'x', 'XX'})
        self.failUnlessEqual(x, {'a', 'ax', 'aXX', '', 'x', 'XX',
            'ABC', 'ABCx', 'ABCXX'})

    def test_words_with_endings_duplicates(self):
        x = model.words_with_endings(["a", "b", "b"], ["1", "2"])
        self.failUnlessEqual(x, {"a1", "a2", "b1", "b2"})


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
