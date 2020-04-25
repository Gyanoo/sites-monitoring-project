import webbrowser

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                           QPixmap, QRadialGradient)
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QFrame,
                               QStackedWidget, QGridLayout, QLabel, QSpacerItem, QSizePolicy, QGroupBox,
                               QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QRadioButton, QScrollArea,
                               QAbstractScrollArea)
import sys
# import element
from ui import stylesheet as styles
import os
# from PySide2 import sip
import read_write_data as data

path = os.path.dirname(os.path.abspath(__file__))


class SitesFrame(QFrame):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.setStyleSheet("""QFrame{background-color:#83a836;}""")


class NavFrame(QFrame):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.setStyleSheet("""QFrame{ background-color:#43454f;}""")
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

        self.frame_nav = QFrame(self)
        self.frame_nav.setMinimumSize(QSize(220, 300))
        self.frame_nav.setStyleSheet("""QFrame{ background-color:#43454f;}""")
        self.frame_nav.setFrameShape(QFrame.StyledPanel)
        self.frame_nav.setFrameShadow(QFrame.Raised)

        self.gridLayout = QGridLayout(self)
        self.gridLayout.setContentsMargins(11, -1, 11, -1)
        self.gridLayout.addWidget(self.frame_nav, 3, 0, 1, 4)

        # set program img and name
        self.label_img = QLabel(self)
        self.label_img.setFixedSize(QSize(60, 60))

        self.label_img.setPixmap(QPixmap(os.path.join(path, 'img/icon.png')))
        # self.label_img.setPixmap(QPixmap("../img/icon.png"))
        self.label_img.setScaledContents(True)
        self.gridLayout.addWidget(self.label_img, 2, 1, 1, 1)

        self.label_name = QLabel("WebCheck        ", self)
        self.label_name.setStyleSheet(styles.label_icon_name)
        self.gridLayout.addWidget(self.label_name, 2, 2, 1, 1)

        self.spacer_name_l = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.spacer_name_r = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.spacer_name_t = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.gridLayout.addItem(self.spacer_name_l, 2, 0, 1, 1)
        self.gridLayout.addItem(self.spacer_name_r, 2, 3, 1, 1)
        self.gridLayout.addItem(self.spacer_name_t, 1, 1, 1, 2)

        # set bottom layout for keeping gb in it
        self.gridLayout_b = QGridLayout(self.frame_nav)
        self.spacer_gb_l = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.spacer_gb_r = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.spacer_gb_t = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.spacer_gb_b = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_b.addItem(self.spacer_gb_l, 1, 2, 1, 1)
        self.gridLayout_b.addItem(self.spacer_gb_r, 1, 0, 1, 1)
        self.gridLayout_b.addItem(self.spacer_gb_t, 0, 1, 1, 1)
        self.gridLayout_b.addItem(self.spacer_gb_b, 2, 1, 1, 1)

        # set gb and radio buttons
        self.groupBox = QGroupBox("", self.frame_nav)
        self.gridLayout_b.addWidget(self.groupBox, 1, 1, 1, 1)
        self.groupBox.setMinimumSize(QSize(220, 350))
        self.groupBox.setStyleSheet("""QGroupBox{background-image: url(ui/img/radioline.png);  border: none;}""")
        self.verticalLayout_gb = QVBoxLayout(self.groupBox)

        self.radioButton_add = QRadioButton(" Add", self.groupBox)
        self.radioButton_add.setStyleSheet(styles.btn_radio)
        self.verticalLayout_gb.addWidget(self.radioButton_add)

        self.radioButton_monitored = QRadioButton(" Monitored", self.groupBox)
        self.radioButton_monitored.setStyleSheet(styles.btn_radio)
        self.verticalLayout_gb.addWidget(self.radioButton_monitored)

        self.radioButton_options = QRadioButton(" Options", self.groupBox)
        self.radioButton_options.setStyleSheet(styles.btn_radio)
        self.verticalLayout_gb.addWidget(self.radioButton_options)

        self.radioButton_about = QRadioButton(" About", self.groupBox)
        self.radioButton_about.setStyleSheet(styles.btn_radio)
        self.verticalLayout_gb.addWidget(self.radioButton_about)


