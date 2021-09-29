import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QHBoxLayout,QTextEdit,QFileDialog,QLabel,QAction,qApp,QMainWindow,QTableView

class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text =QTextEdit()



        self.v_box = QVBoxLayout()
        self.v_box.addWidget(self.text)

        self.setLayout(self.v_box)
        self.setWindowTitle("NOTEPAD")
        self.setGeometry(1400,280,500,500)




class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pencere = Notepad()
        self.setCentralWidget(self.pencere)
        self.setWindowTitle("NOTEPAD")

        self.menu_create()
        self.setGeometry(1400, 280, 500, 500)
        self.show()

    def menu_create(self):
        menubar = self.menuBar()
        open= menubar.addMenu("Open File")
        


        #open file
        open_file =QAction("Open File",self)
        save_file =QAction("Save File", self)
        clear_file = QAction("Clear File",self)
        exit_file= QAction("Exit",self)

        open.addAction(open_file)
        open.addAction(save_file)
        open.addAction(clear_file)
        open.addAction(exit_file)

        open.triggered.connect(self.response1)




    def response1(self,action):
        if (action.text() == "Open File"):
            file_name = QFileDialog.getOpenFileName(self,"Open File",os.getenv("Desktop"))
            with open(file_name[0], "r") as file:
                self.pencere.text.setText(file.read())
        elif (action.text() == "Save File"):
            file_name = QFileDialog.getSaveFileName(self,"Save File", os.getenv("HOME"))
            with open(file_name[0],"w") as file:
                file.write(self.pencere.text.toPlainText())
        elif (action.text() == "Clear File"):
            self.pencere.text.clear()
        elif (action.text() == "Exit"):
            qApp.quit()








app = QApplication(sys.argv)
menü = Menu()
sys.exit(app.exec_())

