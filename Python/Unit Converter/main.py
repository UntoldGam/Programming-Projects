units = {
    "categories": {
        "length": {
            "mm": {"mm": 1, "cm": 0.1, "m": 0.001, "km": 0.000001},
            "cm": {"mm": 10, "cm": 1, "m": 0.01, "km": 0.00001},
            "m":  {"mm": 1000, "cm": 100, "m": 1, "km": 0.001},
            "km": {"mm": 100000, "cm": 10000, "m": 1000, "km": 1},
        },
        "speed": {
            "m/s": {"km/h": 3.6, "mph": 2.237, "ft/s": 3.281},
            "km/h": {"m/s": 0.2778, "mph": 0.622, "ft/s": 0.912},
            "ft/s": {"m/s": 0.305, "km/h": 1.097, "mph": 0.682}
        }
    }
}

while True:
    category=input(f"What kind of unit would you like to convert? \nWe support {units['categories'].keys()} \nAnswer: ")
    if units["categories"][category]:
        oldUnit=input(f"What unit would you like to convert from? \nWe support {units['categories'][category].keys()} \nAnswer: ") # original unit of the value
        categoryOfUnit=units['categories'][category]
        try:
            newUnit=input(f"Which unit would you like to convert to? \nWe support {categoryOfUnit[oldUnit].keys()} \nAnswer: ") # new unit of the value
            value=int(input(f"What number do you want to be converted from {newUnit} to {oldUnit}? "))
            if oldUnit in categoryOfUnit and newUnit in categoryOfUnit[oldUnit]: # authentication / validation of the unit type
                new_value = value * categoryOfUnit[oldUnit][newUnit]
                if str(new_value).find("e"):
                    print(f"{value}{oldUnit} = {'{:.6f}'.format(new_value)}{newUnit}")
                else:
                    print(f"{value}{oldUnit} = {new_value}{newUnit}")
                
        
        except KeyError:
            print(f"{oldUnit} is not a valid unit.")
    else:
        print("The category you provided does not exist.")