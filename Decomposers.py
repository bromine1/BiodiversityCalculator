from OrganismClass import *
Worm = DP(mass_per_organism=0.37, organism_per_acre=1089000, acre=60, unit_num=100)
Maggot = DP(mass_per_organism=12.23, num_of_organism=500)

# Worms chosen at high number due to the huge number of them, and that they basically use nothing to survive
# Unit number is brought down by signifiganct amrgins as to not overrepresent the worms, as many may never
# see the surface

# maggots chosen at a smaller number to limit rampant growth