class PageAllegroAdd(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        parent.addWidget(self)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setRowStretch(0, 0)
        self.gridLayout.setRowStretch(8, 1)
        self.gridLayout.setRowStretch(11, 1)
        self.gridLayout.setRowStretch(14, 1)
        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 5)
        self.gridLayout.setColumnStretch(2, 5)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 4)
        self.gridLayout.setColumnStretch(5, 2)
        self.gridLayout.setColumnStretch(6, 2)
        self.gridLayout.setColumnStretch(7, 2)
        self.gridLayout.setColumnStretch(8, 5)

        # create lineEdits
        self.lineEdit_login = QLineEdit(self)
        self.lineEdit_login.setMinimumSize(QSize(0, 60))
        self.lineEdit_login.setSizeIncrement(QSize(40, 40))
        self.lineEdit_login.setStyleSheet(styles.lineEdit)
        self.lineEdit_login.setMaxLength(32767)
        self.gridLayout.addWidget(self.lineEdit_login, 7, 1, 1, 2)
        self.lineEdit_login.setPlaceholderText("login or email from your account")

        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.setMinimumSize(QSize(20, 60))
        self.lineEdit_password.setStyleSheet(styles.lineEdit)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setReadOnly(False)
        self.gridLayout.addWidget(self.lineEdit_password, 10, 1, 1, 2)
        self.lineEdit_password.setPlaceholderText("password from your account")

        self.lineEdit_email = QLineEdit(self)
        self.lineEdit_email.setMinimumSize(QSize(0, 60))
        self.lineEdit_email.setStyleSheet(styles.lineEdit)
        self.lineEdit_email.setFrame(True)
        self.lineEdit_email.setEchoMode(QLineEdit.Normal)
        self.gridLayout.addWidget(self.lineEdit_email, 10, 4, 1, 4)
        self.lineEdit_email.setPlaceholderText("email to which the message will be sent")

        self.lineEdit_link = QLineEdit(self)
        self.lineEdit_link.setMinimumSize(QSize(0, 60))
        self.lineEdit_link.setStyleSheet(styles.lineEdit)
        self.gridLayout.addWidget(self.lineEdit_link, 13, 1, 1, 7)
        self.lineEdit_link.setPlaceholderText("link to the page that needs to be monitored")

        # Create Labels
        self.label_title = QLabel("Add new monitoring object", self)
        self.label_title.setStyleSheet(styles.label_title)
        self.label_title.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_title, 0, 1, 1, 7)

        self.label_login = QLabel("Login of email", self)
        self.label_login.setStyleSheet(styles.label_lineEdit)
        self.gridLayout.addWidget(self.label_login, 6, 1, 1, 1)

        self.label_password = QLabel("Password", self)
        self.label_password.setStyleSheet(styles.label_lineEdit)
        self.gridLayout.addWidget(self.label_password, 9, 1, 1, 2)

        self.label_email = QLabel("Email", self)
        self.label_email.setStyleSheet(styles.label_lineEdit)
        self.gridLayout.addWidget(self.label_email, 9, 4, 1, 4)

        self.label_link = QLabel("Link", self)
        self.label_link.setStyleSheet(styles.label_lineEdit)
        self.gridLayout.addWidget(self.label_link, 12, 1, 1, 7)

        self.pushButton_search = QPushButton(self)
        self.pushButton_search.clicked.connect(lambda: webbrowser.open('https://allegro.pl/'))
        icon = QIcon()
        icon.addFile(os.path.join(path, "img/search.png"), QSize(), QIcon.Selected, QIcon.Off)
        self.pushButton_search.setIcon(icon)
        self.pushButton_search.setIconSize(QSize(80, 80))
        self.pushButton_search.setStyleSheet("""QPushButton{border:none;}""")
        self.gridLayout.addWidget(self.pushButton_search, 7, 5, 1, 1)

        # Create spacers
        self.spacer_search_l = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.spacer_search_l, 7, 4, 1, 1)

        self.spacer_search_r = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.spacer_search_r, 7, 6, 1, 2)

        self.spacer_search_t = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.spacer_search_t, 1, 1, 3, 7)

        self.spacer_search_b = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.spacer_search_b, 8, 1, 1, 7)

        self.spacer_email_l = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.spacer_email_l, 10, 3, 1, 1)

        self.spacer_link_l = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.spacer_link_l, 13, 0, 1, 1)

        self.spacer_link_r = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.spacer_link_r, 13, 8, 1, 1)

        self.spacer_link_t = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.spacer_link_t, 11, 1, 1, 7)

        self.spacer_link_b = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.spacer_link_b, 14, 1, 1, 7)

        # create frame bottom
        self.frame_bottom = QFrame(self)
        self.frame_bottom.setStyleSheet("""QFrame{background-color: #fff; padding: 10px;}""")
        self.frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.gridLayout.addWidget(self.frame_bottom, 15, 0, 1, 9)
        self.horizontalLayout_frame_bottom = QHBoxLayout(self.frame_bottom)

        self.spacer_frame_bottom_l = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_frame_bottom.addItem(self.spacer_frame_bottom_l)

        self.pushButton_atc = QPushButton("Add to cart", self.frame_bottom)
        self.pushButton_atc.setMinimumSize(QSize(0, 40))
        self.pushButton_atc.setStyleSheet(styles.btn_light)
        self.horizontalLayout_frame_bottom.addWidget(self.pushButton_atc)
        self.pushButton_atc.setShortcut(QCoreApplication.translate('MainWindow', u"Return", None))

        self.spacer_frame_bottom_c = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_frame_bottom.addItem(self.spacer_frame_bottom_c)

        self.pushButton_buy = QPushButton("Buy", self.frame_bottom)
        self.pushButton_buy.setMinimumSize(QSize(0, 40))
        self.pushButton_buy.setStyleSheet(styles.btn_dark)
        self.horizontalLayout_frame_bottom.addWidget(self.pushButton_buy)

        self.spacer_frame_bottom_r = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_frame_bottom.addItem(self.spacer_frame_bottom_r)

        self.horizontalLayout_frame_bottom.setStretch(0, 1)
        self.horizontalLayout_frame_bottom.setStretch(1, 1)
        self.horizontalLayout_frame_bottom.setStretch(2, 2)
        self.horizontalLayout_frame_bottom.setStretch(3, 1)
        self.horizontalLayout_frame_bottom.setStretch(4, 1)

    def add_to_cart(self):
        # check if fields was filled properly
        no_warnings = True
        is_email = False
        is_pwd = False
        if self.lineEdit_email.text() == "":
            self.lineEdit_email.setStyleSheet(styles.lineEdit_warning)
            no_warnings = False
        else:
            self.lineEdit_email.setStyleSheet(styles.lineEdit)
            email = self.lineEdit_email.text()
            for symbol in email:
                if symbol == '@':
                    is_email = True
            if not is_email:
                self.lineEdit_email.setStyleSheet(styles.lineEdit_warning)
                no_warnings = False
        if self.lineEdit_login.text() == "":
            self.lineEdit_login.setStyleSheet(styles.lineEdit_warning)
            no_warnings = False
        else:
            self.lineEdit_login.setStyleSheet(styles.lineEdit)
            login = self.lineEdit_login.text()
        if self.lineEdit_link.text() == "":
            self.lineEdit_link.setStyleSheet(styles.lineEdit_warning)
            no_warnings = False
        else:
            self.lineEdit_link.setStyleSheet(styles.lineEdit)
            link = self.lineEdit_link.text()

        if self.lineEdit_password.text() == "":
            self.lineEdit_password.setStyleSheet(styles.lineEdit_warning)
            no_warnings = False
        else:
            self.lineEdit_password.setStyleSheet(styles.lineEdit)
            password = self.lineEdit_password.text()

        if no_warnings:
            self.lineEdit_login.clear()
            self.lineEdit_password.clear()
            self.lineEdit_email.clear()
            self.lineEdit_link.clear()
            data.add_monitored_elements(link, False)
        return data.get_element(link)


