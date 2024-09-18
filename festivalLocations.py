festivalLocationsDict = {
    "Diwali": "India",
    "Carnival": "Brazil",
    "Oktoberfest": "Germany",
    "Mardi Gras": "USA",
    "Chinese New Year": "China",
    "La Tomatina": "Spain",
    "Holi": "India",
    "St. Patrick's Day": "Ireland"
}
print()
print(festivalLocationsDict)
print()
print("Location of Mardi Gras:", festivalLocationsDict["Mardi Gras"])
print()
festivalLocationsDict["La Tomatina"] = "Valencia, Spain"
print()
del festivalLocationsDict["Carnival"]
print()
last_key = list(festivalLocationsDict.keys())[-1]
print("Last key-value pair:", last_key, ":", festivalLocationsDict[last_key])
print()