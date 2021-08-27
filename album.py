def make_album(artist, name, num_songs = None):
    """Get a dictionary containing an album"""
    if num_songs:
        album = {
            "artist": artist,
            "name": name.title(),
            "number of songs": num_songs,
        }
    else:
        album = {
            "artist": artist,
            "name": name.title(),
        }
    return(album)


print(make_album("Michael Jackson", "thriller"))
print(make_album("Led Zepelin", "the dark side of the moon"))
print(make_album("ACDC", "back in black"))
print(make_album("Nirvana", "Nevermind", 12))