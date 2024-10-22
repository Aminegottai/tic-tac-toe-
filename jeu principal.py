import tkinter as tk
from PIL import Image, ImageTk
import subprocess
def play_friend():
    
    subprocess.run(["python", "C:/Users/hp/intrusion detection/2eme.py"])
def play():
    subprocess.run(["python", "C:/Users/hp/intrusion detection/jj.py"])


window = tk.Tk()
window.geometry('600x600')

image = Image.open("C:/Users/hp/Documents/fff.png")  
image = image.resize((600, 600), Image.LANCZOS)  

background_image = ImageTk.PhotoImage(image)

background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

l1 = tk.Button(window, text='Play', font=('Helvetica', 24), bg='white',command=play)  
l1.place(relx=0.85, rely=0.80, anchor='center') 

l2 = tk.Button(window, text='Play with friend', font=('Helvetica', 18), bg='white',command=play_friend)  
l2.place(relx=0.85, rely=0.90, anchor='center')  

window.mainloop()
