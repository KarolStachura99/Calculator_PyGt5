
class CalculatorLogic:
    def oblicz(self, liczba1, liczba2, operacja):
        try:
            liczba1 = float(liczba1)
            liczba2 = float(liczba2)

            if operacja == "&Dodaj":
                return liczba1 + liczba2
            elif operacja == "&Odejmij":
                return liczba1 - liczba2
            elif operacja == "&Pomnóż":
                return liczba1 * liczba2
            elif operacja == "P&odziel":
                if liczba2 == 0:
                    raise ZeroDivisionError
                return round(liczba1 / liczba2, 9)
        except ValueError:
            raise ValueError("Niepoprawne liczby")
