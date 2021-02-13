##################################################################################################
### DISK SCHEDULING - C SCAN ALGORITHM ###
##################################################################################################

print("##################################################################################################")
print("                                DISK SCHEDULING - C SCAN ALGORITHM ")
print("##################################################################################################")

def CSCAN(arr, disk_size, size, head):
     
    seekCnt = 0
    distance = 0
    curr = 0
    left = []
    right = []
    seekSeq = []

    left.append(0)
    right.append(disk_size - 1)
 
    for i in range(size):
        if (arr[i] < head):
            left.append(arr[i])
        if (arr[i] > head):
            right.append(arr[i])
 
    left.sort()
    right.sort()
 
    for i in range(len(right)):

        curr = right[i]
        seekSeq.append(curr)
        distance = abs(curr - head)  
        seekCnt += distance
        head = curr
 
    head = 0
 
    for i in range(len(left)):

        curr = left[i]
        seekSeq.append(curr)
        distance = abs(curr - head)
        seekCnt += distance
        head = curr
 
    print("Total number of seek operations =", seekCnt)
    print("Seek Sequence is")
    print(*seekSeq, sep = "\n")
 


# MAIN code  
if __name__ =="__main__": 
      
    # arr = [176, 79, 34, 60, 92, 11, 41, 114] 
    disk_size = int(input("Enter Size of Disk: "))
    size = int(input("Enter Size of Request array: "))
    print("Enter the Request Sequence array: ")
    arr = list(map(int,input().split()))
    head = int(input("Enter the initial Head position : "))

    CSCAN(arr, disk_size, size, head) 
