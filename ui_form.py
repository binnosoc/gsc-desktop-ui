# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import rc_resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 709)
        icon = QIcon(QIcon.fromTheme(u"computer"))
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"* {\n"
"padding : 0;\n"
"margin : 0px;\n"
"border : none;\n"
"background-color: transprent;\n"
"color : #fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"background-color : #1f232a;\n"
"}\n"
"\n"
"#label_logo{\n"
"font-size : 50px;\n"
"font-weight : bold;\n"
"letter-spacing: 0px;\n"
"margin-bottom: 5px;\n"
"}\n"
"\n"
"#menuWidget{\n"
"background-color : #1f232a;\n"
"}\n"
"\n"
"QPushButton{\n"
"padding : 2px 5px;\n"
"\n"
"}\n"
"\n"
"#subMenuFrame QPushButton, #adminFrame QPushButton{\n"
"font-size : 16px;\n"
"padding: 12px;\n"
"background-color: #1f232a;\n"
"text-align: left;\n"
"}\n"
"\n"
"#subMenuFrame QPushButton:hover, #adminFrame QPushButton:hover{\n"
"background-color: #2c313c;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"#bodyWidget {\n"
"background-color: #2c313c;\n"
"\n"
"}\n"
"\n"
"#page_home QPushButton{\n"
"font-size: 25px;\n"
"color : #fb5521;\n"
"border: 1px solid  #838ea2;\n"
"font-weight : bold;\n"
"border-radius : 5px;\n"
"}\n"
"\n"
"#page_home QPushButton:hover{\n"
"background-color: #F9F9F9;\n"
"}\n"
"\n"
"#"
                        "frame_btn QPushButton {\n"
"\n"
"	height : 60px;\n"
"font-size: 30px;\n"
"font-weight : bold;\n"
"border-radius : 5px;\n"
"}\n"
"\n"
"#lineEdit_typing {\n"
"padding : 5px 20px;\n"
"text-align : center;\n"
"font-size: 80px;\n"
"font-weight : bold;\n"
"}\n"
"\n"
"\n"
"#moreMenuFrame QPushButton {\n"
"\n"
"\n"
"background-color: #343b44;\n"
"color : #F9F9F9;\n"
"font-weight : bold;\n"
"border-radius : 25px 0px 0px 5px;\n"
"padding: 15px;\n"
"text-align: left;\n"
"}\n"
"\n"
"#moreMenuFrame QPushButton:hover {\n"
"background-color: #343b44;\n"
"\n"
"border: 1px solid #838ea2;\n"
"}\n"
"\n"
"#adminStackedWidget QWidget{\n"
"border: 1px solid #4c5563;\n"
"border-radius : 5px;\n"
"}\n"
"\n"
"#adminStackedWidget QLabel{\n"
"background-color: #343b44;\n"
"border : none;\n"
"color : #F9F9F9;\n"
"}\n"
"\n"
"#adminStackedWidget QLineEdit{\n"
"background-color: #F9F9F9;\n"
"color : #000;\n"
"font-size : 18px;\n"
"padding : 2px 5px;\n"
"}\n"
"\n"
"#label_available_product, #label_expiration_product, #label_rupture_product{\n"
""
                        "text-align : center;\n"
