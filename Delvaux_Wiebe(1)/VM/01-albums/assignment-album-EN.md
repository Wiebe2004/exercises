# Exam Question 1: Albums

* Place all code for this exercise in `album.py`.
* In these instructions, we always omit mentioning `self`.
  It is up to you to know when to add this extra parameter.
* Make sure you get the names exactly right, including the parameter names.
* You have received a file `basic_tests.py` containing basic tests, such as checking whether certain classes exist and if you have used the correct names.
  * Run these tests with the command:

    ```bash
    $ pytest basic_tests.py
    ```

  * A missing class will cause tests targeting that class to be skipped. Skipped tests therefore still count as failed.
  * The tests perform only high-level checks.
    Failed/skipped tests mean that your code is certainly incomplete or incorrect.
    But passing tests do not mean that your code is entirely correct!
* You must also create some tests yourself in the file `test-album.py`.
  * All tests you need to write yourself are indicated in this assignment file.
  * You can add extra tests here if you want to check your code more thoroughly. Only the tests requested in the assignment will be graded.
  * This test file must be able to run correctly to earn points.

## Util

* Define a class `Util`.
* Define a static method `is_valid_song_id(song_id)` that returns `True` if the song_id is valid, otherwise `False`. Check this using a regular expression.
  * A song_id consists of exactly 12 characters.
  * A song_id always starts with SONG.
  * This is followed by a 4-digit number between 0000 and 2999.
  * Finally, there are 4 vowels in lowercase letters.
  * Examples: "SONG0123aeio" and "SONG1543oouu" are valid song_id's, but "SONG3543aeio" and "SONG0543azir" are not.

## Song

* Define a class `Song`.
* Define the constructor of `Song`.
  * The constructor takes three parameters: `song_id` (a string), `title` (a string), and `duration` (an int, expressed in seconds).
  * When an instance of `Song` is created with an invalid song_id, a `ValueError` should be raised.
* Store `title` and `duration` in public fields.
* Store `song_id` in a private field and make it accessible via a property.
  * Define a getter and a setter for `song_id`.
* Add the `dunder method` to provide a readable string representation of the song object.
  * When this function is called, it should produce the following output: `Song: "title", Duration: "duration", Song ID: "song_id"`
  * Example:
    * print(the_chain)
    * "Song: The Chain, Duration: 270, Song ID: SONG0456aaii"

## Album

An `Album` represents a collection of songs. There are different types of albums, but all albums share some common features. Therefore, we will define an abstract class `Album` to store the common features of different types of albums.

* Define an abstract class `Album`.
* Define a constructor for `Album`.
  * It has two parameters: `name` (a string), `total_duration` (an int, expressed in seconds).
  * Store these in *public* fields.
  * Add a *private* field `songs` to store a dictionary of all the songs that are in this album.
    * The keys of this dictionary are the song_id's.
    * The values of this dictionary are the song objects.
  * When created, an `Album` has no songs.
* Define a read-only property `used_duration` that returns the number of used seconds of all added `songs` for this `Album`.
* Define a read-only property `available_duration` that returns the remaining number of seconds for this `Album`.
  * The remaining number of seconds is obtained by subtracting the `used_duration` from the `total_duration`.
* Define a method `add_song(song)` to add a `Song` to the `songs` dictionary.
  * When the duration of the song we want to add is greater than the available duration on the album, this method generates a `RunTimeError`.
* Define a method `remove_song(song)` to remove a `Song` from the `songs` dictionary.
  * When the song to be removed is not in the dictionary, this method generates a `RunTimeError`.
* Define a property `song_titles` that returns a list of titles (strings) of all the songs that are in this `Album`.
  * Use List Comprehension for this.
* Define a method `sort_songs_by_duration` that returns a list of songs sorted by duration (high to low) using a lambda function.
* Define an abstract method `create_back_cover()`.

## Types of Albums

As previously mentioned, there are different types of Albums: DigitalAlbum, CD, Cassette, ...
Common functionality has already been implemented in Album. Below, we will define two such subclasses to distinguish between types of albums. To prevent this exam from becoming too long, we will only implement DigitalAlbum and CD.

### `DigitalAlbum`

A `DigitalAlbum` inherits from `Album`.

