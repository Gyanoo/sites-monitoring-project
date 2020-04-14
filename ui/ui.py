# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qtDesiner.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# import sourse_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 774)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(900, 500))
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_sites = QFrame(self.centralwidget)
        self.frame_sites.setObjectName(u"frame_sites")
        self.frame_sites.setStyleSheet(u"QFrame{\n"
"background-color:#83a836;\n"
"}")
        self.frame_sites.setFrameShape(QFrame.StyledPanel)
        self.frame_sites.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_sites, 0, 1, 1, 1)

        self.frame_left = QFrame(self.centralwidget)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setStyleSheet(u"QFrame{\n"
"background-color:#83a836;\n"
"background-color:#43454f;\n"
"}")
        self.frame_left.setFrameShape(QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_left)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(11, -1, 11, -1)
        self.spacer_pname_l = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.spacer_pname_l, 2, 0, 1, 1)

        self.label_picon = QLabel(self.frame_left)
        self.label_picon.setObjectName(u"label_picon")
        self.label_picon.setMinimumSize(QSize(60, 60))
        self.label_picon.setMaximumSize(QSize(60, 60))
        self.label_picon.setPixmap(QPixmap(u"../../shop_monitoring_python/ui/img/icon.png"))
        self.label_picon.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_picon, 2, 1, 1, 1)

        self.spacer_pname_r = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.spacer_pname_r, 2, 3, 1, 1)

        self.nav_frame = QFrame(self.frame_left)
        self.nav_frame.setObjectName(u"nav_frame")
        self.nav_frame.setMinimumSize(QSize(220, 300))
        self.nav_frame.setStyleSheet(u"QFrame{\n"
"background-color:#43454f;\n"
"}")
        self.nav_frame.setFrameShape(QFrame.StyledPanel)
        self.nav_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.nav_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.spacer_gbnav_u = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_3.addItem(self.spacer_gbnav_u, 0, 1, 1, 1)

        self.spacer_gbnav_d = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.spacer_gbnav_d, 2, 1, 1, 1)

        self.spacer_gbnav_l = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.spacer_gbnav_l, 1, 2, 1, 1)

        self.spacer_gbnav_r = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.spacer_gbnav_r, 1, 0, 1, 1)

        self.groupBox_nav = QGroupBox(self.nav_frame)
        self.groupBox_nav.setObjectName(u"groupBox_nav")
        self.groupBox_nav.setMinimumSize(QSize(220, 350))
        self.groupBox_nav.setStyleSheet(u"QGroupBox{\n"
# "	background-image: url(:/newPrefix/radioline.png);\n"
"	background-image: url(img/radioline.png);\n"                   
"	border: none;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.groupBox_nav)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton_add = QRadioButton(self.groupBox_nav)
        self.radioButton_add.setObjectName(u"radioButton_add")
        self.radioButton_add.setStyleSheet(u"QRadioButton {\n"
"	font: 16pt \"Reem Kufi\";\n"
"	font-size: 23px;\n"
"	font: 13pt \"Corbel\";\n"
"    color:        #7b826b;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"	background-color:     #a8ad9e;\n"
"    width:                  13px;\n"
"    height:                 13px;\n"
"    border-radius:       11px;\n"
"    border:                 5px solid #788f49;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	background-color:		#43454f;\n"
"    border:                		5px solid #83a836;\n"
"    border-radius:         	11px;\n"
"\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"	color:      #83a836;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:    #7b826b;\n"
"    border:                 5px solid #7b826b;\n"
"\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.radioButton_add)

        self.radioButton_monitored = QRadioButton(self.groupBox_nav)
        self.radioButton_monitored.setObjectName(u"radioButton_monitored")
        self.radioButton_monitored.setStyleSheet(u"QRadioButton {\n"
"	font: 16pt \"Reem Kufi\";\n"
"	font-size: 23px;\n"
"	font: 13pt \"Corbel\";\n"
"    color:        #7b826b;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"	background-color:     #a8ad9e;\n"
"    width:                  13px;\n"
"    height:                 13px;\n"
"    border-radius:       11px;\n"
"    border:                 5px solid #788f49;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	background-color:		#43454f;\n"
"    border:                		5px solid #83a836;\n"
"    border-radius:         	11px;\n"
"\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"	color:      #83a836;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:    #7b826b;\n"
"    border:                 5px solid #7b826b;\n"
"\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.radioButton_monitored)

        self.radioButton_options = QRadioButton(self.groupBox_nav)
        self.radioButton_options.setObjectName(u"radioButton_options")
        self.radioButton_options.setStyleSheet(u"QRadioButton {\n"
"	font: 16pt \"Reem Kufi\";\n"
"	font-size: 23px;\n"
"	font: 13pt \"Corbel\";\n"
"    color:        #7b826b;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"	background-color:     #a8ad9e;\n"
"    width:                  13px;\n"
"    height:                 13px;\n"
"    border-radius:       11px;\n"
"    border:                 5px solid #788f49;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	background-color:		#43454f;\n"
"    border:                		5px solid #83a836;\n"
"    border-radius:         	11px;\n"
"\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"	color:      #83a836;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:    #7b826b;\n"
"    border:                 5px solid #7b826b;\n"
"\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.radioButton_options)

        self.radioButton_about = QRadioButton(self.groupBox_nav)
        self.radioButton_about.setObjectName(u"radioButton_about")
        self.radioButton_about.setStyleSheet(u"QRadioButton {\n"
"	font: 16pt \"Reem Kufi\";\n"
"	font-size: 23px;\n"
"	font: 13pt \"Corbel\";\n"
"    color:        #7b826b;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"	background-color:     #a8ad9e;\n"
"    width:                  13px;\n"
"    height:                 13px;\n"
"    border-radius:       11px;\n"
"    border:                 5px solid #788f49;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	background-color:		#43454f;\n"
"    border:                		5px solid #83a836;\n"
"    border-radius:         	11px;\n"
"\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"	color:      #83a836;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:    #7b826b;\n"
"    border:                 5px solid #7b826b;\n"
"\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.radioButton_about)


        self.gridLayout_3.addWidget(self.groupBox_nav, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.nav_frame, 3, 0, 1, 4)

        self.label_pname = QLabel(self.frame_left)
        self.label_pname.setObjectName(u"label_pname")
        self.label_pname.setStyleSheet(u"QLabel{\n"
"	font-size: 20px;\n"
"	color: white;\n"
"}")

        self.gridLayout_2.addWidget(self.label_pname, 2, 2, 1, 1)

        self.spacer_pname_u = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_2.addItem(self.spacer_pname_u, 1, 1, 1, 2)


        self.gridLayout.addWidget(self.frame_left, 0, 0, 9, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QWidget{\n"
"background-color:#f2ede1\n"
"}")
        self.page_monitored = QWidget()
        self.page_monitored.setObjectName(u"page_monitored")
        self.page_monitored.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_5 = QGridLayout(self.page_monitored)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.scrollArea = QScrollArea(self.page_monitored)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
"	border: none;\n"
"\n"
"\n"
"}\n"
"/*\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: yellow;    \n"
" }\n"
"\n"
"/*QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: yellow;    \n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"     background-color: blue;     \n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/"
                        "rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar:vertical\n"
" {\n"
"     background-color: #2A2929;\n"
"   "
                        "  width: 15px;\n"
"     margin: 15px 3px 15px 3px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::handle:vertical\n"
" {\n"
"     background-color: red;         \n"
"     min-height: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"QScrollBar::sub-line:vertical\n"
" {\n"
"     margin: 3px 0px 3px 0px;\n"
"     border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::add-line:vertical\n"
" {\n"
"     margin: 3px 0px 3px 0px;\n"
"     border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
" {\n"
"\n"
"     border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcont"
                        "rol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
" {\n"
"     background: none;\n"
" }\n"
"")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(-286, -158, 922, 1129))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(900, 900))

        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(200, 200))

        self.gridLayout_7.addWidget(self.label_2, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_5.addWidget(self.scrollArea, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_monitored)
        self.page_options = QWidget()
        self.page_options.setObjectName(u"page_options")
        self.gridLayout_6 = QGridLayout(self.page_options)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.dial = QDial(self.page_options)
        self.dial.setObjectName(u"dial")

        self.gridLayout_6.addWidget(self.dial, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_options)
        self.page_add = QWidget()
        self.page_add.setObjectName(u"page_add")
        self.page_add.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.page_add)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_link = QLabel(self.page_add)
        self.label_link.setObjectName(u"label_link")
        self.label_link.setStyleSheet(u"QLabel{\n"
"	font-size: 23px;\n"
"	font: 12pt \"Corbel\";\n"
"    color:        #43454f;\n"
"}")

        self.gridLayout_4.addWidget(self.label_link, 12, 1, 1, 7)

        self.spacer_login_d = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.spacer_login_d, 8, 1, 1, 7)

        self.spacer_link_r = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.spacer_link_r, 13, 8, 1, 1)

        self.spacer_link_u = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.spacer_link_u, 11, 1, 1, 7)

        self.frame_bottom = QFrame(self.page_add)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setStyleSheet(u"QFrame{\n"
"background-color: #fff;\n"
"padding: 10px;\n"
"}")
        self.frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_l = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_l)

        self.pushButton_atc = QPushButton(self.frame_bottom)
        self.pushButton_atc.setObjectName(u"pushButton_atc")
        self.pushButton_atc.setMinimumSize(QSize(0, 40))
        self.pushButton_atc.setStyleSheet(u"QPushButton{\n"
"background-color:  #fff;\n"
"border: 1 solid #83a836;\n"
"border-radius: 20px;\n"
"font: 13pt \"Corbel\";\n"
"padding:6px;\n"
"color: #83a836;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:  #aaa;\n"
"border: 1 solid #ddd;\n"
"border-radius: 20px;\n"
"font: 13pt \"Corbel\";\n"
"padding:6px;\n"
"color: #fff;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"background-color:  #43454f;\n"
"border: 1 solid #ddd;\n"
"border-radius: 20px;\n"
"font: 13pt \"Corbel\";\n"
"padding:6px;\n"
"color: #fff;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_atc)

        self.horizontalSpacer_c = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_c)

        self.pushButton_buy = QPushButton(self.frame_bottom)
        self.pushButton_buy.setObjectName(u"pushButton_buy")
        self.pushButton_buy.setMinimumSize(QSize(0, 40))
        self.pushButton_buy.setStyleSheet(u"QPushButton{\n"
"background-color:  #43454f;\n"
"border: 1 solid #ddd;\n"
"border-radius: 20px;\n"
"font: 13pt \"Corbel\";\n"
"padding:6px;\n"
"color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:  #aaa;\n"
"border: 1 solid #ddd;\n"
"border-radius: 20px;\n"
"font: 13pt \"Corbel\";\n"
"padding:6px;\n"
"color: #fff;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:  #fff;\n"
"border: 1 solid #83a836;\n"
"border-radius: 20px;\n"
"font: 13pt \"Corbel\";\n"
"padding:6px;\n"
"color: #83a836;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_buy)

        self.horizontalSpacer_r = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_r)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 1)

        self.gridLayout_4.addWidget(self.frame_bottom, 15, 0, 1, 9)

        self.lineEdit_password = QLineEdit(self.page_add)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setMinimumSize(QSize(20, 60))
        self.lineEdit_password.setStyleSheet(u"QLineEdit{\n"
"background-color: white;\n"
"border: 1 solid #ddd;\n"
"border-radius: 5px;\n"
"font: 12pt \"Corbel\";\n"
"color: #43454f;\n"
"padding:10px;\n"
"}\n"
"")
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setReadOnly(False)

        self.gridLayout_4.addWidget(self.lineEdit_password, 10, 1, 1, 2)

        self.spacer_email_l = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.spacer_email_l, 10, 3, 1, 1)

        self.label_email = QLabel(self.page_add)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setStyleSheet(u"QLabel{\n"
"	font-size: 23px;\n"
"	font: 12pt \"Corbel\";\n"
"    color:        #43454f;\n"
"}")

        self.gridLayout_4.addWidget(self.label_email, 9, 4, 1, 4)

        self.spacer_search_r = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.spacer_search_r, 7, 6, 1, 2)

        self.spacer_link_d = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.spacer_link_d, 14, 1, 1, 7)

        self.lineEdit_link = QLineEdit(self.page_add)
        self.lineEdit_link.setObjectName(u"lineEdit_link")
        self.lineEdit_link.setMinimumSize(QSize(0, 60))
        self.lineEdit_link.setStyleSheet(u"QLineEdit{\n"
"background-color: white;\n"
"border: 1 solid #ddd;\n"
"border-radius: 5px;\n"
"font: 12pt \"Corbel\";\n"
"color: #43454f;\n"
"padding:10px;\n"
"}")

        self.gridLayout_4.addWidget(self.lineEdit_link, 13, 1, 1, 7)

        self.spacer_search_l = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.spacer_search_l, 7, 4, 1, 1)

        self.label_img_search = QLabel(self.page_add)
        self.label_img_search.setObjectName(u"label_img_search")
        self.label_img_search.setMaximumSize(QSize(80, 80))
        self.label_img_search.setStyleSheet(u"QLabel{\n"
"border: 1px solid #000; \n"
"border:none;\n"
"}")
        self.label_img_search.setPixmap(QPixmap(u"img/search.png"))
        self.label_img_search.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_img_search, 7, 5, 1, 1)

        self.lineEdit_login = QLineEdit(self.page_add)
        self.lineEdit_login.setObjectName(u"lineEdit_login")
        self.lineEdit_login.setMinimumSize(QSize(0, 60))
        self.lineEdit_login.setSizeIncrement(QSize(40, 40))
        self.lineEdit_login.setStyleSheet(u"QLineEdit{\n"
"background-color: white;\n"
"border: 1 solid #ddd;\n"
"border-radius: 5px;\n"
"font: 12pt \"Corbel\";\n"
"color: #43454f;\n"
"padding:10px;\n"
"}")
        self.lineEdit_login.setMaxLength(32767)

        self.gridLayout_4.addWidget(self.lineEdit_login, 7, 1, 1, 2)

        self.label_password = QLabel(self.page_add)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setStyleSheet(u"QLabel{\n"
"	font-size: 23px;\n"
"	font: 12pt \"Corbel\";\n"
"    color:        #43454f;\n"
"}")

        self.gridLayout_4.addWidget(self.label_password, 9, 1, 1, 2)

        self.lineEdit_email = QLineEdit(self.page_add)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setMinimumSize(QSize(0, 60))
        self.lineEdit_email.setStyleSheet(u"QLineEdit{\n"
"background-color: white;\n"
"border: 1 solid #ddd;\n"
"border-radius: 5px;\n"
"font: 12pt \"Corbel\";\n"
"color: #43454f;\n"
"padding:10px;\n"
"}")
        self.lineEdit_email.setFrame(True)
        self.lineEdit_email.setEchoMode(QLineEdit.Normal)

        self.gridLayout_4.addWidget(self.lineEdit_email, 10, 4, 1, 4)

        self.label_login = QLabel(self.page_add)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setStyleSheet(u"QLabel{\n"
"	font-size: 23px;\n"
"	font: 12pt \"Corbel\";\n"
"    color:        #43454f;\n"
"}")

        self.gridLayout_4.addWidget(self.label_login, 6, 1, 1, 1)

        self.spacer_link_l = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.spacer_link_l, 13, 0, 1, 1)

        self.label_title = QLabel(self.page_add)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setStyleSheet(u"QLabel{\n"
"	text-align: center;\n"
"	font-size: 23px;\n"
"	font: 23pt \"Corbel\";\n"
"    color:        #43454f;\n"
"	pudding: 30px;\n"
"}")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_title, 0, 1, 1, 7)

        self.spacer_login_u = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.spacer_login_u, 1, 1, 3, 7)

        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(8, 1)
        self.gridLayout_4.setRowStretch(11, 1)
        self.gridLayout_4.setRowStretch(14, 1)
        self.gridLayout_4.setColumnStretch(0, 5)
        self.gridLayout_4.setColumnStretch(1, 5)
        self.gridLayout_4.setColumnStretch(2, 5)
        self.gridLayout_4.setColumnStretch(3, 1)
        self.gridLayout_4.setColumnStretch(4, 4)
        self.gridLayout_4.setColumnStretch(5, 2)
        self.gridLayout_4.setColumnStretch(6, 2)
        self.gridLayout_4.setColumnStretch(7, 2)
        self.gridLayout_4.setColumnStretch(8, 5)
        self.stackedWidget.addWidget(self.page_add)

        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 10)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 26))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_picon.setText("")
        self.groupBox_nav.setTitle("")
        self.radioButton_add.setText(QCoreApplication.translate("MainWindow", u"   Add", None))
        self.radioButton_monitored.setText(QCoreApplication.translate("MainWindow", u"   Monitored", None))
        self.radioButton_options.setText(QCoreApplication.translate("MainWindow", u"   Options", None))
        self.radioButton_about.setText(QCoreApplication.translate("MainWindow", u"   About", None))
        self.label_pname.setText(QCoreApplication.translate("MainWindow", u"  WebCheck          ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_link.setText(QCoreApplication.translate("MainWindow", u"Link", None))
        self.pushButton_atc.setText(QCoreApplication.translate("MainWindow", u"Add to cart", None))
#if QT_CONFIG(shortcut)
        self.pushButton_atc.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_buy.setText(QCoreApplication.translate("MainWindow", u"Buy", None))
        self.lineEdit_password.setInputMask("")
        self.lineEdit_password.setText("")
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"password from your account", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit_link.setPlaceholderText(QCoreApplication.translate("MainWindow", u"link to the page that needs to be monitored", None))
        self.label_img_search.setText("")
        self.lineEdit_login.setInputMask("")
        self.lineEdit_login.setText("")
        self.lineEdit_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"login or email from your account", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"email to which the message will be sent", None))
        self.label_login.setText(QCoreApplication.translate("MainWindow", u"Login or email", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Add new monitoring object", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    App = QApplication(sys.argv)
    window = QMainWindow()
    win = Ui_MainWindow()
    win.setupUi(window)
    window.show()
    sys.exit(App.exec_())

