planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# variable = [ expression for item in iterable if condition]
short_planets = [ 3 for string in planets if len(string) < 6]
print(short_planets)