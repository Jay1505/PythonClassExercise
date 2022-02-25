# while True:
#     option = input("Do you want to quit? ")
#     if 'y' in option.lower():
#         exit()
x = 0
while x<5:
    print('hello')
    x += 1

for x in range(5):
    print(x)

games = ["Gloomhaven", "Rafdlands", "Res Archana","Shobu", "That time you killed me"]
for game in games:
    game += " sucks!"
    print(game)
print(games)

#In class exercise
#Q.1 Write a for loop that prints out from 1 to 10(including 0, excluding 10)
for num in range(10):
    print(num)

#Q.2 Write a for loop that prints out the numbers 10 to 0(including 10, excluding 0)
for num1 in range(10,0,-1):
    print(num1)

#Q.3 Write a while loop that will run forever
x=5
while x==5:
    print('hello')
#alternate soln
while True:
    print('you will always see me')

#Q.4 Write a while loop that will never run
y=2
while y==5:
    print('hello')
#alternate soln
while False:
    print('you will never see me')