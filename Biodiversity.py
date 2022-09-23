import populations
from PrimaryProducers import *
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


def BiodiversityIndex():
    sum = 0
    for species in SpeciesList:
        sum += (get_n(species)/N) ^ 2

    return (1 - sum)


if __name__ == "__main__":
    print(BiodiversityIndex())
