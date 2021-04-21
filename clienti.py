def adauga_client():
    # citesc fisierul clients.txt
    file_clients = open('clients.txt', 'r')
    clients = file_clients.readlines().copy()
    id_unic = len(clients)
    file_clients.close()
    # redeschidem fisierul, in modul 'w' pentru ca avem deja toate informatiile, pe care pe vom
    # re-adauga in fisierul initial
    nume = input('Nume Client:\n> ')
    prenume = input('Prenume Client:\n> ')
    telefon = input('Telefon Client:\n> ')
    oras = input('Oras Client:\n> ')
    new_client = f'{id_unic}:{nume} {prenume}:{telefon}:{oras}\n'
    file_clients = open('clients.txt', 'w')
    clients.append(new_client)
    for client in clients:
        file_clients.write(f'{client}')
    file_clients.close()
    # adaugam clientul in bank.txt si punem balanta 0
    bank_file = open('bank.txt', 'r')
    balante_clienti = bank_file.readlines().copy()
    bank_file.close()
    bank_file = open('bank.txt', 'w')
    balante_clienti.append(f'{id_unic}:0\n')
    for balanta in balante_clienti:
        bank_file.write(balanta)
    print(f'Added client: {new_client}')