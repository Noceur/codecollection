import os
import re
import sys
import time
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, \
    QLabel, QSpacerItem, QSizePolicy, QMainWindow, QListWidget, QAbstractItemView, QTextEdit
from PyQt5.QtGui import QPixmap, QIcon


class RenamerWindow(QWidget):
    def __init__(self):
        super(RenamerWindow, self).__init__()

        # Layout variables and resources

        # self.list_files    = QTextEdit(self)
        self.list_files = QListWidget(self)
        self.list_files.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_files.setMinimumWidth(400)

        self.log = QTextEdit()
        self.log.setMinimumWidth(400)
        self.log.setReadOnly(True)
        self.log.setPlaceholderText("Log is empty.")

        self.source_btn = QPushButton('source')
        self.target_btn = QPushButton('target')
        self.check_btn = QPushButton('check consistency')
        self.refresh_btn = QPushButton('refresh directory')
        self.run_btn = QPushButton('run')

        self.source_lbl = QLabel('SOURCE: \n')
        self.target_lbl = QLabel('TARGET: \n')
        self.log_lbl = QLabel('LOG:')
        self.files_lbl = QLabel('FILES:')
        self.spacer_lbl = QLabel(' ')
        self.image_lbl = QLabel()
        self.source_lbl.setWordWrap(True)
        self.target_lbl.setWordWrap(True)

        self.vspacer = QSpacerItem(10, 250, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hspacer2 = QSpacerItem(50, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hspacer = QSpacerItem(100, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.neutral_pix = QPixmap(os.getcwd() + '/neutral.png')
        self.good_pix = QPixmap(os.getcwd() + '/good.png')
        self.bad_pix = QPixmap(os.getcwd() + '/error.png')
        self.image_lbl.setPixmap(self.neutral_pix)

        self.log_file = self.open_file("log.txt")
        self.log_timestamp = 0

        # Other variables
        self.source = ""
        self.target = ""
        self.sourceSubStr = ""
        self.targetSubStr = ""
        self.check = False
        self.files = []

        # Initialize UI
        self.init_ui()

    def init_ui(self):
        btn_v_layout = QVBoxLayout()
        lbl_v_layout = QVBoxLayout()
        main_v_layout = QVBoxLayout()
        label_text_v_layout = QVBoxLayout()
        log_v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        btn_v_layout.addWidget(self.spacer_lbl)
        btn_v_layout.addWidget(self.source_btn)
        btn_v_layout.addWidget(self.target_btn)
        btn_v_layout.addWidget(self.check_btn)
        btn_v_layout.addWidget(self.refresh_btn)
        btn_v_layout.addWidget(self.run_btn)
        btn_v_layout.addWidget(self.image_lbl)
        btn_v_layout.addItem(self.vspacer)
        # btn_v_layout.addWidget(self.vspacer)
        # btn_v_layout.addWidget(self.source_lbl)
        # btn_v_layout.addWidget(self.target_lbl)

        label_text_v_layout.addWidget(self.files_lbl)
        label_text_v_layout.addWidget(self.list_files)
        label_text_v_layout.addWidget(self.source_lbl)
        label_text_v_layout.addWidget(self.target_lbl)

        # lbl_v_layout.addWidget(self.source_lbl)
        # lbl_v_layout.addWidget(self.target_lbl)
        # lbl_v_layout.addWidget(self.spacer_lbl)
        # lbl_v_layout.addWidget(self.spacer_lbl)

        # h_layout.addWidget(self.source_btn)
        # h_layout.addWidget(self.target_btn)
        # h_layout.addWidget(self.run_btn)

        # btn_v_layout.addWidget(self.list_files)
        # btn_v_layout.addLayout(h_layout)

        # self.source_btn.clicked.connect(self.select_source("SOURCE: ", self.source))
        self.source_btn.clicked.connect(self.select_source)
        self.target_btn.clicked.connect(self.select_target)
        self.check_btn.clicked.connect(self.check_consistency)
        self.refresh_btn.clicked.connect(self.update_file_list)
        self.run_btn.clicked.connect(self.run_jobs)
        # self.run_btn.clicked.connect(self.select_directory)

        # log_h_layout.addWidget(self.log_lbl)
        # log_h_layout.addItem(self.hspacer)
        # log_h_layout.addWidget(self.files_lbl)
        # log_h_layout.addItem(self.hspacer)

        log_v_layout.addWidget(self.log_lbl)
        log_v_layout.addWidget(self.log)

        # h_layout.addWidget(self.log)
        # h_layout.addWidget(self.list_files)
        h_layout.addLayout(log_v_layout)
        h_layout.addLayout(label_text_v_layout)
        h_layout.addLayout(btn_v_layout)
        h_layout.addLayout(lbl_v_layout)

        main_v_layout.addLayout(h_layout)
        self.setLayout(main_v_layout)
        self.setWindowTitle('Asset order tool')
        self.setWindowIcon(QIcon('PyIcon.png'))

        self.show()

    def open_file(self, filename):
        t = time.strftime('%H:%M:%S - %d %b')
        #with open(filename, "w") as open_file:
        open_file = open(filename, "w", 1)
        open_file.write("Log created at: " + t + "\n")
        print (t)
        return open_file            

    def select_source(self):
        # Clear out old data
        self.list_files.clear()
        self.files = []
        self.source = ""
        self.source_lbl.setText("SOURCE: \n")

        directory = QFileDialog.getExistingDirectory(self)
        if directory:
            self.source = (directory + "/")
            self.source_lbl.setText(("SOURCE:\n" + directory))

            # Open a file
            dirs = os.listdir(directory)

            # This would add all the files and directories to the list
            for file in dirs:
                isFile, isDir = check_if_file((self.source + file))
                if not isDir:
                    self.list_files.addItem(file)
                    self.files.append(file)
            self.add_log("Source set.")
            print (self.source)
                # print (file)

    def select_target(self):
        self.target = ""
        self.target_lbl.setText("TARGET: \n")

        directory = QFileDialog.getExistingDirectory(self)
        if directory:
            self.target = (directory + "/")
            self.target_lbl.setText(("TARGET: \n" + directory))
        self.add_log("Target set.")
        print (self.target)

    def update_file_list(self):
        self.list_files.clear()
        dirs = os.listdir(self.source[:-1])
        for file in dirs:
            isFile, isDir = check_if_file((self.source + file))
            if not isDir:
                self.list_files.addItem(file)
                self.files.append(file)

    def run_jobs(self):
        job_list = []
        if self.check:
            if self.source == "" or self.target == "":
                print("SAD")
                self.image_lbl.setPixmap(self.bad_pix)

            else:
                #print("RUN JOB")
                self.image_lbl.setPixmap(self.good_pix)
                for each in self.list_files.selectedItems():
                    print(each.text())
                    if each:
                        file_jobs = prepare_job(each.text())
                    for entry in file_jobs:
                        job_list.append(entry)
                execute_job(job_list)
            self.check = False
            self.update_file_list()
            self.image_lbl.setPixmap(self.neutral_pix)
        else:
            self.add_log("Check consistency before running job.")

    def check_consistency(self):
        # Locks selection and require new check if selection changes, only way to make sure files exists when moving.
        print("CHECK CONSISTENCY")
        if self.source and self.target:
            self.add_log("Source and target set.")
            # self.sourceSubStr = self.source.replace()
            self.image_lbl.setPixmap(self.good_pix)
            self.check = True
        else:
            self.image_lbl.setPixmap(self.bad_pix)
        # pass
        print(self.source, self.target)

    def add_log(self, message):
        t = time.strftime('%H:%M:%S')
        old_log = self.log.toPlainText()
        if (self.log_timestamp+3)<time.time():
            if old_log == "":
                self.log.setText("- " + str(time.strftime("%H:%M:%S -\n")) + message)
            else:
                #new_log = ("- " + str(time.strftime('%H:%M:%S -\n')) + message + "\n\n" + self.log.toPlainText())
                new_log = (self.log.toPlainText() + "\n\n" + "- " + str(time.strftime('%H:%M:%S -\n')) + message)
                self.log.setText(new_log)
            self.log_file.write("- " + str(time.strftime("%H:%M:%S -\n")) + message + "\n")
            self.log_timestamp = time.time()
        else:
            if old_log == "":
                self.log.setText(message)
            else:
                #new_log = (message + "\n" + self.log.toPlainText())
                new_log = (self.log.toPlainText() + "\n" + message)
                self.log.setText(new_log)
            self.log_file.write(message + "\n")
            self.log_timestamp = time.time()

    def clear_text(self):
        print ("log cleared")
        self.log.clear()


def check_if_file(path):
    isFile = (os.path.isfile(path))
    isDir = (os.path.isdir(path))
    return (isFile, isDir)


def prepare_job(file):
    job_list = []
    for entry in locations:
        fileStr = (file + ".")[:-1]

        # Dices up the path and puts a placeholder in place
        sub_source, sub_target = cut_location(entry)
        source_output = placeholder_biome_level(sub_source)
        target_output = placeholder_biome_level(sub_target)

        # Replaces the placeholder biome and level tag in the string with the real biome depending on the entry in locations. 
        source_output = REplace_string("tempBIOME", source_output, get_biome(entry)[0])
        target_output = REplace_string("tempBIOME", target_output, get_biome(entry)[0])
        source_output = REplace_string("tempLEVEL", source_output, get_level(entry)[0])
        target_output = REplace_string("tempLEVEL", target_output, get_level(entry)[0])

        # Change filename to correct biome and level.
        fileStr = placeholder_biome_level(fileStr)
        fileStr = REplace_string("tempBIOME", fileStr, get_biome(entry)[0])
        fileStr = REplace_string("tempLEVEL", fileStr, get_level(entry)[0])

        # Adds the data to the list of jobs to perform.
        if check_if_available((entry + source_output + fileStr)):
            print ((entry + source_output + fileStr))
            job_list.append(((entry + source_output), (entry + target_output), fileStr))

        # Check if consistency check is OK


    for entry in job_list:
        if not check_if_available((entry[0]+entry[2])):
            mover.add_log(('could not find "' + entry[2] + '" in folder, aborting job.'))
            return

    return job_list


def execute_job(job_list):
    for entry in job_list:
        move_file(entry[0], entry[1], entry[2])


def check_if_available(file):
    # Check if file in use by program or if locked in SVN
    f = file
    if os.path.exists(f):
        try:
            os.rename(f, f)
            print ('Access on file "' + f +'" is available!')
            #mover.add_log(('Access on file "' + f +'" is available.'))
            return True
        except OSError as e:
            print ('Access-error on file "' + f + '"! \n' + str(e))
            mover.add_log(('Access-error on file "' + f + '"! \n' + str(e)))
            return False
    print ('path to file "' + f + '" does not exist... ?')
    mover.add_log(('"' + f + '" does not exist. Skipping.'))
    pass


def mkdirnotex(filename):
    folder=os.path.dirname(filename)
    if not os.path.exists(folder):
        mover.add_log(('Folder "' + folder + '" does not exist. Creating.'))
        os.makedirs(folder)
        if os.path.exists(folder):
            mover.add_log(('"' + folder + '" created.'))


def move_file(source, target, file):
    mkdirnotex((target+file))
    os.rename((source + file), (target + file))
    print(file, "has been moved.")


def load_settings():
    # Load settings from INI file
    pass


def get_biome(string):
    if "forest" in string.lower():
        return ("FOREST", True)

    elif "mountain" in string.lower() or "mountains" in string.lower():
        return ("MOUNTAIN", True)

    elif "steppe" in string.lower():
        return ("STEPPE", True)

    elif "highland" in string.lower() or "highlands" in string.lower():
        return ("HIGHLAND", True)

    elif "swamp" in string.lower():
        return ("SWAMP", True)

    else:
        return ("", False)


def get_level(string):
    if "_green" in string.lower():
        return ("GREEN", True)

    elif "_red" in string.lower():
        return ("RED", True)

    elif "_dead" in string.lower():
        return ("DEAD", True)

    else:
        return ("", False)
        # return red, dead or green


def placeholder_biome_level(string):
    biomes = ["forest", "highland", "mountain", "swamp", "steppe"]
    for entry in biomes:
        string = REplace_string(entry, string, "tempBIOME")
        #if exit:
        #    break

    levels = ["red", "dead", "green"]
    for entry in levels:
        string = REplace_string(entry, string, "tempLEVEL")

    return string


def REplace_string(phrase, string, replaceWith):
    replaceWith = ("_"+ replaceWith + "_")
    phrase = ("_"+ phrase + "_")
    output = re.sub(phrase, replaceWith, string, flags=re.IGNORECASE)

    # reset words
    phrase = remove_first_last_letter(phrase)
    replaceWith = remove_first_last_letter(replaceWith)

    replaceWith = ("/"+ replaceWith + "_")
    phrase = ("/"+ phrase + "_")
    output = re.sub(phrase, replaceWith, output, flags=re.IGNORECASE)
    
    # reset words
    phrase = remove_first_last_letter(phrase)
    replaceWith = remove_first_last_letter(replaceWith)

    replaceWith = ("_"+ replaceWith + "/")
    phrase = ("_"+ phrase + "/")
    output = re.sub(phrase, replaceWith, output, flags=re.IGNORECASE)

    # reset words
    phrase = remove_first_last_letter(phrase)
    replaceWith = remove_first_last_letter(replaceWith)

    replaceWith = ("/"+ replaceWith + "/")
    phrase = ("/"+ phrase + "/")
    output = re.sub(phrase, replaceWith, output, flags=re.IGNORECASE)

    # reset words
    phrase = remove_first_last_letter(phrase)
    replaceWith = remove_first_last_letter(replaceWith)

    replaceWith = (replaceWith + "_")
    phrase = ("^"+ phrase + "_")
    output = re.sub(phrase, replaceWith, output, flags=re.IGNORECASE)

    # reset words
    phrase = remove_first_last_letter(phrase)
    replaceWith = replaceWith[:-1]

    replaceWith = ("/"+ replaceWith + "")
    phrase = ("/"+ phrase + "")
    output = re.sub(phrase, replaceWith, output, flags=re.IGNORECASE)

    # reset words
    phrase = phrase[1:]
    replaceWith = replaceWith[1:]

    replaceWith = ("_"+ replaceWith + "")
    phrase = ("_"+ phrase + "")
    output = re.sub(phrase, replaceWith, output, flags=re.IGNORECASE)

    return output

def remove_first_last_letter(word):
    word = word[:-1]
    word = word[1:]
    return word

def change_biome(location, sourceOrTarget):
    x = placeholder_biome_level(sourceOrTarget)
    y = placeholder_biome_level(locations[0])
    # Add input with biome in string and get output with other biome in same place. Use replace.
    output = x.replace(y, "")
    output = placeholder_biome_level(output)
    output = REplace_string("tempBIOME", output, get_biome(location)[0])
    output = REplace_string("tempLEVEL", output, get_level(location)[0])
    return output


def cut_location(location):

    source_output = change_biome(location, mover.source)
    target_output = change_biome(location, mover.target)
    return (source_output, target_output)


def get_locations(silent = True):
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)

    pathFR = os.path.normpath((application_path + os.sep + os.pardir) + os.sep + os.pardir + "\\client\\unity\\Assets\\Resources\\Prefabs\\ENV_PREFABS\\BIOMES\\FOREST")
    pathHL = os.path.normpath((application_path + os.sep + os.pardir) + os.sep + os.pardir + "\\client\\unity\\Assets\\Resources\\Prefabs\\ENV_PREFABS\\BIOMES\\HIGHLAND")
    pathMN = os.path.normpath((application_path + os.sep + os.pardir) + os.sep + os.pardir + "\\client\\unity\\Assets\\Resources\\Prefabs\\ENV_PREFABS\\BIOMES\\MOUNTAIN")
    pathST = os.path.normpath((application_path + os.sep + os.pardir) + os.sep + os.pardir + "\\client\\unity\\Assets\\Resources\\Prefabs\\ENV_PREFABS\\BIOMES\\STEPPE")
    pathSW = os.path.normpath((application_path + os.sep + os.pardir) + os.sep + os.pardir + "\\client\\unity\\Assets\\Resources\\Prefabs\\ENV_PREFABS\\BIOMES\\SWAMP")

    get_biome_subfolders(pathFR)
    get_biome_subfolders(pathHL)
    get_biome_subfolders(pathMN)
    get_biome_subfolders(pathST)
    get_biome_subfolders(pathSW)

    if not silent:
        mover.add_log("Folders found:")
    for entry in locations:
        mover.add_log(entry)
        if not silent:
            print (entry)


def get_biome_subfolders(path):
    for file in os.listdir(path):
        if os.path.isdir((path + "\\" + file)) and ("GREEN" in file or "RED" in file or "DEAD" in file):
            accepted = (path+"\\"+file).replace("\\", "/")
            locations.append(accepted)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mover = RenamerWindow()

    locations = []
    get_locations(False)
    
    biomesFolder = (os.path.normpath((os.getcwd() + os.sep + os.pardir) + os.sep + os.pardir + "\\client\\unity\\Assets\\Resources\\Prefabs\\ENV_PREFABS\\BIOMES\\"))
    biomesFolder = biomesFolder.replace("\\", "/") 
    print (biomesFolder)


    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    sys.exit(app.exec_())



