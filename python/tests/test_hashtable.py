import pytest
from hashTables.hash_table import LinkedList,Node,HashTable



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



@pytest.fixture

def hash_t():
    return HashTable()
