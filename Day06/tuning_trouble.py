import os.path

input_file = os.path.dirname(os.path.realpath(__file__)) + "/ExampleInput.txt"
input_file = os.path.dirname(os.path.realpath(__file__)) + "/MyInput.txt"


def dupcheck(x):
    for elem in x:
        if x.count(elem) > 1:
            return True    
    return False

with open(input_file) as data_set:
    message = data_set.readline()
    print(message)
    
    for i in range(len(message)):
        package = message[i:(i+4)]
        
        if False == dupcheck(package):
            print("Solution of Part 1:", i + 4)
            break

#Part 2
with open(input_file) as data_set:
    message = data_set.readline()
    print(message)
    
    for i in range(len(message)):
        package = message[i:(i+14)]
        
        if False == dupcheck(package):
            print("Solution of Part 1:", i + 14)
            break