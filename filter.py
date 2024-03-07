# filter() = creates a collection of elements from an iterable for wich a function returns true
# sintaxis: filter(function,iterable)

tennisPlayersInfo = [
    ("Sinner", "Italy", 1.90),
    ("Federer", "Sweden", 1.85),
    ("Nadal", "Spain", 1.85),
    ("Alcaraz", "Spain", 1.83),
    ]

veryTall = lambda data: data[2] >= 1.90

veryTallPlayers = list(filter(veryTall,tennisPlayersInfo)) # filter() being used here. the filtered data was assigned to a new list "veryTallPlayers"

for i in veryTallPlayers:
    print(i)