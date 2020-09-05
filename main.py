cantidad_de_lluvia = 0

def on_button_pressed_a():
    global cantidad_de_lluvia
    cantidad_de_lluvia = 0
    for index in range(30):
        cantidad_de_lluvia += randint(0, 10)
    basic.show_string("cantidad de agua")
    cantidad_de_lluvia = cantidad_de_lluvia * 12
    basic.show_number(cantidad_de_lluvia)
    basic.show_string("1 año")
    cantidad_de_lluvia = cantidad_de_lluvia * 5
    basic.show_number(cantidad_de_lluvia)
    basic.show_string("5 años")
input.on_button_pressed(Button.A, on_button_pressed_a)
