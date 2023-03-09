from tkinter import *
import math

import canvas as canvas

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
#start timer se ejecuta cuando se presiona el boton start con command.
def start_timer():
    count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# funcion de texto y timer, se manda a llamar por la funcion start_timer
def count_down(count):
    #math.flor devuelve valor integral, el mas grande o menor que

    count_min = math.floor(count / 60)
    count_sec = count % 60
    # Canvas intemconfig cambia el comportamiento de un item de canvas
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        #1000 milisegundos = 1s. Contdown es metodo cuenta regresiva.
        window.after(1000, count_down, count -1)



# ---------------------------- UI SETUP ------------------------------- #
#-------WINDOW----------------
window = Tk()
window.title("Pomodoro")



#Los colores fueron configurados en la parte de arriba, el color fue facilitado por https://colorhunt.co/
window.config(padx=100,pady=50, bg=YELLOW)
# highlightthickness: Desaparece el borde que queda de la imamgen y el bg
title_label = Label(text="Timer", fg=GREEN,bg=YELLOW, font=(FONT_NAME,50))
title_label.grid(column=1,row=0)

#--------CANVAS--------------------
canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
#Photoimage es de tkinter, la imagen debe estar en el folder del proyecto.
tomato_img = PhotoImage(file="tomato.png")
#100 y 112 son la ubicación en x y del lienzo.
#image es la imagen de photoimage que se paso a la variable tomato_img
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1)

#--------START BUTTON---------------
#command Ejecutara como metodo la funcion start timer creada (mirar lineas arriba)
start_button = Button(text="Start",highlightthickness=0, command=start_timer)
start_button.grid(column=0,row=2)

#--------RESET BUTTON---------------
start_button = Button(text="Reset",highlightthickness=0)
start_button.grid(column=2,row=2)

#--------CHECK MARK---------------
check_marks = Label(text="✓",fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3 )

window.mainloop()