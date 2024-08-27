"""
# Variant 1: Albums

## Algemene Instructies

* Plaats alle code voor deze oefening in `album.py`.
* In deze instructies laten we altijd het vermelden van `self` achterwege. Het is aan jou om te weten wanneer je deze extra parameter moet toevoegen.
* Zorg ervoor dat je de namen precies goed hebt, zelfs die van de parameters.
* Je hebt een bestand `basic_tests.py` ontvangen dat basis testen bevat, zoals of bepaalde klassen bestaan en of je de juiste namen hebt gebruikt.
  * Voer deze tests uit met het commando:

    ```bash
    $ pytest basic_tests.py
    ```

  * Een ontbrekende klasse zorgt ervoor dat tests die zich richten op die klasse worden overgeslagen. Overgeslagen tests tellen daarom nog steeds als mislukt.
  * De tests voeren alleen oppervlakkige controles uit. Falende/overgeslagen tests betekenen dat je code zeker onvolledig of incorrect is. Maar geslaagde tests betekenen niet dat je code volledig correct is!
* Je moet ook zelf enkele tests maken in het bestand `test-album.py`.
  * Alle tests die je zelf moet schrijven, zijn aangegeven in dit opdrachtbestand.
  * Dit testbestand moet correct kunnen worden uitgevoerd om punten te verdienen.

## Util

* Definieer een klasse `Util`.
* Definieer een statische methode `is_valid_song_id(song_id)` die `True` retourneert als de `song_id` op basis van een reguliere expressie geldig is en anders `False`. Controleer dit door een reguliere expressie te gebruiken.
  * Een `song_id` bestaat uit exact 10 tekens.
  * Een `song_id` begint altijd met `TRK`.
  * Hierna volgt een 3-cijferig nummer tussen `001` en `999`.
  * De laatste vier tekens moeten een combinatie zijn van 2 hoofdletters gevolgd door 2 cijfers.
  * Voorbeelden: `TRK123AB12` is geldig, maar `TRK00112AB`, `TRK999CD99` en `TRK1000EF34` zijn ongeldig.

## Track (Song)

* Definieer een klasse `Track`.
* Definieer de constructor van `Track`.
  * De constructor neemt drie parameters: `track_id` (een string), `title` (een string) en `duration` (een int, uitgedrukt in seconden).
  * Wanneer er een instantie van een `Track` aangemaakt wordt met een ongeldige `track_id`, moet er een `ValueError` gegenereerd worden.
* Sla `title` en `duration` op in openbare velden.
* Sla `track_id` op in een privéveld en maak het toegankelijk via een eigenschap (property).
  * Definieer een getter en een setter voor `track_id`.
* Voeg de `dunder methode` toe om een leesbare stringrepresentatie te geven van het `Track`-object.
  * Wanneer deze functie aangeroepen wordt, wordt de volgende output gemaakt: `Track: "title", Duration: "duration", Track ID: "track_id"`.
  * Voorbeeld:
    * `print(some_track)`
    * `"Track: Imagine, Duration: 183, Track ID: TRK001AB12"`

## Album

Een `Album` vertegenwoordigt een verzameling van tracks. Er zijn verschillende soorten albums, maar alle albums delen enkele gemeenschappelijke kenmerken. Daarom zullen we een abstracte klasse `Album` definiëren om gemeenschappelijke kenmerken van verschillende soorten albums op te slaan.

* Definieer een abstracte klasse `Album`.
* Definieer een constructor voor `Album`.
  * De constructor heeft twee parameters: `title` (een string) en `max_duration` (een int, uitgedrukt in seconden), wat het totale aantal beschikbare minuten muziek weergeeft die op het album kan worden opgeslagen.
  * Sla deze op in *openbare* velden.
  * Voeg nog een *privaat* veld `tracks` toe om een dictionary van alle tracks die op dit album staan, op te slaan.
    * De keys van deze dictionary zijn de `track_id`s.
    * De values van deze dictionary zijn de `Track`-objecten.
  * Bij aanmaak heeft een `Album` geen tracks.
* Definieer een alleen-lezen eigenschap (property) `total_used_duration` die het aantal gebruikte seconden van alle toegevoegde `tracks` voor dit `Album` retourneert.
* Definieer een alleen-lezen eigenschap `remaining_duration` die het resterende aantal seconden voor dit `Album` retourneert.
  * Het resterende aantal seconden krijg je door de `total_used_duration` af te trekken van de `max_duration`.
* Definieer een methode `add_track(track)` om een `Track` aan de `tracks` dictionary toe te voegen.
  * Wanneer de duration van de track die we willen toevoegen, groter is dan de beschikbare duration op het album, genereert deze methode een `RunTimeError`.
* Definieer een methode `remove_track(track)` om een `Track` uit de `tracks` dictionary te verwijderen.
  * Wanneer de te verwijderen track niet in de dictionary zit, genereert deze methode een `RunTimeError`.
* Definieer een eigenschap (property) `track_titles` die een lijst met titels (strings) van alle tracks die op dit `Album` staan, retourneert.
  * Maak hiervoor gebruik van List Comprehension.
* Defineer een methode `sort_tracks_by_title` die aan de hand van een lambda functie een lijst teruggeeft van tracks, gesorteerd op titel (alfabetisch).
* Definieer een abstracte methode `generate_back_cover()`.

## Soorten Albums

Er zijn verschillende soorten `Albums`: `Vinyl`, `Cassette`, `StreamingAlbum`, etc. Hier zullen we `Vinyl` en `StreamingAlbum` implementeren.

## `Vinyl`

Een `Vinyl` erft van `Album`.

* Definieer een constructor voor `Vinyl`.
  * Het heeft één parameter: `title`, overgenomen van de constructor van `Album`.
  * De `max_duration` van een `Vinyl` is altijd 2400 seconden.
* Implementeer `generate_back_cover`.
  * Een vinyl heeft beperkte ruimte, dus de back cover toont alleen de titels van de eerste vijf tracks.
  * De back cover string is opgebouwd uit:
    * De titel van het album.
    * De eerste vijf tracks van het album, gesorteerd op titel (alfabetisch), met alleen de titel en de duration.
    * Bijvoorbeeld: `"Imagine - 183s"`.
* Implementeer de methode `add_track(track)`:
  * Door de beperkte ruimte op een vinyl kunnen alleen tracks van maximaal 300 seconden worden toegevoegd.
  * Indien een track toegevoegd wordt die langer duurt, genereert deze methode een `RunTimeError`.

## `StreamingAlbum`

Een `StreamingAlbum` erft van `Album`.

* Definieer een constructor voor `StreamingAlbum`.
  * Het heeft één parameter: `title`, overgenomen van de constructor van `Album`.
  * Voeg een openbaar veld `description` (een string) toe.
* Implementeer `generate_back_cover`.
  * Een streaming album heeft onbeperkte ruimte, dus de back cover toont alle tracks van het album, gesorteerd op titel (alfabetisch).
  * De back cover string is opgebouwd uit:
    * De titel van het album.
    * De beschrijving van het album.
    * De tracks van het album, gesorteerd op titel (alfabetisch), met de titel en de duration.
    * Bijvoorbeeld: `"Imagine - 183s"`.

## Voorbeeldgebruik

```python
# Create some tracks
>>> imagine = Track("TRK001AB12", "Imagine", 183)
>>> let_it_be = Track("TRK002CD34", "Let it Be", 240)
>>> hey_jude = Track("TRK003EF56", "Hey Jude", 431)
>>> invalid_track = Track("TRK999ZZ99", "Invalid Track", 120)
ValueError: Invalid Track ID provided
>>> yellow_submarine = Track("TRK004GH78", "Yellow Submarine", 145)

# Print Imagine
>>> print(imagine)
Track: "Imagine", Duration: 183, Track ID: TRK001AB12

# Create a vinyl album
>>> beatles_vinyl = Vinyl("The Beatles Vinyl")

# Adding tracks to the vinyl album
>>> beatles_vinyl.add_track(imagine)
>>> beatles_vinyl.add_track(let_it_be)
>>> beatles_vinyl.add_track(hey_jude)
RuntimeError: Tracks longer than 300 seconds cannot be added to a Vinyl
>>> beatles_vinyl.add_track(yellow_submarine)

# Print track titles
>>> print(beatles_vinyl.track_titles)
['Imagine', 'Let it Be', 'Yellow Submarine']

# Print Back Cover
>>> print(beatles_vinyl.generate_back_cover())
Album: The Beatles Vinyl
Imagine - 183s
Let it Be - 240s
Yellow Submarine - 145s

# Create a streaming album
>>> beatles_stream = StreamingAlbum("The Beatles Stream", "Stream all the hits from The Beatles!")

# Adding tracks to the streaming album
>>> beatles_stream.add_track(imagine)
>>> beatles_stream.add_track(let_it_be)
>>> beatles_stream.add_track(hey_jude)
>>> beatles_stream.add_track(yellow_submarine)

# Print the back cover
>>> print(beatles_stream