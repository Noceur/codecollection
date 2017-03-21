import os
import sys
import time
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QLabel, QSpacerItem, QSizePolicy, QMainWindow, QListWidget, QAbstractItemView, QTextEdit
from PyQt5.QtGui import QPixmap, QIcon


class RenamerWindow(QWidget):

    def __init__(self):
        super(RenamerWindow, self).__init__()

        # Layout variables and resources

        #self.list_files    = QTextEdit(self)
        self.list_files     = QListWidget(self)
        self.list_files.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_files.setMinimumWidth(400)

        self.log            = QTextEdit()
        self.log.setMinimumWidth(400)
        self.log.setReadOnly(True)
        self.log.setPlaceholderText("Log is empty.")

        self.source_btn     = QPushButton('source')
        self.target_btn     = QPushButton('target')
        self.check_btn      = QPushButton('check consistency')
        self.run_btn        = QPushButton('run')

        self.source_lbl     = QLabel('SOURCE: \n')
        self.target_lbl     = QLabel('TARGET: \n')
        self.log_lbl        = QLabel('LOG:')
        self.files_lbl      = QLabel('FILES:')
        self.spacer_lbl     = QLabel(' ')
        self.image_lbl      = QLabel()
        self.source_lbl.setWordWrap(True)
        self.target_lbl.setWordWrap(True)

        self.vspacer        = QSpacerItem(10, 250, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hspacer2       = QSpacerItem(50, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hspacer        = QSpacerItem(100, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.neutral_pix    = QPixmap(os.getcwd() + '/trump_neutral.png')
        self.good_pix       = QPixmap(os.getcwd() + '/trump_good.png')
        self.bad_pix        = QPixmap(os.getcwd() + '/trump_bad.png')
        self.image_lbl.setPixmap(self.neutral_pix)

        # Other variables
        self.source         = ""
        self.target         = ""
        self.check          = False
        self.files = []

        #Initialize UI
        self.init_ui()

    def init_ui(self):
        btn_v_layout            = QVBoxLayout()
        lbl_v_layout            = QVBoxLayout()
        main_v_layout           = QVBoxLayout()
        label_text_v_layout     = QVBoxLayout()
        log_v_layout            = QVBoxLayout()
        h_layout                = QHBoxLayout()


        btn_v_layout.addWidget(self.spacer_lbl)
        btn_v_layout.addWidget(self.source_btn)
        btn_v_layout.addWidget(self.target_btn)
        btn_v_layout.addWidget(self.check_btn)
        btn_v_layout.addWidget(self.run_btn)
        btn_v_layout.addWidget(self.image_lbl)
        btn_v_layout.addItem(self.vspacer)
        #btn_v_layout.addWidget(self.vspacer)
        #btn_v_layout.addWidget(self.source_lbl)
        #btn_v_layout.addWidget(self.target_lbl)

        label_text_v_layout.addWidget(self.files_lbl)
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

        #log_h_layout.addWidget(self.log_lbl)
        #log_h_layout.addItem(self.hspacer)
        #log_h_layout.addWidget(self.files_lbl)
        #log_h_layout.addItem(self.hspacer)

        log_v_layout.addWidget(self.log_lbl)
        log_v_layout.addWidget(self.log)

        #h_layout.addWidget(self.log)
        #h_layout.addWidget(self.list_files)
        h_layout.addLayout(log_v_layout)
        h_layout.addLayout(label_text_v_layout)
        h_layout.addLayout(btn_v_layout)
        h_layout.addLayout(lbl_v_layout)

        main_v_layout.addLayout(h_layout)
        self.setLayout(main_v_layout)
        self.setWindowTitle('Make asset order great again')
        self.setWindowIcon(QIcon('python-xxl.png'))

        self.show()

    def select_source(self):
        # Clear out old data
        self.list_files.clear()
        self.files = []
        self.source = ""
        self.source_lbl.setText("SOURCE: \n")

        directory = QFileDialog.getExistingDirectory(self)
        if directory:
            self.source = (directory + "/")
            self.source_lbl.setText(("SOURCE:\n"+ directory))

            # Open a file
            dirs = os.listdir( directory )

            # This would add all the files and directories to the list
            for file in dirs:
                self.list_files.addItem(file)
                self.files.append(file)
                #print (file)


    def select_target(self):
        #directory = QFileDialog.getExistingDirectory(self)
        #if directory:
        #    self. 
        #    self.target_lbl.setText(("TARGET:\n"+ directory))



            # Clear out old data
        self.list_files.clear()
        self.files = []
        self.target = ""
        self.target_lbl.setText("TARGET: \n")

        directory = QFileDialog.getExistingDirectory(self)
        if directory:
            self.target = (directory + "/")
            self.target_lbl.setText(("TARGET: \n"+ directory))

    def run_job(self):
        #print (self.list_files.currentRow())
        #items = []
        #for index in range(self.list_files.count()):
        #     items.append(self.list_files.item(index))

        #for each in items:
        #    print (each)

        #print (self.list_files.selectedItems()[0])
        if self.source == "" or self.target == "":
            print ("SAD")
            self.image_lbl.setPixmap(self.bad_pix)

        else:
            print ("RUN JOB")
            move_file("test.txt")
            self.image_lbl.setPixmap(self.good_pix)
            for each in self.list_files.selectedItems():
                print (each.text())

    def check_consistency(self):
        print ("CHECK CONSISTENCY")
        if self.source and self.target: 
            self.image_lbl.setPixmap(self.good_pix)
        else:
            self.image_lbl.setPixmap(self.bad_pix)
        #pass
        print (self.source, self.target)

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

    def add_log(self, message):
        t = time.strftime('%H:%M:%S')
        old_log = self.log.toPlainText()
        if old_log == "":
            #print (t)
            #self.log.setText(str(time.strftime('%H:%M:%S')))
            self.log.setText("- " + str(time.strftime("%H:%M:%S -\n")) + message)
        else:
            #new_log = (self.log.toPlainText() + "\n" + message)
            new_log = ("- " + str(time.strftime('%H:%M:%S -\n')) + message + "\n\n" + self.log.toPlainText())
            self.log.setText(new_log)

    def clear_text(self):
        self.log.clear()





def check_consistency():
    # Check if source and target is set
    pass

def run_job():
    # Check if consistency check is OK
    pass

def check_if_in_use():
    # Check if file in use by program or if locked in SVN
    pass

def move_file(file):
    os.rename((mover.source + file), (mover.target + file))
    print (file, "has been moved.")
    pass

def load_settings():
    # Load settings from INI file
    pass





if __name__ == "__main__":
    app = QApplication(sys.argv)
    mover = RenamerWindow()
    sys.exit(app.exec_())