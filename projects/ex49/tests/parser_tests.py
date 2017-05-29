from nose.tools import *
from ex49 import ex49
from ex49 import lexicon

def test_peek_none():
    assert_equal(ex49.peek(None), None)

def test_peek_direction():
    word_list = lexicon.scan("north south")
    assert_equal(ex49.peek(word_list), 'direction')

def test_peek_verb():
    word_list = lexicon.scan("go stop")
    assert_equal(ex49.peek(word_list), 'verb')

def test_peek_stop():
    word_list = lexicon.scan("in of")
    assert_equal(ex49.peek(word_list), 'stop')

def test_peek_noun():
    word_list = lexicon.scan("bear door princess")
    assert_equal(ex49.peek(word_list), 'noun')

def test_peek_number():
    word_list = lexicon.scan("746 416 71")
    assert_equal(ex49.peek(word_list), 'number')

def test_peek_error():
    word_list = lexicon.scan("other word")
    assert_equal(ex49.peek(word_list), 'error')

def test_match_none():
    assert_equal(ex49.match(None, None), None)
    #assert_equal(ex49.match(True, None), None)
    word_list = lexicon.scan("kick the bear")
    assert_equal(ex49.match(word_list, None), None)
    assert_equal(len(word_list), 2)
    assert_equal(ex49.match(word_list, 'verb'), None)
    assert_equal(len(word_list), 1)
    assert_equal(ex49.match(word_list, 'stop'), None)
    assert_equal(len(word_list), 0)
    assert_equal(ex49.match(word_list, 'noun'), None)
    assert_equal(len(word_list), 0)

def test_match_word():
    word_list = lexicon.scan("kick the bear")
    assert_equal(ex49.match(word_list, 'error'), ('error', 'kick'))
    assert_equal(len(word_list), 2)
    assert_equal(ex49.match(word_list, 'stop'), ('stop', 'the'))
    assert_equal(len(word_list), 1)
    assert_equal(ex49.match(word_list, 'noun'), ('noun', 'bear'))
    assert_equal(len(word_list), 0)

def test_skip():
    word_list = lexicon.scan("the bear")
    ex49.skip(word_list, 'verb')
    assert_equal(len(word_list), 2)
    ex49.skip(word_list, 'stop')
    assert_equal(word_list[0], ('noun','bear'))
    assert_equal(len(word_list), 1)

def test_parse_verb():
    word_list = lexicon.scan("the kill door")
    assert_equal(ex49.parse_verb(word_list), ('verb', 'kill'))
    assert_raises(ex49.ParserError, ex49.parse_verb, word_list)

def test_parse_object():
    word_list = lexicon.scan("the left door open")
    assert_equal(ex49.parse_object(word_list), ('direction', 'left'))
    assert_equal(ex49.parse_object(word_list), ('noun', 'door'))
    assert_raises(ex49.ParserError, ex49.parse_object, word_list)

def test_parse_subject():
    word_list = lexicon.scan("it kill bear")
    sentence = ex49.parse_subject(word_list, ('noun','player'))
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'kill')
    assert_equal(sentence.object, 'bear')

def test_parse_sentence():
    word_list = lexicon.scan("the bear eat the princess")
    sentence = ex49.parse_sentence(word_list)
    assert_equal(sentence.subject, 'bear')
    assert_equal(sentence.verb, 'eat')
    assert_equal(sentence.object, 'princess')

    word_list = lexicon.scan("go right")
    sentence = ex49.parse_sentence(word_list)
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'go')
    assert_equal(sentence.object, 'right')

    word_list = lexicon.scan("a a a a a a")
    assert_raises(ex49.ParserError, ex49.parse_sentence, word_list)
