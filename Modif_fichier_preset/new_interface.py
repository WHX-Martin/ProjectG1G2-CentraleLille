# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interface.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTabWidget, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(805, 642)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLocale(QLocale(QLocale.English, QLocale.Europe))
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(self.page)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setUsesScrollButtons(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(50, 10, 50, 10)
        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_16)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(14)
        self.label.setFont(font1)

        self.verticalLayout_2.addWidget(self.label)

        self.comboBox = QComboBox(self.tab)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font1)

        self.verticalLayout_2.addWidget(self.comboBox)

        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setBaseSize(QSize(0, 0))
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QSize(19, 19))

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        self.pushButton_2.setBaseSize(QSize(0, 20))
        self.pushButton_2.setFont(font)

        self.verticalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(50, 10, 50, 10)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMinimumSize(QSize(200, 0))
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(13)
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.lineEdit = QLineEdit(self.tab_2)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy3)
        self.lineEdit.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.toolButton_3 = QToolButton(self.tab_2)
        self.toolButton_3.setObjectName(u"toolButton_3")

        self.horizontalLayout_3.addWidget(self.toolButton_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setMinimumSize(QSize(200, 0))
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.lineEdit_2 = QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_4.addWidget(self.lineEdit_2)

        self.toolButton_4 = QToolButton(self.tab_2)
        self.toolButton_4.setObjectName(u"toolButton_4")

        self.horizontalLayout_4.addWidget(self.toolButton_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.pushButton_3 = QPushButton(self.tab_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 50))
        self.pushButton_3.setFont(font2)

        self.verticalLayout_6.addWidget(self.pushButton_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_13 = QVBoxLayout(self.tab_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(50, 10, 50, 10)
        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_17)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_17 = QLabel(self.tab_5)
        self.label_17.setObjectName(u"label_17")
        sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy2)
        self.label_17.setMinimumSize(QSize(200, 0))
        self.label_17.setFont(font2)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_17)

        self.lineEdit_8 = QLineEdit(self.tab_5)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy3.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy3)
        self.lineEdit_8.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_11.addWidget(self.lineEdit_8)

        self.toolButton_8 = QToolButton(self.tab_5)
        self.toolButton_8.setObjectName(u"toolButton_8")

        self.horizontalLayout_11.addWidget(self.toolButton_8)


        self.verticalLayout_12.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_18)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_18 = QLabel(self.tab_5)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)
        self.label_18.setMinimumSize(QSize(200, 0))
        self.label_18.setFont(font2)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_18)

        self.lineEdit_9 = QLineEdit(self.tab_5)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.horizontalLayout_12.addWidget(self.lineEdit_9)

        self.toolButton_9 = QToolButton(self.tab_5)
        self.toolButton_9.setObjectName(u"toolButton_9")

        self.horizontalLayout_12.addWidget(self.toolButton_9)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_19)

        self.pushButton_6 = QPushButton(self.tab_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 50))
        self.pushButton_6.setFont(font2)

        self.verticalLayout_12.addWidget(self.pushButton_6)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_20)


        self.verticalLayout_13.addLayout(self.verticalLayout_12)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_11 = QVBoxLayout(self.tab_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(50, 10, 50, 10)
        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_15)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_15 = QLabel(self.tab_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_15)

        self.comboBox_2 = QComboBox(self.tab_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font2)

        self.horizontalLayout_9.addWidget(self.comboBox_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_14)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_16 = QLabel(self.tab_4)
        self.label_16.setObjectName(u"label_16")
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)
        self.label_16.setMinimumSize(QSize(140, 0))
        self.label_16.setFont(font2)
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_16)

        self.lineEdit_7 = QLineEdit(self.tab_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy3.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy3)
        self.lineEdit_7.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_10.addWidget(self.lineEdit_7)

        self.toolButton_7 = QToolButton(self.tab_4)
        self.toolButton_7.setObjectName(u"toolButton_7")

        self.horizontalLayout_10.addWidget(self.toolButton_7)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_10)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_11 = QLabel(self.tab_4)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setMinimumSize(QSize(160, 0))
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_11)

        self.lineEdit_5 = QLineEdit(self.tab_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy3.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy3)
        self.lineEdit_5.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_7.addWidget(self.lineEdit_5)

        self.toolButton_5 = QToolButton(self.tab_4)
        self.toolButton_5.setObjectName(u"toolButton_5")

        self.horizontalLayout_7.addWidget(self.toolButton_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.label_13 = QLabel(self.tab_4)
        self.label_13.setObjectName(u"label_13")
        font3 = QFont()
        font3.setFamilies([u"Calibri"])
        font3.setPointSize(10)
        self.label_13.setFont(font3)

        self.verticalLayout_10.addWidget(self.label_13)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_11)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.tab_4)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setMinimumSize(QSize(160, 0))
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_12)

        self.lineEdit_6 = QLineEdit(self.tab_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_8.addWidget(self.lineEdit_6)

        self.toolButton_6 = QToolButton(self.tab_4)
        self.toolButton_6.setObjectName(u"toolButton_6")

        self.horizontalLayout_8.addWidget(self.toolButton_6)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.label_14 = QLabel(self.tab_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)

        self.verticalLayout_10.addWidget(self.label_14)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_12)

        self.pushButton_5 = QPushButton(self.tab_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 50))
        self.pushButton_5.setFont(font2)

        self.verticalLayout_10.addWidget(self.pushButton_5)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_13)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_9 = QVBoxLayout(self.tab_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(50, 10, 50, 10)
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setMinimumSize(QSize(200, 0))
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.lineEdit_3 = QLineEdit(self.tab_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy3.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy3)
        self.lineEdit_3.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.lineEdit_3)

        self.toolButton = QToolButton(self.tab_3)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_5.addWidget(self.toolButton)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setMinimumSize(QSize(200, 0))
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_10)

        self.lineEdit_4 = QLineEdit(self.tab_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_6.addWidget(self.lineEdit_4)

        self.toolButton_2 = QToolButton(self.tab_3)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.horizontalLayout_6.addWidget(self.toolButton_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_8)

        self.pushButton_4 = QPushButton(self.tab_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 50))
        self.pushButton_4.setFont(font2)

        self.verticalLayout_8.addWidget(self.pushButton_4)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_9)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_4.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 805, 26))
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuQuickStart = QMenu(self.menubar)
        self.menuQuickStart.setObjectName(u"menuQuickStart")
        self.menuQuickStart.setLocale(QLocale(QLocale.English, QLocale.Europe))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuQuickStart.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select Spotlight Model:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Model1", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Form: \n"
"ax+b(x>0)\n"
"cx+d(x<0)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"a = 0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"b = 0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"c = 0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"d = 0", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Create a new model", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Select Model", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Presets Folder Path: ", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Excel Export Path: ", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Presets To Excel", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"File(.mvr) Path: ", None))
        self.toolButton_8.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Excel Export Path: ", None))
        self.toolButton_9.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"MVR To Config", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Num of sensors:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"5", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Excel_Config Path: ", None))
        self.toolButton_7.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Excel_M* Path: ", None))
        self.toolButton_5.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Excel_M*: An Excel file containing recorded measurement data of the sensors is required.", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Excel_C*  Path: ", None))
        self.toolButton_6.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Excel_C*: An Excel file containing the data of the presets to correct is required.", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Correct", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Correction", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Excel Path: ", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Presets Folder Path: ", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Excel To Preset", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuQuickStart.setTitle(QCoreApplication.translate("MainWindow", u"QuickStart", None))
    # retranslateUi

