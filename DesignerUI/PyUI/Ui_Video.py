# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\12284\Desktop\GitHub\ImageAnalysis\DesignerUI\Video.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1159, 692)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 51))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 51))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_9.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.box1_set = QtWidgets.QPushButton(self.groupBox)
        self.box1_set.setMinimumSize(QtCore.QSize(25, 25))
        self.box1_set.setStyleSheet("border: none;")
        self.box1_set.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.box1_set.setIcon(icon)
        self.box1_set.setIconSize(QtCore.QSize(30, 30))
        self.box1_set.setObjectName("box1_set")
        self.gridLayout_9.addWidget(self.box1_set, 0, 0, 1, 1)
        self.box1_save = QtWidgets.QPushButton(self.groupBox)
        self.box1_save.setMinimumSize(QtCore.QSize(25, 25))
        self.box1_save.setStyleSheet("border: none;")
        self.box1_save.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.box1_save.setIcon(icon1)
        self.box1_save.setIconSize(QtCore.QSize(30, 30))
        self.box1_save.setObjectName("box1_save")
        self.gridLayout_9.addWidget(self.box1_save, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(834, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem, 0, 2, 1, 1)
        self.box1_color = QtWidgets.QPushButton(self.groupBox)
        self.box1_color.setMinimumSize(QtCore.QSize(25, 25))
        self.box1_color.setStyleSheet("border: none;")
        self.box1_color.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/palette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.box1_color.setIcon(icon2)
        self.box1_color.setIconSize(QtCore.QSize(30, 30))
        self.box1_color.setObjectName("box1_color")
        self.gridLayout_9.addWidget(self.box1_color, 0, 3, 1, 1)
        self.box1_power = QtWidgets.QPushButton(self.groupBox)
        self.box1_power.setMinimumSize(QtCore.QSize(25, 25))
        self.box1_power.setStyleSheet("border: none;")
        self.box1_power.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/power-on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/icon/power_start.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap(":/icon/power-on.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/icon/power_start.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.box1_power.setIcon(icon3)
        self.box1_power.setIconSize(QtCore.QSize(30, 30))
        self.box1_power.setCheckable(True)
        self.box1_power.setObjectName("box1_power")
        self.gridLayout_9.addWidget(self.box1_power, 0, 4, 1, 1)
        self.box1_connection_status = QtWidgets.QPushButton(self.groupBox)
        self.box1_connection_status.setMinimumSize(QtCore.QSize(25, 25))
        self.box1_connection_status.setStyleSheet("border: none;")
        self.box1_connection_status.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/broken-link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/icon/broken-link (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap(":/icon/broken-link.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/icon/broken-link (1).png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\12284\\Desktop\\GitHub\\ImageAnalysis\\DesignerUI\\../images/broken-link.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.box1_connection_status.setIcon(icon4)
        self.box1_connection_status.setIconSize(QtCore.QSize(30, 30))
        self.box1_connection_status.setCheckable(True)
        self.box1_connection_status.setObjectName("box1_connection_status")
        self.gridLayout_9.addWidget(self.box1_connection_status, 0, 5, 1, 1)
        self.box1_user = QtWidgets.QToolButton(self.groupBox)
        self.box1_user.setMinimumSize(QtCore.QSize(111, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.box1_user.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/man.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.box1_user.setIcon(icon5)
        self.box1_user.setIconSize(QtCore.QSize(30, 30))
        self.box1_user.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.box1_user.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.box1_user.setAutoRaise(True)
        self.box1_user.setArrowType(QtCore.Qt.NoArrow)
        self.box1_user.setObjectName("box1_user")
        self.gridLayout_9.addWidget(self.box1_user, 0, 6, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.box2_tree = QtWidgets.QTreeWidget(self.groupBox_3)
        self.box2_tree.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.box2_tree.setStyleSheet("")
        self.box2_tree.setObjectName("box2_tree")
        self.box2_tree.headerItem().setBackground(0, QtGui.QColor(170, 255, 255))
        item_0 = QtWidgets.QTreeWidgetItem(self.box2_tree)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.box2_tree)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.box2_tree)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.box2_tree)
        self.gridLayout_3.addWidget(self.box2_tree, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.box3_log = QtWidgets.QTextBrowser(self.groupBox_5)
        self.box3_log.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.box3_log.setObjectName("box3_log")
        self.gridLayout_2.addWidget(self.box3_log, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.horizontalLayout.addWidget(self.groupBox_6)
        self.box4_graphics = QtWidgets.QGraphicsView(self.groupBox_9)
        self.box4_graphics.setObjectName("box4_graphics")
        self.horizontalLayout.addWidget(self.box4_graphics)
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_9)
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.box5_control = QtWidgets.QStackedWidget(self.groupBox_2)
        self.box5_control.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.box5_control.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.box5_control.setObjectName("box5_control")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.checkBox = QtWidgets.QCheckBox(self.page_3)
        self.checkBox.setGeometry(QtCore.QRect(20, 100, 89, 22))
        self.checkBox.setObjectName("checkBox")
        self.box5_control.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.pushButton = QtWidgets.QPushButton(self.page_4)
        self.pushButton.setGeometry(QtCore.QRect(20, 90, 98, 26))
        self.pushButton.setObjectName("pushButton")
        self.box5_control.addWidget(self.page_4)
        self.gridLayout_5.addWidget(self.box5_control, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.box6_sub_interface = QtWidgets.QStackedWidget(self.groupBox_7)
        self.box6_sub_interface.setEnabled(True)
        self.box6_sub_interface.setMinimumSize(QtCore.QSize(0, 0))
        self.box6_sub_interface.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.box6_sub_interface.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.box6_sub_interface.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.box6_sub_interface.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.box6_sub_interface.setObjectName("box6_sub_interface")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.box6_sub_interface.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.box6_sub_first = QtWidgets.QLabel(self.page_2)
        self.box6_sub_first.setText("")
        self.box6_sub_first.setObjectName("box6_sub_first")
        self.gridLayout_8.addWidget(self.box6_sub_first, 0, 0, 1, 1)
        self.box6_sub_interface.addWidget(self.page_2)
        self.gridLayout_4.addWidget(self.box6_sub_interface, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_7, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_8)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addWidget(self.groupBox_9)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1159, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.box5_control.setCurrentIndex(1)
        self.box6_sub_interface.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VideoAnalysis"))
        self.box1_user.setText(_translate("MainWindow", "已登录!"))
        self.groupBox_9.setTitle(_translate("MainWindow", "显示区"))
        self.groupBox_3.setTitle(_translate("MainWindow", "功能列表"))
        self.box2_tree.headerItem().setText(0, _translate("MainWindow", "功能列表"))
        __sortingEnabled = self.box2_tree.isSortingEnabled()
        self.box2_tree.setSortingEnabled(False)
        self.box2_tree.topLevelItem(0).setText(0, _translate("MainWindow", "图像处理"))
        self.box2_tree.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "图像翻转"))
        self.box2_tree.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "提取ROI"))
        self.box2_tree.topLevelItem(1).setText(0, _translate("MainWindow", "图像编码"))
        self.box2_tree.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "编码设置"))
        self.box2_tree.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "视频传输"))
        self.box2_tree.topLevelItem(2).setText(0, _translate("MainWindow", "AI分析"))
        self.box2_tree.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "目标检测"))
        self.box2_tree.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "场景分割"))
        self.box2_tree.topLevelItem(2).child(2).setText(0, _translate("MainWindow", "目标跟踪"))
        self.box2_tree.setSortingEnabled(__sortingEnabled)
        self.groupBox_5.setTitle(_translate("MainWindow", "全局日志"))
        self.groupBox_2.setTitle(_translate("MainWindow", "控制区"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.groupBox_7.setTitle(_translate("MainWindow", "子界面"))
from images import icon_png_rc
