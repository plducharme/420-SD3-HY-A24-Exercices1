from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QFrame


class FenetrePrincipale(QMainWindow):

    def __init__(self):
        super().__init__()

        etiquette = QLabel("Question 3")
        etiquette.setFrameStyle(QFrame.Shape.Box | QFrame.Shape.Panel)

        self.setCentralWidget(etiquette)


app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()

###########
# Question 3
# Le code ci-dessus ne donne pas d'erreur, mais l'effet visuel n'est pas celui attendu. Pourquoi?
# Réponse :

