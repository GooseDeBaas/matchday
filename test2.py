import random

# Declaring variables
teams = ["Anderlecht", "AA Gent", "Union SG", "Genk", "Antwerp", "Club Brugge", ]
aantal_speeldagen = int((len(teams)-1)*2)
aantal_teams = len(teams)
matchdays = []

# Creating starting set-up circle

array1 = teams[:int(len(teams)/2)]
array2 = teams[int((len(teams)/2)):int(len(teams))]
reversed_array2 = array2[::-1]
array2 = reversed_array2

# Rotating function
def rotate(array1, array2):
    team_to_first = array2.pop(0)
    array1.insert(1, team_to_first)
    team_to_last = array1.pop(len(array1)-1)
    array2.append(team_to_last)

heenronde = None

# Create first leg games and rotate

for i in range(int((aantal_speeldagen)/2)):
    speeldag = []
    for j in range(int(aantal_teams/2)):
        heenronde = [array1[j], array2[j]]
        terugronde = [array2[j], array1[j]]
        speeldag.append(heenronde)
    matchdays.append(speeldag)
        

    rotate(array1, array2)

# Create second leg games and rotate

for i in range(int((aantal_speeldagen)/2)):
    speeldag = []
    for j in range(int(aantal_teams/2)):
        terugronde = [array2[j], array1[j]]
        speeldag.append(terugronde)
    matchdays.append(speeldag)
        

    rotate(array1, array2)


# random.shuffle(matchdays)

print(matchdays)

# Print out random matchdays

for i in range(int(aantal_speeldagen)):
    print(f'Speeldag {i+1}: ')
    for j in range(int(aantal_teams/2)):
        print(f'{matchdays[i][j][0]} vs {matchdays[i][j][1]}')
    print("")
