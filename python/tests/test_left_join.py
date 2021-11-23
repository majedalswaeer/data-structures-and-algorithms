from hashTables.hash_table import HashTable,left_join


def test_1():
    #Arrange
    hash_1=HashTable()
    hash_2=HashTable()
    hash_1.add('fond','enamored')
    hash_1.add('wrath','anger')
    hash_1.add('diliget','employed')
    hash_2.add('fond','aversed')
    hash_2.add('wrath','delight')
    hash_2.add('diliget','idle')

    expected=[
        ['fond', 'enamored', 'aversed'],
        ['diliget', 'employed', 'idle'],
        ['wrath', 'anger', 'delight']
        ]

    #Act
    actual=left_join(hash_1,hash_2)

    #Assert
    assert actual==expected

def test_2():
    #Arrange
    hash_1=HashTable()
    hash_2=HashTable()
    hash_1.add('majed','whats')
    hash_1.add('ahmed','going')
    hash_1.add('zaid','on')
    hash_2.add('majed','the')
    hash_2.add('ahmed','meaning')
    hash_2.add('zaid','of')

    expected=[
        ['zaid', 'on', 'of'],
        ['majed', 'whats', 'the'],
        ['ahmed', 'going', 'meaning']
        ]

    #Act
    actual=left_join(hash_1,hash_2)

    #Assert
    assert actual==expected
