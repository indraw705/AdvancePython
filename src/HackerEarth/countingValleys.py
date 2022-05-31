steps = "UDDDUDUU"
sea_level = 100
vally = 0
for element in range(0, len(steps)):
    if steps[element] == "U":
        sea_level += 1
        print(sea_level)
        if sea_level == 100 and steps[element] == "U":
            vally += 1
    else:
        sea_level -= 1
        print(sea_level)

print(vally)


