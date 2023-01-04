import os
import re

input = 'day2_input.txt'

def extract_data(input_filename):
    rounds = []
    with open(input_filename) as file:
        for line in file:
            round = line.split()
            rounds.append(round)
    return rounds

def calculate_round_score(round):

    """
    elf actions:
    ------------
    a = rock
    b = paper
    c = scissors

    my actions + point values:
    -----------
    x = rock = 1
    y = paper = 2
    z = scissors = 3

    round outcomes:
    ---------------
    win = 6
    draw = 3
    loss = 0
    """

    elf = round[0]
    me = round[1]

    my_round_outcome_value = 0
    my_action_value = 0
    my_round_score = 0

    match elf:
        case "A":
            elf = "rock"
        case "B":
            elf = "paper"
        case "C":
            elf = "scissors"

    match me:
        case "X":
            me = "rock"
            my_action_value = 1
        case "Y":
            me = "paper"
            my_action_value = 2
        case "Z":
            me = "scissors"
            my_action_value = 3

    if elf == me:
        # tie
        my_round_outcome_value = 3
    elif elf == "rock":
        if me == "paper":
            # win
            my_round_outcome_value = 6
    elif elf == "paper":
        if me == "scissors":
            # win
            my_round_outcome_value = 6
    elif elf == "scissors":
        if me == "rock":
            # win
            my_round_outcome_value = 6
    # else loss

    my_round_score = my_action_value + my_round_outcome_value

    return my_round_score

def pick_action(opponent_action, outcome):

    match outcome:
        case "tie":
            return opponent_action
        case "win":
            if opponent_action == "rock":
                return "paper"
            if opponent_action == "paper":
                return "scissors"
            if opponent_action == "scissors":
                return "rock"
        case "lose":
            if opponent_action == "rock":
                return "scissors"
            if opponent_action == "paper":
                return "rock"
            if opponent_action == "scissors":
                return "paper"

def get_action_value(action):
    match action:
        case "rock":
            return 1
        case "paper":
            return 2
        case "scissors":
            return 3


def calculate_round_score_v2(round):

    """
    elf actions:
    ------------
    a = rock
    b = paper
    c = scissors

    my outcomes
    -----------
    x = lose = 0
    y = draw = 3
    z = win = 6

    action values:
    rock = 1
    paper = 2
    scissors = 3
    """

    elf = round[0]
    me = round[1]

    my_round_outcome_value = 0
    my_action_value = 0
    my_round_score = 0

    match elf:
        case "A":
            elf = "rock"
        case "B":
            elf = "paper"
        case "C":
            elf = "scissors"

    # convert outcome to action
    match me:
        case "X":
            #lose
            me = pick_action(elf, "lose")
            my_round_outcome_value = 0
        case "Y":
            #tie
            me = pick_action(elf, "tie")
            my_round_outcome_value = 3
        case "Z":
            #win
            me = pick_action(elf, "win")
            my_round_outcome_value = 6
    
    my_action_value = get_action_value(me)

    my_round_score = my_action_value + my_round_outcome_value

    return my_round_score
    
def calculate_tournament_score(rounds):
    tournament_score = 0
    for round in rounds:
        tournament_score += calculate_round_score(round)
    return tournament_score

def calculate_tournament_score_v2(rounds):
    tournament_score = 0
    for round in rounds:
        tournament_score += calculate_round_score_v2(round)
    return tournament_score


rps_rounds = extract_data('day2_input.txt')
print (calculate_tournament_score(rps_rounds))
print (calculate_tournament_score_v2(rps_rounds))


