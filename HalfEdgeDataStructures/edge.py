class Edge:
    def __init__(self):
        self.halfEdge1 = None
        self.halfEdge2 = None

    def setHalfEdge1(self, halfEdge):
        self.halfEdge1 = halfEdge

    def setHalfEdge2(self, halfEdge):
        self.halfEdge2 = halfEdge

    def toString(self):
        string = self.halfEdge1.sourceVertex.toString()
        string = string + ' -- '
        string = string + self.halfEdge1.targetVertex.toString()

        return string
