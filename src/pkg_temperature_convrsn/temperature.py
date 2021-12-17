# Function permettant de convertir une temperature en fahrenheit en celsius et vis versa

def c2f(celcius):
    return (float(celcius) * 9/5) + 32

def f2c(fahrenheit):
    return (float(fahrenheit) - 32) * 5/9