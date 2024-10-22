import tkinter as tk
from random import choice

window = tk.Tk()
window.geometry('480x510')
window.config(bg='#1B019B')

current_state = 'X'  
liste_gagnant = [[1, 2, 3], [1, 4, 7], [4, 5, 6], [7, 8, 9], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
jouers_x = []
jouers_o = []
game_over = False  

# Liste des boutons disponibles
available_buttons = list(range(1, 10))

# Dictionnaire pour stocker les boutons par numéro
buttons = {}

def gagne(jouers_x, jouers_o, liste_gagnant):
    for i in liste_gagnant:
        if all(num in jouers_x for num in i):
            print('Joueur X gagne!')
            return True  

        elif all(num in jouers_o for num in i):
            print('Joueur O gagne!')
            return True  

    if len(jouers_x) + len(jouers_o) == 9:
        print('Dommage, partie nulle!')
        return True  
    return False  

def button_click(button, button_number):
    global current_state, game_over, jouers_o, jouers_x
    if game_over: 
        return

    if current_state == 'X' and button['text'] == '':
        print(f'Button {button_number} cliqué par joueur {current_state}')
        button.config(text='X')
        jouers_x.append(button_number)
        available_buttons.remove(button_number)
        
        if gagne(jouers_x, jouers_o, liste_gagnant):
            game_over = True  
            return
        current_state = 'O'
        computer()

def computer():
    global available_buttons, jouers_o, current_state
    if available_buttons:
        # L'ordinateur choisit un bouton aléatoire
        c = choice(available_buttons)
        available_buttons.remove(c)
        buttons[c].config(text='O')
        jouers_o.append(c)
        
        if gagne(jouers_x, jouers_o, liste_gagnant):
            game_over = True
            return
        current_state = 'X'

# Créer les boutons et les stocker dans le dictionnaire
for row in range(3):
    for col in range(3):
        button_number = row * 3 + col + 1
        button = tk.Button(window, text='', bd=0, highlightthickness=0, bg='#1B019B', width=5, height=2)
        button.grid(row=row * 2, column=col * 2, padx=5, pady=5, sticky='nsew')
        
        # Stocker le bouton avec son numéro
        buttons[button_number] = button
        
        button.config(command=lambda btn=button, num=button_number: button_click(btn, num))

        if col < 2:  
            vertical_line = tk.Canvas(window, width=5, bg='black', highlightthickness=0)
            vertical_line.grid(row=row * 2, column=col * 2 + 1, sticky='ns') 

    if row < 2:  
        horizontal_line = tk.Canvas(window, height=5, bg='black', highlightthickness=0)
        horizontal_line.grid(row=row * 2 + 1, column=0, columnspan=6, sticky='ew')

# Configurer les lignes de la grille
for i in range(3):
    window.grid_rowconfigure(i * 2, weight=1)
    window.grid_columnconfigure(i * 2, weight=1)

window.mainloop()
