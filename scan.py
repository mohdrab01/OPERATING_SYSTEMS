##################################################################################################
### DISK SCHEDULING - SCAN ALGORITHM ###
##################################################################################################

print("##################################################################################################")
print("                                DISK SCHEDULING - SCAN ALGORITHM ")
print("##################################################################################################")

def SCAN(arr, disk_size, size, head, direction):
 
    seekCnt = 0
    distance, curr = 0, 0
    left = []
    right = []
    seekSeq = []
 
    if (direction == "left"):
        left.append(0)
    elif (direction == "right"):
        right.append(disk_size - 1)
 
    for i in range(size):
        if (arr[i] < head):
            left.append(arr[i])
        if (arr[i] > head):
            right.append(arr[i])
 
    left.sort()
    right.sort()
    run = 2

    while (run != 0):

        if (direction == "left"):

            for i in range(len(left) - 1, -1, -1):

                curr = left[i]
                seekSeq.append(curr)
                distance = abs(curr - head)
                seekCnt += distance
                head = curr
             
            direction = "right"
     
        elif (direction == "right"):

            for i in range(len(right)):

                curr = right[i]
                seekSeq.append(curr)
                distance = abs(curr - head)
                seekCnt += distance
                head = curr
             
            direction = "left"
         
        run -= 1
 
    print("Total number of seek operations =", seekCnt) 
    print("Seek Sequence is")
 
    for i in range(len(seekSeq)):
        print(seekSeq[i])
 
# MAIN code  
if __name__ =="__main__": 
      
    # arr = [176, 79, 34, 60, 92, 11, 41, 114] 
    disk_size = int(input("Enter Size of Disk: "))
    size = int(input("Enter Size of Request array: "))
    print("Enter the Request Sequence array: ")
    arr = list(map(int,input().split()))
    head = int(input("Enter the initial Head position : "))
    direction = input("Enter direction of scan (left/right): ")

    SCAN(arr, disk_size, size, head, direction) 
