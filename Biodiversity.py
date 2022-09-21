import populations
from PrimaryProducersers import *
from PrimaryConsumers import *
from Decomposers import *
from SecondaryConcumers import *

SpeciesList = populations.output()


def get_N():
    total = 0
    for species in SpeciesList:
        total += species.unit_num
    return total


def get_n(species):
    species.unit_num


N = get_N()
sum = 0
for species in speciesList:
    sum += (get_n(species)/N) ^ 2

BiodiversityIndex = 1 - sum


if name == __main__:
    print(BiodiversityIndex)
