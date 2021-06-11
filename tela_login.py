from PyQt5 import QtCore, QtGui, uic,QtWidgets
import sys
import sqlite3
import random
import string

global id_carteira
global nome_usuario


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(570, 546)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 50, 531, 411))
        self.widget.setStyleSheet("background-color: rgb(29, 92, 132);\n"
"border-radius:20px;")
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 260, 311, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(62, 62, 62);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 155, 255);\n"
"padding-bottom:7px")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 220, 311, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(62, 62, 62);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 155, 255);\n"
"padding-bottom:7px")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.loginButton = QtWidgets.QPushButton(self.widget)
        self.loginButton.setGeometry(QtCore.QRect(110, 320, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton#loginButton{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#loginButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(66, 199, 255, 100), stop:1 rgba(255, 255, 255, 100));\n"
"}\n"
"\n"
"QPushButton#loginButton{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"}\n"
"")
        self.loginButton.setObjectName("loginButton")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(220, 100, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: 0")
        self.label.setObjectName("label")
        self.msg_label = QtWidgets.QLabel(self.widget)
        self.msg_label.setGeometry(QtCore.QRect(120, 290, 281, 16))
        self.msg_label.setText("")
        self.msg_label.setObjectName("msg_label")
        self.cadastrarButton = QtWidgets.QPushButton(self.widget)
        self.cadastrarButton.setGeometry(QtCore.QRect(280, 320, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cadastrarButton.setFont(font)
        self.cadastrarButton.setStyleSheet("\n"
"QPushButton#cadastrarButton{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#cadastrarButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(66, 199, 255, 100), stop:1 rgba(255, 255, 255, 100));\n"
"}\n"
"\n"
"QPushButton#cadastrarButton{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"}\n"
"")
        self.cadastrarButton.setObjectName("cadastrarButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Digite a senha"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Usuario"))
        self.loginButton.setText(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", ""))
        self.cadastrarButton.setText(_translate("Dialog", "Cadastrar"))
def conectar_banco():
    banco = sqlite3.connect('banco_stonks.db')
    cursor = banco.cursor()
    return cursor

def call_tela_main():
    tela_login.msg_label.setText("")
    nome_usuario = tela_login.lineEdit_2.text()
    senha = tela_login.lineEdit.text()
    banco = sqlite3.connect('banco_stonks.db')
    cursor = banco.cursor()

def catch_id():
    banco = sqlite3.connect('banco_stonks.db')
    cursor = banco.cursor()
    nome_usuario = tela_login.lineEdit_2.text()
    cursor.execute("SELECT id_carteira FROM cadastro WHERE login=?", (nome_usuario,))
    id_carteira = str(cursor.fetchone()[0])
    #print(id_carteira)
    return id_carteira

def catch_idUsuario():
    banco = sqlite3.connect('banco_stonks.db')
    cursor = banco.cursor()
    nome_usuario = tela_login.lineEdit_2.text()
    cursor.execute("SELECT id_usuario FROM cadastro WHERE login=?", (nome_usuario,))
    usuario = str(cursor.fetchone()[0])
    #print(id_carteira)
    return usuario

def catch_senha():
    banco = sqlite3.connect('banco_stonks.db')
    cursor = banco.cursor()
    nome_usuario = tela_login.lineEdit_2.text()
    cursor.execute("SELECT senha FROM cadastro WHERE login=?", (nome_usuario,))
    id_senha = str(cursor.fetchone()[0])
    return id_senha

def login():
    nome_usuario = tela_login.lineEdit_2.text()
    senha = tela_login.lineEdit.text()
    banco = sqlite3.connect('banco_stonks.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM cadastro where login=? AND senha=?", (nome_usuario, senha))
    row=cursor.fetchone()
    if row:
        tela_login.msg_label.setText("Dados de login corretos!")
        catch_id()
        tela_main.show()
        tela_login.close()
    else:
        tela_login.msg_label.setText("Dados de login incorretos!")

def logout():

    tela_login.show()

chavepix = "abc123"
def gerar_chavepix(size=20, chars=string.ascii_uppercase + string.digits):
 return ''.join(random.choice(chars) for _ in range(size))

def gerar_pix1():
    banco = sqlite3.connect('banco_stonks.db')
    cursor = banco.cursor()
    chavepix = gerar_chavepix()
    tela_gerarpix.chavepix_label.setText(chavepix)
    update_pix()

def gerar_pix():
    banco = sqlite3.connect('banco_stonks.db')
    cursor = banco.cursor()
    chavepix1 = gerar_chavepix()
    id_carteira1 = catch_id()
    variavel = 1250
    print(chavepix1)
    query = """UPDATE carteira SET chave_pix = ? WHERE id_carteira = ?"""
    data = (chavepix1, id_carteira1)
    cursor.execute(query, data)
    tela_gerarpix.chavepix_label.setText(chavepix1)
    print(chavepix1)
    banco.commit()

def call_tela_cadastro():
    tela_cadastro.show()

def call_tela_pix():
    tela_gerarpix.show()

def call_tela_gerarpix():
    tela_pix.show()

def cadastrar():
    nome = tela_cadastro.cadastro_usuario.text()
    login = tela_cadastro.cadastro_usuario.text()
    senha = tela_cadastro.cadastro_password.text()
    c_senha = tela_cadastro.repeat_password.text()

    if (senha == c_senha):
        try:
            banco = sqlite3.connect('banco_stonks.db')
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS carteira (chave_pix string,saldo INTEGER,id text, id_carteira int PRIMARY KEY autoincrement)")
            chavepix = gerar_chavepix()
            #chavepix = str(chavepix)
            cursor.execute("INSERT INTO carteira VALUES ('" + chavepix + "', 0, NULL)")
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,senha text, id_usuario int PRIMARY KEY autoincrement)")
            cursor.execute("SELECT id_carteira FROM carteira ORDER BY id_carteira desc Limit 1;")
            id_carteira = str((cursor.fetchall())[0][0])
            print(id_carteira)
            cursor.execute("INSERT INTO cadastro VALUES ('" + nome + "','" + login + "','" + senha + "', NULL, '" + id_carteira + "')")
            banco.commit()
            banco.close()
            tela_cadastro.msg_label2.setText("Usuario cadastrado com sucesso")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)

    else:
        tela_cadastro.label.setText("As senhas digitadas estão diferentes")

def call_tela_apagarconta():
    tela_deletar.show()

def call_tela_perfil():
    tela_perfil.show()

def call_tela_deletar():
    tela_deletar.show()

def deletar_conta():
    banco = sqlite3.connect('banco_stonks.db')
    cursor = banco.cursor()
    usuario = catch_idUsuario()
    print(usuario)
    cursor.execute("delete from cadastro where id_usuario = ?", usuario)
    banco.commit()
    tela_main.close()
    tela_deletar.close()
    tela_perfil.close()
    tela_login.show()

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    tela_login = uic.loadUi("tela_login.ui")
    tela_deletar = uic.loadUi("tela_deletar.ui")
    tela_gerarpix = uic.loadUi("gerarpix.ui")
    tela_cadastro = uic.loadUi("tela_cadastro.ui")
    tela_main = uic.loadUi("tela_main.ui")
    tela_perfil = uic.loadUi("tela_perfil.ui")
    tela_pix = uic.loadUi("pix.ui")
    tela_login.cadastrarButton.clicked.connect(call_tela_cadastro)
    tela_cadastro.cadastrarButton.clicked.connect(cadastrar)
    tela_login.loginButton.clicked.connect(login)
    tela_perfil.apagarconta_botao.clicked.connect(login) #excluir a conta
    tela_main.perfilButton.clicked.connect(call_tela_perfil)
    tela_main.pixButton.clicked.connect(call_tela_pix)
    tela_gerarpix.gerarpixButton.clicked.connect(gerar_pix)
    tela_perfil.apagarconta_botao.clicked.connect(call_tela_deletar)
    tela_deletar.apagarconta_botao2.clicked.connect(deletar_conta)
    Form = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Form)
    tela_login.show()
    app.exec()

