import pytest

from graphs.graph import  Graph, Vertex,business_trip

def test_add_node():
  graph = Graph()
  expected = "test"
  actual = graph.add_node('test').value
  assert actual == expected

def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected


def test_size():

    graph = Graph()

    graph.add_node('spam')

    expected = 1

    actual = graph.size()

    assert actual == expected


def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex('end')

    start = graph.add_node('start')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)
def test_get_nodes():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    loner = Vertex('loner')

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected


def test_get_neighbors():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neigbors(apple)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.vertex.value == 'banana'

    assert neighbor_edge.weight == 44

def test_bussines_trip():

    #Arrange

    my_graph = Graph()
    pandora = my_graph.add_node('Pandora')
    arendelle = my_graph.add_node('Arendelle')
    metroville = my_graph.add_node('Metroville')
    monstropolis = my_graph.add_node('Monstropolis')
    naboo = my_graph.add_node('Naboo')
    narnia = my_graph.add_node('Narnia')
    my_graph.add_edge(pandora,arendelle,150)
    my_graph.add_edge(arendelle,pandora,150)
    my_graph.add_edge(pandora,metroville,82)
    my_graph.add_edge(metroville,pandora,82)
    my_graph.add_edge(arendelle,metroville,99)
    my_graph.add_edge(metroville,arendelle,99)
    my_graph.add_edge(arendelle,monstropolis,42)
    my_graph.add_edge(monstropolis,arendelle,42)
    my_graph.add_edge(monstropolis,metroville,105)
    my_graph.add_edge(metroville,monstropolis,105)
    my_graph.add_edge(monstropolis,naboo,73)
    my_graph.add_edge(naboo,monstropolis,73)
    my_graph.add_edge(metroville,naboo,26)
    my_graph.add_edge(naboo,metroville,26)
    my_graph.add_edge(metroville,narnia,37)
    my_graph.add_edge(narnia,metroville,37)
    my_graph.add_edge(naboo,narnia,250)
    my_graph.add_edge(narnia,naboo,250)

    #Act
    expected=[True, '82$']
    actual=business_trip(my_graph,[metroville,pandora])

    expected1=[True, '115$']
    actual1=business_trip(my_graph,[arendelle,monstropolis,naboo])

    expected2=[False, '0$']
    actual2=business_trip(my_graph,[naboo,pandora])

    expected3=[False, '0$']
    actual3=business_trip(my_graph,[narnia,arendelle,naboo])

    #Assert
    assert actual==expected
    assert actual1==expected1
    assert actual2==expected2
    assert actual3==expected3


def test_breadth_first():
    #Arrange
    graph = Graph()
    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    d = graph.add_node('D')
    e = graph.add_node('E')
    f = graph.add_node('F')
    g = graph.add_node('G')
    h = graph.add_node('H')
    graph.add_edge(a,b)
    graph.add_edge(a,d)
    graph.add_edge(b,c)
    graph.add_edge(b,d)
    graph.add_edge(c,g)
    graph.add_edge(d,e)
    graph.add_edge(d,h)
    graph.add_edge(d,f)
    graph.add_edge(f,h)
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']

    #Act
    actual = graph.depth_first(a)

    #Assert
    assert actual == expected
