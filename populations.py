# Population SIzes for BIO
# Populations can only sustain about 10% of those above them
from PrimaryProducers import *
from PrimaryConsumers import *
from Decomposers import *
from SecondaryConcumers import *
# For Example:
# Primary producer = 100
# Primary COnsumer = 10
# Secondary Producer = 1


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

Owl = TC(mass_per_organism=18.34, num_of_organism=6)
# Chosen to have enough for humans to utilize,

TertiaryConsumers = {
    "Owl":          Owl,
}

Owl = TC(mass_per_organism=18.34, num_of_organism=6)
# Chosen to have enough for humans to utilize,

def BioMassCalculations():
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
    print("Species".center(20), end="")
    print("Biomass (grams)".center(20), end="")
    print("Unit Amount".center(13))
    print("".ljust(50, "_"))
    for group in [PrimaryProducers, PrimaryConsumers, Decomposers, SecondaryConsumers, TertiaryConsumers]:
        if fancy:
            for species in group:
                print(f"{species}".center(20), end="|")
                print(f"{round(group[species].biomass, 2)}".center(20), end="|")
                # print("grams ", end="")
                print(f"{group[species].unit_num}".ljust(10))
        else:
            SpeciesList = []
            for species in group:
                return SpeciesList


if __name__ == "__main__":
    if BioMassCalculations():
        output(fancy=True)
