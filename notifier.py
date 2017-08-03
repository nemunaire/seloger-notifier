#!/usr/bin/env python3

import dbm
import urllib.error
from urllib.request import urlopen
from urllib.parse import urlencode, quote

from seloger import recherche, idTypeBien, TypeBien, TypeTransaction
from seloger.localisation import get_localisation


def send_sms(api_usr, api_key, content):
    try:
        res = urlopen("https://smsapi.free-mobile.fr/sendmsg?" + urlencode({'user': api_usr, 'pass': api_key, 'msg': content}), timeout=5)
    except urllib.error.HTTPError as e:
        if e.code == 400:
            raise Exception("paramètre manquant")
        elif e.code == 402:
            raise Exception("paiement requis")
        elif e.code == 403 or e.code == 404:
            raise Exception("clef incorrecte")
        elif e.code != 200:
            raise Exception("erreur inconnue (%d)" % e.code)


def url_reducer(url):
    return "http://ycc.fr/" + urlopen("http://ycc.fr/redirection/create/" + quote(url, "/:%@&=?")).read().decode()
    return urlopen("http://tinyurl.com/api-create.php?url=" + quote(url, "/:%@&=?")).read().decode()


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Effectue une recherche via l'API de seloger.")

    parser.add_argument('--transaction', choices=["location", "achat"], action='store',
                        help='type de recherche', default="location", required=True)
    parser.add_argument('--localisation', action='append', help='localisation')
    parser.add_argument('--type', dest="type_bien", choices=[v for k,v in idTypeBien.items()] + [k for k,v in idTypeBien.items()], action='append',
                        help='type de bien')
    parser.add_argument('--nb_pieces', choices=["1","2","3","4","+5","all"], action='append',
                        help='nombre de pièces', default="all")
    parser.add_argument('--nb_chambres', choices=["1","2","3","4","+5","all"], action='append',
                        help='nombre de chambres', default="all")

    parser.add_argument('--pxmin', type=int, action='store', help='prix minimal')
    parser.add_argument('--pxmax', type=int, action='store', help='prix maximal')

    parser.add_argument('--surfacemin', type=int, action='store', help='surface minimale')
    parser.add_argument('--surfacemax', type=int, action='store', help='surface maximale')
    parser.add_argument('--surf_terrainmin', type=int, action='store', help='surface minimale du terrain')
    parser.add_argument('--surf_terrainmax', type=int, action='store', help='surface maximale du terrain')

    parser.add_argument('--nb_balconsmin', type=int, action='store', help='nombre de balcons')

    for a in ["ascenseur", "digicode", "interphone", "gardien", "piscine", "terrasse", "parkings", "boxes", "cave"]:
        parser.add_argument('--' + a, dest="si_" + a, action='store_const', const=1, help="présence " + a)
        parser.add_argument('--no-' + a, dest="si_" + a, action='store_const', const=0, help="absence " + a)

    parser.add_argument('--tri', choices=["a_dt_crea", "d_dt_crea", "a_px", "d_px", "a_surface", "d_surface"], action='store', help='tri des résultats')

    parser.add_argument('--skip-old', action='store', help="Adresse du fichier dans lequel stocker les annonces déjà vues")

    parser.add_argument('--freesms_user', action='store', help="Numéro d'utilisateur Free Mobile")
    parser.add_argument('--freesms_key', action='store', help="Clef d'API")

    args = parser.parse_args()

    criteres = {}

    if args.transaction is not None:
        criteres["idtt"] = []
        if "location" in args.transaction: criteres["idtt"].append(TypeTransaction.LOCATION)
        if "achat" in args.transaction: criteres["idtt"].append(TypeTransaction.ACHAT)

    if args.localisation is not None:
        criteres["ci"] = []
        for l in args.localisation:
            loc = get_localisation(l)
            if not loc:
                raise Exception("Localisation non trouvée")
            criteres["ci"].append(loc[0]["Params"]["ci"])

    if args.type_bien is not None:
        criteres["idtypebien"] = []
        for tb in args.type_bien:
            if tb in idTypeBien:
                criteres["idtypebien"].append(tb)
                continue
            for k,v in idTypeBien.items():
                if v == tb:
                    criteres["idtypebien"].append(k)
                    break

    for a in ["nb_pieces", "nb_chambres", "pxmin", "pxmax", "si_ascenseur", "si_digicode", "si_interphone", "si_gardien", "si_piscine", "si_terrasse", "si_parkings", "si_boxes", "si_cave"]:
        if getattr(args, a) is not None:
            criteres[a] = getattr(args, a)

    dbold = None
    if args.skip_old is not None:
        dbold = dbm.open(args.skip_old, 'c')

    for a in recherche.annonces(**criteres):
        if dbold is None or a.idAnnonce not in dbold or dbold[a.idAnnonce] != str(hash(a)).encode():
            for c in ["surface", "surfaceUnite"]:
                if not hasattr(a, c):
                    a.__dict__[c] = ""
            s = "{titre} {surface}{surfaceUnite} {ville_} {prix_}\n{libelle}: {permalink}\n{descriptif}".format(ville_=("sur " + a.ville) if a.ville else "", prix_="%s %s %s" % ("loué" if a.idTypeTransaction == TypeTransaction.LOCATION else "vendu", a.prix if hasattr(a, "prix") else "prix non communiqué", a.prixUnite if hasattr(a, "prixUnite") else "€"), permalink=url_reducer(a.permaLien), **a.__dict__).strip()

            if dbold is not None:
                if a.idAnnonce in dbold:
                    s = "Mise à jour de l'annonce : " + s
                dbold[a.idAnnonce] = str(hash(a))

            if args.freesms_user is not None and args.freesms_key is not None:
                send_sms(args.freesms_user, args.freesms_key, s)
            print(s)
            print("--")

if __name__ == "__main__":
    main()
