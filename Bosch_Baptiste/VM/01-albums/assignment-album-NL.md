# Examen Vraag 1: Albums

* Plaats alle code voor deze oefening in `album.py`.
* In deze instructies laten we altijd het vermelden van `self` achterwege.
  Het is aan jou om te weten wanneer je deze extra parameter moet toevoegen.
* Zorg ervoor dat je de namen precies goed hebt, zelfs die van de parameters.
* Je hebt een bestand `basic_tests.py` ontvangen dat basis testen bevat, zoals of bepaalde klassen bestaan en of je de juiste namen hebt gebruikt.
  * Voer deze tests uit met het commando:

    ```bash
    $ pytest basic_tests.py
    ```

  * Een ontbrekende klasse zorgt ervoor dat tests die zich richten op die klasse worden overgeslagen.
    Overgeslagen tests tellen daarom nog steeds als mislukt.
  * De tests voeren alleen oppervlakkige controles uit.
    Falende/overgeslagen tests betekenen dat je code zeker onvolledig of incorrect is.
    Maar geslaagde tests betekenen niet dat je code volledig correct is!
* Je moet ook zelf enkele tests maken in het bestand `test-album.py`.
  * Alle tests die je zelf moet schrijven, zijn aangegeven in dit opdrachtbestand.
  * Je kunt hier extra tests aan toevoegen als je je code grondiger wilt controleren. Alleen de tests die in de opdracht worden gevraagd, worden beoordeeld.
  * Dit testbestand moet correct kunnen worden uitgevoerd om punten te verdienen.

## Util

* Definieer een klasse `Util`.
* Definieer een statische methode `is_valid_song_id(song_id)` die `True` retourneert als de song_id op basis van een reguliere expressie geldig is en anders `False`. Controleer dit door een reguliere expressie te gebruiken.
  * Een song_id bestaat uit exact 12 characters
  * Een song_id begint altijd met SONG
  * Hierna volgt er een 4-digit nummer tussen 0000 en 2999
  * Tot slot volgen er 4 klinkers die in kleine letters staan
  * Voorbeelden: "SONG0123aeio" en "SONG1543oouu" zijn geldige song_id's, maar "SONG3543aeio" en "SONG0543azir" niet.

## Lied (Song)

* Definieer een klasse `Song`.
* Definieer de constructor van `Song`.
  * De constructor neemt drie parameters: `song_id` (een string), `title` (een string) en `duration` (een int, uitgedrukt in seconden).
  * Wanneer er een instantie van een `Song` aangemaakt wordt met een ongeldige song_id, moet er een ValueError gegenereerd worden.
* Sla `title` en `duration` op in openbare velden.
* Sla `song_id` op in een privéveld en maak het toegankelijk via een eigenschap (property).
  * Definieer een getter en een setter voor `song_id`.
* Voeg de `dunder methode` toe om een leesbare string representatie te geven van het lied-object
  * Wanneer deze functie aangeroepen wordt, wordt de volgende output gemaakt: `Song: "title", Duration: "duration", Song ID: "song_id"`
  * Voorbeeld:
    * print(the_chain)
    * "Song: The Chain, Duration: 270, Song ID: SONG0456aaii"

## Album

Een `Album` vertegenwoordigt een verzameling van liedjes. Er zijn verschillende soorten albums, maar alle albums delen enkele gemeenschappelijke kenmerken. Daarom zullen we een abstracte klasse `Album` definiëren om gemeenschappelijke kenmerken van verschillende soorten albums op te slaan.

* Definieer een abstracte klasse `Album`.
* Definieer een constructor voor `Album`.
  * De constructor heeft twee parameters: `name` (een string), `total_duration` (een int, uitgedrukt in seconden) (die het totaal aantal beschikbare minuten muziek weergeeft die op het album kan worden opgeslagen).
  * Sla deze op in *openbare* velden.
  * Voeg nog een *privaat* veld `songs` toe om een ​​dictionary van alle liedjes die op dit album staan, op te slaan.
    * De keys van deze dictionary zijn de song_id's
    * De values van deze dictionary zijn de lied objecten
  * Bij aanmaak heeft een `Album` geen liedjes.
