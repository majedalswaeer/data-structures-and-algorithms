from graphs.graph import  Graph, Vertex

def test_breadth_first():
    #Arrange
    ins=Graph()
    n1=ins.add_node('pandora')
    n2=ins.add_node('Arendelle')
    n3=ins.add_node('Metroville')
    n4=ins.add_node('Monstroplolis')
    n5=ins.add_node('Narnia')
    n6=ins.add_node('Naboo')
    ins.add_edge(n1,n2,1)
    ins.add_edge(n2,n3,1)
    ins.add_edge(n2,n4,1)
    ins.add_edge(n3,n4,1)
    ins.add_edge(n4,n6,1)
    ins.add_edge(n3,n5,1)
    ins.add_edge(n3,n6,1)
    ins.add_edge(n5,n6,1)
    expected=['pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']

    #Act
    actual=ins.breadth_first(n1)

    #Assert
    assert actual==expected
