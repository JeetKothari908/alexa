from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QFont
from alexa import alexathing
application = QApplication([])
mainWindow = QWidget()
mainWindow.setGeometry(0, 0, 1960,1080)
label = QLabel(mainWindow)
mainWindow.setWindowTitle('Alexa')
pixmap = QPixmap('image.jpg')
label.setPixmap(pixmap)
#ting = QPixmap('microphone.jpg')
#label.setPixmap(ting)
#ting = ting.scaled(64, 64)

def alexathingthing():
    alexathing(1)

pushButton = QPushButton(parent=mainWindow, text='Alexabot')
pushButton.setFont(QFont('Arial', 30))
pushButton.clicked.connect(alexathingthing)
pushButton.resize(450,450)
pushButton.move(905,435)
pushButton.setStyleSheet("background-image : url(images/image.png); border: 0 px solid blue ")
mainWindow.show()
application.exec()