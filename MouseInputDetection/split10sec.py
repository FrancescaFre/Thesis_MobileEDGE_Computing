if __name__ == "__main__": 
	
	groupby = list()
	tempCurrent = 0
	tempPrev = 0
	
	with open(file_name) as input_tracker: 
            lines = input_tracker.read().split("\n")


	#move, time			
	groupby.append([0, lines[0].split()[1]])
	step = [lines[0].split()[1], lines[0].split()[1] + 10000]
	
    for index in range(1,len(lines)): 
        test = false
        
        while !test:  
            if (lines[index].split()[1] > step[0] and lines[index].split()[1] < step[1]): 
                groupby[-1][0]+=1
                test = true
                
            else: 
                temptime = lines[index].split()[1] /
                step = [step[1],  step[1]+10000]  #update step
                groupby[-1][1] = step[0]            #update previous row
                gourpby.append([0, step[1]])
    
    for group in groupby: 
        print(group[0]+ "    "+group[1])
                
            
            
            