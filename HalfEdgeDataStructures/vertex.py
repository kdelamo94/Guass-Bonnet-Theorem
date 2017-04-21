class Vertex:
    def __init__(self):

        self.vId = None

        self.position = None
        self.halfEdge_in = None

    def setPosition(self, point):
        self.position = point

    def setInHalfEdge(self, halfEdge_in):
        if self.halfEdge_in == None:
            self.halfEdge_in = halfEdge_in

    def getPosition(self):
        return self.position

    def getInHalfEdge(self):
        return self.halfEdge_in

    def toString(self, showPos=False):
        string = '' + str(self.vId)

        if showPos:
            string = string + ':' + position

        return string
