from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class FenetrePrincipale(QMainWindow):

    def __init__(self):
        super().__init__()

        etiquette = QLabel("Étiquette")
        self.setCentralWidget(etiquette)


app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()

##########
# Question 1
# Quelle classe implémente la méthode setCentralWidget() dans le code ci-dessus?
# Réponse :
