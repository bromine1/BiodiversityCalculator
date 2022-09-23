# get data from files that contain organisms
from PrimaryProducers import *
from PrimaryConsumers import *
from Decomposers import *
from SecondaryConcumers import *


# assign names to the organisms so python can work with them more easily
PrimaryProducers = {
    'Bamboo':       Bamboo,
    "Junipers":     Junipers,
    "SoyBeans":     SoyBeans,
    "BottleGourds": BottleGourds,
    "Hemp":         Hemp,
    "Poppy":        Poppy,
    "Ginkgo":       Ginkgo,
    "Moss":         Moss,
    "Ferns":        Ferns,
    "Rye":          Rye,
}

PrimaryConsumers = {
    "Bee":          Bee,
    "Ant":          Ant,
    "Butterfly":    Butterfly,
}

Decomposers = {
    "Maggot":       Maggot,
    "Worm":         Worm,
}

SecondaryConsumers = {
    "Spider":       Spider,
    "Toad":         Toad,
    "Quail":        Quail,
    "Dragonfly":    Dragonfly,
}


# Define the owl, no point in a one line file
Owl = TC(mass_per_organism=18.34, num_of_organism=6)
# Chosen to have enough for humans to utilize,

TertiaryConsumers = {
    "Owl":          Owl,
}


def BioMassCalculations():
    # Get the Biomass for every energy level
    PPBiomass = 0
    for x in PrimaryProducers:
        PPBiomass += PrimaryProducers[x].biomass

    PCBiomass = 0
    for x in PrimaryConsumers:
        PCBiomass += PrimaryConsumers[x].biomass

    DPBiomass = 0
    for x in Decomposers:
        DPBiomass += Decomposers[x].biomass

    SCBiomass = 0
    for x in SecondaryConsumers:
        SCBiomass += SecondaryConsumers[x].biomass

    TCBiomass = 0
    for x in TertiaryConsumers:
        TCBiomass += TertiaryConsumers[x].biomass
    
    # Check to make sure that is enough energy in the system,
    # and report back errors
    if TCBiomass * 10 <= (SCBiomass):
        if SCBiomass <= (PCBiomass + DPBiomass):
            if PCBiomass <= PPBiomass:
                return True
            else:
                return "Not Enough Plants"
        else:
            return "Not enough Primary Consumers"
    else:
        return "Not Enough Secondary Consumers"

def output(fancy=False):
    # Function to output to terminal tables of data
    print("Species".center(20), end="")
    print("Biomass (grams)".center(20), end="")
    print("Unit Amount".center(13))
    print("".ljust(50, "_"))
    groups = [
        "Primary Producers",
        "Primary Consumers",
        "Decomposers",
        "Secondary Consumers",
        "Tertiary Consumers"
    ]
    
    CurrentGroup = 0


    for group in [PrimaryProducers, PrimaryConsumers, Decomposers, SecondaryConsumers, TertiaryConsumers]:
        print("\n\n")
        print(f"{groups[CurrentGroup]}".center(53))
        CurrentGroup += 1
        print("Species".center(20), end="")
        print("Biomass (grams)".center(20), end="")
        print("Unit Amount".center(13))
        print("".ljust(50, "_"))
        
        for species in group:
            print(f"{species}".center(20), end="|")
            print(f"{round(group[species].biomass, 2)}".center(20), end="|")
            # print("grams ", end="")
            print(f"{group[species].unit_num}".ljust(10))


def getSpeciesList():
    # get the main species list
    # used in Biodiversity.py
    SpeciesList = []
    for group in [PrimaryProducers, PrimaryConsumers, Decomposers, SecondaryConsumers, TertiaryConsumers]:
        for species in group:
            SpeciesList.append(group[species])
    return SpeciesList
        

if __name__ == "__main__":
    if BioMassCalculations():
        output()
