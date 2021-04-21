file_auth = open('auth.txt', 'r')
users = file_auth.read()
file_auth.close()
dictionar_utilizatori = {"cristi":"parola",
                         "daniel":"123456"}
for user in users.split(','):
    dictionar_utilizatori[user.split(':')[0]] = user.split(':')[1]


# functie auth
def autorizare(user, parola):
    # verific daca utilizatorul exista, daca nu, return nu exista
    # daca exista, verificam parola, return True if ok, daca nu, return parola gresita
    if user in dictionar_utilizatori.keys():
        if dictionar_utilizatori[user] == parola:
            print('Login successful.')
            return True
        else:
            return "parola_gresita"
    else:
        return "nu_exista"