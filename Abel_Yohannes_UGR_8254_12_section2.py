import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import numpy as np
from tkinter import *

gui = Tk()
gui.title("Graph From Given Mathematical Functions Application")


text_1 = "You must choose \n "
text_2 = "ONLY TWO(2) \n"
text_3 = "mathematical functions  from the given choices, to display their graph"

instruct = Label(gui, text=text_1 + text_2 + text_3, font=('times new roman', 25), padx=100, pady=30)
separate = Label(gui, text="NOTICE!! If just one is selected you will not be able to see its graph. (choose 2)",
                 font=12, padx=15, pady=30, fg="red")


#########################################################

line_space = np.linspace(-2.6, 2.6, 100)


def init():
    pygame.init()
    display = (1850, 1000)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(1.0, 1.0, 1.0, 0.0)
    gluOrtho2D(-5.0, 5.0, -6.0, 8.0)


def x_axes():
    glColor3f(1.0, 1.0, 1.0)

    glBegin(GL_LINES)

    glVertex3f(-2.8, 0.0, 0.0)
    glVertex3f(2.8, 0.0, 0.0)

    glEnd()
    glFlush()


def y_axes():

    glColor3f(1.0, 1.0, 1.0)

    glBegin(GL_LINES)

    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glEnd()
    glFlush()


def x_arrow():

    # arrow being drawn and filled color for x-axis starts here #

    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POLYGON)

    glVertex3f(2.8, 0.0, 0.0)
    glVertex3f(2.65, 0.2, 0.0)

    glVertex3f(2.65, -0.2, 0.0)

    glEnd()
    glFlush()

    glBegin(GL_POLYGON)

    glVertex3f(-2.8, 0.0, 0.0)
    glVertex3f(-2.65, 0.2, 0.0)

    glVertex3f(-2.65, -0.2, 0.0)

    glEnd()
    glFlush()
    # arrow being drawn and filled color for x-axis ends here #


def y_arrow():
    # arrow being drawn and filled color for y-axis starts here #
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POLYGON)

    glVertex3f(0.0, 5.0, 0.0)
    glVertex3f(-0.08, 4.75, 0.0)

    glVertex3f(0.08, 4.75, 0.0)

    glEnd()
    glFlush()

    glBegin(GL_POLYGON)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(-0.08, -4.75, 0.0)

    glVertex3f(0.08, -4.75, 0.0)

    glEnd()
    glFlush()
    # arrow being drawn and filled color for y-axis ends here #

##############################################################


# function for inversed exponent lan
def inv_exponent():
    glColor4f(0.5, 1.0, 1.0, 0.0)
    x = line_space
    y = np.log(x)

    glPointSize(10)
    glPushAttrib(GL_ENABLE_BIT)
    glLineStipple(1, 0x3AfC)
    glEnable(GL_LINE_STIPPLE)

    glBegin(GL_LINE_STRIP)
    # for every pair (a, b) of the numbers in x, y
    for a, b in zip(x, y):
        # give (a, b) to OpenGL to draw
        glVertex2f(a, b)

    glEnd()
    glPopAttrib()
    glFlush()


# function for cosine of x
def cosine():
    glColor3f(2.0, 0.5, 1.0)
    x = line_space
    y = np.cos(x)

    glPointSize(10)
    glPushAttrib(GL_ENABLE_BIT)
    glLineStipple(1, 0x3AfC)
    glEnable(GL_LINE_STIPPLE)

    glBegin(GL_LINE_STRIP)
    # for every pair (a, b) of the numbers in x, y
    for a, b in zip(x, y):
        # give (a, b) to OpenGL to draw
        glVertex2f(a, b)

    glEnd()
    glPopAttrib()
    glFlush()


# function for logarithm of x
def logarithm_ten():
    glColor3f(1.0, 1.0, 0.0)
    x = line_space
    y = np.log10(x)

    glPointSize(10)
    glPushAttrib(GL_ENABLE_BIT)
    glLineStipple(1, 0x3AfC)
    glEnable(GL_LINE_STIPPLE)

    glBegin(GL_LINE_STRIP)
    # for every pair (a, b) of the numbers in x, y
    for a, b in zip(x, y):
        # give (a, b) to OpenGL to draw
        glVertex2f(a, b)

    glEnd()
    glPopAttrib()
    glFlush()


# function for exponential of x
def exponent():
    glColor3f(0.0, 0.9, 0.0)
    x = line_space
    y = np.exp(x)

    glPointSize(10)
    glPushAttrib(GL_ENABLE_BIT)
    glLineStipple(1, 0x3AfC)
    glEnable(GL_LINE_STIPPLE)

    glBegin(GL_LINE_STRIP)
    # for every pair (a, b) of the numbers in x, y
    for a, b in zip(x, y):
        # give (a, b) to OpenGL to draw
        glVertex2f(a, b)

    glEnd()
    glPopAttrib()
    glFlush()


