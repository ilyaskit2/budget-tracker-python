"""
Budget Tracker (CLI)
Projet simple en Python pour gérer des dépenses.
"""

from datetime import datetime


depenses = []


def demander_montant() -> float:
    while True:
        montant_str = input("Montant : ").strip().replace(",", ".")
        try:
            montant = float(montant_str)
            if montant <= 0:
                print("Le montant doit être positif.")
                continue
            return montant
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def ajouter_depense() -> None:
    description = input("Description : ").strip()
    categorie = input("Catégorie : ").strip()

    if not description:
        description = "Sans description"
    if not categorie:
        categorie = "Autre"

    montant = demander_montant()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    depense = {
        "description": description,
        "categorie": categorie,
        "montant": montant,
        "date": date,
    }
    depenses.append(depense)
    print("Dépense ajoutée avec succès.")


def afficher_depenses() -> None:
    if not depenses:
        print("Aucune dépense enregistrée.")
        return

    print("\n--- Liste des dépenses ---")
    for i, depense in enumerate(depenses, start=1):
        print(
            f"{i}. {depense['date']} | {depense['description']} | "
            f"{depense['categorie']} | {depense['montant']:.2f} €"
        )


def calculer_total() -> None:
    total = sum(depense["montant"] for depense in depenses)
    print(f"Total des dépenses : {total:.2f} €")


def sauvegarder_depenses() -> None:
    nom_fichier = "depenses.txt"
    with open(nom_fichier, "w", encoding="utf-8") as fichier:
        fichier.write("Liste des dépenses\n")
        fichier.write("=" * 50 + "\n")
        for depense in depenses:
            fichier.write(
                f"{depense['date']} | {depense['description']} | "
                f"{depense['categorie']} | {depense['montant']:.2f} €\n"
            )
        total = sum(depense["montant"] for depense in depenses)
        fichier.write("=" * 50 + "\n")
        fichier.write(f"Total : {total:.2f} €\n")

    print(f"Dépenses sauvegardées dans '{nom_fichier}'.")


def afficher_menu() -> None:
    print("\n=== Budget Tracker ===")
    print("1. Ajouter une dépense")
    print("2. Afficher les dépenses")
    print("3. Calculer le total")
    print("4. Sauvegarder dans un fichier")
    print("5. Quitter")


def main() -> None:
    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()

        if choix == "1":
            ajouter_depense()
        elif choix == "2":
            afficher_depenses()
        elif choix == "3":
            calculer_total()
        elif choix == "4":
            sauvegarder_depenses()
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Réessayez.")


if __name__ == "__main__":
    main()
