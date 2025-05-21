from PyQt5.QtWidgets import (
    QWidget, QMessageBox, QGridLayout, QLabel, QLineEdit,
    QPushButton, QHBoxLayout
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from .CalculatorLogic import CalculatorLogic


class CalculatorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.logika = CalculatorLogic()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(20, 20, 300, 100)
        self.setWindowTitle("Kalkulator")
        self.setWindowIcon(QIcon("kalkulator.png"))
        self.resize(300, 100)

        # Etykiety
        etykieta1 = QLabel("Liczba 1:", self)
        etykieta2 = QLabel("Liczba 2:", self)
        etykieta3 = QLabel("Wynik:", self)

        # Pola edycyjne
        self.liczba1Edt = QLineEdit()
        self.liczba2Edt = QLineEdit()
        self.wynikEdt = QLineEdit()
        self.wynikEdt.setReadOnly(True)
        self.wynikEdt.setToolTip("Wpisz <b>liczbę</b> i wybierz działanie...")

        # Przyciski
        dodajBtn = QPushButton("&Dodaj", self)
        odejmijBtn = QPushButton("&Odejmij", self)
        mnozBtn = QPushButton("&Pomnóż", self)
        dzielBtn = QPushButton("P&odziel", self)
        zamknijBtn = QPushButton("&Zamknij", self)

        # Układ
        układT = QGridLayout()
        układT.addWidget(etykieta1, 0, 0)
        układT.addWidget(etykieta2, 0, 1)
        układT.addWidget(etykieta3, 0, 2)
        układT.addWidget(self.liczba1Edt, 1, 0)
        układT.addWidget(self.liczba2Edt, 1, 1)
        układT.addWidget(self.wynikEdt, 1, 2)

        układH = QHBoxLayout()
        układH.addWidget(dodajBtn)
        układH.addWidget(odejmijBtn)
        układH.addWidget(mnozBtn)
        układH.addWidget(dzielBtn)

        układT.addLayout(układH, 2, 0, 1, 3)
        układT.addWidget(zamknijBtn, 3, 0, 1, 3)

        self.setLayout(układT)
        self.liczba1Edt.setFocus()

        dodajBtn.clicked.connect(self.dzialanie)
        odejmijBtn.clicked.connect(self.dzialanie)
        mnozBtn.clicked.connect(self.dzialanie)
        dzielBtn.clicked.connect(self.dzialanie)
        zamknijBtn.clicked.connect(self.close)

        self.move(self.screen().geometry().center() - self.rect().center())
        self.show()

    def dzialanie(self):
        operacja = self.sender().text()
        try:
            wynik = self.logika.oblicz(
                self.liczba1Edt.text(),
                self.liczba2Edt.text(),
                operacja
            )
            self.wynikEdt.setText(str(wynik))
        except ZeroDivisionError:
            QMessageBox.critical(self, "Błąd", "Nie można dzielić przez zero!", QMessageBox.Ok)
        except ValueError:
            QMessageBox.warning(self, "Błąd", "Wprowadź poprawne liczby!", QMessageBox.Ok)
            self.liczba1Edt.clear()
            self.liczba2Edt.clear()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        odp = QMessageBox.question(
            self, 'Komunikat', 'Czy na pewno chcesz zamknąć kalkulator?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()