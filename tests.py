# -*- coding: utf-8 -*-
import unittest
import model


class VocabFindingTests(unittest.TestCase):

    def test_words_from_text(self):
        words = model.words_from_text("!Abc &§$def,gh   iL..m\r\n\tx")
        self.failUnlessEqual(words, ['Abc', 'def', 'gh', 'iL', 'm', 'x'])

    def test_word_with_endings(self):
        word = 'abc'
        x = model.word_with_endings(word, ['', 'b', 'aBc'])
        self.failUnlessEqual(x, ['abc', 'abcb', 'abcaBc'])

    def test_words_with_endings(self):
        words = ['a', '', 'ABC']
        x = model.words_with_endings(words, ['', 'x', 'XX'])
        self.failUnlessEqual(x, ['a', 'ax', 'aXX', '', 'x', 'XX',
            'ABC', 'ABCx', 'ABCXX'])


if __name__ == '__main__':
    unittest.main()
