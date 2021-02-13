##################################################################################################
### FCFS - FIRST COME FIRST SERVE - (Non Pre-emptive) SCHEDULING ALGORITHM ###
##################################################################################################

print("##################################################################################################")
print("                                FCFS SCHEDULING -- NO ARRIVAL TIMES ")
print("##################################################################################################")

def findWaitingTime(n, bt, wt): 
    wt[0] = 0
    for i in range(1, n ): 
        wt[i] = bt[i - 1] + wt[i - 1]  

def findTurnAroundTime(n, bt, wt, tat): 
    for i in range(n): 
        tat[i] = bt[i] + wt[i] 

def FCFS( pid, n, bt):   
    wt = [0] * n 
    tat = [0] * n  
    total_wt = 0
    total_tat = 0
    findWaitingTime(n, bt, wt) 
    findTurnAroundTime(n,  bt, wt, tat) 
    print( "PID\t\tBT\tWT\tTAT") 
    for i in range(n):       
        total_wt = total_wt + wt[i] 
        total_tat = total_tat + tat[i] 
        print(str(pid[i])+"\t\t" + str(bt[i]) + "\t" + str(wt[i]) + "\t " + str(tat[i]))    
    print( "Average waiting time = "+str(total_wt / n)) 
    print("Average turn around time = "+str(total_tat / n)) 

if __name__ =="__main__": 
    pid = [ 1, 2, 3] 
    n = len(pid) 
    bt = [10, 5, 8]   
    FCFS(pid, n, bt) 
