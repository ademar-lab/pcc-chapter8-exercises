from album import make_album 

# Poll users about their favorite albums
while True:
    album_name = input("\nWhat is your favorite album?"
        "\nType \"quit\" whenever you want to finish the program ")
    if album_name == "quit":
        break
    author = input("Who wrote that album? ")
    if author == "quit":
        break
    num_songs = input("How manu songs does the album have? ")
    if num_songs == "quit":
        break
    print("\nThis is your favorite album:\n")
    print(make_album(author, album_name, num_songs))