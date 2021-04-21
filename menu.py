import clienti
import finance


# aici pornim aplicatia
def meniu_principal():
    while True:
        meniu = ['Adauga client', 'Verifica Balanta', 'Modifica balanta(transfer)', 'Extras', 'Logoff']
        for submeniu in range(len(meniu)):
            print(f'{submeniu + 1}.{meniu[submeniu]}')
        optiune = int(input('> ')) - 1
        if meniu[optiune] == 'Logoff':
            print('Logged off...')
            break
        elif optiune == 0:
            clienti.adauga_client()
        elif optiune == 1:
            finance.verifica_balanta()
