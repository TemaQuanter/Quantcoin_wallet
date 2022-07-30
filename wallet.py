from hash_calculater import get_hash
from keys_generator import get_keys
from cryptographer import get_signature, get_hash_from_signature
import blockchain_validator
from glob import glob
import ntplib
from quantcoin_node import QuantcoinNode
from random import randint
import socket
import time
import threading
import file_worker
import sys
from prime_number_generator import get_random_private_key

from mint_nft import nft_minter

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedWidth(1000)
        MainWindow.setFixedHeight(600)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.tabWidget.setObjectName("tabWidget")
        self.balance = QtWidgets.QWidget()
        self.balance.setObjectName("balance")
        self.balance_label = QtWidgets.QLabel(self.balance)
        self.balance_label.setGeometry(QtCore.QRect(0, 0, 1001, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.balance_label.setFont(font)
        self.balance_label.setStyleSheet("background-color: rgb(241, 241, 241)")
        self.balance_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.balance_label.setObjectName("balance_label")
        self.nfts_textfield = QtWidgets.QTextBrowser(self.balance)
        self.nfts_textfield.setGeometry(QtCore.QRect(10, 190, 971, 241))
        self.nfts_textfield.setObjectName("nfts_textfield")
        self.nfts_label = QtWidgets.QLabel(self.balance)
        self.nfts_label.setGeometry(QtCore.QRect(0, 100, 1001, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.nfts_label.setFont(font)
        self.nfts_label.setAlignment(QtCore.Qt.AlignCenter)
        self.nfts_label.setObjectName("nfts_label")
        self.update_button = QtWidgets.QPushButton(self.balance)
        self.update_button.setGeometry(QtCore.QRect(350, 450, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.update_button.setFont(font)
        self.update_button.setObjectName("update_button")
        self.tabWidget.addTab(self.balance, "")
        self.send = QtWidgets.QWidget()
        self.send.setObjectName("send")
        self.formLayoutWidget = QtWidgets.QWidget(self.send)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 180, 891, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.public_key_label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.public_key_label_2.setFont(font)
        self.public_key_label_2.setObjectName("public_key_label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.public_key_label_2)
        self.public_key_textfield_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.public_key_textfield_2.sizePolicy().hasHeightForWidth())
        self.public_key_textfield_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.public_key_textfield_2.setFont(font)
        self.public_key_textfield_2.setObjectName("public_key_textfield_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.public_key_textfield_2)
        self.qtc_or_nft_to_send_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.qtc_or_nft_to_send_label.setFont(font)
        self.qtc_or_nft_to_send_label.setObjectName("qtc_or_nft_to_send_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.qtc_or_nft_to_send_label)
        self.fee_label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fee_label_2.setFont(font)
        self.fee_label_2.setObjectName("fee_label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.fee_label_2)
        self.fee_textfield_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fee_textfield_2.sizePolicy().hasHeightForWidth())
        self.fee_textfield_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fee_textfield_2.setFont(font)
        self.fee_textfield_2.setObjectName("fee_textfield_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.fee_textfield_2)
        self.qtc_or_nft_to_send_textfield = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qtc_or_nft_to_send_textfield.sizePolicy().hasHeightForWidth())
        self.qtc_or_nft_to_send_textfield.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.qtc_or_nft_to_send_textfield.setFont(font)
        self.qtc_or_nft_to_send_textfield.setObjectName("qtc_or_nft_to_send_textfield")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.qtc_or_nft_to_send_textfield)
        self.send_form_label = QtWidgets.QLabel(self.send)
        self.send_form_label.setGeometry(QtCore.QRect(50, 40, 891, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.send_form_label.setFont(font)
        self.send_form_label.setAlignment(QtCore.Qt.AlignCenter)
        self.send_form_label.setObjectName("send_form_label")
        self.send_button = QtWidgets.QPushButton(self.send)
        self.send_button.setGeometry(QtCore.QRect(350, 390, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.send_button.setFont(font)
        self.send_button.setObjectName("send_button")
        self.tabWidget.addTab(self.send, "")
        self.mint_nft = QtWidgets.QWidget()
        self.mint_nft.setObjectName("mint_nft")
        self.mint_nft_form_label = QtWidgets.QLabel(self.mint_nft)
        self.mint_nft_form_label.setGeometry(QtCore.QRect(50, 40, 891, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mint_nft_form_label.setFont(font)
        self.mint_nft_form_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mint_nft_form_label.setObjectName("mint_nft_form_label")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.mint_nft)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(50, 180, 891, 138))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.nft_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nft_label.setFont(font)
        self.nft_label.setObjectName("nft_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nft_label)
        self.nft_textfield = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nft_textfield.setFont(font)
        self.nft_textfield.setObjectName("nft_textfield")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nft_textfield)
        self.choose_file_button = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.choose_file_button.setObjectName("choose_file_button")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.choose_file_button)
        self.fee_textfield = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.fee_textfield.setObjectName("fee_textfield")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.fee_textfield)
        self.fee_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.fee_label.setObjectName("fee_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.fee_label)
        self.mint_nft_button = QtWidgets.QPushButton(self.mint_nft)
        self.mint_nft_button.setGeometry(QtCore.QRect(350, 390, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mint_nft_button.setFont(font)
        self.mint_nft_button.setObjectName("mint_nft_button")
        self.tabWidget.addTab(self.mint_nft, "")
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.public_key_textfield = QtWidgets.QTextBrowser(self.settings)
        self.public_key_textfield.setGeometry(QtCore.QRect(170, 20, 801, 71))
        self.public_key_textfield.setObjectName("public_key_textfield")
        self.public_key_label = QtWidgets.QLabel(self.settings)
        self.public_key_label.setGeometry(QtCore.QRect(10, 20, 151, 71))
        self.public_key_label.setAlignment(QtCore.Qt.AlignCenter)
        self.public_key_label.setObjectName("public_key_label")
        self.save_button = QtWidgets.QPushButton(self.settings)
        self.save_button.setGeometry(QtCore.QRect(320, 450, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.private_key_textfield = QtWidgets.QTextEdit(self.settings)
        self.private_key_textfield.setGeometry(QtCore.QRect(170, 140, 801, 71))
        self.private_key_textfield.setObjectName("private_key_textfield")
        self.private_key_label = QtWidgets.QLabel(self.settings)
        self.private_key_label.setGeometry(QtCore.QRect(10, 140, 151, 71))
        self.private_key_label.setAlignment(QtCore.Qt.AlignCenter)
        self.private_key_label.setObjectName("private_key_label")
        self.show_private_key_checkbox = QtWidgets.QCheckBox(self.settings)
        self.show_private_key_checkbox.setGeometry(QtCore.QRect(170, 230, 181, 20))
        self.show_private_key_checkbox.setObjectName("show_private_key_checkbox")
        self.hard_update_button = QtWidgets.QPushButton(self.settings)
        self.hard_update_button.setGeometry(QtCore.QRect(170, 280, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hard_update_button.setFont(font)
        self.hard_update_button.setObjectName("hard_update_button")
        self.warning_hard_update_label = QtWidgets.QLabel(self.settings)
        self.warning_hard_update_label.setGeometry(QtCore.QRect(500, 285, 471, 61))
        self.warning_hard_update_label.setWordWrap(True)
        self.warning_hard_update_label.setObjectName("warning_hard_update_label")
        self.tabWidget.addTab(self.settings, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quantcoin wallet"))
        self.balance_label.setText(_translate("MainWindow", "0 QTC"))
        self.nfts_textfield.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.nfts_label.setText(_translate("MainWindow", "NFTs"))
        self.update_button.setText(_translate("MainWindow", "Update"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.balance), _translate("MainWindow", "Balance"))
        self.public_key_label_2.setText(_translate("MainWindow", "Public key"))
        self.qtc_or_nft_to_send_label.setText(_translate("MainWindow", "QTC or NFT to send"))
        self.fee_label_2.setText(_translate("MainWindow", "Fee"))
        self.send_form_label.setText(_translate("MainWindow", " Send form"))
        self.send_button.setText(_translate("MainWindow", "Send"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.send), _translate("MainWindow", "Send"))
        self.mint_nft_form_label.setText(_translate("MainWindow", "Mint NFT form"))
        self.nft_label.setText(_translate("MainWindow", "NFT"))
        self.choose_file_button.setText(_translate("MainWindow", "Choose file"))
        self.fee_label.setText(_translate("MainWindow", "Fee"))
        self.mint_nft_button.setText(_translate("MainWindow", "Mint NFT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mint_nft), _translate("MainWindow", "Mint NFT"))
        self.public_key_textfield.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.public_key_label.setText(_translate("MainWindow", "Public key"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.private_key_label.setText(_translate("MainWindow", "Private key"))
        self.show_private_key_checkbox.setText(_translate("MainWindow", "Show private key"))
        self.hard_update_button.setText(_translate("MainWindow", "Hard update"))
        self.warning_hard_update_label.setText(_translate("MainWindow", "WARNING: Hard update will re-download all the blocks in the blockchain! It may take a lot of time!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), _translate("MainWindow", "Settings"))


        self.balance_label.setText(f'{balance} QTC ')
        nfts_data = ''
        for nft in nfts:
            nfts_data += hex(nft)[2:] + '\n'
        self.nfts_textfield.setText(nfts_data)

        self.public_key_textfield.setText(public_key)
        self.show_private_key_checkbox.setChecked(False)

        self.private_key_textfield.setText('WARNING: The disclosure of the private key may lead to the loss of all QTC and the NFTs!!!')
        self.private_key_textfield.setDisabled(True)

        self.add_functions()


    def add_functions(self):
        self.hard_update_button.clicked.connect(lambda: self.hard_update_button_function())
        self.update_button.clicked.connect(lambda: self.update_button_function())
        self.send_button.clicked.connect(lambda: self.send_button_function())
        self.mint_nft_button.clicked.connect(lambda: self.mint_nft_button_function())
        self.show_private_key_checkbox.stateChanged.connect(self.show_private_key_checkbox_function)
        self.save_button.clicked.connect(lambda: self.save_button_function())
        self.choose_file_button.clicked.connect(lambda: self.choose_file_button_function())


    # Application functions
    def update_button_function(self):
        interactor('update')
        self.balance_label.setText(f'{balance} QTC ')
        nfts_data = ''
        for nft in nfts:
            nfts_data += hex(nft)[2:] + '\n'
        self.nfts_textfield.setText(nfts_data)


    def hard_update_button_function(self):
        message_box = QMessageBox()
        message_box.setWindowTitle('Confirmation')
        message_box.setText('Are you sure you want to do hard update?')
        message_box.setInformativeText('WARNING: All the blocks will be re-downloaded, it may take a lot of time!!!')
        message_box.setIcon(QMessageBox.Warning)
        message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message_box.buttonClicked.connect(self.hard_update_button_pop_up)
        message_box.exec_()


    def hard_update_button_pop_up(self, button):
        if button.text() == 'OK':
            interactor('hard_update')
            self.balance_label.setText(f'{balance} QTC ')
            nfts_data = ''
            for nft in nfts:
                nfts_data += hex(nft)[2:] + '\n'
            self.nfts_textfield.setText(nfts_data)
            self.public_key_textfield.setText(public_key)


    def mint_nft_button_function(self):
        message_box = QMessageBox()
        message_box.setWindowTitle('Confirmation')
        message_box.setText('Are you sure you want to mint this NFT?')
        message_box.setInformativeText('WARNING: It will be impossible to cancel it after confirmation!')
        message_box.setIcon(QMessageBox.Warning)
        message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message_box.buttonClicked.connect(self.mint_nft_button_pop_up)
        message_box.exec_()


    def send_button_function(self):
        message_box = QMessageBox()
        message_box.setWindowTitle('Confirmation')
        message_box.setText('Are you sure you want to confirm the transaction?')
        message_box.setInformativeText('WARNING: It will be impossible to cancel it after confirmation!')
        message_box.setIcon(QMessageBox.Warning)
        message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message_box.buttonClicked.connect(self.send_button_pop_up)
        message_box.exec_()


    def send_button_pop_up(self, button):
        if button.text() == 'OK':
            public_key_recipient = self.public_key_textfield_2.text()
            qtc_or_nft_to_send = self.qtc_or_nft_to_send_textfield.text()
            fee = self.fee_textfield_2.text()
            transaction = interactor(f'send {public_key_recipient} {qtc_or_nft_to_send} {fee}')
            signed_transaction = interactor(f'sign {transaction}')
            if interactor(f'broadcast {signed_transaction}'):
                self.public_key_textfield_2.setText('')
                self.qtc_or_nft_to_send_textfield.setText('')
                self.fee_textfield_2.setText('')
                self.balance_label.setText(f'{balance} QTC ')
                nfts_data = ''
                for nft in nfts:
                    nfts_data += hex(nft)[2:] + '\n'
                self.nfts_textfield.setText(nfts_data)


    def mint_nft_button_pop_up(self, button):
        if button.text() == 'OK':
            nft = self.nft_textfield.text()
            fee = self.fee_textfield.text()
            transaction = interactor(f'createNFT {nft} {fee}')
            signed_transaction = interactor(f'sign {transaction}')
            if interactor(f'broadcast {signed_transaction}'):
                self.nft_textfield.setText('')
                self.fee_textfield.setText('')
                self.balance_label.setText(f'{balance} QTC ')


    def show_private_key_checkbox_function(self, int):
        global temporary_p_q
        if self.show_private_key_checkbox.isChecked():
            self.private_key_textfield.setFontPointSize(12)
            self.private_key_textfield.setDisabled(False)
            self.private_key_textfield.setText(temporary_p_q)
        else:
            temporary_p_q = self.private_key_textfield.toPlainText()
            self.private_key_textfield.setFontPointSize(12)
            self.private_key_textfield.setText('WARNING: The disclosure of the private key may lead to the loss of all QTC and the NFTs!!!')
            self.private_key_textfield.setDisabled(True)


    def save_button_function(self):
        global p
        global q
        global temporary_p_q
        if self.private_key_textfield.toPlainText() != 'WARNING: The disclosure of the private key may lead to the loss of all QTC and the NFTs!!!':
            temporary_p_q = self.private_key_textfield.toPlainText()
        try:
            p, q = map(int, temporary_p_q.split('\n'))
            with open('seed.txt', 'w') as f:
                f.write(f'{p}\n{q}')
            interactor('update')
            self.balance_label.setText(f'{balance} QTC ')
            nfts_data = ''
            for nft in nfts:
                nfts_data += hex(nft)[2:] + '\n'
            self.nfts_textfield.setText(nfts_data)
            self.public_key_textfield.setText(public_key)
        except Exception as e:
            message_box = QMessageBox()
            message_box.setWindowTitle('Wrong key')
            message_box.setText(
                'The key you need to enter consists of 2 parts: the first prime number and the second prime number')
            message_box.setInformativeText('Please, make sure that your key complies with the description above')
            message_box.setIcon(QMessageBox.Warning)
            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.exec_()


    def choose_file_button_function(self):
        file_name = QFileDialog.getOpenFileName()[0]
        if file_name != '':
            print('Please, wait until NFT is calculated')
            print('This may take some time')
            print('Hint: the more is the size of the file, the longer will be the process of NFT calculation')
            try:
                self.nft_textfield.setText(nft_minter(file_name))
            except FileNotFoundError:
                pass


class QuantcoinMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(QuantcoinMainWindow, self).__init__()


    def closeEvent(self, event):
        global node
        print('Exiting, please, wait...')
        node.stop()
        node.join()



ntp_difference = 0


def update_ntp():
    global ntp_difference
    try:
        ntp_difference = int(ntplib.NTPClient().request('pool.ntp.org').tx_time) - time.time()
    except ntplib.NTPException:
        return False
    except socket.gaierror:
        return False
    return True


require_connection = True

exit_program = False

show_private_key = False

start_time = time.time()
while not update_ntp():
    print(f'\rTrying to get UTC time from the servers for {int(time.time() - start_time)}s', end='')
    print('\r', end='')
    time.sleep(1)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", randint(30000, 61000)))

host = s.getsockname()[0]
# port = 51132
port = 51112

s.close()

print('Starting a new node at the following address')
print(f'host: {host}\nport: {port}')

file_worker_thread = threading.Thread(target=file_worker.task_processor, daemon=True)
file_worker_thread.start()

node = QuantcoinNode(host, port, require_connection)
node.ntp_difference = ntp_difference

public_key, private_key = '', ''
p, q = 0, 0

temporary_p_q = ''

balance = 0
transaction_number = 1
nfts = set()
all_nfts = set()


def active_nodes_checker():
    global node
    while True:
        update_ntp()
        node.check_active_nodes()
        time.sleep(60)
        node.update_active_nodes()
        time.sleep(60)


active_nodes_checker_thread = threading.Thread(target=active_nodes_checker, daemon=True)
active_nodes_checker_thread.start()


def establish_connection():
    global require_connection
    global node

    if not require_connection:
        return

    if node.connected_node == None:
        node.connect_with_new_node(True)
        while node.connected_node == None:
            time.sleep(0.2)


def establish_new_connection():
    global require_connection
    global node

    connected_node = node.connected_node

    node.disconnect_with_node(connected_node)
    try:
        node.nodes_list.remove([connected_node.host, int(connected_node.port)])
    except ValueError:
        pass
    node.connected_node = None

    file_worker.put_json('nodes_list.json', {'nodes': node.nodes_list})

    if not require_connection:
        return

    if node.connected_node == None:
        node.connect_with_new_node(True)
        while node.connected_node == None:
            time.sleep(0.2)


def is_valid_transaction(transaction, public_keys):
    split_transaction = transaction.split(';')
    if len(split_transaction) != 6:
        # print(1)
        return False
    transaction_number = None
    try:
        int(split_transaction[3])
        transaction_number = int(split_transaction[4])
        if blockchain_validator.is_nft(split_transaction[2]):
            int(split_transaction[2], 16)
        else:
            int(split_transaction[2])
    except:
        # print(2)
        return False
    for el in split_transaction:
        if str(el).count('.') + str(el).count(',') != 0:
            # print(3)
            return False
    if str(split_transaction[3]).count('e') != 0:
        # print(4)
        return False
    if str(split_transaction[4]).count('e') != 0:
        # print(5)
        return False
    public_key = None
    if blockchain_validator.is_nft(split_transaction[2]) and split_transaction[0] == '0x0000000000000000':
        public_key = split_transaction[1]
        try:
            if public_keys[public_key]['balance'] - int(split_transaction[3]) < 0:
                # print(6)
                return False
            if int(split_transaction[2], 16) in all_nfts:
                return False
        except Exception as e:
            return False
    else:
        public_key = split_transaction[0]
        try:
            if transaction_number < public_keys[public_key]['transaction_number']:
                # print(7)
                return False
        except Exception as e:
            return False
        if blockchain_validator.is_nft(split_transaction[2]):
            try:
                if public_keys[public_key]['balance'] - int(split_transaction[3]) < 0:
                    # print(8)
                    return False
                if not (int(split_transaction[2], 16) in public_keys[public_key]['nfts']):
                    return False
            except Exception as e:
                return False
        elif str(split_transaction[2]).count('e') != 0:
            # print(9)
            return False
        else:
            if public_keys[public_key]['balance'] - int(split_transaction[2]) < 0:
                return False
            if int(split_transaction[2]) - int(split_transaction[3]) <= 0:
                return False
    if int(split_transaction[3]) < 1:
        return False
    signature = split_transaction[-1]
    transaction = ';'.join(split_transaction[:-1])
    transaction_hash = get_hash(transaction)
    if hex(get_hash_from_signature(signature, public_key))[2:] == transaction_hash:
        return True
    # print(10)
    return False


def remove_mined_transactions():
    target_number = -2
    all_files = glob('public_keys_data_final_block_*.json')
    for file in all_files:
        target_number = max(target_number, int(file.strip('public_keys_data_final_block_.json')))
    if target_number == -2:
        return
    data = file_worker.get_json(f'public_keys_data_final_block_{target_number}.json')
    data_set = set(data['st'])
    all_transactions = file_worker.get_json('Blockchain/pending_transactions.json')['transactions']
    potential_transactions = []
    for transaction in all_transactions:
        if (not (int(get_hash(transaction), 16) in data_set)) and is_valid_transaction(transaction, data):
            potential_transactions.append(transaction)
    file_worker.put_json('Blockchain/pending_transactions.json', {'transactions': potential_transactions})


def check_blockchain():
    file_array = set([el.replace('\\', '/').lstrip('Blockchain/').rstrip('.json') for el in glob('Blockchain/*.json')])
    for file_name in file_array:
        if (not file_name.isnumeric()) and (file_name != 'pending_transactions'):
            try:
                file_worker.remove_file(f'Blockchain/{file_name}.json')
            except Exception as e:
                pass
    for i in range(len(file_array) - 1):
        if str(i) in file_array:
            file_array.discard(str(i))
    file_array.discard('pending_transactions')
    for file_name in file_array:
        try:
            file_worker.remove_file(f'Blockchain/{file_name}.json')
        except Exception as e:
            pass
    current_block = len(glob('Blockchain/*.json')) - 2
    while blockchain_validator.blockchain_validator() != 'OK':
        try:
            file_worker.remove_file(f'Blockchain/{current_block}.json')
        except FileNotFoundError:
            pass
        current_block -= 1


def download_blocks(starting_block):
    current_block = starting_block
    node.have_all_blocks = False
    while not node.have_all_blocks:
        print(f'\rDownloading block: {current_block}', end='')
        node.got_block = False
        node.send_to_node(node.connected_node, {'header': 'request_block', 'data': current_block})
        while not node.got_block:
            if node.connected_node == None:
                establish_connection()
                node.send_to_node(node.connected_node, {'header': 'request_block', 'data': current_block})
            time.sleep(0.01)
        if current_block % 5:
            result = blockchain_validator.blockchain_validator()
            if result != 'OK':
                node.have_all_blocks = True
                while not (blockchain_validator.blockchain_validator() == 'OK'):
                    file_worker.remove_file(f'Blockchain/{current_block}.json')
                    current_block -= 1
                establish_new_connection()
        current_block += 1


def download_pending_block():
    establish_connection()
    node.got_block = False
    node.send_to_node(node.connected_node, {'header': 'request_block', 'data': 'pending_block'})
    while not node.got_block:
        if node.connected_node == None:
            establish_connection()
            node.send_to_node(node.connected_node, {'header': 'request_block', 'data': 'pending_block'})
        time.sleep(0.01)


def download_pending_transactions():
    establish_connection()
    node.got_block = False
    node.send_to_node(node.connected_node, {'header': 'request_block', 'data': 'pending_transactions'})
    while not node.got_block:
        if node.connected_node == None:
            establish_connection()
            node.send_to_node(node.connected_node, {'header': 'request_block', 'data': 'pending_transactions'})
        time.sleep(0.01)


def update_seed():
    global public_key
    global private_key
    global p
    global q
    global temporary_p_q

    need_new_private_key = False

    with open('seed.txt') as file:
        try:
            p, q = map(int, file.readlines())
        except Exception as e:
            need_new_private_key = True

    if need_new_private_key:
        print('Creating a new account')
        print('WARNING: This is a hard computational process, so this may take a lot of CPU')
        print('WARNING: This might also take several minutes (usually not more than 5)')
        print('We really care about your security, that is why we do our best to compute the most trustworthy account possible')
        p, q = get_random_private_key()
        with open('seed.txt', 'w') as file:
            file.write(f'{p}\n{q}')

    temporary_p_q = f'{p}\n{q}'
    private_key, public_key = get_keys(p, q)



def update_wallet(hard=False):
    global balance
    global transaction_number
    global nfts
    global all_nfts

    update_seed()

    next_public_keys_data_final_block = -1

    if hard:
        file_arr = glob('public_keys_data_final_block_*.json')
        for file_name in file_arr:
            file_worker.remove_file(file_name)
        if require_connection:
            print('Started downloading all blocks...')
            download_blocks(0)
            print('\nFinished downloading all blocks!')
        check_blockchain()
        next_public_keys_data_final_block = int(glob('public_keys_data_final_block_*.json')[0].strip('public_keys_data_final_block_.json'))
    else:
        check_blockchain()
        file_arr = glob('public_keys_data_final_block_*.json')
        for file_name in file_arr:
            next_public_keys_data_final_block = max(next_public_keys_data_final_block, int(file_name.strip('public_keys_data_final_block_.json')))
        for file_name in file_arr:
            if file_name.strip('public_keys_data_final_block_.json') != str(next_public_keys_data_final_block):
                file_worker.remove_file(file_name)
        if require_connection:
            print('Started downloading new blocks...')
            download_blocks(next_public_keys_data_final_block + 1)
            print('\nFinished downloading new blocks!')
        check_blockchain()
        file_arr = glob('public_keys_data_final_block_*.json')
        for file_name in file_arr:
            next_public_keys_data_final_block = max(next_public_keys_data_final_block, int(file_name.strip('public_keys_data_final_block_.json')))
        for file_name in file_arr:
            if file_name.strip('public_keys_data_final_block_.json') != str(next_public_keys_data_final_block):
                file_worker.remove_file(file_name)

    public_keys = file_worker.get_json(f'public_keys_data_final_block_{next_public_keys_data_final_block}.json')

    # try:
    #     with open(f'public_keys_data_final_block_{next_public_keys_data_final_block}.json') as file:
    #         public_keys = json.load(file)
    # except FileNotFoundError:
    #     pass

    for key in public_keys.keys():
        if key != 'st':
            for nft in public_keys[key]['nfts']:
                all_nfts.add(nft)

    if public_key in public_keys.keys():
        balance = public_keys[public_key]['balance']
        transaction_number = public_keys[public_key]['transaction_number']
        nfts = set(public_keys[public_key]['nfts'])
    else:
        balance = 0
        transaction_number = 1
        nfts = set()


def load_pending():
    global balance
    global transaction_number
    if require_connection:
        print('Downloading pending transactions...')
        download_pending_transactions()
        print('Finished downloading pending transactions!')
    remove_mined_transactions()
    data = file_worker.get_json('Blockchain/pending_transactions.json')
    for line in data['transactions']:
        if not blockchain_validator.is_valid_transaction(line.strip()):
            continue
        line = line.strip().split(';')
        if line[0] == public_key:
            transaction_number = max(transaction_number, int(line[-2]) + 1)
            if blockchain_validator.is_nft(line[2]):
                nfts.discard(int(line[2], 16))
                balance -= int(line[3])
            else:
                balance -= int(line[2])
        if blockchain_validator.is_nft(line[2]) and (line[0] == '0x0000000000000000'):
            balance -= int(line[3])


def interactor(command):
    global balance
    global transaction_number
    global nfts
    global all_nfts
    global node
    global exit_program
    global show_private_key

    # print()
    try:
        command = command.split()
        # print()
        if command == []:
            return
        elif command == ['connections']:
            node.print_connections()
        elif command == ['exit']:
            print('Exiting, please, wait...')
            node.stop()
            node.join()
            exit_program = True
            exit(0)
        elif command == ['update']:
            establish_connection()
            update_wallet()
            load_pending()
        elif command == ['hard_update']:
            establish_connection()
            balance = 0
            transaction_number = 1
            nfts = set()
            all_nfts = set()
            update_wallet(hard=True)
            load_pending()
        elif command == ['show_private_key']:
            show_private_key = True
            print('Private key will be shown when "info" command is entered')
            print('Enter "hide_private_key" to hide a private key')
            print('WARNING: The disclosure of it to anyone may cause the loss of all money and NFTs!!!')
        elif command == ['hide_private_key']:
            show_private_key = False
            print('Private key is hidden')
        elif command == ['info']:
            print('The node is opened at the following address:')
            print(f'host: {host}')
            print(f'port: {port}')
            print('\n\n')
            print('Public key:')
            print(public_key)
            print('\n\n')
            print('Private key:')
            if show_private_key:
                print(private_key)
            else:
                print('Hidden')
                print('To show a private key enter "show_private_key"')
                print('WARNING: The disclosure of it to anyone may cause the loss of all money and NFTs!!!')
            print('\n\n')
            print('Balance:')
            print(str(balance) + ' QTC')
            print('\n\n')
            print('NFTs:')
            for nft in nfts:
                print(hex(nft)[2:])
            print('\n\n')
            print('Current transaction number:')
            print(transaction_number)
        elif command == ['balance']:
            print('Balance:')
            print(str(balance) + ' QTC')
        elif command[0] == 'createNFT':
            if not blockchain_validator.is_nft(command[1]):
                print('Reject\nIncorrect format')
            elif int(command[1], 16) in all_nfts:
                print('Reject\nThis particular NFT already exists')
            elif int(command[2]) > balance:
                print('Reject\nYou do not have enough coins for Miner\'s fee')
            else:
                transaction = '0x0000000000000000' + ';' + public_key + ';' + ';'.join(command[1:]) + ';' + '0'
                print('Unsigned transaction:')
                print(transaction)
                return transaction
        elif command[0] == 'send':
            if blockchain_validator.is_nft(command[2]) and (not (int(command[2], 16) in nfts)):
                print('Reject\nYou do not have this particular NFT')
            elif (not blockchain_validator.is_nft(command[2])) and int(command[2]) <= 0:
                print('Reject\nCannot send negative or zero number of coins')
            elif int(command[3]) < 0:
                print('Reject\nMiner\'s fee cannot be negative')
            elif (not blockchain_validator.is_nft(command[2])) and (int(command[2]) <= int(command[3])):
                print('Reject\nMiner\'s fee cannot be greater than the number of coins you send or equal to it')
            elif blockchain_validator.is_nft(command[2]) and (int(command[3]) > balance):
                print('Reject\nMiner\'s fee is greater than your current balance')
            else:
                transaction = public_key + ';' + ';'.join(command[1:]) + ';' + str(transaction_number)
                print('Unsigned transaction:')
                print(transaction)
                return transaction
        elif command[0] == 'sign':
            unsigned_transaction = command[1]
            signed_transaction = unsigned_transaction + ';' + hex(
                get_signature(get_hash(unsigned_transaction), private_key, public_key))[2:]
            print('Signed transaction:')
            print(signed_transaction)
            return signed_transaction
        elif command[0] == 'broadcast':
            establish_connection()
            transaction_number += 1
            split_broadcast = command[1].split(';')
            transaction_content = split_broadcast[2]
            sender = split_broadcast[0]
            miner_fee = int(split_broadcast[3])
            if blockchain_validator.is_nft(transaction_content):
                if not (int(transaction_content, 16) in nfts) and (sender != '0x0000000000000000'):
                    print('Reject\nYou do not have this particular NFT')
                else:
                    balance -= miner_fee
                    nfts.discard(int(transaction_content, 16))
                    if balance < 0:
                        print('Reject\nYou do not have enough coins for Miner\'s fee')
                        balance += miner_fee
                        transaction_number -= 1
                    else:
                        data = file_worker.get_json('Blockchain/pending_transactions.json')
                        # with open('Blockchain/pending_transactions.json', 'r') as file:
                        #     data = json.load(file)
                        data['transactions'].append(command[1])
                        file_worker.put_json('Blockchain/pending_transactions.json', data)
                        data = dict()
                        data['transaction'] = command[1]
                        # with open('Blockchain/pending_transactions.json', 'w') as file:
                        #     json.dump(data, file)
                        data['header'] = 'pending_transaction'
                        node.send_to_nodes(data)
                        print('The transaction is broadcast successfully!')
                        return True
            else:
                balance -= int(transaction_content)
                if balance < 0:
                    print('Reject\nYou do not have enough coins')
                    balance += int(transaction_content)
                    transaction_number -= 1
                else:
                    data = file_worker.get_json('Blockchain/pending_transactions.json')
                    # with open('Blockchain/pending_transactions.json', 'r') as file:
                    #     data = json.load(file)
                    data['transactions'].append(command[1])
                    file_worker.put_json('Blockchain/pending_transactions.json', data)
                    data = dict()
                    data['transaction'] = command[1]
                    # with open('Blockchain/pending_transactions.json', 'w') as file:
                    #     json.dump(data, file)
                    data['header'] = 'pending_transaction'
                    node.send_to_nodes(data)
                    print('The transaction is broadcast successfully!')
                    return True
    except IndexError:
        print('The format of the command is incorrect\nPlease, try again')
    except ValueError:
        print('The format of the command is incorrect\nPlease, try again')
    except Exception as e:
        if str(e) == '0':
            exit(0)
        print('Error:')
        print(e)
        print('Please, contact support to solve the problem')
    except BaseException as e:
        if str(e) == '0':
            exit(0)
        print('Error:')
        print(e)
        print('Please, contact support to solve the problem')
    return False


if __name__ == '__main__':
    establish_connection()
    update_wallet()
    load_pending()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QuantcoinMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    # while True:
    #     try:
    #         interactor()
    #         update_ntp()
    #     except IndexError:
    #         print('The format of the command is incorrect\nPlease, try again')
    #     except ValueError:
    #         print('The format of the command is incorrect\nPlease, try again')
    #     except Exception as e:
    #         if str(e) == '0':
    #             exit(0)
    #         print('Error:')
    #         print(e)
    #         print('Please, contact support to solve the problem')
    #     except BaseException as e:
    #         if str(e) == '0':
    #             exit(0)
    #         print('Error:')
    #         print(e)
    #         print('Please, contact support to solve the problem')


