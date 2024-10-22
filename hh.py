import tkinter as tk

window = tk.Tk()
window.geometry('480x510')
window.config(bg='#1B019B')

current_state = 'X'  
liste_gagnant = [[1, 2, 3], [1, 4, 7], [4, 5, 6], [7, 8, 9], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
jouers_x = []
jouers_o = []
game_over = False  

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
    global current_state, game_over  
    if game_over: 
        return

    print(f'Button {button_number} clicked! par joueur {current_state}')

    if current_state == 'X':
        button.config(text='X')
        jouers_x.append(button_number)
        if gagne(jouers_x, jouers_o, liste_gagnant):
            game_over = True  
            return
        current_state = 'O'  
    else:
        button.config(text='O')
        jouers_o.append(button_number)
        if gagne(jouers_x, jouers_o, liste_gagnant):
            game_over = True  
            return
        current_state = 'X'

for row in range(3):
    for col in range(3):
        button_number = row * 3 + col + 1
        button = tk.Button(window, text='', bd=0, highlightthickness=0, bg='#1B019B', width=5, height=2)
        button.grid(row=row * 2, column=col * 2, padx=5, pady=5, sticky='nsew')  
        button.config(command=lambda btn=button, num=button_number: button_click(btn, num))

        if col < 2:  
            vertical_line = tk.Canvas(window, width=5, bg='black', highlightthickness=0)
            vertical_line.grid(row=row * 2, column=col * 2 + 1, sticky='ns') 

    if row < 2:  
        horizontal_line = tk.Canvas(window, height=5, bg='black', highlightthickness=0)
        horizontal_line.grid(row=row * 2 + 1, column=0, columnspan=6, sticky='ew')

for i in range(3):
    window.grid_rowconfigure(i * 2, weight=1)
    window.grid_columnconfigure(i * 2, weight=1)

window.mainloop()
