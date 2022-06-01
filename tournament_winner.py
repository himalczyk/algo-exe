
# competitions[i]
# results[i] - this specifies the winner
# 1 in results means that the home team won
# 0 means that the away team won

competitions = [
    ['HTML', "C#"],
    ['C#', "Python"],
    ['Python', 'HTML']
]
results = [0, 0, 1]

def tournamentWinner(competitions, results):
    # create hashmap to store teams
    teams = {}
    # loop over each matchup in competitions which is a nested linked array of arrays
    for match in competitions:
        for team in match:
            if team not in teams:
                teams[team] = 0

    # results len equals competitions number as there is always a match and a score
    while len(results) > 0:
        # get current competition
        current_match = competitions[0]
        # get current not winner, since they are with swapped places
        current_not_winner = results[0]
        # delete the not winning one
        current_match.pop(current_not_winner)
        # add points to the left team which is the winner
        teams[current_match[0]] += 3
        # delete elements from the main list to get the next winners
        competitions.pop(0)
        results.pop(0)
    # use max method to get the teams with the max value from the dict
    max_points = max(teams, key=teams.get)
    return max_points

print(tournamentWinner(competitions, results))