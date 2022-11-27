while True:
    debug=False # quicker testing of the multiple years choice during quickfire testing of the system
    if debug == True:
        choice="m"
    else:
        choice = input("Would you like to add together multiple years or just one year? (m for multiple, o for one) ")

    if choice.lower() == 'o':
        year_input = input("What year would you like to add together? (sum of each individual number) ")
        split = ([int(single) for single in str(year_input)]) # shorthand splitting of the year as it's only one year, rather than multiple

        total = 0
        iteration = 0

        while iteration < len(split):
            total = total + split[iteration]
            iteration += 1 # goes to the next number in the split year
        print(f"Each number in the year given sums to {total}")
    elif choice.lower() == 'm':
        
        if debug == True:
            year_input = "2019,2020,2021"
        else:
            year_input = input("What years would you like to add together? (separate using commas with no spaces: 2019,2020,2021) ") # looks like this: "2019,2020,2021"
        years = year_input.split(",") # looks like this: ["2019","2020","2021"]
        #print(years)
        total = 0
        
        for year in years: # each year within the list of years  e.g. [2020,2021,2022]
            #print(year)
            index = 0 # reset after each year is broken down into individual numbers
            for number in year: # individual number within the year
                index = index + 1
                total = total + int(number) # "2" in 2020 turned tp 2 and added to the total
        print(f"Each number in the years given sums to {total}")
    else:
        print("Invalid input, please try again")
        continue