class ElementAllegroMonitored(QFrame):

    def on_delete(self, link):
        data.delete_monitored_element(link)

    def __init__(self, name, link, is_done, parent=None):
        QFrame.__init__(self, parent)
        self.setMinimumSize(QSize(0, 140))
        self.setStyleSheet("""QFrame{border-bottom: 0.5px solid #aaa;}""")
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self)

        # create description frame and layout
        self.frame_description = QFrame(self)
        self.frame_description.setMaximumSize(QSize(440, 16777215))
        self.frame_description.setStyleSheet("""QFrame{border: none;}""")
        self.frame_description.setFrameShape(QFrame.StyledPanel)
        self.frame_description.setFrameShadow(QFrame.Raised)
        self.gridLayout_description = QGridLayout(self.frame_description)
        self.horizontalLayout.addWidget(self.frame_description)

        # fill description layout
        self.label_name = QLabel(name, self.frame_description)
        self.label_name.setStyleSheet(styles.label_allegro_monitored_name)
        self.label_name.setTextFormat(Qt.MarkdownText)
        self.label_name.setAlignment(Qt.AlignJustify | Qt.AlignVCenter)
        self.label_name.setWordWrap(False)
        self.gridLayout_description.addWidget(self.label_name, 0, 0, 1, 2)

        url_link = "<a href=\"" + link + "\" style = \" color: #43454f; text-decoration: none; font-family:corbel; title=\"Go to monitored page\"\">check hire</a>"
        self.label_link = QLabel(url_link, self.frame_description)
        self.label_link.setStyleSheet(styles.label_allegro_monitored_stat)
        self.gridLayout_description.addWidget(self.label_link, 1, 1, 1, 1)
        self.label_link.setOpenExternalLinks(True)

        self.label_stat = QLabel(self.frame_description)
        self.label_stat.setStyleSheet(styles.label_allegro_monitored_stat)
        self.gridLayout_description.addWidget(self.label_stat, 2, 1, 1, 1)

        self.label_img_link = QLabel(self.frame_description)
        self.label_img_link.setMaximumSize(QSize(20, 20))
        self.label_img_link.setStyleSheet("""QLabel{border: none;}""")
        self.label_img_link.setPixmap(QPixmap(os.path.join(path, "img/link.png")))
        # self.label_img_link.setPixmap(QPixmap(u"img/link.png"))
        self.label_img_link.setScaledContents(True)
        self.gridLayout_description.addWidget(self.label_img_link, 1, 0, 1, 1)

        self.label_img_stat = QLabel("done", self.frame_description)
        if is_done:
            self.label_stat.setText("done")
            self.label_img_stat.setPixmap(QPixmap(os.path.join(path, "img/check.png")))
        else:
            self.label_stat.setText("in progress")
            self.label_img_stat.setPixmap(QPixmap(os.path.join(path, "img/loading.png")))
        self.label_img_stat.setMaximumSize(QSize(20, 20))
        self.label_img_stat.setStyleSheet("""QLabel{border: none;}""")
        # self.label_img_stat.setPixmap(QPixmap("img/loading.png"))
        self.label_img_stat.setScaledContents(True)
        self.gridLayout_description.addWidget(self.label_img_stat, 2, 0, 1, 1)

        # create spacer and delete btn
        self.spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.spacer)

        self.pushButton_delete = QPushButton(self)
        self.pushButton_delete.clicked.connect(lambda: self.on_delete(link))
        icon = QIcon()
        icon.addFile(os.path.join(path, "img/delete.png"), QSize(), QIcon.Selected, QIcon.Off)
        # icon.addFile("img/delete.png", QSize(), QIcon.Selected, QIcon.Off)
        self.pushButton_delete.setIcon(icon)
        self.pushButton_delete.setIconSize(QSize(50, 50))
        self.pushButton_delete.setStyleSheet("""QPushButton{border:none;}""")
        self.horizontalLayout.addWidget(self.pushButton_delete)


