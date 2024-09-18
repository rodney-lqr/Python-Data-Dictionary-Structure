athleteAchievements = {
    'Michael Jordan': '6 NBA Championships',
    'Usain Bolt': '8 Olympic Gold Medals',
    'Serena Williams': '23 Grand Slam Titles',
    'Tom Brady': '7 Super Bowl Wins',
    'Lionel Messi': '7 Ballon d\'Or Awards',
    'Cristiano Ronaldo': '5 Ballon d\'Or Awards',
    'Tiger Woods': '15 Major Golf Championships',
    'Roger Federer': '20 Grand Slam Titles'
}
print()
print(athleteAchievements)
print()
print("Achievement of fifth athlete:", athleteAchievements['Lionel Messi'])
print()
athleteAchievements['Serena Williams'] = '24 Grand Slam Titles'
print()
del athleteAchievements['Tiger Woods']
print()
print("Last key-value pair:", list(athleteAchievements.items())[-1])
print()
print()