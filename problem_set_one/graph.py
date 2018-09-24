class Graph:
  def __init__(self, edges):
    self.edges = edges


class Vertex:
  def __init__(self, data):
    self.data = data


class Edge:
  def __init__(self, vertex_to, vertex_from):
    self.vertex_to = vertex_to
    self.vertex_from = vertex_from
