##################################################################################################
### DISK SCHEDULING - FCFS ALGORITHM ###
##################################################################################################

print("##################################################################################################")
print("                                DISK SCHEDULING - FCFS ALGORITHM ")
print("##################################################################################################")

def FCFS(arr, size, head): 
  
    seekCnt = 0; 
    distance, curr = 0, 0; 
  
    for i in range(size): 
        curr = arr[i]; 
        distance = abs(curr - head); 
        seekCnt += distance; 
        head = curr; 

    print("Total number of seek operations = ", seekCnt); 
    print("Seek Sequence is"); 

    for i in range(size): 
        print(arr[i]); 
      
# MAIN code 
if __name__ == '__main__': 

    # arr = [ 176, 79, 34, 60, 92, 11, 41, 114 ]; 
    # head = 50; 

    size = int(input("Enter Size of Request array: "))
    print("Enter the Request Sequence array: ")
    arr = list(map(int,input().split()))
    head = int(input("Enter the initial Head position : "))
  
    FCFS(arr, size, head); 