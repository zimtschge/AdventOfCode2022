import os.path

#input_file = os.path.dirname(os.path.realpath(__file__)) + "/ExampleInput.txt"
input_file = os.path.dirname(os.path.realpath(__file__)) + "/MyInput.txt"

def findDuplicateChar(a: str,b : str):
    #Try to find the char of a in b
    for ch in a:
        if -1 != b.find(ch):
            return ch

def getPriority(ch : str):
    if ch.islower():
        priority = 1 + ord(ch) - ord('a')
    else:
        priority = 27 + ord(ch) - ord('A')
    return priority

def findCommonChar(a: str, b: str, c: str):
    for ch in a:
        if -1 != b.find(ch) and -1 != c.find(ch):
            return ch

with open(input_file) as rucksacks:
    throuple = []
    priorities = []
    badge_priorities = []
    for item_list in rucksacks.readlines():
        # Split the compartments
        compartment_size = int((len(item_list) / 2) // 1) # Round down for possible endline char
        compartment1 = item_list[0:compartment_size]
        compartment2 = item_list.replace(compartment1, "")

        # Find the duplicate
        duplicate = findDuplicateChar(compartment1, compartment2)

        # Get the priority
        priorities.append(getPriority(duplicate))

        # PART 2: Search the batch of 3
        throuple.append(item_list)

        if 3 == len(throuple):            
            common_char = findCommonChar(throuple[0], throuple[1], throuple[2])
            badge_priorities.append(getPriority(common_char))

            #Reset throuple for next three
            throuple = []

    print("Solution of Part 1 is: ", sum(priorities))
    print("Solution of Part 2 is: ", sum(badge_priorities))