* Definieer een alleen-lezen eigenschap (property) `used_duration` die het aantal gebruikte seconden van alle toegevoegde `songs` voor dit `Album` retourneert.
* Definieer een alleen-lezen eigenschap `available_duration` die het resterende aantal seconden voor dit `Album` retourneert.
  * Het resterende aantal seconden krijg je door de `used_duration` af te trekken van de `total_duration` .
* Definieer een methode `add_song(song)` om een ​​`Song` aan de `songs` dictionary toe te voegen.
  * Wanneer de duration van de song die we willen toevoegen, groter is dan de beschikbare duration op het album, genereert deze methode een `RunTimeError`.
* Definieer een methode `remove_song(song)` om een `Song` uit de `songs` dictionary te verwijderen.
  * Wanneer de te verwijderen song niet in de dictionary zit, genereert deze methode een `RunTimeError`.
* Definieer een eigenschap (property) `song_titels` die een lijst met titels (strings) van alle liedjes die op dit `Album` staan, retourneert.
  * Maak hiervoor gebruik van List Comprehension.
* Defineer een methode `sort_songs_by_duration` die aan de hand van een lambda functie een lijst teruggeeft van liedjes, gesorteerd op duration (hoog naar laag).
* Definieer een abstracte methode `create_back_cover()`.

## Soorten Albums

Zoals eerder vermeld, zijn er verschillende soorten Albums: DigitalAlbum, CD, Casette, ...
Gemeenschappelijke functionaliteit is al geïmplementeerd in `Album`. Hieronder zullen we twee dergelijke subklassen definiëren om onderscheid te maken tussen soorten albums. Om te voorkomen dat dit examen te lang wordt, zullen we alleen `DigitalAlbum` en `CD` implementeren.

### `DigitalAlbum`

Een `DigitalAlbum` erft (inherits) van `Album`.

* Definieer een constructor voor `DigitalAlbum`.
  * Het heeft twee parameters: alle twee overgenomen van de constructor van `Album`.
  * Voeg een ander openbaar veld `credits`(een string) toe.
* Implementeer `create_back_cover`
  * Gezien we een DigitalAlbum hebben, hebben we veel ruimte om de back_cover op te stellen
  * Deze functie geeft een string terug die de tekst op de back_cover moet voorstellen
  * De string is opgebouwd uit
    * De titel van het Album
    * De credits van het album
    * De liedjes van het album (1 lijn per liedje), gesorteerd op duration van het liedje (van hoog naar laag)
      * Elke lijn is opgebouwd uit de titel van elk liedje, gevolgd door de duration van het liedje en de song_id
    * Zie voorbeeldgebruik onderaan

### `CD`

Een `CD` erft (inherits) van `Album`.

* Definieer een constructor voor `CD`.
  * Het heeft een parameter: `name`, overgenomen van de constructor van `Album`.
  * De `duration` van een `CD` is altijd gelijk aan 4320.
* Implementeer `create_back_cover`
  * Gezien we bij een CD maar een beperkte ruimte hebben voor de back_cover, zal er minder ruimte beschikbaar zijn
  * Deze functie geeft een string terug die de tekst op de back_cover moet voorstellen
  * De string is opgebouwd uit
    * De titel van het Album
    * De liedjes van het album (1 lijn per liedje), gesorteerd op duration van het liedje (van hoog naar laag)
      * Elke lijn is opgebouwd uit de titel van elk liedje, gevolgd door de duration van het liedje en de song_id
    * Zie voorbeeldgebruik onderaan
* Implementeer de methode `add_song(song)`:
  * Door de beperkte plaats op een CD, kunnen enkel songs van maximaal 360 seconden toegevoegd worden
  * Indien een song toegevoegd wordt die langer duurt, genereert deze methode een `RunTimeError`


## Voorbeeldgebruik

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
Je moet tests schrijven die voldoende de methode `create_back_cover` testen. Neem deze tests op in het bestand `test-album.py`.

* Raadpleeg de beschrijving van zowel `DigitalAlbum` als `CD` voor informatie over hoe je `create_back_cover` kunt implementeren.
* Gebruik de conventies die je hebt geleerd in het hoofdstuk over Testen om deze functionaliteit te kunnen testen.
