from functools import partial


def search_pokedex(name, pokedex):
    return name in pokedex


# Use partial to create a new function that always searches for Pikachu
search_pikachu = partial(search_pokedex, "Pikachu")

print(
    search_pikachu(["Pikachu", "Charmander", "Squirtle", "Bulbasaur"])
)  # Output: True
print(search_pikachu(["Charmander", "Squirtle", "Bulbasaur"]))  # Output: False
