technologyInnovators = {
    "Internet": "Vint Cerf",
    "Telephone": "Alexander Graham Bell",
    "Electric Lightbulb": "Thomas Edison",
    "Airplane": "Wright Brothers",
    "Personal Computer": "Steve Jobs & Bill Gates",
    "World Wide Web": "Tim Berners-Lee",
    "Nuclear Reactor": "Enrico Fermi",
    "Bluetooth": "Jaap Haartsen"
}
print()
print(technologyInnovators)
print()
print("Innovator of Airplane:", technologyInnovators["Airplane"])
print()
technologyInnovators["Telephone"] = "Elisha Gray"
print()
del technologyInnovators["World Wide Web"]
print()
last_key = list(technologyInnovators.keys())[-1]
print("Last key-value pair:", last_key, ":", technologyInnovators[last_key])
print()
print()