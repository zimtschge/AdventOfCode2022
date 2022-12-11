import os.path

input_file = os.path.dirname(os.path.realpath(__file__)) + "/ExampleInput.txt"
input_file = os.path.dirname(os.path.realpath(__file__)) + "/MyInput.txt"

class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

    def getName(self):
        return self.name
    
    def getSize(self):
        return self.size

class Directory:
    def __init__(self, dir_name : str, parent_dir) -> None:
        self.dir_name = dir_name
        self.parent_dir = parent_dir
        self.files = []
        self.subdirectories = []

    def addSubdirectory(self, sub_dir_name : str):
        """ Adds a new subdirectory to the current directory objects"""
        new_dir = Directory(sub_dir_name, self)
        self.subdirectories.append(new_dir)
        return new_dir
    
    def addFile(self, name, size):
        new_file = File(name, size)
        self.files.append(new_file)

    def getSubDirectories(self):
        return self.subdirectories

    def getSubDirectory(self, name):
        for dir in self.subdirectories:
            if dir.getName() == name:
                return dir
        return None

    def getParentDirectory(self):
        return self.parent_dir

    def getName(self):
        return self.dir_name

    def getFiles(self):
        return self.files

    def getSize(self):
        size = 0
        for file in self.files:
            size = size + file.getSize()
        for dir in self.subdirectories:
            size = size + dir.getSize()
        return size


with open(input_file) as data_set:

    #Parse the command log to a directory tree
    main_directory = Directory("/", None)
    current_directory = main_directory

    for line in data_set:
        line = line.replace('\n', '')
        command = line.split(' ')
    
        # Is this a command?
        if command[0] == '$':
            if command[1] == "cd":
                if command[2] == '/':
                    # This is the main dir
                    current_directory = main_directory
                elif command[2] == "..":
                    current_directory = current_directory.getParentDirectory()
                else:
                    current_directory = current_directory.getSubDirectory(command[2])
            
            # ls can be ignored for parsing

        elif command[0] == "dir":
            # This says there is a new directory
            current_directory.addSubdirectory(command[1])
        else:
            # This is a file description
            current_directory.addFile(command[1], int(command[0]))

    # Now get all directories with at most 100000
    def searchForSmallDir(dir: Directory):
        global size
        if dir.getSize() < 100_000:
            size = size + dir.getSize()

        #Iterate over subdirectories
        for subdir in dir.getSubDirectories():
            searchForSmallDir(subdir)

    size = 0
    searchForSmallDir(main_directory)
    print("Solution of Part 1:", size)


    #Part 2
    # First get all directories which would be possible to delete
    possibleDeletes = []
    def getPossibleDeletes(dir: Directory):
        global possibleDeletes
        if (main_directory.getSize() - dir.getSize()) < 40_000_000:
            possibleDeletes.append(dir)

        #Iterate over subdirectories
        for subdir in dir.getSubDirectories():
            getPossibleDeletes(subdir)

    getPossibleDeletes(main_directory)

    # Now get the minimum of the possible deletes
    min_delete_size = 40_000_000
    for dir in possibleDeletes:
        if dir.getSize() < min_delete_size:
            min_delete_size = dir.getSize()

    print("Solution of Part 2:", min_delete_size)

