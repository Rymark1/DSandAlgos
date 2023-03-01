nbrOfTemps = int(input("How many day's temperature?"))

temps = []
for x in range(nbrOfTemps):
    temp = int(input(f"Enter day {x+1} temperature: "))
    temps.append(int(temp))

avgTemp = sum(temps)/len(temps)
print(f"The average temperature for the day is {avgTemp}")

days_above = []
for idx, temp in enumerate(temps):
    if temp > avgTemp:
        days_above.append([idx, temp])

print(f"The number of days above the average temperature were {len(days_above)} and are listed below:")
for day in days_above:
    print(f"Day {day[0]+1} was {day[1]} degrees")



numDays = input