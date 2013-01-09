# -*- coding: utf-8 -*-
import unittest
import model
import endings


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
        x = model.words_from_text("A A A B C")
        self.failUnlessEqual(x, {"A", "B", "C"})


class WordWithEndings(unittest.TestCase):
    def test_connecting(self):
        x = model.word_with_endings("abc", {'', 'b', 'aBc'})
        self.failUnlessEqual(x, {'abc', 'abcb', 'abcaBc'})

    def test_empty_wordlist(self):
        x = model.word_with_endings(set(), {"a", "b"})
        self.failUnlessEqual(x, set())

    def test_empty_endings(self):
        x = model.word_with_endings("x", set())
        self.failUnlessEqual(x, {"x"})

    def test_empty_both(self):
        x = model.word_with_endings(set(), set())
        self.failUnlessEqual(x, set())

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

    def test_empty_both(self):
        x = model.words_with_endings(set(), set())
        self.failUnlessEqual(x, set())

    def test_duplicates(self):
        x = model.words_with_endings(["a", "b", "b"], ["1", "2"])
        self.failUnlessEqual(x, {"a1", "a2", "b1", "b2"})


class MissingVocabulary(unittest.TestCase):
    def test_basic(self):
        x = model.missing_vocabulary({"a1", "a2", "a3"}, {"a", "b"}, {"1", "2"})
        self.failUnlessEqual(x, {"a3"})

    def test_basic_case(self):
        x = model.missing_vocabulary({"A1", "A2", "A3"}, {"A", "B"}, {"1", "2"})
        self.failUnlessEqual(x, {'a3'})

    def test_empty_words(self):
        x = model.missing_vocabulary(set(), {"a", "b"}, {"1", "2"})
        self.failUnlessEqual(x, set())

    def test_empty_basicforms(self):
        x = model.missing_vocabulary({"a", "b", "c", "d"}, set(), {"a", "b"})
        self.failUnlessEqual(x, {"a", "b", "c", "d"})

    def test_empty_endings(self):
        x = model.missing_vocabulary({"a", "b", "c", "d"}, {"c", "d"}, set())
        self.failUnlessEqual(x, {"a", "b"})

    def test_only_words(self):
        x = model.missing_vocabulary({"a", "b", "c", "d"}, set(), set())
        self.failUnlessEqual(x, {"a", "b", "c", "d"})

    def test_words_and_basicforms(self):
        x = model.missing_vocabulary({"a", "b", "c", "d"}, {"a", "b"}, set())
        self.failUnlessEqual(x, {"c", "d"})

    def test_words_and_endings(self):
        x = model.missing_vocabulary({"a", "b", "c", "d"}, set(), {"c", "d"})
        self.failUnlessEqual(x, {"a", "b", "c", "d"})

    def test_empty_args(self):
        x = model.missing_vocabulary(set(), set(), set())
        self.failUnlessEqual(x, set())

    def test_word_is_in_vocab(self):
        x = model.missing_vocabulary({"xxx", "yyy"}, {"xxx", "yyy"}, set())
        self.failUnlessEqual(x, set())


class ParsingTests(unittest.TestCase):
    def setUp(self):
        endings.save(['abc', '# def', '', '  ', '  test', ' ##'],
            'test_endings.txt')

    def test_load_endings(self):
        x = endings.load('test_endings.txt')
        self.failUnlessEqual(x, ['abc', 'test'])

    def tearDown(self):
        import os
        os.remove('test_endings.txt')


if __name__ == '__main__':
    unittest.main()
