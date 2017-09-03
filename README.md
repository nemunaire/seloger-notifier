seloger
=======

Basic SDK to interact with seloger.com API.

This package is not endorsed by seloger.com, this is only a unofficial proof of
concept, not fully featured at all and made by reversing the website.


Usage
-----

```
usage: seloger-notifier [-h] --transaction {location,achat}
                        [--localisation LOCALISATION]
                        [--type {loft,local commercial,bureaux,terrain,bâtiment,maison,immeuble,boutique,programme neuf,hôtel particulier,parking,château,appartement,9,7,8,4,12,2,11,6,15,14,3,13,1}]
                        [--nb_pieces {1,2,3,4,+5,all}]
                        [--nb_chambres {1,2,3,4,+5,all}] [--pxmin PXMIN]
                        [--pxmax PXMAX] [--surfacemin SURFACEMIN]
                        [--surfacemax SURFACEMAX]
                        [--surf_terrainmin SURF_TERRAINMIN]
                        [--surf_terrainmax SURF_TERRAINMAX]
                        [--nb_balconsmin NB_BALCONSMIN] [--ascenseur]
                        [--no-ascenseur] [--digicode] [--no-digicode]
                        [--interphone] [--no-interphone] [--gardien]
                        [--no-gardien] [--piscine] [--no-piscine] [--terrasse]
                        [--no-terrasse] [--parkings] [--no-parkings] [--boxes]
                        [--no-boxes] [--cave] [--no-cave]
                        [--tri {a_dt_crea,d_dt_crea,a_px,d_px,a_surface,d_surface}]
                        [--skip-old SKIP_OLD] [--freesms_user FREESMS_USER]
                        [--freesms_key FREESMS_KEY]

Effectue une recherche via l'API de seloger.

optional arguments:
  -h, --help            show this help message and exit
  --transaction {location,achat}
                        type de recherche
  --localisation LOCALISATION
                        localisation
  --type {loft,local commercial,bureaux,terrain,bâtiment,maison,immeuble,boutique,programme neuf,hôtel particulier,parking,château,appartement,9,7,8,4,12,2,11,6,15,14,3,13,1}
                        type de bien
  --nb_pieces {1,2,3,4,+5,all}
                        nombre de pièces
  --nb_chambres {1,2,3,4,+5,all}
                        nombre de chambres
  --pxmin PXMIN         prix minimal
  --pxmax PXMAX         prix maximal
  --surfacemin SURFACEMIN
                        surface minimale
  --surfacemax SURFACEMAX
                        surface maximale
  --surf_terrainmin SURF_TERRAINMIN
                        surface minimale du terrain
  --surf_terrainmax SURF_TERRAINMAX
                        surface maximale du terrain
  --nb_balconsmin NB_BALCONSMIN
                        nombre de balcons
  --ascenseur           présence ascenseur
  --no-ascenseur        absence ascenseur
  --digicode            présence digicode
  --no-digicode         absence digicode
  --interphone          présence interphone
  --no-interphone       absence interphone
  --gardien             présence gardien
  --no-gardien          absence gardien
  --piscine             présence piscine
  --no-piscine          absence piscine
  --terrasse            présence terrasse
  --no-terrasse         absence terrasse
  --parkings            présence parkings
  --no-parkings         absence parkings
  --boxes               présence boxes
  --no-boxes            absence boxes
  --cave                présence cave
  --no-cave             absence cave
  --tri {a_dt_crea,d_dt_crea,a_px,d_px,a_surface,d_surface}
                        tri des résultats
  --skip-old SKIP_OLD   Adresse du fichier dans lequel stocker les annonces
                        déjà vues
  --freesms_user FREESMS_USER
                        Numéro d'utilisateur Free Mobile
  --freesms_key FREESMS_KEY
                        Clef d'API
```

### Search

#### Minimal terms

At least, you have to indicate the kind of transaction (even rent or buy:
'location', 'achat') to the `--transaction` parameter, and the desired location
(gives a city name). For example:

    seloger-notifier --transaction achat --location Paris

This will display all existing goods available in Paris.


#### Advanced search

List with `--help` parameter, all others parameters you can append in order to
cap the results to interresting item (depend on your wishes).

For example, this command will display only houses in Paris or Asnière sur
Seine with 4 main rooms and parking, with a maximal price of 765432 €:

    seloger-notifier --transaction location --location Paris --location Asnière-sur-Seine --type maison --nb_pieces 4 --pxmax 765432 --parkings


### Sort results

You can sort results with the `--sort` parameter:

* `a_dt_crea`or `d_dt_crea`: by announce creation date: Ascending/Descending.
* `a_px` or `d_px`: by price: Ascending/Descending.
* `a_surface` or `d_surface`: by size: Ascending/Descending.


### Show only newest/updated entries

`seloger-notifier` can store entries you've already seen to only display newest
or updated ones. To enable this feature, you can use the `--skip-old`
parameter; it takes a filename as argument. The file will be created if
necessary and managed the program.

    seloger-notifier --transaction achat --location Paris --skip-old paris.db
	[First time called, this will initialize the file and display all entries]

    seloger-notifier --transaction achat --location Paris --skip-old paris.db
	[If no entries have been added or updated, this will display nothing]

    seloger-notifier --transaction achat --location Paris --skip-old paris.db
	[If there is new or updated entries: they will  bedisplayed]


### SMS

You can receive a SMS for each displayed entry.

Currently, there is only the Free Mobile API support. Get an API key and use it
with your account number.


### `crontab`

To be a real notifier, you should run the notifier as a cron job. You can add a
line like:

    */15 7-21 * * * seloger-notifier --transaction achat --localisation Paris --localisation asnière-sur-seine --type maison --type appartement --type "programme neuf" --pxmax 123450 --skip-old ~/.cache/seen.db --freesms_user 12345678 --freesms_key "AbCdEfGhIjKlM0"

This will launch a check every quarter between 7:00 AM and 9:45 PM.


Installation
------------

Use the `setup.py` file: `python setup.py install`.

### VirtualEnv setup

The easiest way to do this is through a virtualenv:

```sh
virtualenv venv
. venv/bin/activate
python setup.py install
```
