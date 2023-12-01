def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Erreur: Division par zéro")

def calculatrice():
    historique = []  # stocker l'historique des calculs

    try:
        while True:
            # saisir deux nombres
            nombre1 = float(input("Entrez le premier nombre: "))
            nombre2 = float(input("Entrez le deuxième nombre: "))

            # choisir l'opération
            operation = input("Choisissez l'opération (+, -, *, /) ou 'q' pour quitter: ")

            # Quitter la calculatrice si l'utilisateur le souhaite
            if operation.lower() == 'q':
                break

            # l'opération appropriée
            if operation == '+':
                resultat = addition(nombre1, nombre2)
            elif operation == '-':
                resultat = soustraction(nombre1, nombre2)
            elif operation == '*':
                resultat = multiplication(nombre1, nombre2)
            elif operation == '/':
                resultat = division(nombre1, nombre2)
            else:
                raise ValueError("Erreur: Opération non valide")

            # Afficher le résultat
            print(f"Le résultat de {nombre1} {operation} {nombre2} est égal à {resultat}")

            # Ajouter l'opération à l'historique
            historique.append(f"{nombre1} {operation} {nombre2} = {resultat}")

    except ValueError as e:
        print(f"Erreur: {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite: {e}")
    finally:
        # Afficher l'historique
        print("\nHistorique des calculs:")
        for calcul in historique:
            print(calcul)

        # Demander à l'utilisateur s'il souhaite effacer l'historique
        effacer_historique = input("Voulez-vous effacer l'historique? (Oui/Non): ").lower()
        if effacer_historique == 'oui':
            historique.clear()
            print("Historique effacé.")

# Exécuter la calculatrice
calculatrice()
