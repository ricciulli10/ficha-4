let cantidad_de_lluvia = 0
input.onButtonPressed(Button.A, function () {
    cantidad_de_lluvia = 0
    for (let index = 0; index < 30; index++) {
        cantidad_de_lluvia += randint(0, 10)
    }
    basic.showString("cantidad de agua")
    cantidad_de_lluvia = cantidad_de_lluvia * 12
    basic.showNumber(cantidad_de_lluvia)
    basic.showString("1 año")
    cantidad_de_lluvia = cantidad_de_lluvia * 5
    basic.showNumber(cantidad_de_lluvia)
    basic.showString("5 años")
})
