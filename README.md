# Calculator_PyGt5

Prosty graficzny kalkulator stworzony w Pythonie z wykorzystaniem biblioteki **PyQt5**.  
Aplikacja umożliwia wykonywanie podstawowych działań matematycznych na dwóch liczbach: dodawania, odejmowania, mnożenia i dzielenia.

---

## Struktura projektu

Projekt został podzielony na trzy moduły zgodnie z zasadą separacji odpowiedzialności:

- `CalculatorLogic.py` – zawiera logikę obliczeń.
- `CalculatorUI.py` – odpowiada za interfejs graficzny (GUI) przy użyciu PyQt5.
- `main.py` – uruchamia aplikację i łączy interfejs z logiką.

---

## Funkcje

- Przyjazny interfejs graficzny
- Obsługa błędów:
  - Dzielenie przez zero
  - Wprowadzenie nieprawidłowych danych
- Automatyczne centrowanie okna na ekranie
- Skróty klawiaturowe (np. Alt+D, Alt+O)
- Zamknięcie okna za pomocą Esc
- Okno potwierdzenia przy zamknięciu

---

## Uruchamianie

1. Upewnij się, że masz zainstalowane PyQt5:

   ```bash
   pip install pyqt5
Uruchom projekt z katalogu głównego:

python -m Calculator_PyQt5.main
Uwaga: Uruchamiaj polecenie z poziomu folderu, który zawiera katalog Calculator_PyQt5.
