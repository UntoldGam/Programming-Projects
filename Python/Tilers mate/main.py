# User enters width and length of the floor + width and length of a tile + the cost of a tile
# Program then calculates the total cost to cover the floor plan using the cost entered by the user

floor_W_L = input("Please enter the width and length of the floor separated by commas (width,length): ")
tile_W_L = input("Please enter the width and length of the tile separated by commas (width,length): ")
tile_cost = float(input("What is the cost of a tile? "))

floor_W, floor_L = floor_W_L.split(",")
tile_W, tile_L = tile_W_L.split(",")

floor_W = float(floor_W)
floor_L = float(floor_L)
tile_W = float(tile_W)
tile_L = float(tile_L)

if tile_W <= 0 or tile_L <= 0 or floor_W <= 0 or floor_L <= 0 or tile_cost <= 0:
    print("The values inputted cannot be less than or equal to zero.")
else:
    floorArea = floor_W * floor_L # width times length = area
    tileArea = tile_W * tile_L # width times length = area

    costOfTiling = floorArea / tileArea * tile_cost # number of tiles that can fit in the area multiplied by the cost
    costOfTiling = float(costOfTiling)
    print(f"Your total cost of tiling: £{round(costOfTiling, 2)}") # puts it to 2 decimal places and outputs the cost in pounds