import os
import sys

sys.path.append(
    os.path.normpath(
        os.path.join(os.path.abspath(__file__), "..", "..", "..", "common")
    )
)
from env_indigo import *

indigo = Indigo()


def testSmarts(m):
    print(m.smarts())
    print(m.smiles())


molstr = """
  Ketcher 11241617102D 1   1.00000     0.00000     0

  8  7  0     0  0            999 V2000
    3.7000   -4.9000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    4.5660   -5.4000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    5.4321   -4.9000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    6.2981   -5.4000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    7.1641   -4.9000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    8.0301   -5.4000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    8.8962   -4.9000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    9.7622   -5.4000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  1  0     0  0
  2  3  1  0     0  0
  3  4  1  0     0  0
  4  5  1  0     0  0
  5  6  1  0     0  0
  6  7  1  0     0  0
  7  8  1  0     0  0
M  CHG  1   3   5
M  END
"""

notlist = """
  -INDIGO-06202202172D

  0  0  0  0  0  0  0  0  0  0  0 V3000
M  V30 BEGIN CTAB
M  V30 COUNTS 9 8 0 0 0
M  V30 BEGIN ATOM
M  V30 1 C 4.9359 -3.675 0.0 0
M  V30 2 C 5.80192 -3.175 0.0 0
M  V30 3 NOT[B,C,N] 6.66795 -3.675 0.0 0
M  V30 4 C 7.53397 -3.175 0.0 0
M  V30 5 C 8.4 -3.675 0.0 0
M  V30 6 C 9.26603 -3.175 0.0 0
M  V30 7 C 10.1321 -3.675 0.0 0
M  V30 8 C 10.9981 -3.175 0.0 0
M  V30 9 C 11.8641 -3.675 0.0 0
M  V30 END ATOM
M  V30 BEGIN BOND
M  V30 1 1 1 2
M  V30 2 1 2 3
M  V30 3 1 3 4
M  V30 4 1 4 5
M  V30 5 1 5 6
M  V30 6 1 6 7
M  V30 7 1 7 8
M  V30 8 1 8 9
M  V30 END BOND
M  V30 END CTAB
M  END
"""

print("**** Load and Save as Query ****")
m = indigo.loadQueryMolecule(molstr)
testSmarts(m)

print("**** Load and Save as Molecule ****")
m = indigo.loadMolecule(molstr)
testSmarts(m)

print("**** Load and Save as Query with not list ****")
m = indigo.loadQueryMolecule(notlist)
print(m.smarts())
