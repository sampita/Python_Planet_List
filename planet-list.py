planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

#add Uranus and Neptune to the list
planet_list.extend(["Uranus", "Neptune"])

#add Pluto to the list
planet_list.append("Pluto")



# slice the list into a new list called rocky_planets
rocky_planets = planet_list[0:6]

#remove the last thing on the list, Pluto.
del planet_list[-1]

print(planet_list)