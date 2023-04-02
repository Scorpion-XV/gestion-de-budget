print("Plateforme de gestion de budget")

from tinydb import TinyDB, Query

db = TinyDB('budget_db.json')
table_transactions = db.table('transactions')
table_categroies = db.table('categories')

def transactions():
    type_transaction = input("veuillez saisir le type de transaction (depense/revenu) : ")
    montant = int(input("le montant : "))
    categorie = input("Categorie : ")
    table_transactions.insert({'type' : type_transaction, 'montant' : montant, 'categorie' : categorie})
    print('transaction ajoutee')

def categories():
    categorie = input('categorie : ')
    table_categroies.insert({'name': categorie})
    print('categorie ajoutee')

def calcul_depenses():
    depenses = table_transactions.search(Query().type == 'depense')
    somme_total = sum([depense['montant'] for depense in depenses])
    return somme_total

def calcul_revenus():
    revenu = table_transactions.search(Query().type == 'revenu')
    somme_total = sum([revenus['montant'] for revenus in revenu])
    return somme_total

def rapport():
    depenses = calcul_depenses()
    revenus = calcul_revenus()
    Ecart = revenus - depenses
    print(f'depenses: {depenses}')
    print(f'revenus: {revenus}')
    print(f'Ecart : {Ecart}')
    
if __name__ == '__main__':
    while True:
        print('1 - Ajouter une transaction')
        print('2 - Ajouter une categorie')
        print("3 - generer l'ecart")
        print('4 - quitter')
        choix = int(input('entrer votre choix: '))
        if choix == 1:
            transactions()
        elif choix == 2:
            categories()
        elif choix == 3:
            rapport()
        elif choix == 4:
            print('Fin du programme')
            break
        else:
            print('choix invalide. veuillez reessayer!')