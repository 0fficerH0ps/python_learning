# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title, number_of_songs):
    """Return Dictionary of info on artist name, album, and songs in album (optional)."""
    album = {'artist': artist_name, 'title': album_title, 'song_count': number_of_songs}
    return album

while True:
    print("\nLet's create an album!")
    print("(Enter 'q' at any time to quit.)")

    artist = input("Enter the artist's name: ")
    if artist == 'q':
        break
    
    title = input("Enter the album name: ")
    if title =='q':
        break

    song_count = input("Enter in the number of songs: ")
    if song_count == 'q':
        break

    completed_album = make_album(artist, title, song_count)
    print(completed_album)

    # Tested, works.