class PageAllegroMonitored(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        parent.addWidget(self)
        self.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout = QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setStyleSheet("""QScrollArea{border: none;}""")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 654, 479))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_scroll_area = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_scroll_area.setSpacing(0)
        self.gridLayout_scroll_area.setContentsMargins(40, 0, 40, -1)

        self.label_title = QLabel("List of your monitored objects", self.scrollAreaWidgetContents)
        self.label_title.setStyleSheet(styles.label_title)
        self.label_title.setAlignment(Qt.AlignCenter)
        self.gridLayout_scroll_area.addWidget(self.label_title)

        self.spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.load_list()

    def load_list(self):
        elements = data.read_monitored_elements()
        for element in elements:
            e = ElementAllegroMonitored(element['name'], element['link'], element['is_done'],
                                        self.scrollAreaWidgetContents)
            self.gridLayout_scroll_area.addWidget(e)

        self.gridLayout_scroll_area.addItem(self.spacer)

    def add_to_list(self, name, link, is_done):
        print(name)


class PageAllegroOptions(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.gridLayout = QGridLayout(self)
        parent.addWidget(self)


class PageAbout(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        parent.addWidget(self)
        self.gridLayout_about = QGridLayout(self)

        self.frame_about = QFrame(self)
        self.frame_about.setEnabled(True)
        self.frame_about.setStyleSheet(styles.frame_about)
        self.frame_about.setFrameShape(QFrame.StyledPanel)
        self.frame_about.setFrameShadow(QFrame.Raised)
        self.gridLayout_about.addWidget(self.frame_about, 0, 0, 1, 1)

        self.gridLayout_frame_about = QGridLayout(self.frame_about)
        self.gridLayout_frame_about.setContentsMargins(-1, 60, -1, -1)

        self.spacer_about_l = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.spacer_about_r = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.spacer_about_b = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_frame_about.addItem(self.spacer_about_l, 0, 0, 1, 1)
        self.gridLayout_frame_about.addItem(self.spacer_about_r, 0, 2, 1, 1)
        self.gridLayout_frame_about.addItem(self.spacer_about_b, 3, 1, 1, 1)

        self.label_about_name = QLabel("WebCheck", self.frame_about)
        self.label_about_name.setStyleSheet(styles.label_about_name)
        self.label_about_name.setAlignment(Qt.AlignCenter)
        self.gridLayout_frame_about.addWidget(self.label_about_name, 0, 1, 1, 1)

        self.label_about_version = QLabel("Version 1.0.0", self.frame_about)
        self.label_about_version.setStyleSheet(styles.label_about_version)
        self.label_about_version.setAlignment(Qt.AlignCenter)
        self.gridLayout_frame_about.addWidget(self.label_about_version, 1, 0, 1, 3)

        self.label_about_c = QLabel("\u00a9 All rights reserved", self.frame_about)
        self.label_about_c.setStyleSheet(styles.label_about_c)
        self.label_about_c.setAlignment(Qt.AlignCenter)
        self.gridLayout_frame_about.addWidget(self.label_about_c, 2, 0, 1, 3)


class StackedWidget(QStackedWidget):
    def __init__(self, parent=None):
        QStackedWidget.__init__(self, parent)
        self.setStyleSheet("""QWidget{background-color:#f2ede1;}""")
        self.pageAllegroAdd = PageAllegroAdd(self)
        self.pageAllegroMonitored = PageAllegroMonitored(self)
        self.pageAllegroOptions = PageAllegroOptions(self)
        self.pageAbout = PageAbout(self)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.centralWidget = QWidget(self)
        self.gridLayout_central = QGridLayout(self.centralWidget)
        self.navFrame = NavFrame(self.centralWidget)
        self.sitesFrame = SitesFrame(self.centralWidget)
        self.stackedWidget = StackedWidget(self.centralWidget)
        self.init_window()
        self.set_start_state()

    def set_start_state(self):
        # set nav btn connection
        self.navFrame.radioButton_add.toggled.connect(lambda: self.go_to_page(0))
        self.navFrame.radioButton_monitored.toggled.connect(lambda: self.go_to_page(1))
        self.navFrame.radioButton_options.toggled.connect(lambda: self.go_to_page(2))
        self.navFrame.radioButton_about.toggled.connect(lambda: self.go_to_page(3))
        self.navFrame.radioButton_add.setChecked(True)
        self.stackedWidget.pageAllegroAdd.pushButton_atc.clicked.connect(lambda: self.add_to_cart())

    def add_to_cart(self):
        element = self.stackedWidget.pageAllegroAdd.add_to_cart()
        if element is not None:
            self.stackedWidget.pageAllegroMonitored.add_to_list(element["name"], element["link"], element["is_done"])

    def init_window(self):
        # set window
        self.setGeometry(100, 100, 900, 600)
        import os
        self.setWindowIcon(QIcon(os.path.join(path, './img/icon.png')))
        # self.setWindowIcon(QIcon('./img/icon.png'))
        self.setWindowTitle("WebCheck")

        # set centralWidget
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setMinimumSize(QSize(900, 500))
        self.setCentralWidget(self.centralWidget)

        # set grid layout central
        self.gridLayout_central.setSpacing(0)
        self.gridLayout_central.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_central.setRowStretch(0, 1)
        self.gridLayout_central.setRowStretch(1, 10)
        self.gridLayout_central.setColumnStretch(0, 1)
        self.gridLayout_central.setColumnStretch(1, 3)
        self.gridLayout_central.addWidget(self.navFrame, 0, 0, 9, 1)
        self.gridLayout_central.addWidget(self.sitesFrame, 0, 1, 1, 1)
        self.gridLayout_central.addWidget(self.stackedWidget, 1, 1, 1, 1)

    def go_to_page(self, index):
        if index == 0:
            self.stackedWidget.setCurrentIndex(0)
        elif index == 1:
            self.stackedWidget.setCurrentIndex(1)
        elif index == 2:
            self.stackedWidget.setCurrentIndex(2)
        elif index == 3:
            self.stackedWidget.setCurrentIndex(3)


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
