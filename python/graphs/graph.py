from collections import deque


class Vertex:
  """
  Class for Adding a node to the graph
  Arguments: value
  Returns: The added node
  """
  def __init__(self, value):
    """
    Initalization for a Vertex to hold a value.

    """
    self.value = value

class Queue:
  def __init__(self):
    self.dq = deque()

  def enqueue(self, value):
    self.dq.appendleft(value)

  def dequeue(self):
    self.dq.pop()

  def __len__(self):
    return len(self.dq)


class Stack:
  def __init__(self):
    """
		The constructor method for the stack class and it initializes the dq property to a new double ended queue instance.
		"""
    self.dq = deque()

  def push(self, value):
    """
		Store the passed value in a node and then push the node on top of the stack.

		PARAMETERS
		----------
			value: any
				The value that will get stored in a node to be pushed on top of the stack.
		"""
    self.dq.append(value)

  def pop(self):
    """
		Return the top node in a stack.
		"""
    self.dq.pop()

class Edge:
  """
    a class for Adding a new edge between two nodes in the graph
    If specified, assigning a weight to the edge
    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing

  """
  def __init__(self, vertex, weight):
    self.vertex = vertex
    self.weight = weight

class Graph:
  def __init__(self):
    """
    Initalization for a hashmap to hold the vertices
    """
    self.__adjacency_list = {}

  def add_node(self, value):
    """
      Method for Adding a node to the graph
      Arguments: value
      Returns: The added node
    """
    # new node
    v = Vertex(value)
    self.__adjacency_list[v] = []
    return v

  def size(self):
    return len(self.__adjacency_list)

  def add_edge(self, start_vertex, end_vertex, weight=0):
    """Adds an edge to the graph"""
    if start_vertex not in self.__adjacency_list:
      raise KeyError("Start Vertex not found in graph")

    if end_vertex not in self.__adjacency_list:
      raise KeyError("End Vertex not found in graph")

    edge = Edge(end_vertex, weight)
    self.__adjacency_list[start_vertex].append(edge)

  def get_nodes(self):
    """
    Method to get all nodes in Graph
    Arguments: None
    return: All nodes
    """
    return self.__adjacency_list.keys()

  def get_neigbors(self, vertex):
    """ """
    return self.__adjacency_list.get(vertex, [])

  def breadth_first_search(self, start_vertex, action=(lambda vertex: None)):
    queue = Queue()
    visited = set()
    print(queue)
    queue.enqueue(start_vertex)
    visited.add(start_vertex)
    while len(queue):
      current_vertex = queue.dequeue()
      action(current_vertex)

      neighbors = self.get_neigbors(current_vertex)

      for edge in neighbors:
        neighbor =  edge.vertex

        if neighbor not in visited:
          visited.add(neighbor)
          queue.enqueue(neighbor)

  def breadth_first(self, start_vertex):
    """

      This function takes a vertex to start with, and return a list containing the nodes in the graph according to the breadth first order

       Args:
          start_vertex ([type]): Vertex

       Returns:
          List

    """

    queue = []
    results=[]
    visited = set()
    queue.append(start_vertex)
    visited.add(start_vertex)
    while len(queue):
      current_vertex = queue.pop(0)
      results.append(current_vertex.value)

      neighbors = self.get_neigbors(current_vertex)

      for edge in neighbors:
        neighbor =  edge.vertex

        if neighbor not in visited:
          visited.add(neighbor)
          queue.append(neighbor)
    return results





if __name__ =='__main__':
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
    print(ins.breadth_first(n1))
    # x=ins.get_nodes()
    # y=list(x)
    # for i in range(len(x)):
    #     print(y[i].value)






