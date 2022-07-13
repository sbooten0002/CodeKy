current_movies = {'Batman': '7:50',
                  'Narturo': '9:00',
                  'Spiderman': '6:00',
                  'Dr. Strange': '8:00'}

print("We're showing the following")
for key in current_movies:
    print(key)
movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)
if showtime == None:
    print("Requested movies is playing: ")
else:
    print(movie, 'is playing at', showtime)

