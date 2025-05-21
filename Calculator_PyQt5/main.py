import sys
from PyQt5.QtWidgets import QApplication
from .CalculatorUI import CalculatorUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = CalculatorUI()
    sys.exit(app.exec_())