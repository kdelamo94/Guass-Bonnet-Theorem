from obj_loader.obj_loader import load
import sys

import math

aMesh = load(sys.argv[1])
print(aMesh.toString())



print(len(aMesh.vertices))
print(len(aMesh.faces))
print(len(aMesh.edges))
print(len(aMesh.halfEdges))
X = len(aMesh.vertices) + len(aMesh.faces) - len(aMesh.edges)

print("X = " + str(X))

K = 0

for vertex in aMesh.vertices:

    totalAngles = 0

    currentHalfEdge = vertex.halfEdge_in.getReverse()

    v1 = currentHalfEdge.toVector()

    while currentHalfEdge.targetVertex.vId != vertex.vId:
        currentHalfEdge = currentHalfEdge.halfEdge_next

    currentHalfEdge = currentHalfEdge.getReverse()
    v2 = currentHalfEdge.toVector()

    #calculate dot product of vector1 and vector2
    dp = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

    #Calculate angle using the Law of Cosines
    maga = math.sqrt(float(v1[0]*v1[0]+v1[1]*v1[1]+v1[2]*v1[2]))
    magb = math.sqrt(float(v2[0]*v2[0]+v2[1]*v2[1]+v2[2]*v2[2]))
    dp = dp/(maga*magb)
    angle = math.acos(dp)

    #Adding to running sum of angles of this vertex
    totalAngle = totalAngles + angle

    while id(currentHalfEdge) != id(vertex.halfEdge_in.getReverse()):
        print("New Set")
        #set first vector for angle calculation
        v1 = currentHalfEdge.toVector()
        print("V2: " + str(v1))
        #loop through face halfedges to get ingoing halfedge
        while currentHalfEdge.targetVertex.vId != vertex.vId:
            currentHalfEdge = currentHalfEdge.halfEdge_next

        currentHalfEdge = currentHalfEdge.getReverse()

        #Set second vector for angle calulation
        v2 = currentHalfEdge.toVector()
        print("V2: " + str(v2))
        #calculate dot product of vector1 and vector2
        dp = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
        print("Dot Product: "  + str(dp))
        #Calculate angle using the Law of Cosines
        maga = math.sqrt(v1[0]*v1[0]+v1[1]*v1[1]+v1[2]*v1[2])
        print("Magnitude V1: " + str(maga))
        magb = math.sqrt(v2[0]*v2[0]+v2[1]*v2[1]+v2[2]*v2[2])
        print("Magnitude V2: " + str(magb))
        dp = dp/(maga*magb)
        print("Before ArcCos: " + str(dp))
        angle = math.acos(dp)
        print("Angle: " + str(angle))
        print("Angle Degrees: " + str(math.degrees(angle)))
        #Adding to running sum of angles of this vertex
        totalAngle = totalAngle + angle

        print

        print totalAngle

        print

    #calulate 2pi - sumOfAngles
    Kv = 2*math.pi - totalAngle
    #add to running total of Gaussian Curvature
    K = K + Kv
#check that Gaussian curvature = 2pi*X

print(str(K) + ' = ' + str(2*math.pi*X))
