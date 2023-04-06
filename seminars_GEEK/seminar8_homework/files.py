import global_vars

def open_file():
    with open(global_vars.path, 'r', encoding='UTF-8') as file:
        global_vars.data = file.readlines()
        
        for line in global_vars.data:
            line = line.rstrip()
            line = line.split(';')
            #print("line = ", line)
            global_vars.base[line[0]] = line[1],line[2],line[3]
        #print(global_vars.base)
        #print("test: ", global_vars.base['1'][1])

def save_file():
    with open(global_vars.path, 'w', encoding='UTF-8') as file:
        print()
        for index , value in enumerate(global_vars.base.values()):
            #print(str(index) + ';' + '; '.join(value) + '\n')   #values to write in file
            file.write((str(index) + ';' + '; '.join(value) + '\n'))
        global_vars.base.clear()
    

    
        
