import os.path

#input_file = os.path.dirname(os.path.realpath(__file__)) + "/ExampleInput.txt"
input_file = os.path.dirname(os.path.realpath(__file__)) + "/MyInput.txt"

LOSE = 0
DRAW = 3
WIN = 6

ROCK = 1
PAPER = 2
SCISSORS = 3

look_up_a = { # X = Rock, Y = Paper, Z = Scissors
  "A X": DRAW + ROCK,    
  "A Y": WIN + PAPER,
  "A Z": LOSE + SCISSORS,
  "B X": LOSE + ROCK,
  "B Y": DRAW + PAPER,
  "B Z": WIN + SCISSORS,
  "C X": WIN + ROCK,
  "C Y": LOSE + PAPER,
  "C Z": DRAW + SCISSORS,
}

look_up_b = { # X = Lose, Y = Draw, Z = Lose
  "A X": LOSE + SCISSORS,    
  "A Y": DRAW + ROCK,
  "A Z": WIN + PAPER,
  "B X": LOSE + ROCK,
  "B Y": DRAW + PAPER,
  "B Z": WIN + SCISSORS,
  "C X": LOSE + PAPER,
  "C Y": DRAW + SCISSORS,
  "C Z": WIN + ROCK,
}

with open(input_file) as data_set:
    
    #Iterate over file
    score_a = 0
    score_b = 0

    for move in data_set.readlines():
        # Use the look_up to get the score of this move
        score_a = score_a + look_up_a[move[0:3]] #       

        score_b = score_b + look_up_b[move[0:3]] #   

    # Result of a
    print("a: your score is: ", score_a)

    # Result of b
    print("b: your score is: ", score_b)


