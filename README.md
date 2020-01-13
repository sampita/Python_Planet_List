# Python_Planet_List

# Setup

`mkdir -p ~/workspace/python/lists && cd $_`
`echo 'planet_list = ["Mercury", "Mars"]' >> planets.py`

# Instructions
Use append() to add Jupiter and Saturn at the end of the list.
Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
Use insert() to add Earth, and Venus in the correct order.
Use append() again to add Pluto to the end of the list.
Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.

# Challenge: Iterating over planets
Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on.

# Example spacecraft list
```spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
]```

Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which satellites have visited it.
