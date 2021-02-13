##################################################################################################
### DEADLOCK AVOIDANCE - BANKERS ALGORITHM ###
##################################################################################################

print("##################################################################################################")
print("                                DEADLOCK AVOIDANCE - BANKERS ALGORITHM ")
print("##################################################################################################")

def printMatrix(m):
    print("\tR1\tR2\tR3")
    i=1
    for lists in m:
        print("P"+str(i), end = "\t")
        for li in lists:
            print(li,end = "\t")
        i+=1
        print()

def calculateNeed(n,m,alloc,max,avail):     
    need = [[ 0 for i in range(m)]for i in range(n)] 
    for i in range(n): 
        for j in range(m): 
            need[i][j] = max[i][j] - alloc[i][j] 

    print("Need Matrix: ")
    print("##################################################################################################")
    printMatrix(need)
    return need

def isSafe(n, m, processes, alloc, max, avail): 
    
    need = calculateNeed(n, m, alloc, max, avail)
    finish = [0] * n
    safeSeq = [0] * n
    work = [0] * m

    for i in range(m): 
        work[i] = avail[i]  

    count = 0

    while (count < n):  

        found = False

        for p in range(n):   

            if (finish[p] == 0): 

                for j in range(m): 
                    if (need[p][j] > work[j]): 
                        break

                if (j == m - 1):  
                    for k in range(m):  
                        work[k] += alloc[p][k]  

                    safeSeq[count] = p 
                    count += 1
                    finish[p] = 1  
                    found = True

        if (found == False): 
            print("System is not in safe state") 
            return False

    print("\nSystem is in safe state.","\nSafe sequence is: ", end = " ") 
    print(*safeSeq)  
  
    return True
 

if __name__=="__main__": 
      
    n = 5 # Number of processes 
    m = 3 # Number of resources 

    # Processes
    processes = [i for i in range(n)]
      
    # Allocation Matrix 
    alloc = [[0, 1, 0 ],[ 2, 0, 0 ],[3, 0, 2 ],[2, 1, 1] ,[ 0, 0, 2]] 
      
    # MAX Matrix  
    max = [[7, 5, 3 ],[3, 2, 2 ],[ 9, 0, 2 ],[2, 2, 2],[4, 3, 3]] 
    
    # Available Resources  
    avail = [3, 3, 2]  

    print("No. of processes, n = ",n)
    print("No. of resources, m = ",m)
    print("Allocation Matrix: ")
    print("##################################################################################################")
    printMatrix(alloc)
    print("Max Matrix: ")
    print("##################################################################################################")
    printMatrix(max)
    print("Available Resources: ",avail)

    isSafe(n, m, processes, alloc, max, avail)
      


      
