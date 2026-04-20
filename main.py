import csv
import matplotlib.pyplot as plt

TAUX_TVA = 0.20


def lire_ventes(nom_fichier):
    ventes = []

    with open(nom_fichier, mode="r", newline="", encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier)

        for ligne in lecteur:
            vente = {
                "ID": ligne["ID"],
                "Prix": float(ligne["Prix"]),
                "Quantite": int(ligne["Quantite"]),
                "Remise": float(ligne["Remise"])
            }
            ventes.append(vente)

    return ventes


def calculer_donnees(ventes):
    ca_total = 0
    produit_max = None
    max_ca_net = -1

    for vente in ventes:
        ca_brut = vente["Prix"] * vente["Quantite"]
        montant_remise = ca_brut * (vente["Remise"] / 100)
        ca_net = ca_brut - montant_remise
        tva = ca_net * TAUX_TVA
        ca_ttc = ca_net + tva

        vente["CA_Brut"] = round(ca_brut, 2)
        vente["Montant_Remise"] = round(montant_remise, 2)
        vente["CA_Net"] = round(ca_net, 2)
        vente["TVA"] = round(tva, 2)
        vente["CA_TTC"] = round(ca_ttc, 2)

        ca_total += ca_net

        if ca_net > max_ca_net:
            max_ca_net = ca_net
            produit_max = vente["ID"]

    return round(ca_total, 2), produit_max


def exporter_resultats(ventes, nom_fichier):
    champs = [
        "ID", "Prix", "Quantite", "Remise",
        "CA_Brut", "Montant_Remise", "CA_Net", "TVA", "CA_TTC"
    ]

    with open(nom_fichier, mode="w", newline="", encoding="utf-8") as fichier:
        writer = csv.DictWriter(fichier, fieldnames=champs)
        writer.writeheader()
        writer.writerows(ventes)


def afficher_resultats(ventes, ca_total, produit_max):
    print("=== RESULTATS DES VENTES ===")
    for vente in ventes:
        print(
            f"Produit {vente['ID']} | "
            f"CA Brut: {vente['CA_Brut']} | "
            f"CA Net: {vente['CA_Net']} | "
            f"TVA: {vente['TVA']} | "
            f"CA TTC: {vente['CA_TTC']}"
        )

    print("\n=== RESUME ===")
    print(f"CA Total de l'entreprise : {ca_total}")
    print(f"Produit ayant généré le plus gros bénéfice : {produit_max}")


def tracer_graphique(ventes):
    ids = [vente["ID"] for vente in ventes]
    ca_nets = [vente["CA_Net"] for vente in ventes]

    plt.figure(figsize=(10, 6))

    max_val = max(ca_nets)
    couleurs = ["red" if val == max_val else "skyblue" for val in ca_nets]

    barres = plt.bar(ids, ca_nets, color=couleurs)

    plt.title("Chiffre d'Affaires Net par Produit", fontsize=14)
    plt.xlabel("ID Produit", fontsize=12)
    plt.ylabel("CA Net (€)", fontsize=12)


    for barre, valeur in zip(barres, ca_nets):
        plt.text(
            barre.get_x() + barre.get_width() / 2,
            valeur,
            str(valeur),
            ha='center',
            va='bottom'
        )

    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.show()

def main():
    fichier_entree = "ventes.csv"
    fichier_sortie = "resultats_final.csv"

    ventes = lire_ventes(fichier_entree)
    ca_total, produit_max = calculer_donnees(ventes)
    afficher_resultats(ventes, ca_total, produit_max)
    exporter_resultats(ventes, fichier_sortie)
    tracer_graphique(ventes)

    print(f"\nLe fichier '{fichier_sortie}' a été créé avec succès.")


if __name__ == "__main__":
    main()