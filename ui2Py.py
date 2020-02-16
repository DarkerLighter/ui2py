import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from subprocess import Popen, PIPE, STDOUT



class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Useless title"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        sys.exit()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.openFileNameDialog()

    def openFileNameDialog(self):
        self.file, trash = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py);; Qt Designer files (*.ui)")
        self.convertFile()
        if self.file:
            print(self.file)

    def convertFile(self):
        outfile = self.file[:-2] + "py"  #Getting file name, removing .ui and replacing with .ui


        com = r"pyuic5 -x {} -o {}".format(self.file, outfile)  # Command to convert and formatted names
        Popen(com, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True) # Running CMD command


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

