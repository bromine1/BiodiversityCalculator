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



PrimaryProducers = [
    "Bamboo",
    "Junipers",
    "SoyBeans",
    "BottleGourds",
    "Hemp",
    "Poppy",
    "Ginkgo",
    "Moss",
    "Ferns",
    "Rye"
]

PrimaryConsumers = [
    "Bee",
    "Ant",
    "Butterfly"
]

Decomposers = [
    "Fly",
    "Worm"
]
SecondaryConsumers = [
    "Spider",
    "Toad",
    "Quail",
    "Dragonfly"
]

TertiaryConsumers = [
    "Owl"
]

Owl = TC()

def BioMassCalculations():
    PPBiomass = 0
    for x in PrimaryProducers:
        PPBiomass += vars()[x].biomass

    PCBiomass = 0
    for x in PrimaryConsumers:
        PCBiomass += vars()[x].biomass

    DPBiomass = 0
    for x in Decomposers:
        DPBiomass += vars()[x].biomass

    SCBiomass = 0
    for x in SecondaryConsumers:
        SCBiomass += vars()[x].biomass

    TCBiomass = 0
    for x in TertiaryConsumers:
        TCBiomass += vars()[x].biomass

    if TCBiomass * 10 <= (SCBiomass) and SCBiomassB <= (PCBiomass + DPBiomass) and PCBiomass <= PPBiomass:
        return True

def output(fancy=false):
    for group in [PrimaryProducers, PrimaryConsumers, Decomposers, SecondaryConsumers, TertiaryConsumers]:
        if fancy:
            for species in group:
                print(f"{species}: {vars()[species].biomass}")
            return True
        else:
            SpeciesList = []
            for species in group:
                return SpeciesList
                

if name == __main__:
    if BioMassCalculations():
        output(true)
