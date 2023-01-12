from functools import cmp_to_key

"""Using the functools.cmp_to_key() function to sort a list of Pokemon by their length of their names:"""


pokemon = ["Pikachu", "Charmander", "Squirtle", "Bulbasaur"]

# Sort the list of Pokemon by the length of their names
sorted_pokemon = sorted(pokemon, key=cmp_to_key(lambda a, b: len(a) - len(b)))
print(sorted_pokemon)
