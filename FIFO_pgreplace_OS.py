
##################################################################################################
### FIFO - FIRST IN FIRST OUT - PAGE REPLACEMENT ALGORITHM ###
##################################################################################################

print("##################################################################################################")
print("                                FIFO PAGE REPLACEMENT ALGORITHM ")
print("##################################################################################################")

from queue import Queue  
  
# FIND NO. OF PAGE FAULTS USING QUEUE (FIFO) 
def pageFaultsFIFO(pages, n, frame_size): 
      
    # FOR CURR. PAGES => CHECK IF PAGE IN SET OR NOT
    frame = set()  
  
    # STORE PAGES IN QUEUE
    q = Queue()  
  
    page_faults = 0
    for i in range(n): 
          
        if (len(frame) < frame_size): 
              
            if (pages[i] not in frame): 

                frame.add(pages[i])  
                page_faults += 1
                q.put(pages[i]) 
  
        else: 
              
            if (pages[i] not in frame): 
                  
                val = q.queue[0]  
  
                q.get()  
                frame.remove(val)  
                frame.add(pages[i])  
                q.put(pages[i])  
                page_faults += 1

        # FRAME PER ITERATION        
        # print(pages[i],"-->",frame)
  
    return page_faults 
  
# MAIN CODE
if __name__ == '__main__': 

	# COMPILE TIME INPUT
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0 ,1]  
    n = len(pages)  
    frame_size = 3
    print("PAGES : ",pages)
    print("No. of PAGES: ",n)
    print("FRAME SIZE : ",frame_size)

    # RUN TIME INPUT 
    # print("Enter number of pages: ")
    # n = int(input())
    # print("Enter ",n," PAGES: ")
    # pages = list(map(int,input().split()))
    # print("Enter FRAME SIZE: ")
    # frame_size = int(input())

    page_faults = pageFaultsFIFO(pages, n, frame_size)
    print("NO. OF PAGE FALUTS USING FIFO PAGE REPLACEMENT ALGORITHM = ",page_faults) 
  
