import os
import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QLabel, QSpacerItem, QSizePolicy, QMainWindow, QListWidget, QAbstractItemView
from PyQt5.QtGui import QPixmap


class RenamerWindow(QWidget):

    def __init__(self):
        super(RenamerWindow, self).__init__()

        # Layout variables and resources

        #self.list_files    = QTextEdit(self)
        self.list_files     = QListWidget(self)
        self.list_files.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.source_btn     = QPushButton('source')
        self.target_btn     = QPushButton('target')
        self.check_btn      = QPushButton('check consistency')
        self.run_btn        = QPushButton('run')

        self.source_lbl     = QLabel('SOURCE: \n')
        self.target_lbl     = QLabel('TARGET: \n')
        self.spacer_lbl     = QLabel(' ')
        self.image_lbl      = QLabel()

        self.vspacer        = QSpacerItem(10, 250, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.neutral_pix    = QPixmap(os.getcwd() + '/trump_neutral.png')
        self.good_pix       = QPixmap(os.getcwd() + '/trump_good.png')
        self.bad_pix        = QPixmap(os.getcwd() + '/trump_bad.png')
        self.image_lbl.setPixmap(self.neutral_pix)

        # Other variables

        self.source         = ""
        self.target         = ""

        self.files = []


        #Initialize UI

        self.init_ui()

    def init_ui(self):
        btn_v_layout =          QVBoxLayout()
        lbl_v_layout =          QVBoxLayout()
        main_v_layout =         QVBoxLayout()
        label_text_v_layout =   QVBoxLayout()
        h_layout = QHBoxLayout()

        btn_v_layout.addWidget(self.source_btn)
        btn_v_layout.addWidget(self.target_btn)
        btn_v_layout.addWidget(self.check_btn)
        btn_v_layout.addWidget(self.run_btn)
        btn_v_layout.addWidget(self.image_lbl)
        btn_v_layout.addItem(self.vspacer)
        #btn_v_layout.addWidget(self.vspacer)
        #btn_v_layout.addWidget(self.source_lbl)
        #btn_v_layout.addWidget(self.target_lbl)

        label_text_v_layout.addWidget(self.list_files)
        label_text_v_layout.addWidget(self.source_lbl)
        label_text_v_layout.addWidget(self.target_lbl)

        #lbl_v_layout.addWidget(self.source_lbl)
        #lbl_v_layout.addWidget(self.target_lbl)
        #lbl_v_layout.addWidget(self.spacer_lbl)
        #lbl_v_layout.addWidget(self.spacer_lbl)

        #h_layout.addWidget(self.source_btn)
        #h_layout.addWidget(self.target_btn)
        #h_layout.addWidget(self.run_btn)

        #btn_v_layout.addWidget(self.list_files)
        #btn_v_layout.addLayout(h_layout)

        #self.source_btn.clicked.connect(self.select_source("SOURCE: ", self.source))
        self.source_btn.clicked.connect(self.select_source)
        self.target_btn.clicked.connect(self.select_target)
        self.check_btn.clicked.connect(self.check_consistency)
        self.run_btn.clicked.connect(self.run_job)
        #self.run_btn.clicked.connect(self.select_directory)

        #h_layout.addWidget(self.list_files)
        h_layout.addLayout(label_text_v_layout)
        h_layout.addLayout(btn_v_layout)
        h_layout.addLayout(lbl_v_layout)

        main_v_layout.addLayout(h_layout)
        self.setLayout(main_v_layout)
        self.setWindowTitle('PyQt5 TextEdit')

        self.show()

    def select_source(self):
        # Clear out old data
        self.list_files.clear()
        self.files = []
        self.source = ""
        self.source_lbl.setText("SOURCE: \n")

        directory = QFileDialog.getExistingDirectory(self)
        if directory:
            self.source = directory
            self.source_lbl.setText(("SOURCE:\n"+ directory))

            # Open a file
            dirs = os.listdir( directory )

            # This would add all the files and directories to the list
            for file in dirs:
                self.list_files.addItem(file)
                self.files.append(file)
                #print (file)


    def select_target(self):
        directory = QFileDialog.getExistingDirectory(self)
        if directory:
            self.target_lbl.setText(("TARGET:\n"+ directory))

    def run_job(self):
        #print (self.list_files.currentRow())
        for each in self.list_files.selectedItems():
            print (each.text())
        #items = []
        #for index in range(self.list_files.count()):
        #     items.append(self.list_files.item(index))

        #for each in items:
        #    print (each)

        #print (self.list_files.selectedItems()[0])
        if self.source == "":
            print ("SAD")
            self.image_lbl.setPixmap(self.bad_pix)

        else:
            print ("RUN JOB")
            self.image_lbl.setPixmap(self.good_pix)

    def check_consistency(self):
        print ("CHECK CONSISTENCY")
        self.image_lbl.setPixmap(self.bad_pix)
        pass

    #def save_text(self):
    #    filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
    #    with open(filename[0], 'w') as f:
    #        my_text = self.text.toPlainText()
    #        f.write(my_text)
    #        
    #def open_text(self):
    #    filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
    #    with open(filename[0], 'r') as f:
    #        file_text = f.read()
    #        self.text.setText(file_text)



    def clear_text(self):
        self.text.clear()



app = QApplication(sys.argv)
#mainApp = 
#app.set
#app.setWindowTitle('test')
#window = QMainWindow()
#window.setWindowTitle('PictureWorkshop');
writer = RenamerWindow()
#writer.
sys.exit(app.exec_())