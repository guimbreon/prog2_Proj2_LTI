from devolveLista import *
from constants import * 
from readLN import * 
from findAllStations import *

def writeMS(objeto, myStations, allStations, filePath):
    lines = []

    for i in range(len(objeto)):
        #i is the index of the lists, that will indicate which stations we are working on at the moment
        #this will be used for myStations, objeto and allStations, since they are organized
        #so that the items are coordinated, which means, "i" will always be related to the same src-dest search
        lines.append("# " + myStations[i][0] + " - " + myStations[i][1])
        if objeto[i] != "out of network" and objeto[i] != "do not communicate":
            for caminho, tempo in objeto[i]:
                caminhoStr = str(tempo) + ", "
                count = 1
                for item in caminho:
                    if len(caminho) > count:
                        caminhoStr += item.__str__() + ", "
                    else:
                        caminhoStr += item.__str__()
                    count += 1

                lines.append(caminhoStr)
        elif objeto[i] == "out of network":
            if allStations[i][1] == "sour":  # source doesn't exist
                lines.append(myStations[i][0] + " " + objeto[i])
            else:
                lines.append(myStations[i][1] + " " + objeto[i])
        elif objeto[i] == "do not communicate":
            lines.append(myStations[i][0] + " and " + myStations[i][1] + " " + objeto[i])

    with open(filePath, "w") as fp:
        fp.write("\n".join(lines))

