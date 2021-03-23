from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import random
import types
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(756, 586)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 140, 641, 386))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.canvas = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())
        self.canvas.setSizePolicy(sizePolicy)
        self.canvas.setText("")
        self.canvas.setObjectName("canvas")
        self.horizontalLayout.addWidget(self.canvas)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.brushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brushButton.sizePolicy().hasHeightForWidth())
        self.brushButton.setSizePolicy(sizePolicy)
        self.brushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.brushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.brushButton.setCheckable(True)
        self.brushButton.setObjectName("brushButton")
        self.gridLayout.addWidget(self.brushButton, 1, 1, 1, 1)
        self.eraserButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eraserButton.sizePolicy().hasHeightForWidth())
        self.eraserButton.setSizePolicy(sizePolicy)
        self.eraserButton.setMinimumSize(QtCore.QSize(30, 30))
        self.eraserButton.setMaximumSize(QtCore.QSize(30, 30))
        self.eraserButton.setCheckable(True)
        self.eraserButton.setObjectName("eraserButton")
        self.gridLayout.addWidget(self.eraserButton, 0, 0, 1, 1)
        self.penButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.penButton.sizePolicy().hasHeightForWidth())
        self.penButton.setSizePolicy(sizePolicy)
        self.penButton.setMinimumSize(QtCore.QSize(30, 30))
        self.penButton.setMaximumSize(QtCore.QSize(30, 30))
        self.penButton.setCheckable(True)
        self.penButton.setObjectName("penButton")
        self.gridLayout.addWidget(self.penButton, 1, 0, 1, 1)
        self.sprayButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sprayButton.sizePolicy().hasHeightForWidth())
        self.sprayButton.setSizePolicy(sizePolicy)
        self.sprayButton.setMinimumSize(QtCore.QSize(30, 30))
        self.sprayButton.setMaximumSize(QtCore.QSize(30, 30))
        self.sprayButton.setCheckable(True)
        self.sprayButton.setFlat(False)
        self.sprayButton.setObjectName("sprayButton")
        self.gridLayout.addWidget(self.sprayButton, 2, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.widget)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(60, 40, 641, 101))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setContentsMargins(15, 0, 15, 15)
        self.gridLayout_2.setSpacing(15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.colorButton_11 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_11.sizePolicy().hasHeightForWidth())
        self.colorButton_11.setSizePolicy(sizePolicy)
        self.colorButton_11.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_11.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_11.setText("")
        self.colorButton_11.setObjectName("colorButton_11")
        self.gridLayout_2.addWidget(self.colorButton_11, 0, 10, 1, 1)
        self.colorButton_4 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_4.sizePolicy().hasHeightForWidth())
        self.colorButton_4.setSizePolicy(sizePolicy)
        self.colorButton_4.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_4.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_4.setText("")
        self.colorButton_4.setObjectName("colorButton_4")
        self.gridLayout_2.addWidget(self.colorButton_4, 0, 3, 1, 1)
        self.colorButton_6 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_6.sizePolicy().hasHeightForWidth())
        self.colorButton_6.setSizePolicy(sizePolicy)
        self.colorButton_6.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_6.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_6.setText("")
        self.colorButton_6.setObjectName("colorButton_6")
        self.gridLayout_2.addWidget(self.colorButton_6, 0, 5, 1, 1)
        self.colorButton_15 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_15.sizePolicy().hasHeightForWidth())
        self.colorButton_15.setSizePolicy(sizePolicy)
        self.colorButton_15.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_15.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_15.setText("")
        self.colorButton_15.setObjectName("colorButton_15")
        self.gridLayout_2.addWidget(self.colorButton_15, 1, 0, 1, 1)
        self.colorButton_14 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_14.sizePolicy().hasHeightForWidth())
        self.colorButton_14.setSizePolicy(sizePolicy)
        self.colorButton_14.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_14.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_14.setText("")
        self.colorButton_14.setObjectName("colorButton_14")
        self.gridLayout_2.addWidget(self.colorButton_14, 0, 13, 1, 1)
        self.colorButton_9 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_9.sizePolicy().hasHeightForWidth())
        self.colorButton_9.setSizePolicy(sizePolicy)
        self.colorButton_9.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_9.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_9.setText("")
        self.colorButton_9.setObjectName("colorButton_9")
        self.gridLayout_2.addWidget(self.colorButton_9, 0, 8, 1, 1)
        self.colorButton_23 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_23.sizePolicy().hasHeightForWidth())
        self.colorButton_23.setSizePolicy(sizePolicy)
        self.colorButton_23.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_23.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_23.setText("")
        self.colorButton_23.setObjectName("colorButton_23")
        self.gridLayout_2.addWidget(self.colorButton_23, 1, 8, 1, 1)
        self.colorButton_24 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_24.sizePolicy().hasHeightForWidth())
        self.colorButton_24.setSizePolicy(sizePolicy)
        self.colorButton_24.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_24.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_24.setText("")
        self.colorButton_24.setObjectName("colorButton_24")
        self.gridLayout_2.addWidget(self.colorButton_24, 1, 9, 1, 1)
        self.colorButton_19 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_19.sizePolicy().hasHeightForWidth())
        self.colorButton_19.setSizePolicy(sizePolicy)
        self.colorButton_19.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_19.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_19.setText("")
        self.colorButton_19.setObjectName("colorButton_19")
        self.gridLayout_2.addWidget(self.colorButton_19, 1, 4, 1, 1)
        self.colorButton_8 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_8.sizePolicy().hasHeightForWidth())
        self.colorButton_8.setSizePolicy(sizePolicy)
        self.colorButton_8.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_8.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_8.setText("")
        self.colorButton_8.setObjectName("colorButton_8")
        self.gridLayout_2.addWidget(self.colorButton_8, 0, 7, 1, 1)
        self.colorButton_1 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_1.sizePolicy().hasHeightForWidth())
        self.colorButton_1.setSizePolicy(sizePolicy)
        self.colorButton_1.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_1.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_1.setStyleSheet("")
        self.colorButton_1.setText("")
        self.colorButton_1.setObjectName("colorButton_1")
        self.gridLayout_2.addWidget(self.colorButton_1, 0, 0, 1, 1)
        self.colorButton_12 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_12.sizePolicy().hasHeightForWidth())
        self.colorButton_12.setSizePolicy(sizePolicy)
        self.colorButton_12.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_12.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_12.setText("")
        self.colorButton_12.setObjectName("colorButton_12")
        self.gridLayout_2.addWidget(self.colorButton_12, 0, 11, 1, 1)
        self.colorButton_17 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_17.sizePolicy().hasHeightForWidth())
        self.colorButton_17.setSizePolicy(sizePolicy)
        self.colorButton_17.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_17.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_17.setText("")
        self.colorButton_17.setObjectName("colorButton_17")
        self.gridLayout_2.addWidget(self.colorButton_17, 1, 2, 1, 1)
        self.colorButton_18 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_18.sizePolicy().hasHeightForWidth())
        self.colorButton_18.setSizePolicy(sizePolicy)
        self.colorButton_18.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_18.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_18.setText("")
        self.colorButton_18.setObjectName("colorButton_18")
        self.gridLayout_2.addWidget(self.colorButton_18, 1, 3, 1, 1)
        self.colorButton_2 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_2.sizePolicy().hasHeightForWidth())
        self.colorButton_2.setSizePolicy(sizePolicy)
        self.colorButton_2.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_2.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_2.setText("")
        self.colorButton_2.setObjectName("colorButton_2")
        self.gridLayout_2.addWidget(self.colorButton_2, 0, 1, 1, 1)
        self.colorButton_26 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_26.sizePolicy().hasHeightForWidth())
        self.colorButton_26.setSizePolicy(sizePolicy)
        self.colorButton_26.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_26.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_26.setText("")
        self.colorButton_26.setObjectName("colorButton_26")
        self.gridLayout_2.addWidget(self.colorButton_26, 1, 11, 1, 1)
        self.colorButton_13 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_13.sizePolicy().hasHeightForWidth())
        self.colorButton_13.setSizePolicy(sizePolicy)
        self.colorButton_13.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_13.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_13.setText("")
        self.colorButton_13.setObjectName("colorButton_13")
        self.gridLayout_2.addWidget(self.colorButton_13, 0, 12, 1, 1)
        self.colorButton_25 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_25.sizePolicy().hasHeightForWidth())
        self.colorButton_25.setSizePolicy(sizePolicy)
        self.colorButton_25.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_25.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_25.setText("")
        self.colorButton_25.setObjectName("colorButton_25")
        self.gridLayout_2.addWidget(self.colorButton_25, 1, 10, 1, 1)
        self.colorButton_20 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_20.sizePolicy().hasHeightForWidth())
        self.colorButton_20.setSizePolicy(sizePolicy)
        self.colorButton_20.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_20.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_20.setText("")
        self.colorButton_20.setObjectName("colorButton_20")
        self.gridLayout_2.addWidget(self.colorButton_20, 1, 5, 1, 1)
        self.colorButton_21 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_21.sizePolicy().hasHeightForWidth())
        self.colorButton_21.setSizePolicy(sizePolicy)
        self.colorButton_21.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_21.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_21.setText("")
        self.colorButton_21.setObjectName("colorButton_21")
        self.gridLayout_2.addWidget(self.colorButton_21, 1, 6, 1, 1)
        self.colorButton_16 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_16.sizePolicy().hasHeightForWidth())
        self.colorButton_16.setSizePolicy(sizePolicy)
        self.colorButton_16.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_16.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_16.setText("")
        self.colorButton_16.setObjectName("colorButton_16")
        self.gridLayout_2.addWidget(self.colorButton_16, 1, 1, 1, 1)
        self.colorButton_27 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_27.sizePolicy().hasHeightForWidth())
        self.colorButton_27.setSizePolicy(sizePolicy)
        self.colorButton_27.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_27.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_27.setText("")
        self.colorButton_27.setObjectName("colorButton_27")
        self.gridLayout_2.addWidget(self.colorButton_27, 1, 12, 1, 1)
        self.colorButton_28 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_28.sizePolicy().hasHeightForWidth())
        self.colorButton_28.setSizePolicy(sizePolicy)
        self.colorButton_28.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_28.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_28.setText("")
        self.colorButton_28.setObjectName("colorButton_28")
        self.gridLayout_2.addWidget(self.colorButton_28, 1, 13, 1, 1)
        self.colorButton_10 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_10.sizePolicy().hasHeightForWidth())
        self.colorButton_10.setSizePolicy(sizePolicy)
        self.colorButton_10.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_10.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_10.setText("")
        self.colorButton_10.setObjectName("colorButton_10")
        self.gridLayout_2.addWidget(self.colorButton_10, 0, 9, 1, 1)
        self.colorButton_3 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_3.sizePolicy().hasHeightForWidth())
        self.colorButton_3.setSizePolicy(sizePolicy)
        self.colorButton_3.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_3.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_3.setText("")
        self.colorButton_3.setObjectName("colorButton_3")
        self.gridLayout_2.addWidget(self.colorButton_3, 0, 2, 1, 1)
        self.colorButton_7 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_7.sizePolicy().hasHeightForWidth())
        self.colorButton_7.setSizePolicy(sizePolicy)
        self.colorButton_7.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_7.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_7.setText("")
        self.colorButton_7.setObjectName("colorButton_7")
        self.gridLayout_2.addWidget(self.colorButton_7, 0, 6, 1, 1)
        self.colorButton_5 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_5.sizePolicy().hasHeightForWidth())
        self.colorButton_5.setSizePolicy(sizePolicy)
        self.colorButton_5.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_5.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_5.setText("")
        self.colorButton_5.setObjectName("colorButton_5")
        self.gridLayout_2.addWidget(self.colorButton_5, 0, 4, 1, 1)
        self.colorButton_22 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_22.sizePolicy().hasHeightForWidth())
        self.colorButton_22.setSizePolicy(sizePolicy)
        self.colorButton_22.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_22.setMaximumSize(QtCore.QSize(20, 13))
        self.colorButton_22.setText("")
        self.colorButton_22.setObjectName("colorButton_22")
        self.gridLayout_2.addWidget(self.colorButton_22, 1, 7, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 756, 21))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpenImage = QtWidgets.QAction(MainWindow)
        self.actionOpenImage.setObjectName("actionOpenImage")
        self.actionNewImage = QtWidgets.QAction(MainWindow)
        self.actionNewImage.setObjectName("actionNewImage")
        self.actionSaveImage = QtWidgets.QAction(MainWindow)
        self.actionSaveImage.setObjectName("actionSaveImage")
        self.menu.addAction(self.actionNewImage)
        self.menu.addAction(self.actionOpenImage)
        self.menu.addAction(self.actionSaveImage)
        self.menuBar.addAction(self.menu.menuAction())
        self.penButton.setIcon(QIcon('pen.png'))
        self.penButton.setIconSize(QSize(28, 40))
        self.eraserButton.setIcon(QIcon('t.png'))
        self.eraserButton.setIconSize(QSize(28, 40))
        self.brushButton.setIcon(QIcon('brush.png'))
        self.brushButton.setIconSize(QSize(28, 40))
        self.sprayButton.setIcon(QIcon('spray.png'))
        self.sprayButton.setIconSize(QSize(28, 40))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Paint-01"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.actionOpenImage.setText(_translate("MainWindow", "Добавить файл"))
        self.actionNewImage.setText(_translate("MainWindow", "Новый файл"))
        self.actionSaveImage.setText(_translate("MainWindow", "Сохранить как"))


