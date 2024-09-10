from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout


class FenetrePrincipale(QMainWindow):
    def __init__(self):
        super().__init__()

        etiquette1 = QLabel("Étiquette1")
        font1 = etiquette1.font()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setUnderline(True)
        etiquette1.setFont(font1)

        etiquette2 = QLabel("Étiquette2")
        font2 = etiquette2.font()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setUnderline(True)
        etiquette2.setFont(font2)

        etiquette3 = QLabel("Étiquette3")
        font3 = etiquette3.font()
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setUnderline(True)
        etiquette3.setFont(font3)

        widget_central = QWidget()
        disposition = QVBoxLayout()
        disposition.addWidget(etiquette1)
        disposition.addWidget(etiquette2)
        disposition.addWidget(etiquette3)
        widget_central.setLayout(disposition)
        self.setCentralWidget(widget_central)


app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()

##########
# Question 4
# Simplifiez le code ci-dessus pour éviter la répétition de code
