cityLandmarks = {
    "Paris": "Eiffel Tower",
    "New York": "Statue of Liberty",
    "Rome": "Colosseum",
    "London": "Big Ben",
    "Beijing": "Great Wall of China",
    "Cairo": "Pyramids of Giza",
    "Sydney": "Sydney Opera House",
    "Rio de Janeiro": "Christ the Redeemer"
}
print()
print("City Landmarks Dictionary:", cityLandmarks)
print()
print("Landmark of Cairo:", cityLandmarks["Cairo"])
print()
cityLandmarks["New York"] = "Empire State Building"
print()
del cityLandmarks["Sydney"]
print()
last_key = list(cityLandmarks.keys())[-1]
print("Last key-value pair:", last_key, ":", cityLandmarks[last_key])
print()