import sys

if __name__ == "__main__": 
    groupby = list()
    lines = list()
    with open(sys.argv[1]) as input_tracker: 
            lines = input_tracker.read().strip().split("\n")
	#move, time			
    groupby.append([0, lines[0].split()[1]])
    step = [int(lines[0].split()[1]), int(lines[0].split()[1]) + 10000]

    for index in range(1,len(lines)): 
        test = False
        
        while not test:  
            if (int(lines[index].split()[1]) > step[0] and int(lines[index].split()[1]) < step[1]): 
                groupby[-1][0]+=1
                test = True
                
            else: 
                temptime = lines[index].split()[1] 
                step = [step[1],  step[1]+10000]  #update step
                groupby[-1][1] = step[0]            #update previous row
                groupby.append([0, step[1]])
    
    name = 'group' + sys.argv[1].split(".")[0] + '.csv'
    newfile = open(name, 'w')
    
    
    for line in groupby: 
        newfile.write("{0};{1}\n".format(line[0], line[1]))
    newfile.close()
    
    print(len(groupby))
    print(sum([ x[0] for x in groupby]))
