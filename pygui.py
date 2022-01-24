from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from alexa import alexathing
application = QApplication([])
mainWindow = QWidget()
mainWindow.setGeometry(0, 0, 350, 400)
mainWindow.setWindowTitle('Alexa')
def alexathingthing():
    alexathing(1)

pushButton = QPushButton(parent=mainWindow, text='Click me')
pushButton.clicked.connect(alexathingthing)

mainWindow.show()
application.exec()