# function for arc tanget(h) of x
def arc_tan_h():
    glColor3f(0.5, 0.0, 1.0)
    x = line_space
    y = np.arctanh(x)

    glPointSize(10)
    glPushAttrib(GL_ENABLE_BIT)
    glLineStipple(1, 0x3AfC)
    glEnable(GL_LINE_STIPPLE)

    glBegin(GL_LINE_STRIP)
    # for every pair (a, b) of the numbers in x, y
    for a, b in zip(x, y):
        # give (a, b) to OpenGL to draw
        glVertex2f(a, b)

    glEnd()
    glPopAttrib()
    glFlush()


# function for arc cosine(h) of x
def arc_cosine_h():
    glColor4f(1.0, 0.0, 0.0, 0.5)
    x = line_space
    y = np.arccosh(x)

    glPointSize(10)
    glPushAttrib(GL_ENABLE_BIT)
    glLineStipple(1, 0x3AfC)
    glEnable(GL_LINE_STIPPLE)

    glBegin(GL_LINE_STRIP)
    # for every pair (a, b) of the numbers in x, y
    for a, b in zip(x, y):
        # give (a, b) to OpenGL to draw
        glVertex2f(a, b)

    glEnd()
    glPopAttrib()
    glFlush()
#####################################################

# to remove(hide) the buttons exceeding more than 2


def disable_first():
    if (fun_1['state'] == DISABLED) and (fun_2['state'] == DISABLED):
        fun_3.grid_forget()
        fun_4.grid_forget()
        fun_5.grid_forget()
        fun_6.grid_forget()
    if (fun_1['state'] == DISABLED) and (fun_3['state'] == DISABLED):
        fun_2.grid_forget()
        fun_4.grid_forget()
        fun_5.grid_forget()
        fun_6.grid_forget()
    if (fun_1['state'] == DISABLED) and (fun_4['state'] == DISABLED):
        fun_2.grid_forget()
        fun_3.grid_forget()
        fun_5.grid_forget()
        fun_6.grid_forget()
    if (fun_1['state'] == DISABLED) and (fun_5['state'] == DISABLED):
        fun_2.grid_forget()
        fun_4.grid_forget()
        fun_3.grid_forget()
        fun_6.grid_forget()
    if (fun_1['state'] == DISABLED) and (fun_6['state'] == DISABLED):
        fun_2.grid_forget()
        fun_4.grid_forget()
        fun_5.grid_forget()
        fun_3.grid_forget()
    if (fun_2['state'] == DISABLED) and (fun_3['state'] == DISABLED):
        fun_1.grid_forget()
        fun_4.grid_forget()
        fun_5.grid_forget()
        fun_6.grid_forget()
    if (fun_2['state'] == DISABLED) and (fun_4['state'] == DISABLED):
        fun_1.grid_forget()
        fun_3.grid_forget()
        fun_5.grid_forget()
        fun_6.grid_forget()
    if (fun_2['state'] == DISABLED) and (fun_5['state'] == DISABLED):
        fun_1.grid_forget()
        fun_4.grid_forget()
        fun_3.grid_forget()
        fun_6.grid_forget()
    if (fun_2['state'] == DISABLED) and (fun_6['state'] == DISABLED):
        fun_1.grid_forget()
        fun_4.grid_forget()
        fun_5.grid_forget()
        fun_3.grid_forget()
    if (fun_3['state'] == DISABLED) and (fun_4['state'] == DISABLED):
        fun_2.grid_forget()
        fun_1.grid_forget()
        fun_5.grid_forget()
        fun_6.grid_forget()
    if (fun_3['state'] == DISABLED) and (fun_5['state'] == DISABLED):
        fun_2.grid_forget()
        fun_4.grid_forget()
        fun_1.grid_forget()
        fun_6.grid_forget()
    if (fun_3['state'] == DISABLED) and (fun_6['state'] == DISABLED):
        fun_2.grid_forget()
        fun_4.grid_forget()
        fun_5.grid_forget()
        fun_1.grid_forget()
    if (fun_4['state'] == DISABLED) and (fun_5['state'] == DISABLED):
        fun_2.grid_forget()
        fun_1.grid_forget()
        fun_3.grid_forget()
        fun_6.grid_forget()
    if (fun_4['state'] == DISABLED) and (fun_6['state'] == DISABLED):
        fun_2.grid_forget()
        fun_1.grid_forget()
        fun_5.grid_forget()
        fun_3.grid_forget()
    if (fun_5['state'] == DISABLED) and (fun_6['state'] == DISABLED):
        fun_2.grid_forget()
        fun_4.grid_forget()
        fun_1.grid_forget()
        fun_3.grid_forget()


