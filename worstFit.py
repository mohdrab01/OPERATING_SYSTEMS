##################################################################################################
### MEMORY MANAGEMENT - WORST FIT ALGORITHM ###
##################################################################################################

print("##################################################################################################")
print("                                MEMORY MANAGEMENT - WORST FIT ALGORITHM ")
print("##################################################################################################")

def worstFit(partitions, m, processSize, n): 

    allocation = [-1] * n 

    for i in range(n): 
        worst = -1
        for j in range(m): 
            if partitions[j] >= processSize[i]: 
                if worst == -1:  
                    worst = j  
                elif partitions[worst] < partitions[j]:  
                    worst = j 
 
        if worst != -1: 
            allocation[i] = worst  
            partitions[worst] -= processSize[i] 
  
    print("Process No. Process Size  Partition no.") 
    for i in range(n): 
        print( i + 1, "         ", processSize[i],"         ", end = " ")  
        if allocation[i] != -1:  
            print(allocation[i] + 1)  
        else: 
            print("Not Allocated") 
  

if __name__ == '__main__': 
    partitions = [100, 500, 200, 300, 600]  
    processSize = [212, 417, 112, 426]  
    m = len(partitions)  
    n = len(processSize)  

    print("No. of Memory Partitions, m = ",m)
    print("Memory Partitions: ", partitions)
    print("No. of Processes, n = ",n)
    print("Processes Sizes: ",processSize)
    print("#######################################  WORST - FIT  #########################################")
  
    worstFit(partitions, m, processSize, n)
