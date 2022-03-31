print("Kalkulator")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
print("5. Procent")


def main():

    koniec = False
    while not koniec:
        a = int(input("Podaj pierwszą liczbę: "))
        b = int(input("Podaj drugą liczbę: "))
        działanie = input("Wybierz działanie: ")
        wynik = 0

        if działanie == "1":
            wynik = a + b
        elif działanie == "2":
            wynik = a - b
        elif działanie == "3":
            wynik = a * b
        elif działanie == "4":
            wynik = a / b
        elif działanie == "5":
            wynik = a % b
        else:
            print("Niepoprawna operacja")
            break

        print("Twój wynik to: " + str(wynik))
        print("Chcesz wykonać kolejne działanie? Wpisz literę T lub N")

        kolejne = input()
        if kolejne == "N":
            koniec = True
        elif kolejne != "T":
            print("Niepoprawny wybór")
            break


if __name__ == "__main__":
    main()