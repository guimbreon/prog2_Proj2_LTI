import sys
from readLN import *
from findAllStations import *
from writeMS import *
def safelevadas(inputFile1, inputFile2, outputFile):
    """
    Processes a network of levadas (irrigation channels) and pairs of stations, and writes the results to an output file.
    
    Args:
        inputFile1 (str): Path to the input file containing the network of levadas in a specific format.
        inputFile2 (str): Path to the input file containing pairs of station names, one pair per line.
        outputFile (str): Path to the output file where the results will be written.
    """
    #Testing if the filePaths are the correct
    
    dataLN = readLN(filePath2)
    myStations = readMyStations(filePath)
    dig = buildNetwork(dataLN)
    srcDestNodes = findSrcDestNodes(myStations, dig)

    todasOsCaminhos = findAllStations(srcDestNodes, dig)

    writeMS(todasOsCaminhos, myStations, srcDestNodes, outputFile)
    
    

filePath = "l:/Aulas/Ano1/2Sem/ProgII/prog2_Proj2_LTI/test_set/myStations_B.txt"
filePath2 = "l:/Aulas/Ano1/2Sem/ProgII/prog2_Proj2_LTI/test_set/myLevadasNetwork.txt"
filePath3 = "teste.txt"

safelevadas(filePath, filePath2, filePath3)
#safelevadas(sys.argv[1],sys.argv[2],sys.argv[3])