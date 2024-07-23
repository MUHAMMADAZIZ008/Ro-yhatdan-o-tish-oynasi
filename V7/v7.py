import json
import re
from abc import abstractmethod 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
    QToolBox,

)

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # self.setGeometry(700, 400, 600, 800)
        self.setFixedSize(600, 670)
        self.setWindowTitle("Najot Ta'lim")
        self.main_box = QVBoxLayout()
        self.title_lable_box = QFormLayout()


        self.title_lable1 = QLabel("Najot")
        self.title_lable2 = QLabel("chat")
        self.title_lable_box.addRow(self.title_lable1, self.title_lable2)

        self.user_login = QLineEdit()
        self.user_password = QLineEdit()

        self.info_lable = QLabel()

        self.login_bnt = QPushButton("LOGIN")
        self.create_btn = QPushButton("Create new account")


        #All add
        self.main_box.addLayout(self.title_lable_box)
        self.main_box.addWidget(self.user_login)
        self.main_box.addWidget(self.user_password)
        self.main_box.addWidget(self.info_lable)
        self.main_box.addWidget(self.login_bnt)
        self.main_box.addWidget(self.create_btn)

        self.setLayout(self.main_box)
        #Style
        self.setStyleSheet("""
            background-color: #F8EDED;
            font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
            margin: auto;
        
        """)


        #title_lable
        self.title_lable1.setStyleSheet("""
            font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
            font-size: 50px;
            color: #000044;
            margin: 50px 0 0 170px;
        """)
        
        self.title_lable2.setStyleSheet("""
            font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
            font-size: 50px;
            color: #FF6500;
            margin: 80px 150px 0 0;
        """)
        #

        #login
        self.user_login.setFixedSize(400, 50)
        self.user_login.setPlaceholderText("User name")
        self.user_login.setStyleSheet("""
            QLineEdit {
                border: 2px solid #fff;
                font-size: 25px;
                background-color: #FF8A08;
                margin: 0 0 0 auto;
                font-family: Arial, Helvetica, sans-serif;
                border-radius: 15px;
                padding: 10px;
            }
            QLineEdit:focus{
                border: 2px solid #004225;
                background-color: #000044;
                color: #fff;
                border: 2px solid #FF8A08;
                
            }

        """)


        self.user_password.setFixedSize(400, 50)
        self.user_password.setPlaceholderText("Password")
        self.user_password.setStyleSheet("""
            QLineEdit {
                border: 2px solid #fff;
                font-size: 25px;
                background-color: #FF8A08;
                margin: 0 auto 0 auto;
                font-family: Arial, Helvetica, sans-serif;
                border-radius: 15px;
                padding: 10px;
            }
            QLineEdit:focus{
                border: 2px solid #004225;
                background-color: #000044;
                color: #fff;
                border: 2px solid #FF8A08;
            }
        """)
        #

        #info
        self.info_lable.setFixedHeight(40)
        self.info_lable.setStyleSheet("""
            padding: 10px;
            font-size: 25px;
            color: red;
        """)



        #login btn
        self.login_bnt.setFixedWidth(350)
        self.login_bnt.setStyleSheet("""
        QPushButton{
            padding: 10px;
            background-color: #1715a1;
            color: #fff;
            font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
            font-size: 25px;
            border-radius: 15px;
            }
            QPushButton:hover{
                border: 2px solid #FF8A08;
                background-color: #F8EDED;
                color: #000;
            }                         
        """)
        #
        #creat btn
        self.create_btn.setFixedWidth(350)
        self.create_btn.setStyleSheet("""
        QPushButton{
            padding: 10px;
            background-color: #004225;
            color: #fff;
            font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
            font-size: 25px;
            border-radius: 15px;
            }
            QPushButton:hover{
                border: 2px solid #FF8A08;
                background-color: #F8EDED;
                color: #000;
            }                         
        """)
        #
        #

        # function
        self.login_bnt.clicked.connect(self.check_users)

        self.create_btn.clicked.connect(self.creat_new_win)
        #
        self.show()




    def check_users(self):
        login = self.user_login.text()
        pasword = self.user_password.text()
        users = ReadJson.readingUser()
        if login and pasword:
            for user in users:
                if user["login"] == login and user["password"] == pasword:
                    self.welcom = Welcom(login)
                    self.close()
                else:
                    self.info_lable.setText("Login yoki parol notog'ri")
        else:
            self.info_lable.setText("Login va parolni kiriting❗")


    def creat_new_win(self):
        self.fill_window = FillWindow()
        self.close()



class FillWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(600, 700)
        self.main_box = QVBoxLayout()
        self.main_title = QLabel()

        self.back_btn = QPushButton("🔙")

        self.fill_info_box = QVBoxLayout()
        self.user_email = QLineEdit()
        self.user_full_name = QLineEdit()
        self.user_name = QLineEdit()
        self.user_password = QLineEdit()

        self.info_lable = QLabel()
        self.sing_up_btn = QPushButton("SING UP")

        self.fill_info_box.addWidget(self.user_email)
        self.fill_info_box.addWidget(self.user_full_name)
        self.fill_info_box.addWidget(self.user_name)
        self.fill_info_box.addWidget(self.user_password)

        self.main_box.addWidget(self.main_title)
        self.main_box.addLayout(self.fill_info_box)
        self.main_box.addWidget(self.info_lable)
        self.main_box.addWidget(self.sing_up_btn)
        self.main_box.addWidget(self.back_btn)

        self.setLayout(self.main_box)

        #style
        self.setStyleSheet("""
            background-color: #F8EDED;
            font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
            margin: auto;
        """)
        
        self.back_btn.setStyleSheet("""
            padding: 5px;
            background-color: #393E46;
            font-size: 30px;
            border: 0;
            border-radius: 5px;
        """)

        self.main_title.setText("SING UP")
        self.main_title.setStyleSheet("""
            font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
            font-size: 50px;
            color: #000044;
            margin: 50px 0 0 200px;
        """)


        self.user_email.setPlaceholderText("Email")
        self.user_email.setStyleSheet("""
            QLineEdit {
                border: 2px solid #fff;
                font-size: 25px;
                background-color: #FF8A08;
                margin: 0 auto 0 auto;
                font-family: Arial, Helvetica, sans-serif;
                border-radius: 15px;
                padding: 10px;
            }
            QLineEdit:focus{
                border: 2px solid #004225;
                background-color: #000044;
                color: #fff;
                border: 2px solid #FF8A08;
            }
        """)



        self.user_full_name.setPlaceholderText("Full Name")
        self.user_full_name.setStyleSheet("""
            QLineEdit {
                border: 2px solid #fff;
                font-size: 25px;
                background-color: #FF8A08;
                margin: 0 auto 0 auto;
                font-family: Arial, Helvetica, sans-serif;
                border-radius: 15px;
                padding: 10px;
            }
            QLineEdit:focus{
                border: 2px solid #004225;
                background-color: #000044;
                color: #fff;
                border: 2px solid #FF8A08;
            }
        """)


        self.user_name.setPlaceholderText("User Name")
        self.user_name.setStyleSheet("""
            QLineEdit {
                border: 2px solid #fff;
                font-size: 25px;
                background-color: #FF8A08;
                margin: 0 auto 0 auto;
                font-family: Arial, Helvetica, sans-serif;
                border-radius: 15px;
                padding: 10px;
            }
            QLineEdit:focus{
                border: 2px solid #004225;
                background-color: #000044;
                color: #fff;
                border: 2px solid #FF8A08;
            }
        """)

        self.user_password.setPlaceholderText("Password")
        self.user_password.setStyleSheet("""
            QLineEdit {
                border: 2px solid #fff;
                font-size: 25px;
                background-color: #FF8A08;
                margin: 0 auto 0 auto;
                font-family: Arial, Helvetica, sans-serif;
                border-radius: 15px;
                padding: 10px;
            }
            QLineEdit:focus{
                border: 2px solid #004225;
                background-color: #000044;
                color: #fff;
                border: 2px solid #FF8A08;
            }
        """)

        self.sing_up_btn.setStyleSheet("""
        QPushButton{
            padding: 10px;
            background-color: #1715a1;
            color: #fff;
            font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
            font-size: 25px;
            border-radius: 15px;
            }
            QPushButton:hover{
                border: 2px solid #FF8A08;
                background-color: #F8EDED;
                color: #000;
            }                         
        """)

        self.info_lable.setFixedHeight(40)
        self.info_lable.setStyleSheet("""
            padding: 10px;
            font-size: 25px;
            color: red;
        """)
        #

        #function
        
        self.back_btn.clicked.connect(self.back_main)
        self.show()

        self.sing_up_btn.clicked.connect(self.creat_new_account)
    
    def back_main(self):
        self.main_win = Window()
        self.close()
        #
    
    def creat_new_account(self):
        users = ReadJson.readingUser()
        email_text = self.user_email.text()
        full_text = self.user_full_name.text()
        name_text = self.user_name.text()
        password_text = self.user_password.text()

        email_check = False
        name_check = False
        password_check = False
        if email_text and full_text and name_text and password_text:
            if "@email.com" in email_text:
                email_check = True
            
            for user in users:
                if user["login"] != name_text:
                    name_check = True
                else:
                    name_check = False
            if len(password_text) >= 8 and re.search(r"[A-Z]", password_text) and re.search(r'[a-z]', password_text) and re.search(r'[0-9]', password_text) and re.search(r'[!@#$%]', password_text):
                password_check = True
            
            
            if  not email_check:
                self.info_lable.setText("Emailni xato kirtdingiz")
            if not name_check:
                self.info_lable.setText("Bunday user name mavjut")
            if not password_check:
                self.info_lable.setText("Parolda(A-a,1-9,!@#$) bo'lishi shart")
        else:
            self.info_lable.setText("Ma'lumotlarni to'ldiring")

        if email_check and name_check and password_check:
            self.close()
            self.welcom = Welcom(name_text)

        
            





class Welcom(QWidget):
    def __init__(self, login) -> None:
        super().__init__()
        self.setGeometry(700, 400, 400, 300)
        self.login = login
        self.v_box = QVBoxLayout()
        self.label = QLabel(f"Welcome: {self.login}")
        self.back_btn = QPushButton("🔙")
        self.v_box.addWidget(self.label)
        self.v_box.addWidget(self.back_btn)
        self.setLayout(self.v_box)

        #style
        self.setStyleSheet("""
            background-color: #EEEEEE;

        """)
        self.label.setStyleSheet("""
            color: #00ADB5;
            font-size: 35px;
            font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
            margin-left: 15px;
        """)
        self.back_btn.setFixedSize(50, 50)
        self.back_btn.setStyleSheet("""
            background-color: #393E46;
            font-size: 30px;
            border: 0;
            border-radius: 5px;
        """)
        #

        self.back_btn.clicked.connect(self.back_main)
        self.show()
    
    def back_main(self):
        self.main_win = Window()
        self.close()



class ReadJson(QWidget):
    def __init__(self) -> None:
        super().__init__()
    @abstractmethod
    def readingUser():
        with open("user_info.json") as info:
            user = json.load(info)
        return user
    
        
        

app = QApplication([])

win = Window()

app.exec_()
