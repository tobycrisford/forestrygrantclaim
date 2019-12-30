# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 16:48:11 2019

@author: Toby
"""

import scipy.optimize
import scipy.linalg


def constraints(species, percentage, minimum):
    
    r = [percentage for i in range(0, totalspecies)]
    for tree in species:
        r[speciesdict[tree]] = percentage - 1
    if not minimum:
        for i in range(0, totalspecies):
            r[i] = -1 * r[i]
    return r
    


#The total number of different species in the area (include 'open ground' as a species)
totalspecies = 5

#A labelling for the different species - just list all the species names with numbers 0 upwards
#A list of all the species names in the same order (just needed for nice looking output at the end)
speciesdict = {"Sitka": 0, "MainConifer": 1, "OtherConifer": 2,"NativeBroad": 3, "Open": 4}
specieslist = ["Sitka", "MainConifer", "OtherConifer", "NativeBroad", "Open"]

#Specify total hectares of each species in same order as dictionary above
specieshectares = [100, 40, 30, 9, 6]

#Create empty list for each scheme, list of scheme names (for output at end), and list of all schemes (in order)
conifer = []
divconifer = []
schemelist = ["Conifer", "Diverse Conifer"]
schemes = [conifer, divconifer]

#Add all the constraints
#Syntax is: YOURSCHEMENAME.append(constraints(...))
#Arguments to 'constraints' are (list of species involved in this constraint, percentage bound, 'True' if minimum or 'False' if maximum)
conifer.append(constraints(["Sitka"], 0.65, minimum=True))
conifer.append(constraints(["Sitka"], 0.75, minimum=False))
conifer.append(constraints(["MainConifer","OtherConifer"], 0.1, minimum=True))
conifer.append(constraints(["MainConifer","OtherConifer"], 0.15, minimum=False))
conifer.append(constraints(["NativeBroad"], 0.05, minimum=True))
conifer.append(constraints(["NativeBroad"], 0.1, minimum=False))
conifer.append(constraints(["Open"], 0.1, minimum=False))
divconifer.append(constraints(["MainConifer"], 0.4, minimum=True))
divconifer.append(constraints(["MainConifer"], 0.75, minimum=False))
divconifer.append(constraints(["OtherConifer"], 0.1, minimum=True))
divconifer.append(constraints(["OtherConifer"], 0.4, minimum=False))
divconifer.append(constraints(["NativeBroad"], 0.05, minimum=True))
divconifer.append(constraints(["NativeBroad"], 0.1, minimum=False))
divconifer.append(constraints(["Open"], 0.1, minimum=False))

#Payment rate per hectare of each scheme in same order as 'schemes' list above
schemevalues = [2960,3840]

#Everything past this point doesn't need modifying


A = scipy.linalg.block_diag(*schemes).tolist()
b = [0 for i in range(0,len(A))]
for i in range(0, totalspecies):
    c = [0 for j in range(0,totalspecies*len(schemes))]
    for k in range(0, len(schemes)):
        c[i + k*totalspecies] = 1
    A.append(c)
    b.append(specieshectares[i])

objective = []
for i in range(0,len(schemes)):
    objective = objective + [-schemevalues[i] for j in range(0, totalspecies)]

result = scipy.optimize.linprog(objective, A_ub=A, b_ub=b)

print(result.message)
print("Maximum possible payment rate is: " + str(-1*result.fun))
print("This is achieved by the following distribution\n")
for i in range(0, len(schemes)):
    print("Scheme: " + schemelist[i] + "\n")
    totalcount = 0
    for j in range(0, totalspecies):
        r = result.x[j + i*totalspecies]
        totalcount = totalcount + r
        print(specieslist[j] + ": " + str(r) + " hectares")
    print("Total: " + str(totalcount) + " hectares")
    print("\n")
