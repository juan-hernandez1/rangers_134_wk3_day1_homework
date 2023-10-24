# Exercise #1
# Filter out all of the empty strings from the list below
# Output: ['Argentina', 'San Diego', 'Boston', 'New York']

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

print(list(filter(lambda places: places.strip() != "", places)))


# Exercise #2
# Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"
# Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

author.sort(key=lambda name: name.split()[-1].lower())

print(author)


# Exercise #3
# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...
# Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)] 

# F = (9/5)*C + 32

places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

print(list(map(lambda place: (place[0], place[1] * 9/5 + 32), places)))


# Exercise #4
# Create a generator function that individually returns each movie genre back from the list

genres = ["adventure", "drama", "horror", "comedy", "action", "romance"]

def movie_genres():
    for genre in genres:
        yield genre

genre_generator = movie_genres()

try:
    print(next(genre_generator))
except:
    print("End of list")