from num2words import num2words

def convert_number_to_words(number):
    try:
        words = num2words(number, lang='es')
        return words
    except ValueError:
        return "Error: No se puede convertir el número en palabras."


"""
# Solicitar entrada del usuario
number = input("Ingresa un número: ")
number = int(number)  # Convertir la entrada a un número entero
"""

# Ejemplo de uso
number = 1000
words = convert_number_to_words(number)
print(f"{number} en palabras es: {words}")
