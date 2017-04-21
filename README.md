# Gauss-Bonnet Theorem Verification Tool

## Installation

This program has no dependencies on any third party libraries. All that is necessary is a python interpreter. This program was
written and tested with python 2.7

## Running the program

In order to run this program execute the following command while in the installation directory of this project:

  python test.py [fileName]

where [fileName] should be a simple .obj file.

## Known Bugs

- .obj files that contain more face data than associated vertices will not be parsed correctly

- With larger models, the precision is not high enough to keep track of the angles for the calculation of the Gaussian Curvature. Thus, the final results will not show verification of the Gauss-Bonnet Theorem in the case of high fidelity models
