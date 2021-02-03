
##################################################################################################
### OPTIMAL PAGE REPLACEMENT ALGORITHM ###
##################################################################################################

print("##################################################################################################")
print("                                OPTIMAL PAGE REPLACEMENT ALGORITHM ")
print("##################################################################################################")

def predict(pages, frame, n, idx):
	
	res = -1
	far = idx

	for i in range(len(frame)):

		j = idx

		while j < n:

			if frame[i] == pages[j]:
				if j > far:
					far = j
					res = i 
				break 

			j += 1

		if j == n:
			return i 

	return 0 if (res == -1) else res


# FIND NO. OF PAGE FAULTS USING OPTIMAL 
def pageFaultsOPTIMAL(pages, n, frame_size):

	# STORE CURR. PAGES IN LIST
	frame = []  
	  
	no_page_faults = 0

	for i in range(n):
		
		if pages[i] in frame:
			no_page_faults += 1

			# FRAME IN THIS ITERATION	
			# print(pages[i],"-->",frame)

			continue 

		if len(frame) < frame_size:			
			frame.append(pages[i])

		else:
			p = predict(pages, frame, n, i+1)
			frame[p] = pages[i]

		# FRAME PER ITERATION	
		# print(pages[i],"-->",frame)

	return n - no_page_faults




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

    page_faults = pageFaultsOPTIMAL(pages, n, frame_size)
    print("NO. OF PAGE FALUTS USING OPTIMAL PAGE REPLACEMENT ALGORITHM = ",page_faults) 
  