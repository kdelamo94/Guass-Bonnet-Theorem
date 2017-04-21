from HalfEdgeDataStructures.edge import Edge
from HalfEdgeDataStructures.face import Face
from HalfEdgeDataStructures.halfEdge import HalfEdge
from HalfEdgeDataStructures.mesh import Mesh
from HalfEdgeDataStructures.vertex import Vertex

def load(filename):
    vertices = []
    edges = []
    halfEdges = []
    faces = []

    f = open(filename, 'r')
    vId = 1
    fId = 1
    for line in f:
        dataType = line.split()[0]

        if dataType == 'v':
            vertex = Vertex()
            vertex.position = (
                float(line.split()[1]),
                float(line.split()[2]),
                float(line.split()[3])
            )
            vertex.vId = vId
            vertices.append(vertex)
            vId = vId + 1


        if dataType == 'f':

            #print("Face " + str(fId))
            #instantiate this face
            face = Face()
            fId = fId + 1
            """
            create halfedge 1 and set as face's first half edge. Associate with
            current edge or create new edge
            """
            he1 = HalfEdge()
            he1.sourceVertex = vertices[int(line.split()[1]) - 1]
            he1.targetVertex = vertices[int(line.split()[2]) - 1]
            he1.targetVertex.setInHalfEdge(he1)
            face.setHalfEdge(he1)

            found = False
            for edge in edges:
                if (
                    (edge.halfEdge1.sourceVertex == he1.targetVertex) and
                    (edge.halfEdge1.targetVertex == he1.sourceVertex)
                ):
                    edge.halfEdge2 = he1
                    he1.adjacentEdge = edge
                    found = True
                    #print("Found Existing Edge: " + edge.toString())

            if not found:
                edge = Edge()
                edge.halfEdge1 = he1
                he1.adjacentEdge = edge
                edges.append(edge)
                #print("Created New Edge: " + edge.toString())

            halfEdges.append(he1)

            """
            create halfedge 2. Associate with current edge or create new edge
            """
            he2 = HalfEdge()
            he2.sourceVertex = vertices[int(line.split()[2]) - 1]
            he2.targetVertex = vertices[int(line.split()[3]) - 1]
            he2.targetVertex.setInHalfEdge(he2)
            he1.halfEdge_next = he2
            he2.halfEdge_prev = he1

            found = False
            for edge in edges:
                if (
                    (edge.halfEdge1.sourceVertex == he2.targetVertex) and
                    (edge.halfEdge1.targetVertex == he2.sourceVertex)
                ):
                    edge.halfEdge2 = he2
                    he2.adjacentEdge = edge
                    found = True
                    #print("Found Existing Edge: " + edge.toString())
            if not found:
                edge = Edge()
                edge.halfEdge1 = he2
                he2.adjacentEdge = edge
                edges.append(edge)
                #print("Created New Edge: " + edge.toString())
            halfEdges.append(he2)

            """
            create halfedge 3. Associate with current edge or create new edge
            """
            he3 = HalfEdge()
            he3.sourceVertex = vertices[int(line.split()[3]) - 1]
            he3.targetVertex = vertices[int(line.split()[1]) - 1]
            he3.targetVertex.setInHalfEdge(he3)
            he2.halfEdge_next = he3
            he3.halfEdge_prev = he2

            found = False
            for edge in edges:
                if (
                    (edge.halfEdge1.sourceVertex == he3.targetVertex) and
                    (edge.halfEdge1.targetVertex == he3.sourceVertex)
                ):
                    edge.halfEdge2 = he3
                    he3.adjacentEdge = edge
                    found = True
                    #print("Found Existing Edge: " + edge.toString())

            if not found:
                edge = Edge()
                edge.halfEdge1 = he3
                he3.adjacentEdge = edge
                edges.append(edge)
                #print("Created New Edge: " + edge.toString())
            halfEdges.append(he3)

            he3.halfEdge_next = he1
            he1.halfEdge_prev = he3

            faces.append(face)

    aMesh = Mesh()

    aMesh.faces = faces
    aMesh.vertices = vertices
    aMesh.halfEdges = halfEdges
    aMesh.edges = edges


    print("loading complete")
    print(len(edges))
    print(len(halfEdges))
    return aMesh
