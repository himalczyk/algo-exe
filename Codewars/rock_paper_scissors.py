"""Let's play! You have to return which player won! In case of a draw return Draw!.

Examples:

rps('scissors','paper') // Player 1 won!
rps('scissors','rock') // Player 2 won!
rps('paper','paper') // Draw!"""


"""Simple rules:
    Scissors beats paper
    Paper beats rock
    Rock beats scissors

"""

def rps(p1, p2):
    score = "Draw!"
    winner = ''
    hashmap = {
        # winner : loser
        'scissors' : ['paper', 'scissors'],
        'paper' : ['rock', 'paper'],
        'rock' : ['scissors', 'rock']
    }
    if not p1 == p2:
        for key, value in hashmap.items():
            if p1 in value and p2 in value:
                winner = key
        if winner == p1:
            score = 'Player 1 won!'
        elif winner == p2:
            score = 'Player 2 won!'
    return score

rps('scissors','paper')
rps('scissors','rock')
rps('paper','paper')
    