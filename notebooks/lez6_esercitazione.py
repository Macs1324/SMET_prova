def es_1():
    numero = int(input("Inserire un numero intero"))

    if numero % 2 == 0:
        print("Il numero è pari")
    else:
        print("Il numero è dispari")

def es_2():
    numero1 = int(input("Inserisci un numero > "))
    numero2 = int(input("Inserisci un altro numero > "))

    if numero1 * numero2 > 1000:
        print(numero1 + numero2)
    else:
        print(numero1 * numero2)

def es_3():
    # svolgimento
    stringa = input("Inserisci una stringa > ")
    numero = int(input("Inserisci un numero > "))

    if len(stringa) <= numero:
        print("Numero adeguato")
    else:
        print("Il numero è troppo alto!")

def es_4():
    # svolgimento
    stringa = input("Inserisci una stringa > ")

    if len(stringa) % 2 == 0:
        print(stringa[::2])
    else:
        print(stringa[1::2])

def es_5():
    stringa = input("Inserisci una stringa > ")
    if len(stringa) % 2 == 0:
        print(stringa[::-1])
    else:
        print(stringa)

def es_6():
    numero1 = int(input("Inserisci un numero > "))
    numero2 = int(input("Inserisci un altro numero > "))

    print(numero1 * int(numero1 > numero2) + numero2 * int(numero2 > numero1))

def es_7():
    numero1 = int(input("Inserisci un numero > "))
    numero2 = int(input("Inserisci un altro numero > "))

    print(numero1 * int(numero1 < numero2) + numero2 * int(numero2 < numero1))


def es_8():
    numero = int(input("Inserisci un numero > "))
    if numero % 3 == 0 or numero % 2 == 0:
        if numero % 3 == 0:
            print("Il numero e' divisibile per 3")
        if numero % 2 == 0:
            print("Il numero e' divisibile per 2")
    else:
        print("Il numero non e' divisibile ne per 2 ne per 3")

def es_9():
    numero = int(input("Inserisci un numero > "))

    if numero <= 100:
        print('*' * numero)
    else:
        print('+' * numero)


for i in range(1, 10):
    print(f"Esercizio {i}")
    exec(f"es_{i}()")