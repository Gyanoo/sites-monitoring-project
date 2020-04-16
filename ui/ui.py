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
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import *
import sys


# import sourse_rc
# import s_delete_rc
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_win()
        self.set_start_state()

    def set_start_state(self):
        self.radioButton_add.setChecked(True)

    def init_win(self):
        self.setGeometry(100, 100, 900, 600)
        self.setStyleSheet(u"")
        self.centralwidget = QWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(900, 500))
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.init_sites()
        self.init_stack()
        self.init_nav()



    def init_sites(self):
        self.frame_sites = QFrame(self.centralwidget)
        self.frame_sites.setStyleSheet(u"QFrame{\n"
                                       "background-color:#83a836;\n"
                                       "}")
        self.frame_sites.setFrameShape(QFrame.StyledPanel)
        self.frame_sites.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_sites, 0, 1, 1, 1)


    def init_stack(self):
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet(u"QWidget{\n"
                                         "background-color:#f2ede1\n"
                                         "}")
        self.init_page_monitored()
        self.init_page_ops()
        self.init_page_about()
        self.init_page_add()

        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 1, 1)


    def init_page_add(self):
        self.page_add = QWidget()
        self.page_add.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.page_add)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_link = QLabel(self.page_add)
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
        self.frame_bottom.setStyleSheet(u"QFrame{\n"
                                        "background-color: #fff;\n"
                                        "padding: 10px;\n"
                                        "}")
        self.frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_bottom)
        self.horizontalSpacer_l = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_l)

        self.pushButton_atc = QPushButton(self.frame_bottom)
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
        self.label_img_search.setMaximumSize(QSize(80, 80))
        self.label_img_search.setStyleSheet(u"QLabel{\n"
                                            "border: 1px solid #000; \n"
                                            "border:none;\n"
                                            "}")
        self.label_img_search.setPixmap(QPixmap(u"img/search.png"))
        self.label_img_search.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_img_search, 7, 5, 1, 1)

        self.lineEdit_login = QLineEdit(self.page_add)
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
        self.label_password.setStyleSheet(u"QLabel{\n"
                                          "	font-size: 23px;\n"
                                          "	font: 12pt \"Corbel\";\n"
                                          "    color:        #43454f;\n"
                                          "}")

        self.gridLayout_4.addWidget(self.label_password, 9, 1, 1, 2)

        self.lineEdit_email = QLineEdit(self.page_add)
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
        self.label_login.setStyleSheet(u"QLabel{\n"
                                       "	font-size: 23px;\n"
                                       "	font: 12pt \"Corbel\";\n"
                                       "    color:        #43454f;\n"
                                       "}")

        self.gridLayout_4.addWidget(self.label_login, 6, 1, 1, 1)

        self.spacer_link_l = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.spacer_link_l, 13, 0, 1, 1)

        self.label_title = QLabel(self.page_add)
        self.label_title.setStyleSheet(u"QLabel{\n"
                                       "	text-align: center;\n"
                                       "	font-size: 23px;\n"
                                       "	font: 23pt \"Corbel\";\n"
                                       "    color:        #43454f;\n"
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


    def init_page_monitored(self):
        self.page_monitored = QWidget()
        self.page_monitored.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_5 = QGridLayout(self.page_monitored)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page_monitored)
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
                                      "	border: none;\n"
                                      "\n"
                                      "\n"
                                      "}")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 654, 479))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setContentsMargins(40, 0, 40, -1)
        self.spaser_list = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.spaser_list, 5, 0, 1, 1)

        self.frame_list_e = QFrame(self.scrollAreaWidgetContents)
        self.frame_list_e.setMinimumSize(QSize(0, 140))
        self.frame_list_e.setStyleSheet(u"QFrame{\n"
                                        " border-bottom: 0.5px solid #aaa\n"
                                        "}")
        self.frame_list_e.setFrameShape(QFrame.StyledPanel)
        self.frame_list_e.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_list_e)
        self.frame_about_e = QFrame(self.frame_list_e)
        self.frame_about_e.setMaximumSize(QSize(440, 16777215))
        self.frame_about_e.setStyleSheet(u"QFrame{\n"
                                         "	border: none;\n"
                                         "}")
        self.frame_about_e.setFrameShape(QFrame.StyledPanel)
        self.frame_about_e.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_about_e)
        self.label_stat = QLabel(self.frame_about_e)
        self.label_stat.setStyleSheet(u"QLabel{\n"
                                      "	border: none;\n"
                                      "	font-size: 23px;\n"
                                      "	font: 10pt \"Corbel\";\n"
                                      "    color:        #43454f;\n"
                                      "}")

        self.gridLayout_8.addWidget(self.label_stat, 2, 1, 1, 1)

        self.label_list_e_name = QLabel(self.frame_about_e)
        self.label_list_e_name.setStyleSheet(u"QLabel{\n"
                                             "	font: 75 12pt \"Noto Serif Lao\";\n"
                                             "	border: none;\n"
                                             "	font-size: 23px;\n"
                                             "	font: 10pt \"Corbel\";\n"
                                             "    font: 75 12pt \"Noto Serif Lao\";\n"
                                             "    color:        #43454f;\n"
                                             "}")
        self.label_list_e_name.setTextFormat(Qt.MarkdownText)
        self.label_list_e_name.setAlignment(Qt.AlignJustify | Qt.AlignVCenter)
        self.label_list_e_name.setWordWrap(False)

        self.gridLayout_8.addWidget(self.label_list_e_name, 0, 0, 1, 2)

        self.label_link_list = QLabel(self.frame_about_e)
        self.label_link_list.setStyleSheet(u"QLabel{\n"
                                           "	border: none;\n"
                                           "	font-size: 23px;\n"
                                           "	font: 10pt \"Corbel\";\n"
                                           "    color:        #43454f;\n"
                                           "}")

        self.gridLayout_8.addWidget(self.label_link_list, 1, 1, 1, 1)

        self.label_img_link_list = QLabel(self.frame_about_e)
        self.label_img_link_list.setMaximumSize(QSize(20, 20))
        self.label_img_link_list.setStyleSheet(u"QLabel{\n"
                                               "	border: none;\n"
                                               "\n"
                                               "}")
        self.label_img_link_list.setPixmap(QPixmap(u"img/link.png"))
        self.label_img_link_list.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_img_link_list, 1, 0, 1, 1)

        self.label_img_stat = QLabel(self.frame_about_e)
        self.label_img_stat.setMaximumSize(QSize(20, 20))
        self.label_img_stat.setStyleSheet(u"QLabel{\n"
                                          "	border: none;\n"
                                          "}")
        self.label_img_stat.setPixmap(QPixmap(u"img/loading.png"))
        self.label_img_stat.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_img_stat, 2, 0, 1, 1)

        self.horizontalLayout_2.addWidget(self.frame_about_e)

        self.spaser_list_e = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.spaser_list_e)

        self.pushButton_delete = QPushButton(self.frame_list_e)

        icon = QIcon()
        icon.addFile(u"img/delete.png", QSize(), QIcon.Selected, QIcon.Off)
        self.pushButton_delete.setIcon(icon)
        self.pushButton_delete.setIconSize(QSize(50, 50))

        self.pushButton_delete.setStyleSheet(u"QPushButton{\n"
                                             "max-width:50px;\n"
                                             "max-height: 50px;\n"
                                             "min-width:50px;\n"
                                             "min-height: 50px;\n"
                                             "border:none;\n"
                                             "border-radius: 0px;\n"
                                             # "background-image: url(img/searching.png);\n"
                                             # "border-image: url(:/qss_icons/rc/delete.png);\n"
                                             # "background-size: cover;\n"
                                             "}\n"
                                             "")

        self.horizontalLayout_2.addWidget(self.pushButton_delete)

        self.gridLayout_7.addWidget(self.frame_list_e, 4, 0, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setStyleSheet(u"QLabel{\n"
                                 "	text-align: center;\n"
                                 "	font-size: 23px;\n"
                                 "	font: 23pt \"Corbel\";\n"
                                 "    color:        #43454f;\n"
                                 "	padding: 30px;\n"
                                 "	border-bottom: 0.5px solid #aaa;\n"
                                 "}")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_monitored)


    def init_page_ops(self):
        self.page_options = QWidget()
        self.gridLayout_6 = QGridLayout(self.page_options)
        self.stackedWidget.addWidget(self.page_options)


    def init_page_about(self):
        self.page_about = QWidget()
        self.gridLayout_9 = QGridLayout(self.page_about)
        self.frame_about = QFrame(self.page_about)
        self.frame_about.setEnabled(True)
        self.frame_about.setStyleSheet(u"QFrame{\n"
                                       " margin: 0px;\n"
                                       " max-height:400px;\n"
                                       " max-width: 600px;\n"
                                       " background-color: #fff;\n"
                                       " border: 10px solid #43454;\n"
                                       " border-color: #43454;\n"
                                       " border-radius: 20%;\n"
                                       "}")
        self.frame_about.setFrameShape(QFrame.StyledPanel)
        self.frame_about.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_about)
        self.gridLayout_10.setContentsMargins(-1, 60, -1, -1)
        self.label_about_version = QLabel(self.frame_about)
        self.label_about_version.setStyleSheet(u"QLabel{\n"
                                               " margin: 0 40px 40px 40px;\n"
                                               " padding-top: 30px;\n"
                                               " border-top: 1px solid #aaa;\n"
                                               " border-radius: none;\n"
                                               " color: #555;\n"
                                               " font: 15pt \"Corbel\";\n"
                                               "}")
        self.label_about_version.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_about_version, 1, 0, 1, 3)

        self.spacer_about_r = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.spacer_about_r, 0, 2, 1, 1)

        self.spacer_about_d = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.spacer_about_d, 3, 1, 1, 1)

        self.spacer_about_l = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.spacer_about_l, 0, 0, 1, 1)

        self.label_about_name = QLabel(self.frame_about)
        self.label_about_name.setStyleSheet(u"QLabel{\n"
                                            "	font-size: 20px;\n"
                                            "	color: #43454f;;\n"
                                            "	font: 25pt \"Reem Kufi\";\n"
                                            "}")
        self.label_about_name.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_about_name, 0, 1, 1, 1)

        self.label_abou_c = QLabel(self.frame_about)
        self.label_abou_c.setStyleSheet(u"QLabel{\n"
                                        " margin: 0 40px 40px 40px;\n"
                                        " color: #555;\n"
                                        " font: 15pt \"Corbel\";\n"
                                        "}")
        self.label_abou_c.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_abou_c, 2, 0, 1, 3)

        self.gridLayout_9.addWidget(self.frame_about, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_about)

    def init_nav(self):
        self.frame_left = QFrame(self.centralwidget)
        self.frame_left.setStyleSheet(u"QFrame{\n"
                                      "background-color:#43454f;\n"
                                      "}")
        self.frame_left.setFrameShape(QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_left)
        self.gridLayout_2.setContentsMargins(11, -1, 11, -1)
        self.spacer_pname_l = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.spacer_pname_l, 2, 0, 1, 1)

        self.label_picon = QLabel(self.frame_left)
        self.label_picon.setMinimumSize(QSize(60, 60))
        self.label_picon.setMaximumSize(QSize(60, 60))
        self.label_picon.setPixmap(QPixmap(u"../../shop_monitoring_python/ui/img/icon.png"))
        self.label_picon.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_picon, 2, 1, 1, 1)

        self.spacer_pname_r = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.spacer_pname_r, 2, 3, 1, 1)

        self.nav_frame = QFrame(self.frame_left)
        self.nav_frame.setMinimumSize(QSize(220, 300))
        self.nav_frame.setStyleSheet(u"QFrame{\n"
                                     "background-color:#43454f;\n"
                                     "}")
        self.nav_frame.setFrameShape(QFrame.StyledPanel)
        self.nav_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.nav_frame)
        self.spacer_gbnav_u = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_3.addItem(self.spacer_gbnav_u, 0, 1, 1, 1)

        self.spacer_gbnav_d = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.spacer_gbnav_d, 2, 1, 1, 1)

        self.spacer_gbnav_l = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.spacer_gbnav_l, 1, 2, 1, 1)

        self.spacer_gbnav_r = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.spacer_gbnav_r, 1, 0, 1, 1)

        self.groupBox_nav = QGroupBox(self.nav_frame)
        self.groupBox_nav.setMinimumSize(QSize(220, 350))
        self.groupBox_nav.setStyleSheet(u"QGroupBox{\n"
                                        "	background-image: url(img/radioline.png);\n"
                                        "	border: none;\n"
                                        "}\n"
                                        "")

        rbutton_css= """
        QRadioButton {
            font: 16pt 'Reem Kufi';
            font-size: 23px;
            font: 13pt 'Corbel';
            color:        #7b826b;
        }
        QRadioButton::indicator {
            background-color: #a8ad9e;
            width: 13px;
            height: 13px;
            border-radius: 11px;
            border: 5px solid #788f49;
        }
        QRadioButton::indicator:checked {
            background-color:		#43454f;
            border:                		5px solid #83a836;
            border-radius:         	11px;
        }
        QRadioButton:checked {
            color:      #83a836;
            border:        none;
        }
        QRadioButton::indicator:unchecked {
            background-color:    #7b826b;
            border:                 5px solid #7b826b;
        }
        """
        self.verticalLayout = QVBoxLayout(self.groupBox_nav)

        self.radioButton_add = QRadioButton(self.groupBox_nav)
        self.radioButton_add.toggled.connect(lambda: self.go_to_page(3))
        self.radioButton_add.setStyleSheet(rbutton_css)
        self.verticalLayout.addWidget(self.radioButton_add)

        self.radioButton_monitored = QRadioButton(self.groupBox_nav)
        self.radioButton_monitored.toggled.connect(lambda: self.go_to_page(0))
        self.radioButton_monitored.setStyleSheet(rbutton_css)
        self.verticalLayout.addWidget(self.radioButton_monitored)

        self.radioButton_options = QRadioButton(self.groupBox_nav)
        self.radioButton_options.toggled.connect(lambda: self.go_to_page(1))
        self.radioButton_options.setStyleSheet(rbutton_css)
        self.verticalLayout.addWidget(self.radioButton_options)

        self.radioButton_about = QRadioButton(self.groupBox_nav)
        self.radioButton_about.toggled.connect(lambda: self.go_to_page(2))
        self.radioButton_about.setStyleSheet(rbutton_css)
        self.verticalLayout.addWidget(self.radioButton_about)

        self.gridLayout_3.addWidget(self.groupBox_nav, 1, 1, 1, 1)

        self.gridLayout_2.addWidget(self.nav_frame, 3, 0, 1, 4)

        self.label_pname = QLabel(self.frame_left)
        self.label_pname.setStyleSheet("""
                                        QLabel{
                                            font-size: 20px;
                                            color: white;
                                            font: 16pt "Reem Kufi";
                                        }
                                        """)

        self.gridLayout_2.addWidget(self.label_pname, 2, 2, 1, 1)

        self.spacer_pname_u = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_2.addItem(self.spacer_pname_u, 1, 1, 1, 2)

        self.gridLayout.addWidget(self.frame_left, 0, 0, 9, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 10)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 900, 26))
        self.setMenuBar(self.menubar)

        self.retranslateUi(self)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_stat.setText(QCoreApplication.translate("MainWindow", u"in progress", None))
        self.label_list_e_name.setText(
                QCoreApplication.translate("MainWindow", u"BUTY HALOWE ASICS GEL-ROCKET 9 1071A030-400 47",None))
        self.label_link_list.setText(QCoreApplication.translate("MainWindow", u"check hire", None))
        self.label_img_link_list.setText("")
        self.label_img_stat.setText("")
        self.pushButton_delete.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"List of your monitered objects", None))
        self.label_about_version.setText(QCoreApplication.translate("MainWindow", u"Version 1.0.0", None))
        self.label_about_name.setText(QCoreApplication.translate("MainWindow", u"WebCheck", None))
        self.label_abou_c.setText(QCoreApplication.translate("MainWindow", u"\u00a9 All rights reserved", None))
        self.label_link.setText(QCoreApplication.translate("MainWindow", u"Link", None))
        self.pushButton_atc.setText(QCoreApplication.translate("MainWindow", u"Add to cart", None))
        # if QT_CONFIG(shortcut)
        self.pushButton_atc.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
        # endif // QT_CONFIG(shortcut)
        self.pushButton_buy.setText(QCoreApplication.translate("MainWindow", u"Buy", None))
        self.lineEdit_password.setInputMask("")
        self.lineEdit_password.setText("")
        self.lineEdit_password.setPlaceholderText(
                QCoreApplication.translate("MainWindow", u"password from your account", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit_link.setPlaceholderText(
                QCoreApplication.translate("MainWindow", u"link to the page that needs to be monitored", None))
        self.label_img_search.setText("")
        self.lineEdit_login.setInputMask("")
        self.lineEdit_login.setText("")
        self.lineEdit_login.setPlaceholderText(
                QCoreApplication.translate("MainWindow", u"login or email from your account", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_email.setPlaceholderText(
                QCoreApplication.translate("MainWindow", u"email to which the message will be sent", None))
        self.label_login.setText(QCoreApplication.translate("MainWindow", u"Login or email", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Add new monitoring object", None))
        self.label_picon.setText("")
        self.groupBox_nav.setTitle("")
        self.radioButton_add.setText(QCoreApplication.translate("MainWindow", u"   Add", None))
        self.radioButton_monitored.setText(QCoreApplication.translate("MainWindow", u"   Monitored", None))
        self.radioButton_options.setText(QCoreApplication.translate("MainWindow", u"   Options", None))
        self.radioButton_about.setText(QCoreApplication.translate("MainWindow", u"   About", None))
        self.label_pname.setText(QCoreApplication.translate("MainWindow", u"WebCheck          ", None))


    def go_to_page(self, index):
        if index == 0:
            self.stackedWidget.setCurrentIndex(0)
        elif index == 1:
            self.stackedWidget.setCurrentIndex(1)
        elif index == 2:
            self.stackedWidget.setCurrentIndex(2)
        elif index == 3:
            self.stackedWidget.setCurrentIndex(3)


def window():
        app = QApplication(sys.argv)
        win = MainWindow()
        win.show()
        sys.exit(app.exec_())
window()