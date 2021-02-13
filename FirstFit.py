##################################################################################################
### MEMORY MANAGEMENT - FIRST FIT ALGORITHM ###
##################################################################################################

print("##################################################################################################")
print("                                MEMORY MANAGEMENT - FIRST FIT ALGORITHM ")
print("##################################################################################################")

def firstFit(partitions, m, processSize, n): 
      
    allocation = [-1] * n  
  
    for i in range(n): 
        for j in range(m): 
            if partitions[j] >= processSize[i]: 
                allocation[i] = j  
                partitions[j] -= processSize[i]   
                break
  
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
    print("#######################################  FIRST - FIT  #########################################")
    firstFit(partitions, m, processSize, n) 
