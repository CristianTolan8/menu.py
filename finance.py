def verifica_balanta():
    # citit bank.txt file
    bank_file = open('bank.txt', 'r')
    balanta = bank_file.readlines().copy()
    bank_file.close()

    clients_file = open('clients.txt', 'r')
    clients = clients_file.readlines().copy()
    clients_file.close()
    # aici oferim utilizatorului optiunea sa aleaga intre clienti
    for client in clients:
        print(client)