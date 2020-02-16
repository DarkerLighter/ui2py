import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets

class mainUI(QtWidgets.QWidget):
        def __init__(self):
                super(mainUI, self).__init__()
                self.initUI()

        def initUI(self):

                self.showFullScreen() #This sets the screen to fullscreen
                """
                Set it after central QWidget definition or QMainWindow
                (setting it to QMainWindow also works I tested             
                """
                qbtn = QtWidgets.QPushButton('Quit')
                qbtn.clicked.connect(QtCore.QCoreApplication.quit)
                qbtn.move(5,5)
                self.button = qbtn
                qbtn.show()


def main():
        app = QtWidgets.QApplication(sys.argv)
        window = mainUI()
        sys.exit(app.exec_())

if __name__ == '__main__':
        main()