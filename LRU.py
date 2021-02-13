
##################################################################################################
### LRU - LEAST RECENTLY USED - PAGE REPLACEMENT ALGORITHM ###
##################################################################################################

print("##################################################################################################")
print("                                LRU PAGE REPLACEMENT ALGORITHM ")
print("##################################################################################################")


# FIND NO. OF PAGE FAULTS USING LRU 
def pageFaultsLRU(pages, n, frame_size):

	# STORE CURR. PAGES IN LIST
	frame = []  
	  
	page_faults = 0
	  
	for i in pages: 
	  
	    if i not in frame: 
	  
	        if(len(frame) == frame_size): 
	            frame.remove(frame[0]) 
	            frame.append(i) 
	  
	        else: 
	            frame.append(i) 
	  
	        page_faults +=1
	  
	    else: 
	          
	        frame.remove(i) 
	        frame.append(i)

	    # FRAME PER ITERATION
	    # print(i,"-->",frame)

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

    page_faults = pageFaultsLRU(pages, n, frame_size)
    print("NO. OF PAGE FALUTS USING LRU PAGE REPLACEMENT ALGORITHM = ",page_faults) 
  
