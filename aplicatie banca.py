import menu
from auth import autorizare

print('Bank Application Online...')
while True:
    user = input('username:\n> ')
    password = input('password\n> ')
    if autorizare(user, password) == True:
        menu.meniu_principal()
    elif autorizare(user, password) == 'nu exista':
        print('Utilizatorul nu exista, incearca din nou')
        continue
    elif autorizare(user, password) == 'parola_gresita':
        print('Parola gresita, incearca din nou')
        continue