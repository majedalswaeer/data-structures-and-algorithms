import pytest
from hashTables.hash_table import LinkedList,Node,HashTable
from hashTables.repeat import hashmap_repeated_word


def test_hash(hash_t):

    expected=779

    actual=hash_t._HashTable__hash('m')

    assert actual==expected


def test_add(hash_t):

    expected=True
    added=hash_t.add('majed',1)

    actual=hash_t.contains('majed')

    assert actual==expected


def test_contains_true(hash_t):

    expected=True
    added=hash_t.add('majed','so what')

    actual=hash_t.contains('majed')

    assert actual==expected


def test_contains_false(hash_t):

    expected=False

    actual=hash_t.contains('whatever')

    assert actual==expected


def test_get(hash_t):

    expected='so what'
    added=hash_t.add('majed','so what')

    actual=hash_t.get('majed')

    assert actual==expected

def test_repeat():
    x='Once upon a time, there was a brave princess who...'
    expected='a'
    actual=hashmap_repeated_word(x)
    assert actual==expected


def test_repeat_2():
    x='It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...'
    expected='it'
    actual=hashmap_repeated_word(x)
    assert actual==expected
    
def test_repeat_3():
    x='It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...'
    expected='summer'
    actual=hashmap_repeated_word(x)
    assert actual==expected
@pytest.fixture

def hash_t():
    return HashTable()
