pokedex = ["Pikachu", "Charmander", "Squirtle", "Bulbasaur", "Jigglypuff", "Snorlax"]


# Define a function to filter out Pokemon that begin with 'S'
def starts_with_s(pokemon):
    return pokemon.startswith("S")


# Use the filter function to get a list of Pokemon that start with 'S'
s_pokemon = list(filter(starts_with_s, pokedex))
print(s_pokemon)

s_pokemon = [p for p in pokedex if starts_with_s(p)]
print(s_pokemon)


def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
