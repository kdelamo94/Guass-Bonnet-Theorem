class Face:
    def __init__(self):
        self.halfEdge = None

    def setHalfEdge(self, halfEdge):
        if self.halfEdge == None:
            self.halfEdge = halfEdge

    def getHalfEdge(self):
        return self.halfEdge

    def toString(self):
        v1 = self.halfEdge.sourceVertex
        v2 = self.halfEdge.halfEdge_next.sourceVertex
        v3 = self.halfEdge.halfEdge_prev.sourceVertex

        string = (
            '(' +
            v1.toString() + ', ' +
            v2.toString() + ', ' +
            v3.toString() +
            ')'
        )

        return string
