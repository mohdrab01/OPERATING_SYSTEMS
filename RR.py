##################################################################################################
### ROUND ROBIN (Pre-emptive) SCHEDULING ALGORITHM ###
##################################################################################################

print("##################################################################################################")
print("                                ROUND ROBIN SCHEDULING -- NO ARRIVAL TIMES ")
print("##################################################################################################")

def findWaitingTime(pid, n, bt, wt, qtm):  
    rt = [0] * n 
    for i in range(n):  
        rt[i] = bt[i] 
    t = 0 
    while(1): 
        done = True
        for i in range(n):               
            if (rt[i] > 0) : 
                done = False
                  
                if (rt[i] > qtm) :                   
                    t += qtm  
                    rt[i] -= qtm  
                else: 
                    t = t + rt[i]  
                    wt[i] = t - bt[i]  
                    rt[i] = 0                  
        if (done == True): 
            break
              
def findTurnAroundTime(pid, n, bt, wt, tat): 
    for i in range(n): 
        tat[i] = bt[i] + wt[i]  
  
def RR(pid, n, bt, qtm):  
    wt = [0] * n 
    tat = [0] * n  
    total_wt, total_tat = 0, 0
    findWaitingTime(pid, n, bt, wt, qtm)  
    findTurnAroundTime(pid, n, bt, wt, tat)  
    print( "PID\t\tBT\tWT\tTAT") 
    for i in range(n):       
        total_wt = total_wt + wt[i] 
        total_tat = total_tat + tat[i] 
        print(str(pid[i])+"\t\t" + str(bt[i]) + "\t" + str(wt[i]) + "\t " + str(tat[i]))    
    print( "Average waiting time = "+str(total_wt / n)) 
    print("Average turn around time = "+str(total_tat / n)) 
      
if __name__ =="__main__": 
    pid = [1, 2, 3] 
    n = 3 
    bt = [10, 5, 8]  
    qtm = 2;  
    RR(pid, n, bt, qtm) 
  
