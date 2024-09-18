beachesCountriesDict = {
    "Bondi Beach": "Australia",
    "Copacabana": "Brazil",
    "Waikiki Beach": "USA",
    "Whitehaven Beach": "Australia",
    "Anse Source d'Argent": "Seychelles",
    "Navagio Beach": "Greece",
    "Tulum Beach": "Mexico",
    "Bora Bora Beach": "French Polynesia"
}
print()
print(beachesCountriesDict)
print()
print("Country of Waikiki Beach:", beachesCountriesDict["Waikiki Beach"])
print()
beachesCountriesDict["Navagio Beach"] = "Zakynthos, Greece"
print()
del beachesCountriesDict["Anse Source d'Argent"]
print()
last_key = list(beachesCountriesDict.keys())[-1]
print("Last key-value pair:", last_key, ":", beachesCountriesDict[last_key])
print()
print()