"\n"
"font-weight : bold;\n"
"font-size : 40px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftWidget = QWidget(self.centralwidget)
        self.leftWidget.setObjectName(u"leftWidget")
        self.leftWidget.setMinimumSize(QSize(230, 0))
        self.leftWidget.setMaximumSize(QSize(230, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menuWidget = QWidget(self.leftWidget)
        self.menuWidget.setObjectName(u"menuWidget")
        self.menuWidget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.menuWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.logoFrame = QFrame(self.menuWidget)
        self.logoFrame.setObjectName(u"logoFrame")
        self.logoFrame.setMinimumSize(QSize(0, 50))
        self.logoFrame.setMaximumSize(QSize(16777215, 100))
        self.logoFrame.setFrameShape(QFrame.StyledPanel)
        self.logoFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.logoFrame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.logoPushButton = QPushButton(self.logoFrame)
        self.logoPushButton.setObjectName(u"logoPushButton")
        self.logoPushButton.setMinimumSize(QSize(0, 50))
        icon1 = QIcon()
        icon1.addFile(u":/icon_2/aperture.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logoPushButton.setIcon(icon1)
        self.logoPushButton.setIconSize(QSize(50, 50))

        self.horizontalLayout_13.addWidget(self.logoPushButton)

        self.label_logo = QLabel(self.logoFrame)
        self.label_logo.setObjectName(u"label_logo")

        self.horizontalLayout_13.addWidget(self.label_logo)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.logoFrame)

        self.subMenuFrame = QFrame(self.menuWidget)
        self.subMenuFrame.setObjectName(u"subMenuFrame")
        self.subMenuFrame.setStyleSheet(u"")
        self.subMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.subMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.subMenuFrame)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.accueilPushButton = QPushButton(self.subMenuFrame)
        self.accueilPushButton.setObjectName(u"accueilPushButton")
        icon2 = QIcon()
        icon2.addFile(u":/icon_2/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accueilPushButton.setIcon(icon2)
        self.accueilPushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.accueilPushButton)

        self.newPushButton = QPushButton(self.subMenuFrame)
        self.newPushButton.setObjectName(u"newPushButton")
        self.newPushButton.setMinimumSize(QSize(0, 50))
        self.newPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icon_2/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.newPushButton.setIcon(icon3)
        self.newPushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.newPushButton)

        self.rupturePushButton = QPushButton(self.subMenuFrame)
        self.rupturePushButton.setObjectName(u"rupturePushButton")
        self.rupturePushButton.setMinimumSize(QSize(0, 50))
        self.rupturePushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icon_2/alert-triangle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rupturePushButton.setIcon(icon4)
        self.rupturePushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.rupturePushButton)

        self.expirationPushButton = QPushButton(self.subMenuFrame)
        self.expirationPushButton.setObjectName(u"expirationPushButton")
        self.expirationPushButton.setMinimumSize(QSize(0, 50))
        self.expirationPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.expirationPushButton.setIcon(icon4)
        self.expirationPushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.expirationPushButton)

        self.availablePushButton = QPushButton(self.subMenuFrame)
        self.availablePushButton.setObjectName(u"availablePushButton")
        self.availablePushButton.setMinimumSize(QSize(0, 50))
        self.availablePushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icon_2/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.availablePushButton.setIcon(icon5)
        self.availablePushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.availablePushButton)


        self.verticalLayout_2.addWidget(self.subMenuFrame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.adminFrame = QFrame(self.menuWidget)
        self.adminFrame.setObjectName(u"adminFrame")
        self.adminFrame.setStyleSheet(u"")
        self.adminFrame.setFrameShape(QFrame.StyledPanel)
        self.adminFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.adminFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.adminPushButton = QPushButton(self.adminFrame)
        self.adminPushButton.setObjectName(u"adminPushButton")
        self.adminPushButton.setMinimumSize(QSize(0, 50))
        self.adminPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icon_2/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.adminPushButton.setIcon(icon6)
        self.adminPushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.adminPushButton)

        self.pushButton_6 = QPushButton(self.adminFrame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icon_2/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon7)
        self.pushButton_6.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.pushButton_6)


        self.verticalLayout_2.addWidget(self.adminFrame)


        self.verticalLayout.addWidget(self.menuWidget)


        self.horizontalLayout.addWidget(self.leftWidget)

        self.rightWidget = QWidget(self.centralwidget)
        self.rightWidget.setObjectName(u"rightWidget")
        self.verticalLayout_6 = QVBoxLayout(self.rightWidget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.topBarWidget = QWidget(self.rightWidget)
        self.topBarWidget.setObjectName(u"topBarWidget")
        self.topBarWidget.setMaximumSize(QSize(16777215, 65))
        self.topBarWidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.topBarWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toggleMenuFrame = QFrame(self.topBarWidget)
        self.toggleMenuFrame.setObjectName(u"toggleMenuFrame")
        self.toggleMenuFrame.setMaximumSize(QSize(100, 60))
        self.toggleMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.toggleMenuFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.toggleMenuFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toggleMenuPushButton = QPushButton(self.toggleMenuFrame)
        self.toggleMenuPushButton.setObjectName(u"toggleMenuPushButton")
        self.toggleMenuPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icon_2/chevron-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toggleMenuPushButton.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.toggleMenuPushButton)


        self.horizontalLayout_2.addWidget(self.toggleMenuFrame)

        self.topLabelFrame = QFrame(self.topBarWidget)
        self.topLabelFrame.setObjectName(u"topLabelFrame")
        self.topLabelFrame.setMaximumSize(QSize(16777215, 60))
        self.topLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.topLabelFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.topLabelFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.topLabel = QLabel(self.topLabelFrame)
        self.topLabel.setObjectName(u"topLabel")
        self.topLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.topLabel)


        self.horizontalLayout_2.addWidget(self.topLabelFrame)

        self.actionFrame = QFrame(self.topBarWidget)
        self.actionFrame.setObjectName(u"actionFrame")
        self.actionFrame.setMinimumSize(QSize(0, 0))
        self.actionFrame.setMaximumSize(QSize(200, 60))
        self.actionFrame.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"width : 50px;\n"
