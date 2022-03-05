# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.

# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value for
# the number of songs, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of songs on an album.

def make_album(artist_name, album_title, number_of_songs = None):
    """Return Dictionary of info on artist name, album, and songs in album (optional)."""
    album = {'artist': artist_name, 'title': album_title, 'song_count': number_of_songs}
    return album

album_1 = make_album('lin-manuel miranda', 'hamilton', '46')
print(album_1)

album_2 = make_album('the beatles', 'yellow submarine', '13')
print(album_2)

album_3 = make_album('marilyn minroe', 'wanted', '12')
print(album_3)

album_4 = make_album('the vontrapp family singers', 'dream a little dream')
print(album_4)

# Tested, works.