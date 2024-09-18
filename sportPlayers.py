sportsPlayers = {
    'Soccer': 'Lionel Messi',
    'Basketball': 'Michael Jordan',
    'Tennis': 'Roger Federer',
    'Cricket': 'Sachin Tendulkar',
    'Football': 'Tom Brady',
    'Golf': 'Tiger Woods',
    'Baseball': 'Babe Ruth',
    'Swimming': 'Michael Phelps',
    'Boxing': 'Muhammad Ali',
    'Track': 'Usain Bolt'
}
print()
print(sportsPlayers)
print()
print("Player of fourth sport:", sportsPlayers['Cricket'])
print()
sportsPlayers['Golf'] = 'Jack Nicklaus'
print()
del sportsPlayers['Track']
print()
print("Last key-value pair:", list(sportsPlayers.items())[-1])
print()