* Define a constructor for `DigitalAlbum`.
  * It has two parameters, both inherited from the constructor of `Album`.
  * Add another public field `credits` (a string).
* Implement `create_back_cover`
  * Since we have a DigitalAlbum, we have plenty of space to format the back_cover.
  * This function returns a string representing the back_cover's text.
  * The string is composed of:
    * The title of the Album
    * The credits of the album
    * The songs of the album (one line per song), sorted on the duration of the song (high to low)
      * Each line is constructed with the title of each song followed by the duration of the song and the song_id.
    * See example usage below.

### `CD`

A `CD` inherits from `Album`.

* Define a constructor for `CD`.
  * It has one parameter: `name`, inherited from the constructor of `Album`.
  * The `duration` of a `CD` is always equal to 4320.
* Implement `create_back_cover`
  * Given that a CD has limited space for the back cover, less space will be available
  * This function returns a string representing the back cover's text
  * The string is composed of
    * The title of the Album
    * The songs of the album (one line per song), sorted on the duration of the song (high to low)
      * Each line is constructed with the title of each song followed by the duration of the song and the song_id.
    * See example usage below
* Implement the method `add_song(song)`:
  * Due to the limited space on a CD, only songs with a maximum duration of 360 seconds can be added
  * If a song longer than this is added, this method raises a `RunTimeError`


## Example Usage

```python
# Create some songs
>>> alors_on_dance = Song("SONG0001aaaa", "Alors on dance", 205)
>>> la_tribu_de_dana = Song("SONG0002eeee", "La tribu de Dana", 224)
>>> les_lac_du_connemara = Song("SONG1001aeio", "Les Lac du Connemara", 364)
>>> aline = Song("SONG3001abba", "Aline", 170)
ValueError: Invalid Song ID provided
>>> ca_plane_pour_moi = Song("SONG1002oooo", "Ca plane pour moi", 182)
>>> tout_oublier = Song("SONG2998aaaa", "Tout oublier", 202)
>>> sensualite = Song("SONG2999uoie", "Sensualité", 232 )

# Print Alors On Dance
>>> print(alors_on_dance)
Song: "Alors on dance", Duration: 205, Song ID: SONG0001aaaa

# Create an digitalalbum
>>> french_songs = DigitalAlbum("French Songs", 1000, "This is a digital album, full of french songs")

# Adding songs to our digital album
>>> french_songs.add_song(alors_on_dance)
>>> french_songs.add_song(la_tribu_de_dana)
>>> french_songs.add_song(les_lac_du_connemara)
>>> french_songs.add_song(ca_plane_pour_moi)
>>> french_songs.add_song(tout_oublier)
RuntimeError: Not enough available duration to add this song
>>> french_songs.remove_song(ca_plane_pour_moi)
>>> french_songs.add_song(tout_oublier)
>>> french_songs.remove_song(ca_plane_pour_moi)
RuntimeError: Song not found in album

# Print song titles
>>> print(french_songs.song_titles)
['Alors on dance', 'La tribu de Dana', 'Les Lac du Connemara', 'Tout oublier']

# Print Back Cover
>>> print(french_songs.create_back_cover())
Album: French Songs
Credits: This is a digital album, full of french songs
Les Lac du Connemara - 364s (ID: SONG1001aeio)
La tribu de Dana - 224s (ID: SONG0002eeee)
Alors on dance - 205s (ID: SONG0001aaaa)
Tout oublier - 202s (ID: SONG2998aaaa)

# Create a CD
>>> cd_chanson = CD("Chanson CD")

# Adding songs to our CD
>>> cd_chanson.add_song(alors_on_dance)
>>> cd_chanson.add_song(les_lac_du_connemara)
RuntimeError: Songs longer than 360 seconds cannot be added to a CD
>>> cd_chanson.add_song(ca_plane_pour_moi)
>>> cd_chanson.add_song(sensualite)

# Print the back cover
>>> print(cd_chanson.create_back_cover())
Album: Chanson CD
Sensualité - 232s
Alors on dance - 205s
Ca plane pour moi - 182s
```

# Testing
You need to write tests that adequately test the `create_back_cover` method. Include these tests in the `test-album.py` file.

* Refer to the description of both `DigitalAlbum` and `CD` for information on how to implement `create_back_cover`.
* Use the conventions you have learned in the Testing chapter to test this functionality.
