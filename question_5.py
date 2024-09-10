from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar, QPushButton, QLabel


class FenetrePrincipale(QMainWindow):

    def __init__(self):
        super().__init__()

        etiquette_message = QLabel("PySide6 est flexible")
        bouton = QPushButton("Afficher")
        bouton.clicked.connect(self.action_afficher)
        self.barre_statut = QStatusBar()
        self.barre_statut.addWidget(etiquette_message)
        self.setStatusBar(self.barre_statut)
        self.setCentralWidget(bouton)

    def action_afficher(self):
        self.barre_statut.showMessage("PySide6 est trop fort", 5000)


app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()

###################
# Question 5
# Quel message sera affiché dans la barre de statut 7 secondes après avoir cliqué sur le bouton Afficher et pourquoi?
# Réponses :
