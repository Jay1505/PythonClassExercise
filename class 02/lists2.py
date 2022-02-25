games = ["Gloomhaven", "Rafdlands", "Res Archana","Shobu", "That time you killed me"]
print(games)
print(games[1])
print(games[1:])
print(games[:2])
print(games[3:7])
print(games[0:3])
print(games[0:3:2])
print(games[0:3:-2])
print(games[3:0:-2])
print(games[::-1])

#in python you can do the same things to strings as well!!
best="Res Archana"
print(best[::-1])

#accessing to a string is possible but writing/editing is not possible unlike lists. You can read and write in lists but not in strings.
games[2]="Island"
print(games)
#this is not possible for string
best[2]='a'
print(best)

