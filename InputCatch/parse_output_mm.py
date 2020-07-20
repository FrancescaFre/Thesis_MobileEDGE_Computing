import sys

if __name__ == "__main__":
    list_input = list()
    ms_passed = 0
    n_input=0

    file_name = sys.argv[1]
    with open(file_name) as input_tracker: 
            lines = input_tracker.read().split("\n")

    for line in lines: 
        ms_passed += int(line.split("|")[3])
        n_input +=1
        list_input.append([n_input, ms_passed, line.split("|")[4]])

    name = 'parsed' + file_name.split(".")[0] + '.csv'
    newfile = open(name, 'w')
    for line in list_input:
        newfile.write("{0};{1};{2}\n".format(line[0], line[1], line[2]))
    newfile.close()    