# draw the function selected two buttons
def draw():

    if fun_1['state'] == DISABLED:

        if fun_2['state'] == DISABLED:
            logarithm_ten()
            exponent()

        elif fun_3['state'] == DISABLED:
            logarithm_ten()
            inv_exponent()

        elif fun_4['state'] == DISABLED:
            logarithm_ten()
            arc_tan_h()

        elif fun_5['state'] == DISABLED:
            logarithm_ten()
            arc_cosine_h()

        elif fun_6['state'] == DISABLED:
            logarithm_ten()
            cosine()

    elif fun_2['state'] == DISABLED:
        if fun_3['state'] == DISABLED:
            exponent()
            inv_exponent()
        elif fun_4['state'] == DISABLED:
            exponent()
            arc_tan_h()
        elif fun_5['state'] == DISABLED:
            exponent()
            arc_cosine_h()
        elif fun_6['state'] == DISABLED:
            cosine()
            exponent()

    elif fun_3['state'] == DISABLED:
        if fun_4['state'] == DISABLED:
            inv_exponent()
            arc_tan_h()
        elif fun_5['state'] == DISABLED:
            inv_exponent()
            arc_cosine_h()
        elif fun_6['state'] == DISABLED:
            inv_exponent()
            cosine()

    elif fun_4['state'] == DISABLED:
        if fun_5['state'] == DISABLED:
            arc_tan_h()
            arc_cosine_h()
        elif fun_6['state'] == DISABLED:
            arc_tan_h()
            cosine()

    elif fun_5['state'] == DISABLED:
        if fun_6['state'] == DISABLED:
            arc_cosine_h()
            cosine()
    else:
        return gui.destroy()

    x_axes()
    y_axes()
    x_arrow()
    y_arrow()


# call the pygame window to display the math functions on the same co-ordinates
def two_graphs():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw()
        pygame.display.flip()
        pygame.time.wait(10)


selections = Entry(gui, bg="white", fg="black", borderwidth=5, width=50, font='arial 14 italic')
selections.grid(row=1, column=3)
selections.insert(0, " ")


# selected buttons
def chosen(value):
    fun_first = selections.get()
    selections.delete(0, END)

    selections.insert(0, fun_first + value + " and ")


# what happens when the back button is clicked
def _back():
    selections.delete(0, END)
    fun_1['state'] = NORMAL
    fun_1['bg'] = "blue"
    fun_1.grid(row=2, column=1)
    fun_1_label.grid_forget()

    fun_2['bg'] = "blue"
    fun_2['state'] = NORMAL
    fun_2.grid(row=3, column=0)
    fun_2_label.grid_forget()

    fun_3['state'] = NORMAL
    fun_3['bg'] = "blue"
    fun_3.grid(row=3, column=2)
    fun_3_label.grid_forget()

    fun_4['bg'] = "blue"
    fun_4['state'] = NORMAL
    fun_4.grid(row=4, column=1)
    fun_4_label.grid_forget()

    fun_5['state'] = NORMAL
    fun_5['bg'] = "blue"
    fun_5.grid(row=5, column=0)
    fun_5_label.grid_forget()

    fun_6['bg'] = "blue"
    fun_6['state'] = NORMAL
    fun_6.grid(row=5, column=2)
    fun_6_label.grid_forget()


# each button saving their number of times clicked to determine the state
count = 0
fun_1_label = Label(gui,width=8,text="color 1",  bg = "yellow", font='12', fg = "black")
fun_2_label = Label(gui,width=8,text="color 2", bg = "#000fff000", font='12',fg = "black")
fun_3_label = Label(gui,width=8,text="color 3",bg = "#ADD8E6", font='12', fg = "black")
fun_4_label = Label(gui,width=8,text="color 4", bg = "#4B0082", font='12', fg = "white" )
fun_5_label = Label(gui,width=8,text="color 5",  bg = "#fff000000", font='12', fg = "white")
fun_6_label = Label(gui,width=8,text="color 6",  bg = "#FFC0CB", font='12', fg = "black")


def func_1():
    global count
    count += 1
    if count >= 1:
        fun_1['state'] = DISABLED
        fun_1['bg'] = "orange"
        fun_1.unbind("<Button-1>")
        fun_1_label.grid(row= 2, column=3 )
        count = 0


