#input_file = "ExampleData.txt"
input_file = "MyDataSet.txt"

with open(input_file) as data_set:
    elf_no = 0
    calories = [0]

    # Iterate over files
    for line in data_set:
        if line != "\n":
            calories[elf_no] = calories[elf_no] + int(line)
        else:
            # \n means next elf
            calories.append(0)
            elf_no = elf_no + 1

    print("Max calories (Answer of Part 1): ", max(calories))

    # Answer of part 2
    calories.sort(reverse=True)
    print("Max 3 calories: ", calories[0], calories[1], calories[2])
    print("And the sum is: ", sum(calories[0:3]))


