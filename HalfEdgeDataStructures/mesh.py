class Mesh:
    def __init__(self):
        self.faces = None
        self.vertices = None
        self.edges = None
        self.halfEdges = None

    def addFace(self, face):
        self.faces.append(face)

    def addVertex(self, vertex):
        self.vertices.append(vertex)

    def toString(self):
        string = ''

        print(string)
        string = string + "Vertices:\n"
        print(string)
        for vertex in self.vertices:
            string = string + vertex.toString() + '\n'

        string = string + "\nFaces:\n"
        for face in self.faces:
            string = string + face.toString() + '\n'

        string = string + "\nEdges:\n"
        for edge in self.edges:
            string = string + edge.toString() + '\n'

        string = string + "\nHalfEdges:\n"
        for halfEdge in self.halfEdges:
            string = string + halfEdge.toString() + '\n'

        return string