def func_2():
    global count
    count += 1
    if count >= 1:
        fun_2['state'] = DISABLED
        fun_2['bg'] = "orange"
        fun_2.unbind("<Button-1>")
        fun_2_label.grid(row=3, column=3)
        count = 0


def func_3():
    global count
    count += 1
    if count >= 1:
        fun_3['state'] = DISABLED
        fun_3['bg'] = "orange"
        fun_3.unbind("<Button-1>")
        fun_3_label.grid(row=4, column=3)
        count = 0


def func_4():
    global count
    count += 1
    if count >= 1:
        fun_4['state'] = DISABLED
        fun_4['bg'] = "orange"
        fun_4.unbind("<Button-1>")
        fun_4_label.grid(row=5, column=3)
        count = 0


def func_5():
    global count
    count += 1
    if count >= 1:
        fun_5['state'] = DISABLED
        fun_5['bg'] = "orange"
        fun_5.unbind("<Button-1>")
        fun_5_label.grid(row=6, column=3)
        count = 0


def func_6():
    global count
    count += 1
    if count >= 1:
        fun_6['state'] = DISABLED
        fun_6['bg'] = "orange"
        fun_6.unbind("<Button-1>")
        fun_6_label.grid(row=7, column=3)
        count = 0


# function buttons

fun_1 = Checkbutton(gui, text="1. Log to base 10 (log10(x))", fg="white",bg="blue", font=('elephant', 15), borderwidth=5,
                    cursor="pirate", activebackground="orange", width=30, padx=30, pady=20, relief="raised",
                    command=lambda: [chosen("First selected ---"), func_1(), disable_first()])

fun_2 = Checkbutton(gui, text="2. Exponent of x (exp(x))", fg="white", bg="blue", font=('elephant', 15),
                    cursor="pirate", activebackground="orange", width=30, padx=30, pady=20,relief="raised",
                    command=lambda: [chosen("Second selected ---"), func_2(), disable_first()])


fun_3 = Checkbutton(gui, text="3. Inverse of exponent (ln(x))", fg="white", bg="blue", font=('elephant', 15), borderwidth=5,
                    cursor="pirate", activebackground="orange", width=30, padx=30, pady=20, relief="raised",
                    command=lambda: [chosen("Third selected ---"), func_3(), disable_first()])

fun_4 = Checkbutton(gui, text="4. Arctangeth of x (arctanh(x))", fg="white", bg="blue", font=('elephant', 15), borderwidth=5,
                    cursor="pirate", activebackground="orange", width=30, padx=30, pady=20, relief="raised",
                    command=lambda: [chosen("Forth selected ---"), func_4(), disable_first()])

fun_5 = Checkbutton(gui, text="5. Arccosineh (arccosh(x))", fg="white", bg="blue", font=('elephant', 15), borderwidth=5,
                    cursor="pirate", activebackground="orange", width=30, padx=30, pady=20, relief="raised",
                    command=lambda: [chosen("Fifth selected ---"), func_5(), disable_first()])

fun_6 = Checkbutton(gui, text="6. Cosine of x (cos(x))", fg="white", bg="blue", font=('elephant', 15), borderwidth=5,
                    cursor="pirate", activebackground="orange", width=30, padx=30, pady=20, relief="raised",
                    command=lambda: [chosen("Sixth selected ---"), func_6(), disable_first()])


# positioning the buttons in rows and columns
fun_1.grid(row=2, column=1)
fun_1.bind("<Button-1>", func_1)

fun_2.grid(row=3, column=0)
fun_2.bind("<Button-1>", func_2)

fun_3.grid(row=3, column=2)
fun_3.bind("<Button-1>", func_3)

fun_4.grid(row=4, column=1)
fun_4.bind("<Button-1>", func_4)

fun_5.grid(row=5, column=0)
fun_5.bind("<Button-1>", func_5)

fun_6.grid(row=5, column=2)
fun_6.bind("<Button-1>", func_6)

instruct.grid(row=0, column=0, columnspan=3)


# draw graph and back button
graph = Button(gui, text="PROCEED TO GRAPH", fg="white", bg="green", font=('elephant', 15), cursor="spider",
               borderwidth=5, activebackground="blue", padx=30, pady=20, relief="groove",
               command=two_graphs)

back = Button(gui, text="BACK", fg="black", bg="white", font=('elephant', 15), borderwidth=5, cursor="exchange",
              justify=LEFT, activebackground="red", padx=30, pady=20, relief="groove", command=_back)

separate.grid(row=6, column=0, columnspan=2)
graph.grid(row=8, column=1)
back.grid(row=8, column=2)

gui.mainloop()
