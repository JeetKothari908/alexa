from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from alexa import alexathing, closer, closeradd, takething

application = QApplication([])
mainWindow = QWidget()
mainWindow.setGeometry(0, 0, 350, 400)
mainWindow.setWindowTitle('Slot and Signal')
thing = 1
dont = 1

pushButton = QPushButton(parent=mainWindow, text='Click me')
pushButton.clicked.connect(alexathing(1))

mainWindow.show()
application.exec()