"height : 40px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #2c313c;\n"
"\n"
"}\n"
"\n"
"#closePushButton:hover {\n"
"	background-color: red;\n"
"}\n"
"")
        self.actionFrame.setFrameShape(QFrame.StyledPanel)
        self.actionFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.actionFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.reducePushButton = QPushButton(self.actionFrame)
        self.reducePushButton.setObjectName(u"reducePushButton")
        self.reducePushButton.setMinimumSize(QSize(0, 0))
        self.reducePushButton.setMaximumSize(QSize(16777215, 40))
        icon9 = QIcon()
        icon9.addFile(u":/icon_2/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reducePushButton.setIcon(icon9)

        self.horizontalLayout_3.addWidget(self.reducePushButton)

        self.enlargePushButton = QPushButton(self.actionFrame)
        self.enlargePushButton.setObjectName(u"enlargePushButton")
        self.enlargePushButton.setMinimumSize(QSize(0, 0))
        self.enlargePushButton.setMaximumSize(QSize(16777215, 40))
        icon10 = QIcon()
        icon10.addFile(u":/icon_2/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.enlargePushButton.setIcon(icon10)

        self.horizontalLayout_3.addWidget(self.enlargePushButton)

        self.closePushButton = QPushButton(self.actionFrame)
        self.closePushButton.setObjectName(u"closePushButton")
        self.closePushButton.setMinimumSize(QSize(0, 0))
        self.closePushButton.setMaximumSize(QSize(16777215, 40))
        icon11 = QIcon()
        icon11.addFile(u":/icon_2/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closePushButton.setIcon(icon11)

        self.horizontalLayout_3.addWidget(self.closePushButton)


        self.horizontalLayout_2.addWidget(self.actionFrame)


        self.verticalLayout_6.addWidget(self.topBarWidget)

        self.bodyWidget = QWidget(self.rightWidget)
        self.bodyWidget.setObjectName(u"bodyWidget")
        self.bodyWidget.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.bodyWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.bodyWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.gridLayout = QGridLayout(self.page_home)
        self.gridLayout.setObjectName(u"gridLayout")
        self.reportPushButton_2 = QPushButton(self.page_home)
        self.reportPushButton_2.setObjectName(u"reportPushButton_2")
        self.reportPushButton_2.setMinimumSize(QSize(0, 120))
        self.reportPushButton_2.setMaximumSize(QSize(400, 16777215))
        self.reportPushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reportPushButton_2.setIcon(icon12)
        self.reportPushButton_2.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.reportPushButton_2, 3, 0, 1, 1)

        self.availablePushButton_2 = QPushButton(self.page_home)
        self.availablePushButton_2.setObjectName(u"availablePushButton_2")
        self.availablePushButton_2.setMinimumSize(QSize(0, 120))
        self.availablePushButton_2.setMaximumSize(QSize(400, 16777215))
        self.availablePushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.availablePushButton_2.setIcon(icon13)
        self.availablePushButton_2.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.availablePushButton_2, 2, 1, 1, 1)

        self.rupturePushButton_2 = QPushButton(self.page_home)
        self.rupturePushButton_2.setObjectName(u"rupturePushButton_2")
        self.rupturePushButton_2.setMinimumSize(QSize(0, 120))
        self.rupturePushButton_2.setMaximumSize(QSize(400, 16777215))
        self.rupturePushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/alert-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rupturePushButton_2.setIcon(icon14)
        self.rupturePushButton_2.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.rupturePushButton_2, 0, 1, 1, 1)

        self.newPushButton_2 = QPushButton(self.page_home)
        self.newPushButton_2.setObjectName(u"newPushButton_2")
        self.newPushButton_2.setMinimumSize(QSize(0, 120))
        self.newPushButton_2.setMaximumSize(QSize(400, 16777215))
        self.newPushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.newPushButton_2.setIcon(icon15)
        self.newPushButton_2.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.newPushButton_2, 0, 0, 1, 1)

        self.expirationPushButton_2 = QPushButton(self.page_home)
        self.expirationPushButton_2.setObjectName(u"expirationPushButton_2")
        self.expirationPushButton_2.setMinimumSize(QSize(0, 120))
        self.expirationPushButton_2.setMaximumSize(QSize(400, 16777215))
        self.expirationPushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.expirationPushButton_2.setIcon(icon14)
        self.expirationPushButton_2.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.expirationPushButton_2, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_home)
        self.page_new = QWidget()
        self.page_new.setObjectName(u"page_new")
        self.page_new.setStyleSheet(u"border : 1px solid gray;")
        self.horizontalLayout_7 = QHBoxLayout(self.page_new)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.cartFrame = QFrame(self.page_new)
        self.cartFrame.setObjectName(u"cartFrame")
        self.cartFrame.setFrameShape(QFrame.StyledPanel)
        self.cartFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.cartFrame)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.frame_29 = QFrame(self.cartFrame)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)

        self.verticalLayout_44.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.cartFrame)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_30)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_21 = QLabel(self.frame_30)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_45.addWidget(self.label_21, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_44.addWidget(self.frame_30)


        self.horizontalLayout_7.addWidget(self.cartFrame)

        self.recentCartFrame = QFrame(self.page_new)
        self.recentCartFrame.setObjectName(u"recentCartFrame")
        self.recentCartFrame.setMaximumSize(QSize(500, 16777215))
        self.recentCartFrame.setFrameShape(QFrame.StyledPanel)
        self.recentCartFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.recentCartFrame)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.frame_26 = QFrame(self.recentCartFrame)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(16777215, 150))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_26)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.lineEdit_typing = QLineEdit(self.frame_26)
        self.lineEdit_typing.setObjectName(u"lineEdit_typing")
        self.lineEdit_typing.setMinimumSize(QSize(0, 100))

        self.verticalLayout_46.addWidget(self.lineEdit_typing)


        self.verticalLayout_43.addWidget(self.frame_26)

        self.frame_btn = QFrame(self.recentCartFrame)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setFrameShape(QFrame.StyledPanel)
        self.frame_btn.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_btn)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_egal = QPushButton(self.frame_btn)
        self.pushButton_egal.setObjectName(u"pushButton_egal")

        self.gridLayout_5.addWidget(self.pushButton_egal, 3, 2, 1, 1)

        self.pushButton_validate = QPushButton(self.frame_btn)
        self.pushButton_validate.setObjectName(u"pushButton_validate")

        self.gridLayout_5.addWidget(self.pushButton_validate, 4, 2, 1, 1)

        self.pushButton_09 = QPushButton(self.frame_btn)
        self.pushButton_09.setObjectName(u"pushButton_09")

        self.gridLayout_5.addWidget(self.pushButton_09, 0, 2, 1, 1)

        self.pushButton_08 = QPushButton(self.frame_btn)
        self.pushButton_08.setObjectName(u"pushButton_08")

        self.gridLayout_5.addWidget(self.pushButton_08, 0, 1, 1, 1)

        self.pushButton_02 = QPushButton(self.frame_btn)
        self.pushButton_02.setObjectName(u"pushButton_02")

        self.gridLayout_5.addWidget(self.pushButton_02, 2, 1, 1, 1)

        self.pushButton_remove = QPushButton(self.frame_btn)
        self.pushButton_remove.setObjectName(u"pushButton_remove")
        icon16 = QIcon()
        icon16.addFile(u":/icon_2/corner-down-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_remove.setIcon(icon16)

        self.gridLayout_5.addWidget(self.pushButton_remove, 3, 1, 1, 1)

        self.pushButton_05 = QPushButton(self.frame_btn)
        self.pushButton_05.setObjectName(u"pushButton_05")

        self.gridLayout_5.addWidget(self.pushButton_05, 1, 1, 1, 1)

        self.pushButton_03 = QPushButton(self.frame_btn)
        self.pushButton_03.setObjectName(u"pushButton_03")

        self.gridLayout_5.addWidget(self.pushButton_03, 2, 2, 1, 1)

        self.pushButton_00 = QPushButton(self.frame_btn)
        self.pushButton_00.setObjectName(u"pushButton_00")

        self.gridLayout_5.addWidget(self.pushButton_00, 3, 0, 1, 1)

        self.pushButton_06 = QPushButton(self.frame_btn)
        self.pushButton_06.setObjectName(u"pushButton_06")

        self.gridLayout_5.addWidget(self.pushButton_06, 1, 2, 1, 1)

        self.pushButton_07 = QPushButton(self.frame_btn)
        self.pushButton_07.setObjectName(u"pushButton_07")

        self.gridLayout_5.addWidget(self.pushButton_07, 0, 0, 1, 1)

        self.pushButton_04 = QPushButton(self.frame_btn)
        self.pushButton_04.setObjectName(u"pushButton_04")

        self.gridLayout_5.addWidget(self.pushButton_04, 1, 0, 1, 1)

        self.pushButton_cancel = QPushButton(self.frame_btn)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.gridLayout_5.addWidget(self.pushButton_cancel, 4, 1, 1, 1)

        self.pushButton_clear = QPushButton(self.frame_btn)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.gridLayout_5.addWidget(self.pushButton_clear, 4, 0, 1, 1)

        self.pushButton_01 = QPushButton(self.frame_btn)
        self.pushButton_01.setObjectName(u"pushButton_01")

        self.gridLayout_5.addWidget(self.pushButton_01, 2, 0, 1, 1)


        self.verticalLayout_43.addWidget(self.frame_btn)


        self.horizontalLayout_7.addWidget(self.recentCartFrame)

        self.stackedWidget.addWidget(self.page_new)
        self.page_stock_rupture = QWidget()
        self.page_stock_rupture.setObjectName(u"page_stock_rupture")
        self.page_stock_rupture.setStyleSheet(u"")
        self.verticalLayout_34 = QVBoxLayout(self.page_stock_rupture)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.widget_12 = QWidget(self.page_stock_rupture)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(0, 100))
        self.widget_12.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout_35 = QVBoxLayout(self.widget_12)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_rupture_product = QLabel(self.widget_12)
        self.label_rupture_product.setObjectName(u"label_rupture_product")

        self.verticalLayout_35.addWidget(self.label_rupture_product, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_34.addWidget(self.widget_12)

        self.widget_rupture_product = QWidget(self.page_stock_rupture)
        self.widget_rupture_product.setObjectName(u"widget_rupture_product")

        self.verticalLayout_34.addWidget(self.widget_rupture_product)

        self.stackedWidget.addWidget(self.page_stock_rupture)
        self.page_stock_expiration = QWidget()
        self.page_stock_expiration.setObjectName(u"page_stock_expiration")
        self.page_stock_expiration.setStyleSheet(u"")
        self.verticalLayout_32 = QVBoxLayout(self.page_stock_expiration)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.widget_11 = QWidget(self.page_stock_expiration)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 100))
        self.widget_11.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout_33 = QVBoxLayout(self.widget_11)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_expiration_product = QLabel(self.widget_11)
        self.label_expiration_product.setObjectName(u"label_expiration_product")

        self.verticalLayout_33.addWidget(self.label_expiration_product, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_32.addWidget(self.widget_11)

        self.widget_expiration_product = QWidget(self.page_stock_expiration)
        self.widget_expiration_product.setObjectName(u"widget_expiration_product")

        self.verticalLayout_32.addWidget(self.widget_expiration_product)

        self.stackedWidget.addWidget(self.page_stock_expiration)
        self.page_stock_available = QWidget()
        self.page_stock_available.setObjectName(u"page_stock_available")
        self.page_stock_available.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.page_stock_available)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_9 = QWidget(self.page_stock_available)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 100))
        self.widget_9.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout_31 = QVBoxLayout(self.widget_9)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_available_product = QLabel(self.widget_9)
        self.label_available_product.setObjectName(u"label_available_product")

        self.verticalLayout_31.addWidget(self.label_available_product, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_4.addWidget(self.widget_9)

        self.widget_available_product = QWidget(self.page_stock_available)
        self.widget_available_product.setObjectName(u"widget_available_product")

        self.verticalLayout_4.addWidget(self.widget_available_product)

        self.stackedWidget.addWidget(self.page_stock_available)
        self.page_admin = QWidget()
        self.page_admin.setObjectName(u"page_admin")
        self.horizontalLayout_8 = QHBoxLayout(self.page_admin)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.moreMenuFrame = QFrame(self.page_admin)
        self.moreMenuFrame.setObjectName(u"moreMenuFrame")
        self.moreMenuFrame.setMinimumSize(QSize(200, 0))
        self.moreMenuFrame.setMaximumSize(QSize(200, 16777215))
        self.moreMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.moreMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.moreMenuFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.generalPushButton = QPushButton(self.moreMenuFrame)
        self.generalPushButton.setObjectName(u"generalPushButton")
        self.generalPushButton.setMinimumSize(QSize(0, 35))
        self.generalPushButton.setIcon(icon6)

        self.verticalLayout_7.addWidget(self.generalPushButton)

        self.addPushButton = QPushButton(self.moreMenuFrame)
        self.addPushButton.setObjectName(u"addPushButton")
        self.addPushButton.setMinimumSize(QSize(0, 35))
        icon17 = QIcon()
        icon17.addFile(u":/icon_2/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addPushButton.setIcon(icon17)

        self.verticalLayout_7.addWidget(self.addPushButton)

        self.reportPushButton = QPushButton(self.moreMenuFrame)
        self.reportPushButton.setObjectName(u"reportPushButton")
        self.reportPushButton.setMinimumSize(QSize(0, 35))
        icon18 = QIcon()
        icon18.addFile(u":/icon_2/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reportPushButton.setIcon(icon18)

        self.verticalLayout_7.addWidget(self.reportPushButton)

        self.analysePushButton = QPushButton(self.moreMenuFrame)
        self.analysePushButton.setObjectName(u"analysePushButton")
        self.analysePushButton.setMinimumSize(QSize(0, 35))
        icon19 = QIcon()
        icon19.addFile(u":/icon_2/figma.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.analysePushButton.setIcon(icon19)

        self.verticalLayout_7.addWidget(self.analysePushButton)

        self.userPushButton = QPushButton(self.moreMenuFrame)
        self.userPushButton.setObjectName(u"userPushButton")
        self.userPushButton.setMinimumSize(QSize(0, 35))
        icon20 = QIcon()
        icon20.addFile(u":/icon_2/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userPushButton.setIcon(icon20)

        self.verticalLayout_7.addWidget(self.userPushButton)

        self.unitePushButton = QPushButton(self.moreMenuFrame)
        self.unitePushButton.setObjectName(u"unitePushButton")
        self.unitePushButton.setMinimumSize(QSize(0, 35))
        icon21 = QIcon()
        icon21.addFile(u":/icon_2/dollar-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.unitePushButton.setIcon(icon21)

        self.verticalLayout_7.addWidget(self.unitePushButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_8.addWidget(self.moreMenuFrame)

        self.adminStackedWidget = QStackedWidget(self.page_admin)
        self.adminStackedWidget.setObjectName(u"adminStackedWidget")
        self.page_general = QWidget()
        self.page_general.setObjectName(u"page_general")
        self.verticalLayout_8 = QVBoxLayout(self.page_general)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget = QWidget(self.page_general)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 45))
        self.widget.setMaximumSize(QSize(16777215, 45))
        self.widget.setStyleSheet(u"background-color: #838ea2;\n"
"color : #16191d;\n"
"font-weight : bold;\n"
"border-radius : 5px;")
        self.horizontalLayout_10 = QHBoxLayout(self.widget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 0))
        self.pushButton_2.setIcon(icon6)

        self.horizontalLayout_10.addWidget(self.pushButton_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)


        self.verticalLayout_8.addWidget(self.widget)

        self.widget_2 = QWidget(self.page_general)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_11 = QFrame(self.widget_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_11)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_11 = QLabel(self.frame_11)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_18.addWidget(self.label_11)

        self.lineEdit_10 = QLineEdit(self.frame_11)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(0, 0))

        self.verticalLayout_18.addWidget(self.lineEdit_10)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_12)


        self.gridLayout_2.addWidget(self.frame_11, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.widget_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_9.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_9.addWidget(self.lineEdit_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)


        self.gridLayout_2.addWidget(self.frame_3, 0, 2, 1, 1)

        self.frame_10 = QFrame(self.widget_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_10 = QLabel(self.frame_10)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_17.addWidget(self.label_10)

        self.lineEdit_9 = QLineEdit(self.frame_10)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(0, 0))

        self.verticalLayout_17.addWidget(self.lineEdit_9)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_11)


        self.gridLayout_2.addWidget(self.frame_10, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.widget_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_10.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 0))

        self.verticalLayout_10.addWidget(self.lineEdit)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)


        self.gridLayout_2.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame_5 = QFrame(self.widget_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_12.addWidget(self.label_5)

        self.lineEdit_4 = QLineEdit(self.frame_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 0))

        self.verticalLayout_12.addWidget(self.lineEdit_4)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_6)


        self.gridLayout_2.addWidget(self.frame_5, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.widget_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_11.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.frame_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 0))

        self.verticalLayout_11.addWidget(self.lineEdit_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_5)


        self.gridLayout_2.addWidget(self.frame_4, 1, 1, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_13, 2, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.widget_2)

        self.adminStackedWidget.addWidget(self.page_general)
        self.page_user = QWidget()
        self.page_user.setObjectName(u"page_user")
        self.verticalLayout_13 = QVBoxLayout(self.page_user)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_3 = QWidget(self.page_user)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 45))
        self.widget_3.setMaximumSize(QSize(16777215, 45))
        self.widget_3.setStyleSheet(u"background-color: #838ea2;\n"
"color : #16191d;\n"
"font-weight : bold;\n"
"border-radius : 5px;")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_3 = QPushButton(self.widget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setIcon(icon20)

        self.horizontalLayout_11.addWidget(self.pushButton_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)


        self.verticalLayout_13.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.page_user)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_14 = QVBoxLayout(self.widget_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_6 = QFrame(self.widget_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_8)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")

        self.verticalLayout_15.addWidget(self.label)

        self.lineEdit_5 = QLineEdit(self.frame_8)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_15.addWidget(self.lineEdit_5)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_7)


        self.gridLayout_3.addWidget(self.frame_8, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_9)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_16.addWidget(self.label_6)

        self.lineEdit_6 = QLineEdit(self.frame_9)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_16.addWidget(self.lineEdit_6)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_8)


        self.gridLayout_3.addWidget(self.frame_9, 0, 1, 1, 1)

        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_12)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_7 = QLabel(self.frame_12)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_19.addWidget(self.label_7)

        self.lineEdit_7 = QLineEdit(self.frame_12)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout_19.addWidget(self.lineEdit_7)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_9)


        self.gridLayout_3.addWidget(self.frame_12, 0, 2, 1, 1)

        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_13)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_8 = QLabel(self.frame_13)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_22.addWidget(self.label_8)

        self.lineEdit_8 = QLineEdit(self.frame_13)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.verticalLayout_22.addWidget(self.lineEdit_8)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_14)


        self.gridLayout_3.addWidget(self.frame_13, 1, 0, 1, 1)

        self.frame_14 = QFrame(self.frame_6)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_14)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_9 = QLabel(self.frame_14)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_21.addWidget(self.label_9)

        self.lineEdit_11 = QLineEdit(self.frame_14)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.verticalLayout_21.addWidget(self.lineEdit_11)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_15)


        self.gridLayout_3.addWidget(self.frame_14, 1, 1, 1, 1)

        self.frame_15 = QFrame(self.frame_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_15)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_12 = QLabel(self.frame_15)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_20.addWidget(self.label_12)

        self.lineEdit_12 = QLineEdit(self.frame_15)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.verticalLayout_20.addWidget(self.lineEdit_12)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_16)


        self.gridLayout_3.addWidget(self.frame_15, 1, 2, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_6)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_10)

        self.frame_7 = QFrame(self.widget_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 50))
        self.frame_7.setMaximumSize(QSize(16777215, 100))
        self.frame_7.setStyleSheet(u"*{\n"
"border : none;\n"
"font-size: 18px;\n"
"\n"
"padding: 5px 10px;\n"
"}\n"
"\n"
"#listPushButton {\n"
"background-color: green;\n"
"}\n"
"\n"
"#createPushButton {\n"
"width: 60px;\n"
"background-color: red;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.listPushButton = QPushButton(self.frame_7)
        self.listPushButton.setObjectName(u"listPushButton")
        self.listPushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.listPushButton)

        self.createPushButton = QPushButton(self.frame_7)
        self.createPushButton.setObjectName(u"createPushButton")
        self.createPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.createPushButton.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.createPushButton)


        self.verticalLayout_14.addWidget(self.frame_7)


        self.verticalLayout_13.addWidget(self.widget_4)

        self.adminStackedWidget.addWidget(self.page_user)
        self.page_report = QWidget()
        self.page_report.setObjectName(u"page_report")
        self.verticalLayout_36 = QVBoxLayout(self.page_report)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.widget_10 = QWidget(self.page_report)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 45))
        self.widget_10.setMaximumSize(QSize(16777215, 45))
        self.widget_10.setStyleSheet(u"background-color: #838ea2;\n"
"color : #16191d;\n"
"font-weight : bold;\n"
"border-radius : 5px;")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pushButton_4 = QPushButton(self.widget_10)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setIcon(icon18)

        self.horizontalLayout_16.addWidget(self.pushButton_4)

        self.horizontalSpacer_6 = QSpacerItem(467, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_6)


        self.verticalLayout_36.addWidget(self.widget_10)

        self.widget_13 = QWidget(self.page_report)
        self.widget_13.setObjectName(u"widget_13")

        self.verticalLayout_36.addWidget(self.widget_13)

        self.adminStackedWidget.addWidget(self.page_report)
        self.page_analyse = QWidget()
        self.page_analyse.setObjectName(u"page_analyse")
        self.verticalLayout_29 = QVBoxLayout(self.page_analyse)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.widget_17 = QWidget(self.page_analyse)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(0, 45))
        self.widget_17.setMaximumSize(QSize(16777215, 45))
        self.widget_17.setStyleSheet(u"background-color: #838ea2;\n"
"color : #16191d;\n"
"font-weight : bold;\n"
"border-radius : 5px;")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(11, -1, -1, -1)
        self.pushButton = QPushButton(self.widget_17)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setIcon(icon19)

        self.horizontalLayout_15.addWidget(self.pushButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_5)


        self.verticalLayout_29.addWidget(self.widget_17)

        self.widget_16 = QWidget(self.page_analyse)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_38 = QVBoxLayout(self.widget_16)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget_16)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame)
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(11, -1, -1, 0)
        self.horizontalSpacer_9 = QSpacerItem(253, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_9)

        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_19.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_19.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_19.addWidget(self.pushButton_10)


        self.verticalLayout_38.addWidget(self.frame)

        self.stackedWidget_2 = QStackedWidget(self.widget_16)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_39 = QVBoxLayout(self.page)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.widget_19 = QWidget(self.page)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_20 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.widget_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(200, 0))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_20)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(11, -1, 11, 0)
        self.label_20 = QLabel(self.frame_20)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_41.addWidget(self.label_20)

        self.frame_25 = QFrame(self.frame_20)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_25)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.comboBox_categories = QComboBox(self.frame_25)
        self.comboBox_categories.setObjectName(u"comboBox_categories")
        self.comboBox_categories.setMinimumSize(QSize(0, 40))

        self.verticalLayout_42.addWidget(self.comboBox_categories)


        self.verticalLayout_41.addWidget(self.frame_25)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_18)


        self.horizontalLayout_20.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.widget_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_21)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(11, 11, 11, 0)
        self.label_13 = QLabel(self.frame_21)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_40.addWidget(self.label_13)

        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 0))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_23)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(100, 0))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_start_date = QLabel(self.frame_22)
        self.label_start_date.setObjectName(u"label_start_date")
        self.label_start_date.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_23.addWidget(self.label_start_date)

        self.pushButton_start_date = QPushButton(self.frame_22)
        self.pushButton_start_date.setObjectName(u"pushButton_start_date")
        self.pushButton_start_date.setMinimumSize(QSize(40, 40))
        icon22 = QIcon()
        icon22.addFile(u":/icons/icons/clock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_start_date.setIcon(icon22)

        self.horizontalLayout_23.addWidget(self.pushButton_start_date)


        self.horizontalLayout_21.addWidget(self.frame_22)

        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(100, 0))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_end_date = QLabel(self.frame_24)
        self.label_end_date.setObjectName(u"label_end_date")
        self.label_end_date.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_22.addWidget(self.label_end_date)

        self.pushButton_end_date = QPushButton(self.frame_24)
        self.pushButton_end_date.setObjectName(u"pushButton_end_date")
        self.pushButton_end_date.setMinimumSize(QSize(40, 40))
        self.pushButton_end_date.setIcon(icon22)

        self.horizontalLayout_22.addWidget(self.pushButton_end_date)


        self.horizontalLayout_21.addWidget(self.frame_24)


        self.verticalLayout_40.addWidget(self.frame_23)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_40.addItem(self.verticalSpacer_17)


        self.horizontalLayout_20.addWidget(self.frame_21)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_10)


        self.verticalLayout_39.addWidget(self.widget_19)

        self.widget_charts = QWidget(self.page)
        self.widget_charts.setObjectName(u"widget_charts")

        self.verticalLayout_39.addWidget(self.widget_charts)

        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_2.addWidget(self.page_2)

        self.verticalLayout_38.addWidget(self.stackedWidget_2)


        self.verticalLayout_29.addWidget(self.widget_16)

        self.adminStackedWidget.addWidget(self.page_analyse)
        self.page_unite = QWidget()
        self.page_unite.setObjectName(u"page_unite")
        self.verticalLayout_28 = QVBoxLayout(self.page_unite)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.widget_14 = QWidget(self.page_unite)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(0, 45))
        self.widget_14.setMaximumSize(QSize(16777215, 45))
        self.widget_14.setStyleSheet(u"background-color: #838ea2;\n"
"color : #16191d;\n"
"font-weight : bold;\n"
"border-radius : 5px;")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pushButton_7 = QPushButton(self.widget_14)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setIcon(icon21)

        self.horizontalLayout_18.addWidget(self.pushButton_7)

        self.horizontalSpacer_8 = QSpacerItem(557, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_8)


        self.verticalLayout_28.addWidget(self.widget_14)

        self.widget_8 = QWidget(self.page_unite)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_4 = QGridLayout(self.widget_8)
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        self.verticalLayout_28.addWidget(self.widget_8)

        self.adminStackedWidget.addWidget(self.page_unite)
        self.page_scanner = QWidget()
        self.page_scanner.setObjectName(u"page_scanner")
        self.verticalLayout_37 = QVBoxLayout(self.page_scanner)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.widget_15 = QWidget(self.page_scanner)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(0, 45))
        self.widget_15.setMaximumSize(QSize(16777215, 45))
        self.widget_15.setStyleSheet(u"background-color: #838ea2;\n"
"color : #16191d;\n"
"font-weight : bold;\n"
"border-radius : 5px;")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pushButton_5 = QPushButton(self.widget_15)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setIcon(icon17)

        self.horizontalLayout_17.addWidget(self.pushButton_5)

        self.horizontalSpacer_7 = QSpacerItem(479, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_7)


        self.verticalLayout_37.addWidget(self.widget_15)

        self.widget_6 = QWidget(self.page_scanner)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(1677215, 150))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_19 = QFrame(self.widget_6)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_19)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_18 = QLabel(self.frame_19)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_27.addWidget(self.label_18)

        self.lineEdit_17 = QLineEdit(self.frame_19)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMinimumSize(QSize(0, 50))

        self.verticalLayout_27.addWidget(self.lineEdit_17)


        self.horizontalLayout_14.addWidget(self.frame_19)

        self.frame_18 = QFrame(self.widget_6)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_18)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_17 = QLabel(self.frame_18)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_26.addWidget(self.label_17)

        self.lineEdit_16 = QLineEdit(self.frame_18)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMinimumSize(QSize(0, 50))

        self.verticalLayout_26.addWidget(self.lineEdit_16)


        self.horizontalLayout_14.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.widget_6)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_17)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_16 = QLabel(self.frame_17)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_25.addWidget(self.label_16)

        self.lineEdit_15 = QLineEdit(self.frame_17)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setMinimumSize(QSize(0, 50))

        self.verticalLayout_25.addWidget(self.lineEdit_15)


        self.horizontalLayout_14.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.widget_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_16)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_15 = QLabel(self.frame_16)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_24.addWidget(self.label_15)

        self.lineEdit_14 = QLineEdit(self.frame_16)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMinimumSize(QSize(0, 50))

        self.verticalLayout_24.addWidget(self.lineEdit_14)


        self.horizontalLayout_14.addWidget(self.frame_16)

        self.widget_5 = QWidget(self.widget_6)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_30 = QVBoxLayout(self.widget_5)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_14 = QLabel(self.widget_5)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_30.addWidget(self.label_14)

        self.lineEdit_13 = QLineEdit(self.widget_5)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMinimumSize(QSize(0, 50))

        self.verticalLayout_30.addWidget(self.lineEdit_13)


        self.horizontalLayout_14.addWidget(self.widget_5)


        self.verticalLayout_37.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.page_scanner)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 400))
        self.verticalLayout_23 = QVBoxLayout(self.widget_7)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_19 = QLabel(self.widget_7)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_19)


        self.verticalLayout_37.addWidget(self.widget_7)

        self.adminStackedWidget.addWidget(self.page_scanner)

        self.horizontalLayout_8.addWidget(self.adminStackedWidget)

        self.stackedWidget.addWidget(self.page_admin)

        self.horizontalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_6.addWidget(self.bodyWidget)

        self.buttomWidget = QWidget(self.rightWidget)
        self.buttomWidget.setObjectName(u"buttomWidget")
        self.buttomWidget.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_9 = QHBoxLayout(self.buttomWidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.buttomLabel = QLabel(self.buttomWidget)
        self.buttomLabel.setObjectName(u"buttomLabel")
        self.buttomLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.buttomLabel)


        self.verticalLayout_6.addWidget(self.buttomWidget)


        self.horizontalLayout.addWidget(self.rightWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.adminStackedWidget.setCurrentIndex(3)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"G-STOCK", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.logoPushButton.setText("")
        self.label_logo.setText(QCoreApplication.translate("MainWindow", u"GSC", None))
        self.accueilPushButton.setText(QCoreApplication.translate("MainWindow", u" Accueil", None))
        self.newPushButton.setText(QCoreApplication.translate("MainWindow", u" Nouvel enregistrement", None))
        self.rupturePushButton.setText(QCoreApplication.translate("MainWindow", u" Stocks en rupture", None))
        self.expirationPushButton.setText(QCoreApplication.translate("MainWindow", u" Stocks \u00e0 expiration", None))
        self.availablePushButton.setText(QCoreApplication.translate("MainWindow", u" Stocks disponibles", None))
        self.adminPushButton.setText(QCoreApplication.translate("MainWindow", u" Admin", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u" Help", None))
        self.toggleMenuPushButton.setText(QCoreApplication.translate("MainWindow", u" Menu", None))
        self.topLabel.setText(QCoreApplication.translate("MainWindow", u"CONTROLEUR DE FLUX DE STOCK", None))
        self.reducePushButton.setText("")
        self.enlargePushButton.setText("")
        self.closePushButton.setText("")
        self.reportPushButton_2.setText(QCoreApplication.translate("MainWindow", u" Rapport de ventes", None))
        self.availablePushButton_2.setText(QCoreApplication.translate("MainWindow", u" Stocks disponibles", None))
        self.rupturePushButton_2.setText(QCoreApplication.translate("MainWindow", u" Stocks en rupture", None))
        self.newPushButton_2.setText(QCoreApplication.translate("MainWindow", u" Nouvel enregistrement", None))
        self.expirationPushButton_2.setText(QCoreApplication.translate("MainWindow", u" Stocks \u00e0 expiration", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Client suivant", None))
        self.pushButton_egal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton_validate.setText(QCoreApplication.translate("MainWindow", u"VALIDER", None))
        self.pushButton_09.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_08.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_02.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_remove.setText("")
        self.pushButton_05.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_03.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_00.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_06.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_07.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_04.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("MainWindow", u"ANNULER", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"CLEAR", None))
        self.pushButton_01.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_rupture_product.setText(QCoreApplication.translate("MainWindow", u"Liste des produits en vois de rupture", None))
        self.label_expiration_product.setText(QCoreApplication.translate("MainWindow", u"Liste des produits en vois d'expiration", None))
        self.label_available_product.setText(QCoreApplication.translate("MainWindow", u"Liste des stocks disponibles", None))
        self.generalPushButton.setText(QCoreApplication.translate("MainWindow", u" G\u00e9n\u00e9ral", None))
        self.addPushButton.setText(QCoreApplication.translate("MainWindow", u" Ajouter produits", None))
        self.reportPushButton.setText(QCoreApplication.translate("MainWindow", u" Rapports de vente", None))
        self.analysePushButton.setText(QCoreApplication.translate("MainWindow", u"Analyses des tendances", None))
        self.userPushButton.setText(QCoreApplication.translate("MainWindow", u" Utilisateur", None))
        self.unitePushButton.setText(QCoreApplication.translate("MainWindow", u" Unit\u00e9", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u" G\u00e9n\u00e9ral", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Logo de l'application", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Version de l'application", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Nom de l'application", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Autheur de l'application", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Th\u00e8me de l'application", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Langue de l'application", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u" Utilisateur", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nom de l'utilisateur", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"T\u00e9l\u00e9phone", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Droit de permission", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Confirmer mot de passe", None))
        self.listPushButton.setText(QCoreApplication.translate("MainWindow", u"Lister les utilisateurs", None))
        self.createPushButton.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9er", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u" Rapports de vente", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u" Analyse", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Les plus vendus", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Les moins vendus", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"P\u00e9riode de pointe", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Cat\u00e9gorie", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"P\u00e9riode", None))
        self.label_start_date.setText(QCoreApplication.translate("MainWindow", u"D\u00e9but: --:--:-- ", None))
        self.pushButton_start_date.setText("")
        self.label_end_date.setText(QCoreApplication.translate("MainWindow", u"Fin: --:--:--", None))
        self.pushButton_end_date.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u" Unit\u00e9", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u" Ajouter produits", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Devise", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Prix unitaire du produit", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Quantit\u00e9 du produit", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Nom du produit", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Num\u00e9ro du produit", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Scannage code-barres", None))
        self.buttomLabel.setText(QCoreApplication.translate("MainWindow", u"Copyright Innov SOC", None))
    # retranslateUi

