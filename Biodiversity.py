from populations import *
from PrimaryProducers import *
from PrimaryConsumers import *
from Decomposers import *
from SecondaryConcumers import *


SpeciesList = getSpeciesList()

def get_N(): #get the total number of organisms
    total = 0
    for species in SpeciesList:
        total += species.unit_num
    return total


def get_n(species): #get the number of organisms in a species
    return species.unit_num


N = get_N()

def BiodiversityIndex(): #calculate the biodiversity index
    # for every species, divide it's population by the total population,
    # square it, and add it to the sum
    sum = 0
    for species in SpeciesList:
        sum += (get_n(species)/N) ** 2

    return (1 - sum)


if __name__ == "__main__": # run the program
    print(BiodiversityIndex())
