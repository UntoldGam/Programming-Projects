units = {
    "mm": {"mm": 1, "cm": 0.1, "m": 0.001, "km": 0.000001},
    "cm": {"mm": 10, "cm": 1, "m": 0.01, "km": 0.00001},
    "m":  {"mm": 1000, "cm": 100, "m": 1, "km": 0.001},
    "km": {"mm": 100000, "cm": 10000, "m": 1000, "km": 1},
}

while True:

    oldUnit=input(f"What unit would you like to convert from? \nWe support {units.keys()} \nAnswer: ") # original unit of the value
    
    try:
        newUnit=input(f"Which unit would you like to convert to? \nWe support {units[oldUnit].keys()} \nAnswer: ") # new unit of the value
        value=int(input(f"What number do you want to be converted from {newUnit} to {oldUnit}? "))
        if oldUnit in units and newUnit in units: # authentication / validation of the unit type
            new_value = value * units[oldUnit][newUnit]
            if str(new_value).find("e"):
                print(f"{value}{oldUnit} = {'{:.6f}'.format(new_value)}{newUnit}")
            else:
                print(f"{value}{oldUnit} = {new_value}{newUnit}")
            
    
    except KeyError:
        print(f"{oldUnit} is not a valid unit.")
    