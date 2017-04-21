class HalfEdge:
    def __init__(self):

        self.halfEdge_next = None
        self.halfEdge_prev = None

        self.targetVertex = None
        self.sourceVertex = None

        self.adjacentEdge = None

        self.face = None

    def setHalfEdge_next(self, halfEdge_next):
        self.halfEdge_next = halfEdge_next

    def setHalfEdge_prev(self, halfEdge_prev):
        self.halfEdge_prev = halfEdge_prev

    def setTarget(self, target):
        self.targetVertex = target

    def setSource(self, source):
        self.sourceVertex = source

    def setAdjacentEdge(self, edge):
        self.adjacentEdge = edge

    def setFace(self, face):
        self.face = face

    def getReverse(self):
        if(id(self.adjacentEdge.halfEdge1) == id(self)):
            return self.adjacentEdge.halfEdge2
        else:
            return self.adjacentEdge.halfEdge1
    def toVector(self):
        x = self.targetVertex.position[0] - self.sourceVertex.position[0]
        y = self.targetVertex.position[1] - self.sourceVertex.position[1]
        z = self.targetVertex.position[2] - self.sourceVertex.position[2]

        return (x, y, z)

    def toString(self):

        string = self.sourceVertex.toString()
        string = string + ' -> '
        string = string + self.targetVertex.toString()

        return string
