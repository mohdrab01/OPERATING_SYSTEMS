##################################################################################################
### DISK SCHEDULING - SSTF ALGORITHM ###
##################################################################################################

print("##################################################################################################")
print("                                DISK SCHEDULING - SSTF ALGORITHM ")
print("##################################################################################################")

def calculateDifference(q, h, d): 
    for i in range(len(d)): 
        d[i][0] = abs(q[i] - h)  

def findMin(d):  
  
    idx = -1
    minn = 999999999
  
    for i in range(len(d)): 
        if (not d[i][1] and 
                minn > d[i][0]): 
            minn = d[i][0] 
            idx = i 
    return idx  
      
def SSTF(req, head): 

        if (len(req) == 0):  
            return
          
        l = len(req)  
        diff = [0] * l 
          
        for i in range(l): 
            diff[i] = [0, 0] 
              
        seek_count = 0
        seek_sequence = [0] * (l + 1)  
          
        for i in range(l):  

            seek_sequence[i] = head  
            calculateDifference(req, head, diff)  
            index = findMin(diff)  
            diff[index][1] = True
            seek_count += diff[index][0]  
            head = req[index]  
      
        seek_sequence[len(seek_sequence) - 1] = head  
          
        print("Total number of seek operations =", seek_count)                                                            
        print("Seek Sequence is")  
          
        for i in range(l + 1): 
            print(seek_sequence[i])  
      
# MAIN code  
if __name__ =="__main__": 
      
    # arr = [176, 79, 34, 60, 92, 11, 41, 114] 
    size = int(input("Enter Size of Request array: "))
    print("Enter the Request Sequence array: ")
    arr = list(map(int,input().split()))
    head = int(input("Enter the initial Head position : "))

    SSTF(arr, head) 