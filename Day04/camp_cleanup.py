import os.path

input_file = os.path.dirname(os.path.realpath(__file__)) + "/ExampleInput.txt"
input_file = os.path.dirname(os.path.realpath(__file__)) + "/MyInput.txt"

with open(input_file) as data_set:

    subsets = 0
    overlaps = 0
    for section_assignment_pairs in data_set:

        elf_sections = section_assignment_pairs.split(",")
        elf1 = elf_sections[0].split("-")
        elf2 = elf_sections[1].split("-")

        # Convert list to int completely
        elf1 = [int(x) for x in elf1]
        elf2 = [int(x) for x in elf2]

        range1 = range(elf1[0], elf1[1]+1) 
        range2 = range(elf2[0], elf2[1]+1)

        isSubSet = False
        if elf1[0] in range2 and elf1[-1] in range2:
            isSubSet = True
        if elf2[0] in range1 and elf2[-1] in range1:
            isSubSet = True
    
        if isSubSet:
            subsets = subsets + 1

        isOverlapping = False
        if elf1[0] in range2 or elf1[-1] in range2:
            isOverlapping = True
        if elf2[0] in range1 or elf2[-1] in range1:
            isOverlapping = True
        
        if isOverlapping:
            overlaps = overlaps + 1
    print("Solution of part 1: ", subsets)
    print("Solution of part 2: ", overlaps)
