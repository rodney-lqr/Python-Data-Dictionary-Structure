sportsEventsDict = {
    "Olympics": 2021,
    "FIFA World Cup": 2022,
    "Super Bowl": 2023,
    "Wimbledon": 2023,
    "Tour de France": 2023,
    "Cricket World Cup": 2023,
    "Ryder Cup": 2023
}
print()
print(sportsEventsDict)
print()
print("Year of Super Bowl:", sportsEventsDict["Super Bowl"])
print()
sportsEventsDict["Cricket World Cup"] = 2024
print()
del sportsEventsDict["Tour de France"]
print()
last_key = list(sportsEventsDict.keys())[-1]
print("Last key-value pair:", last_key, ":", sportsEventsDict[last_key])
print()