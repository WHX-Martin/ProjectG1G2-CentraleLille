# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interface.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os, sys, re
import json
import shutil
import read_excel as cpre
import read_preset as rpre

from openpyxl import load_workbook
from openpyxl.utils.exceptions import InvalidFileException

sys.path.append(os.getcwd())
import calcul_erreur.corrige as corrige
import create_config
import Read_mvr

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QStatusBar,
    QTabWidget,
    QToolButton,
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QDialog,
    QFormLayout,
    QDoubleSpinBox,
    QDialogButtonBox,
    QMessageBox,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Variables
        # json file path
        self.file_path = "data/data.json"
        self.parameters = self.load_parameters_from_file()

        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 642)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setLocale(QLocale(QLocale.English, QLocale.Europe))
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QTabWidget(self.page)
        self.tabWidget.setObjectName("tabWidget")
        font = QFont()
        font.setFamilies(["Calibri"])
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setUsesScrollButtons(True)
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(50, 10, 50, 10)
        self.verticalSpacer_16 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_16)

        self.label = QLabel(self.tab)
        self.label.setObjectName("label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies(["Calibri"])
        font1.setPointSize(14)
        self.label.setFont(font1)

        self.verticalLayout_2.addWidget(self.label)

        self.comboBox = QComboBox(self.tab)
        self.comboBox.addItem("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setFont(font1)
        self.comboBox.setStyleSheet("color: white;")
        self.comboBox.addItems(self.parameters.keys())

        self.verticalLayout_2.addWidget(self.comboBox)

        self.widget = QWidget(self.tab)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_6)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(
            20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        self.pushButton_2.setBaseSize(QSize(0, 20))
        self.pushButton_2.setFont(font)

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.verticalLayout_2.addWidget(self.widget)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(50, 10, 50, 10)
        self.verticalSpacer_4 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMinimumSize(QSize(200, 0))
        font2 = QFont()
        font2.setFamilies(["Calibri"])
        font2.setPointSize(13)
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.lineEdit = QLineEdit(self.tab_2)
        self.lineEdit.setObjectName("lineEdit")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy3)
        self.lineEdit.setMinimumSize(QSize(0, 0))
        self.lineEdit.setStyleSheet("color:white;")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.toolButton_3 = QToolButton(self.tab_2)
        self.toolButton_3.setObjectName("toolButton_3")

        self.horizontalLayout_3.addWidget(self.toolButton_3)

        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setMinimumSize(QSize(200, 0))
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.lineEdit_2 = QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("color:white;")

        self.horizontalLayout_4.addWidget(self.lineEdit_2)

        self.toolButton_4 = QToolButton(self.tab_2)
        self.toolButton_4.setObjectName("toolButton_4")

        self.horizontalLayout_4.addWidget(self.toolButton_4)

        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.pushButton_3 = QPushButton(self.tab_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 50))
        self.pushButton_3.setFont(font2)

        self.verticalLayout_6.addWidget(self.pushButton_3)

        self.verticalSpacer_5 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_13 = QVBoxLayout(self.tab_5)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(50, 10, 50, 10)
        self.verticalSpacer_18 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_12.addItem(self.verticalSpacer_18)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_19 = QLabel(self.tab_5)
        self.label_19.setObjectName("label_19")
        sizePolicy2.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy2)
        self.label_19.setMinimumSize(QSize(200, 0))
        self.label_19.setFont(font2)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_19)

        self.lineEdit_10 = QLineEdit(self.tab_5)
        self.lineEdit_10.setObjectName("lineEdit_10")
        sizePolicy3.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy3)
        self.lineEdit_10.setMinimumSize(QSize(0, 0))
        self.lineEdit_10.setStyleSheet("color:white;")

        self.horizontalLayout_13.addWidget(self.lineEdit_10)

        self.toolButton_10 = QToolButton(self.tab_5)
        self.toolButton_10.setObjectName("toolButton_10")

        self.horizontalLayout_13.addWidget(self.toolButton_10)

        self.verticalLayout_12.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_19 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_12.addItem(self.verticalSpacer_19)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_18 = QLabel(self.tab_5)
        self.label_18.setObjectName("label_18")
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)
        self.label_18.setMinimumSize(QSize(200, 0))
        self.label_18.setFont(font2)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_18)

        self.lineEdit_9 = QLineEdit(self.tab_5)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setStyleSheet("color:white;")

        self.horizontalLayout_12.addWidget(self.lineEdit_9)

        self.toolButton_9 = QToolButton(self.tab_5)
        self.toolButton_9.setObjectName("toolButton_9")

        self.horizontalLayout_12.addWidget(self.toolButton_9)

        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_20 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_12.addItem(self.verticalSpacer_20)

        self.pushButton_6 = QPushButton(self.tab_5)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 50))
        self.pushButton_6.setFont(font2)

        self.verticalLayout_12.addWidget(self.pushButton_6)

        self.verticalSpacer_21 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_12.addItem(self.verticalSpacer_21)

        self.verticalLayout_13.addLayout(self.verticalLayout_12)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_11 = QVBoxLayout(self.tab_4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(50, 10, 50, 10)
        self.verticalSpacer_15 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_10.addItem(self.verticalSpacer_15)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_15 = QLabel(self.tab_4)
        self.label_15.setObjectName("label_15")
        self.label_15.setFont(font2)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_15)

        self.comboBox_2 = QComboBox(self.tab_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setFont(font2)
        self.comboBox_2.setStyleSheet("color: white;")

        self.horizontalLayout_9.addWidget(self.comboBox_2)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_14 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_10.addItem(self.verticalSpacer_14)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_16 = QLabel(self.tab_4)
        self.label_16.setObjectName("label_16")
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)
        self.label_16.setMinimumSize(QSize(150, 0))
        self.label_16.setFont(font2)
        self.label_16.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_16)

        self.lineEdit_7 = QLineEdit(self.tab_4)
        self.lineEdit_7.setObjectName("lineEdit_7")
        sizePolicy3.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy3)
        self.lineEdit_7.setMinimumSize(QSize(0, 0))
        self.lineEdit_7.setStyleSheet("color:white;")

        self.horizontalLayout_10.addWidget(self.lineEdit_7)

        self.toolButton_7 = QToolButton(self.tab_4)
        self.toolButton_7.setObjectName("toolButton_7")

        self.horizontalLayout_10.addWidget(self.toolButton_7)

        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_10 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_10.addItem(self.verticalSpacer_10)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QLabel(self.tab_4)
        self.label_11.setObjectName("label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setMinimumSize(QSize(150, 0))
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_11)

        self.lineEdit_5 = QLineEdit(self.tab_4)
        self.lineEdit_5.setObjectName("lineEdit_5")
        sizePolicy3.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy3)
        self.lineEdit_5.setMinimumSize(QSize(0, 0))
        self.lineEdit_5.setStyleSheet("color:white;")

        self.horizontalLayout_7.addWidget(self.lineEdit_5)

        self.toolButton_5 = QToolButton(self.tab_4)
        self.toolButton_5.setObjectName("toolButton_5")

        self.horizontalLayout_7.addWidget(self.toolButton_5)

        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.label_13 = QLabel(self.tab_4)
        self.label_13.setObjectName("label_13")
        font3 = QFont()
        font3.setFamilies(["Calibri"])
        font3.setPointSize(10)
        self.label_13.setFont(font3)

        self.verticalLayout_10.addWidget(self.label_13)

        self.verticalSpacer_11 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_10.addItem(self.verticalSpacer_11)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_12 = QLabel(self.tab_4)
        self.label_12.setObjectName("label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setMinimumSize(QSize(150, 0))
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_12)

        self.lineEdit_6 = QLineEdit(self.tab_4)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setStyleSheet("color:white;")

        self.horizontalLayout_8.addWidget(self.lineEdit_6)

        self.toolButton_6 = QToolButton(self.tab_4)
        self.toolButton_6.setObjectName("toolButton_6")

        self.horizontalLayout_8.addWidget(self.toolButton_6)

        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.label_14 = QLabel(self.tab_4)
        self.label_14.setObjectName("label_14")
        self.label_14.setFont(font3)

        self.verticalLayout_10.addWidget(self.label_14)

        self.verticalSpacer_12 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_10.addItem(self.verticalSpacer_12)

        self.pushButton_5 = QPushButton(self.tab_4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 50))
        self.pushButton_5.setFont(font2)

        self.verticalLayout_10.addWidget(self.pushButton_5)

        self.verticalSpacer_13 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_10.addItem(self.verticalSpacer_13)

        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_9 = QVBoxLayout(self.tab_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(50, 10, 50, 10)
        self.verticalSpacer_6 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_8.addItem(self.verticalSpacer_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName("label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setMinimumSize(QSize(200, 0))
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.lineEdit_3 = QLineEdit(self.tab_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        sizePolicy3.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy3)
        self.lineEdit_3.setMinimumSize(QSize(0, 0))
        self.lineEdit_3.setStyleSheet("color:white;")

        self.horizontalLayout_5.addWidget(self.lineEdit_3)

        self.toolButton = QToolButton(self.tab_3)
        self.toolButton.setObjectName("toolButton")

        self.horizontalLayout_5.addWidget(self.toolButton)

        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_7 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_8.addItem(self.verticalSpacer_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName("label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setMinimumSize(QSize(200, 0))
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_10)

        self.lineEdit_4 = QLineEdit(self.tab_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setStyleSheet("color:white;")

        self.horizontalLayout_6.addWidget(self.lineEdit_4)

        self.toolButton_2 = QToolButton(self.tab_3)
        self.toolButton_2.setObjectName("toolButton_2")

        self.horizontalLayout_6.addWidget(self.toolButton_2)

        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_8 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_8.addItem(self.verticalSpacer_8)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_17 = QLabel(self.tab_3)
        self.label_17.setObjectName("label_17")
        sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy2)
        self.label_17.setMinimumSize(QSize(200, 0))
        self.label_17.setFont(font2)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_17)

        self.lineEdit_8 = QLineEdit(self.tab_3)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setStyleSheet("color:white;")

        self.horizontalLayout_11.addWidget(self.lineEdit_8)

        self.toolButton_8 = QToolButton(self.tab_3)
        self.toolButton_8.setObjectName("toolButton_8")

        self.horizontalLayout_11.addWidget(self.toolButton_8)

        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_17 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_8.addItem(self.verticalSpacer_17)

        self.pushButton_4 = QPushButton(self.tab_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 50))
        self.pushButton_4.setFont(font2)

        self.verticalLayout_8.addWidget(self.pushButton_4)

        self.verticalSpacer_9 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_8.addItem(self.verticalSpacer_9)

        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_4.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 805, 26))
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        # self.menuQuickStart = QMenu(self.menubar)
        # self.menuQuickStart.setObjectName("menuQuickStart")
        # self.menuQuickStart.setLocale(QLocale(QLocale.English, QLocale.Europe))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # self.menubar.addAction(self.menuQuickStart.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

        # Slot links
        self.toolButton_3.clicked.connect(
            lambda: self.open_folder_dialog(self.lineEdit)
        )
        self.toolButton_4.clicked.connect(
            lambda: self.open_save_file_dialog(self.lineEdit_2)
        )
        self.toolButton_10.clicked.connect(
            lambda: self.open_mvr_file_dialog(self.lineEdit_10)
        )
        self.toolButton_9.clicked.connect(
            lambda: self.open_save_file_dialog(self.lineEdit_9)
        )
        self.toolButton_7.clicked.connect(
            lambda: self.open_file_dialog(self.lineEdit_7)
        )
        self.toolButton_5.clicked.connect(
            lambda: self.open_file_dialog(self.lineEdit_5)
        )
        self.toolButton_6.clicked.connect(
            lambda: self.open_file_dialog(self.lineEdit_6)
        )
        self.toolButton.clicked.connect(lambda: self.open_file_dialog(self.lineEdit_3))
        self.toolButton_2.clicked.connect(
            lambda: self.open_folder_dialog(self.lineEdit_4)
        )
        self.toolButton_8.clicked.connect(
            lambda: self.open_folder_dialog(self.lineEdit_8)
        )
        self.pushButton_3.clicked.connect(
            lambda: self.readPreset(self.lineEdit.text(), self.lineEdit_2.text())
        )
        self.pushButton_4.clicked.connect(
            lambda: self.changePreset(
                self.lineEdit_4.text(), self.lineEdit_3.text(), self.lineEdit_8.text()
            )
        )
        self.comboBox.currentTextChanged.connect(self.load_parameters)
        self.pushButton.clicked.connect(self.open_new_model_dialog)
        self.pushButton_2.clicked.connect(lambda: self.change_tab(1))
        self.pushButton_5.clicked.connect(self.corrige_erreur)
        self.pushButton_6.clicked.connect(
            lambda: self.mvr_to_config(self.lineEdit_10.text(), self.lineEdit_9.text())
        )

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", "Select Spotlight Model:", None)
        )
        self.comboBox.setItemText(
            0, QCoreApplication.translate("MainWindow", "Model1", None)
        )

        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                "x : theoretical tilt\n"
                "y : real tilt\n"
                "Form: \n"
                "y = ax+b(x>=0)\n"
                "y = cx+d(x<0)\n",
                None,
            )
        )
        self.label_3.setText(QCoreApplication.translate("MainWindow", "a = 0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", "b = 0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", "c = 0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", "d = 0", None))
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", "Create a new model", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", "Select", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("MainWindow", "Select Model", None),
        )
        self.label_7.setText(
            QCoreApplication.translate(
                "MainWindow", "Preset Source Folder Path: ", None
            )
        )
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", "...", None))
        self.label_8.setText(
            QCoreApplication.translate(
                "MainWindow", "Excel Preset Source Export: ", None
            )
        )
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", "...", None))
        self.pushButton_3.setText(
            QCoreApplication.translate("MainWindow", "Export", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("MainWindow", "Presets To Excel", None),
        )
        self.label_19.setText(
            QCoreApplication.translate("MainWindow", "File(.mvr) Path: ", None)
        )
        self.toolButton_10.setText(
            QCoreApplication.translate("MainWindow", "...", None)
        )
        self.label_18.setText(
            QCoreApplication.translate("MainWindow", "Excel Export Path: ", None)
        )
        self.toolButton_9.setText(QCoreApplication.translate("MainWindow", "...", None))
        self.pushButton_6.setText(
            QCoreApplication.translate("MainWindow", "Export", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_5),
            QCoreApplication.translate("MainWindow", "MVR To Config", None),
        )
        self.label_15.setText(
            QCoreApplication.translate("MainWindow", "Num of sensors:", None)
        )
        self.comboBox_2.setItemText(
            0, QCoreApplication.translate("MainWindow", "4", None)
        )
        self.comboBox_2.setItemText(
            1, QCoreApplication.translate("MainWindow", "5", None)
        )

        self.label_16.setText(
            QCoreApplication.translate("MainWindow", "Excel_Config Path: ", None)
        )
        self.toolButton_7.setText(QCoreApplication.translate("MainWindow", "...", None))
        self.label_11.setText(
            QCoreApplication.translate(
                "MainWindow", "Excel Preset Sensors Path: ", None
            )
        )
        self.toolButton_5.setText(QCoreApplication.translate("MainWindow", "...", None))
        self.label_13.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Excel Preset Sensors: An Excel file containing recorded measurement data of the sensors is required.",
                None,
            )
        )
        self.label_12.setText(
            QCoreApplication.translate(
                "MainWindow", "Excel Preset Source Path:   ", None
            )
        )
        self.toolButton_6.setText(QCoreApplication.translate("MainWindow", "...", None))
        self.label_14.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Excel Preset Source: An Excel file containing the data of the presets to correct is required.",
                None,
            )
        )
        self.pushButton_5.setText(
            QCoreApplication.translate("MainWindow", "Correct", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_4),
            QCoreApplication.translate("MainWindow", "Correction", None),
        )
        self.label_9.setText(
            QCoreApplication.translate("MainWindow", "Excel Preset Final Path: ", None)
        )
        self.toolButton.setText(QCoreApplication.translate("MainWindow", "...", None))
        self.label_10.setText(
            QCoreApplication.translate(
                "MainWindow", "Preset Source Folder Path: ", None
            )
        )
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", "...", None))
        self.label_17.setText(
            QCoreApplication.translate("MainWindow", "Preset Export Path: ", None)
        )
        self.toolButton_8.setText(QCoreApplication.translate("MainWindow", "...", None))
        self.pushButton_4.setText(
            QCoreApplication.translate("MainWindow", "Export", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3),
            QCoreApplication.translate("MainWindow", "Excel To Presets", None),
        )
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", "Tools", None))
        # self.menuQuickStart.setTitle(
        #     QCoreApplication.translate("MainWindow", "QuickStart", None)
        # )

    # retranslateUi

    # Slot functions
    # Slot function: select folder path
    def open_folder_dialog(self, line_edit):

        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            line_edit.setText(folder_path)

    # Slot function: select excel path
    def open_file_dialog(self, line_edit):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Excel File", "", "Excel Files (*.xlsx *.xls);;All Files (*)"
        )
        if file_path:
            line_edit.setText(file_path)

    # Slot function: select mvr path
    def open_mvr_file_dialog(self, line_edit):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select MVR File", "", "MVR Files (*.mvr);;All Files (*)"
        )
        if file_path:
            line_edit.setText(file_path)

    # Slot function: select save path and name of the Excel
    def open_save_file_dialog(self, line_edit):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save File As",
            "",  # 默认目录（空字符串表示当前目录）
            "Excel Files (*.xlsx *.xls);;All Files (*)",  # 文件过滤器
        )
        if file_path:  # 如果用户指定了文件
            line_edit.setText(file_path)  # 将保存路径和文件名显示到 QLineEdit 中

    # Slot function: read presets informations
    def readPreset(self, xml_folder_path, excel_path):
        if xml_folder_path and excel_path:
            if self.is_excel_file_open(excel_path):
                self.show_warning_dialog("Excel not closed!")
                return
            excel_folder_path = os.path.dirname(excel_path)
            excel_name = os.path.basename(excel_path)
            base, ext = os.path.splitext(excel_name)
            base_excel_sensor = base + "_sensor"
            base_excel_source = base + "_source"
            excel_sensor_name = base_excel_sensor + ext
            excel_source_name = base_excel_source + ext
            excel_sensor_path = os.path.join(excel_folder_path, excel_sensor_name)
            excel_source_path = os.path.join(excel_folder_path, excel_source_name)
            # Get all the xml files in the folder
            xml_files = rpre.get_xml_files(xml_folder_path)
            print("xml file in the folder：", xml_files)
            for file in xml_files:
                data = rpre.readXml(file)
                rpre.writeExcel(data, excel_path)
                if not re.fullmatch(r".*Sensor_\d+\.xml", file):
                    rpre.writeExcel(data, excel_source_path)
                else:
                    rpre.writeExcel(data, excel_sensor_path)

    # Slot function: copy and change presets
    def changePreset(self, xml_folder_path, excel_path, export_path):
        if self.is_excel_file_open(excel_path) or self.is_excel_file_open(export_path):
            self.show_warning_dialog("Excel not closed!")
            return
        # create a new folder
        # new_folder_path = os.path.join(xml_folder_path, "presets_change")
        new_folder_path = export_path
        # create folder if not exist
        # if not os.path.exists(new_folder_path):
        #     os.makedirs(new_folder_path)
        #     print(f"Create folder: {new_folder_path}")

        # walk through xml_folder_path and copy xml files to the new folder
        for filename in os.listdir(xml_folder_path):
            # check if xml and not preset sensor
            if not re.fullmatch(r".*Sensor_\d+\.xml", filename) and filename.endswith(
                ".xml"
            ):
                new_filename = "corrected_" + filename
                src_file_path = os.path.join(xml_folder_path, filename)
                dst_file_path = os.path.join(new_folder_path, new_filename)
                shutil.copy2(src_file_path, dst_file_path)
                print(f"Copy: {src_file_path} -> {dst_file_path}")

        print(f"all XML files are copyed into folder: {export_path}")
        if xml_folder_path and excel_path:
            noms_feuilles = cpre.obtenir_noms_feuilles(excel_path)
            for nom_feuille in noms_feuilles:
                valeurs_pan_tilt_par_id = cpre.recuperer_pan_tilt_par_id(
                    excel_path, nom_feuille
                )
                for id_unique, valeurs in valeurs_pan_tilt_par_id.items():
                    print(
                        f"ID: {id_unique}, Pan: {valeurs['Pan']}, Tilt: {valeurs['Tilt']}"
                    )
                    cpre.modifier_xml(
                        new_folder_path + f"/corrected_{nom_feuille}",
                        id_unique,
                        "Pan",
                        valeurs["Pan"][0],
                    )
                    cpre.modifier_xml(
                        new_folder_path + f"/corrected_{nom_feuille}",
                        id_unique,
                        "Tilt",
                        valeurs["Tilt"][0],
                    )

    # Slot Function: load model parameters by name
    def load_parameters(self):

        selected_name = self.comboBox.currentText()
        params = self.parameters.get(selected_name, {})
        if params:
            self.label_3.setText(f"a = {params['a']}")
            self.label_4.setText(f"b = {params['b']}")
            self.label_5.setText(f"c = {params['c']}")
            self.label_6.setText(f"d = {params['d']}")

    # Function: load parameters from json file
    def load_parameters_from_file(self):

        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print(
                        "Failed to decode JSON. Starting with an empty parameter set."
                    )
        return {}

    # Function: save parameters in json file
    def save_parameters_to_file(self):

        with open(self.file_path, "w") as file:
            json.dump(self.parameters, file, indent=4)
        print("Parameters saved to file.")

    # Slot function: open parameters save window
    def open_new_model_dialog(self):

        dialog = NewModelDialog(self)
        if dialog.exec() == QDialog.Accepted:
            name, params = dialog.get_data()
            if name and name not in self.parameters:
                # save to parameters
                self.parameters[name] = params

                # renew ComboBox
                self.comboBox.addItem(name)

                self.save_parameters_to_file()
                print(f"New model saved: {name} -> {params}")
            else:
                print("Invalid or duplicate name, not saved.")

    # Slot function: change the tab num of the tabWidget
    def change_tab(self, n):
        if n < 4 and n >= 0:
            self.tabWidget.setCurrentIndex(n)

    # Slot function: corrige the erreurs
    def corrige_erreur(self):
        config_path = self.lineEdit_7.text()
        sensors_dict, spotlight_dict = corrige.readConfig(config_path)
        position_sensors = []
        for key, values in sensors_dict.items():
            position_sensors.append(values)
        file_path = self.lineEdit_5.text()
        file_path_change = self.lineEdit_6.text()
        model_name = self.comboBox.currentText()
        params = self.parameters[model_name]
        a = params["a"]
        b = params["b"]
        c = params["c"]
        d = params["d"]
        num_sensor = int(self.comboBox_2.currentText())
        if config_path and file_path and file_path_change:
            if (
                self.is_excel_file_open(config_path)
                or self.is_excel_file_open(file_path)
                or self.is_excel_file_open(file_path_change)
            ):
                self.show_warning_dialog(f"Excel not closed!")
                return
            corrige.corrigePreset(
                file_path,
                file_path_change,
                position_sensors,
                spotlight_dict,
                a,
                b,
                c,
                d,
                num_sensor,
            )

    # Slot Function : read mvr file and create config excel
    def mvr_to_config(self, mvr_path, export_path):
        create_config.create_excel_template(export_path)
        Read_mvr.add_mvr_data(mvr_path, export_path)

    # Function : check if excel is open
    def is_excel_file_open(self, file_path):
        """
        Checks if an Excel file is open by attempting to rename it.

        Args:
            file_path: The path to the Excel file.

        Returns:
            True if the file is open, False otherwise.
        """
        if not os.path.exists(file_path):
            return False  # File doesn't exist

        try:
            # Try to rename the file by appending a temporary suffix
            #     temp_file_path = file_path + "_temp"
            #     os.rename(file_path, temp_file_path)
            #     os.rename(temp_file_path, file_path)  # Rename it back
            #     return False
            # except OSError:
            #     return True
            wb = load_workbook(filename=file_path)
            return False  # 文件没有被锁定
        except PermissionError:
            return True  # 文件被另一个程序打开
        except FileNotFoundError:
            return False  # 文件不存在
        except InvalidFileException:
            return False  # 文件不是有效的Excel文件
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return True  # 处理其他未预见的异常

    # Function : show the warning window
    def show_warning_dialog(self, message):
        """
        show warning if Excel not closed

        Args:
            message: message to show
        """
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Warning")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()


class NewModelDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("New Model")

        layout = QFormLayout(self)

        # name input
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter model name")
        self.name_input.setStyleSheet("color:white;")
        layout.addRow("Name:", self.name_input)

        # parameters input
        self.spin_a = QDoubleSpinBox(self)
        self.spin_a.setRange(-100, 100)
        self.spin_a.setStyleSheet("color:white;")
        self.spin_a.setSingleStep(0.1)
        self.spin_a.setDecimals(3)
        self.spin_b = QDoubleSpinBox(self)
        self.spin_b.setRange(-100, 100)
        self.spin_b.setStyleSheet("color:white;")
        self.spin_b.setSingleStep(0.1)
        self.spin_b.setDecimals(3)
        self.spin_c = QDoubleSpinBox(self)
        self.spin_c.setRange(-100, 100)
        self.spin_c.setStyleSheet("color:white;")
        self.spin_c.setSingleStep(0.1)
        self.spin_c.setDecimals(3)
        self.spin_d = QDoubleSpinBox(self)
        self.spin_d.setRange(-100, 100)
        self.spin_d.setStyleSheet("color:white;")
        self.spin_d.setSingleStep(0.1)
        self.spin_d.setDecimals(3)

        layout.addRow("Parameter a:", self.spin_a)
        layout.addRow("Parameter b:", self.spin_b)
        layout.addRow("Parameter c:", self.spin_c)
        layout.addRow("Parameter d:", self.spin_d)

        # buttons
        button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    def get_data(self):
        name = self.name_input.text().strip()
        params = {
            "a": self.spin_a.value(),
            "b": self.spin_b.value(),
            "c": self.spin_c.value(),
            "d": self.spin_d.value(),
        }
        return name, params