'============================================================================================================='
'==========================================ДИЗАЙН ЗАКОНЧЕН===================================================='
'============================================================================================================='
Razmer_mishi = 3
Razbros_spreya = 100

COLORS = [
    '#000000', '#82817f', '#820300', '#868417', '#007e03', '#037e7b', '#040079',
    '#81067a', '#7f7e45', '#05403c', '#0a7cf6', '#093c7e', '#7e07f9', '#7c4002',
    '#ffffff', '#c1c1c1', '#f70406', '#fffd00', '#08fb01', '#0bf8ee', '#0000fa',
    '#b92fc2', '#fffc91', '#00fd83', '#87f9f9', '#8481c4', '#dc137d', '#fb803c',
]

Khopki_otvechauishie_za_instrumenty = [
    'eraser', 'pen',
    'brush', 'spray'

]

Razmer_polya_dla_rusovania = 600, 400


class Canvas(QLabel):
    tekushiy_vibrannity_instrument = ''

    cvet_po_umolchaniyu = QColor(Qt.black)
    vtoroy_cvet = None

    # Сохраняем изначальную конфигурацию
    config = {
        # Опции рисования.
        'size': 1,
        'fill': True
    }
    # Текущий активный цвет
    tekushiy_cvet_vibraniy_polsovatelem = None

    def initialize(self):
        # Указывается текущий цвет фона.
        if self.vtoroy_cvet:
            self.background_color = QColor(self.vtoroy_cvet)
        else:
            # self.background_color отвечает за текущий цвет фона.
            self.background_color = QColor(Qt.white)
        if self.vtoroy_cvet:
            # self.eraser_color отвечает за цвет ластика
            self.eraser_color = QColor(self.vtoroy_cvet)
        else:
            # Происходит установка цвета для ластика
            self.eraser_color = QColor(Qt.white)
        self.reset()

    def reset(self):
        # Создаем изображение для отображения.
        self.setPixmap(QPixmap(*Razmer_polya_dla_rusovania))

        # Очищаем холст.
        self.pixmap().fill(self.background_color)

    def set_primary_color(self, event):
        # первичный цвет(начальный)
        self.cvet_po_umolchaniyu = QColor(event)

    def set_secondary_color(self, event):
        # второй цвет(выбранный пользователем)
        self.vtoroy_cvet = QColor(event)

    def set_mode(self, mode):
        # Сбрасываем прошлую позицию курсора

        self.proslaya_pozicia = None

        # Применить режим
        self.tekushiy_vibrannity_instrument = mode

    # События мыши.

    def mousePressEvent(self, event):
        """getattr(self - Объект, значение атрибута которого требуется получить,
        "f"{self.mode}_mousePressEvent" - Имя атрибута, значение которого требуется получить,
         None - Значение по умолчанию, которое будет возвращено"""
        fn = getattr(self, f"{self.tekushiy_vibrannity_instrument}_mousePressEvent", None)
        if fn:
            return fn(event)

    def mouseMoveEvent(self, event):
        fn = getattr(self, f"{self.tekushiy_vibrannity_instrument}_mouseMoveEvent", None)
        if fn:
            return fn(event)

    def mouseReleaseEvent(self, event):
        fn = getattr(self, f"{self.tekushiy_vibrannity_instrument}_mouseReleaseEvent", None)
        if fn:
            return fn(event)

    # Общие события мыши

    def generic_mousePressEvent(self, event):
        self.proslaya_pozicia = event.pos()

        if event.button() == Qt.LeftButton:
            self.tekushiy_cvet_vibraniy_polsovatelem = self.cvet_po_umolchaniyu
        else:
            self.tekushiy_cvet_vibraniy_polsovatelem = self.vtoroy_cvet

    def generic_mouseReleaseEvent(self, event):
        self.proslaya_pozicia = None

    def pen_mousePressEvent(self, event):
        self.generic_mousePressEvent(event)

    def eraser_mousePressEvent(self, event):
        self.generic_mousePressEvent(event)

    def eraser_mouseMoveEvent(self, event):
        if self.proslaya_pozicia:
            p = QPainter(self.pixmap())
            p.setPen(QPen(self.eraser_color, 30))
            p.drawLine(self.proslaya_pozicia, event.pos())

            self.proslaya_pozicia = event.pos()
            self.update()

    def eraser_mouseReleaseEvent(self, e):
        self.generic_mouseReleaseEvent(e)

    def pen_mouseMoveEvent(self, event):
        if self.proslaya_pozicia:
            p = QPainter(self.pixmap())
            p.setPen(QPen(self.tekushiy_cvet_vibraniy_polsovatelem))
            p.drawLine(self.proslaya_pozicia, event.pos())

            self.proslaya_pozicia = event.pos()
            self.update()

    def pen_mouseReleaseEvent(self, event):
        self.generic_mouseReleaseEvent(event)

    # Моменты кисти

    def brush_mousePressEvent(self, event):
        self.generic_mousePressEvent(event)

    def brush_mouseMoveEvent(self, event):
        if self.proslaya_pozicia:
            p = QPainter(self.pixmap())
            p.setPen(QPen(self.tekushiy_cvet_vibraniy_polsovatelem, Razmer_mishi))
            p.drawLine(self.proslaya_pozicia, event.pos())

            self.proslaya_pozicia = event.pos()
            self.update()

    def brush_mouseReleaseEvent(self, event):
        self.generic_mouseReleaseEvent(event)

    # Моменты спрея

    def spray_mousePressEvent(self, event):
        self.generic_mousePressEvent(event)

    def spray_mouseMoveEvent(self, event):
        if self.proslaya_pozicia:
            p = QPainter(self.pixmap())
            p.setPen(QPen(self.tekushiy_cvet_vibraniy_polsovatelem, 1))

            for n in range(Razbros_spreya):
                xo = random.randint(0, 50)
                yo = random.randint(0, 50)
                p.drawPoint(event.x() + xo, event.y() + yo)

        self.update()

    def spray_mouseReleaseEvent(self, event):
        self.generic_mouseReleaseEvent(event)


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.dfdf = QHBoxLayout(self)

        # Замените заполнитель холста из QtDesigner.
        self.horizontalLayout.removeWidget(self.canvas)
        self.canvas = Canvas()
        self.canvas.initialize()
        # Нам нужно включить отслеживание мыши, чтобы она следовала за мышью без нажатия кнопки.
        self.canvas.setMouseTracking(True)
        self.horizontalLayout.addWidget(self.canvas)

        # Настройте кнопки режима

        # проходимся по всем кнопкам, которые выполняют действия
        for mode in Khopki_otvechauishie_za_instrumenty:
            btn = getattr(self, f'{mode}Button')
            btn.pressed.connect(lambda mode=mode: self.canvas.set_mode(mode))

        # Проходимся по кнопкам, отвечающим за цвета и устанавливаем цвета кнопок.
        for n, color in enumerate(COLORS, 1):
            btn = getattr(self, f'colorButton_{n}')
            btn.setStyleSheet(f"background-color: {color}")
            btn.hex = color  # Для использования в функции patch_mousePressEvent

            def patch_mousePressEvent(_self_, event):
                """Если мы нажмем левой или правой кнопкой мыши
                 по кнопкам выбора цвета, то мы установим выбранный цвет"""
                if event.button() == Qt.LeftButton:
                    self.set_primary_color(_self_.hex)

                elif event.button() == Qt.RightButton:
                    self.set_primary_color(_self_.hex)

            btn.mousePressEvent = types.MethodType(patch_mousePressEvent, btn)

        # Опции меню
        self.actionNewImage.triggered.connect(self.canvas.initialize)
        self.actionOpenImage.triggered.connect(self.open_file)
        self.actionSaveImage.triggered.connect(self.save_file)

        self.show()

    def set_primary_color(self, color):
        self.canvas.set_primary_color(color)

    def open_file(self):
        """
        Откройте файл изображения для редактирования, масштабируя меньший размер и обрезая остаток.
        """
        path, _ = QFileDialog.getOpenFileName(self)

        if path:
            pixmap = QPixmap()
            pixmap.load(path)

            # Нам нужно обрезать до размера нашего холста. Получите размер загруженного изображения.
            iw = pixmap.width()
            ih = pixmap.height()

            # Получите размер заполняемого пространства.
            cw, ch = Razmer_polya_dla_rusovania

            if iw / cw < ih / ch:  # Высота относительно больше ширины.
                pixmap = pixmap.scaledToWidth(cw)
                hoff = (pixmap.height() - ch) // 2
                pixmap = pixmap.copy(
                    QRect(QPoint(0, hoff), QPoint(cw, pixmap.height() - hoff))
                )

            elif iw / cw > ih / ch:  # Высота относительно меньше ширины.
                pixmap = pixmap.scaledToHeight(ch)
                woff = (pixmap.width() - cw) // 2
                pixmap = pixmap.copy(
                    QRect(QPoint(woff, 0), QPoint(pixmap.width() - woff, ch))
                )

            self.canvas.setPixmap(pixmap)

    def save_file(self):
        """
        Сохраняем наше изображение в формате PNG.
        """
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "open", "*.png")

        if path:
            pixmap = self.canvas.pixmap()
            pixmap.save(path, "PNG")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon())
    window = MainWindow()
    app.exec_()