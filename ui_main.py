# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maininXAJZ.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 640)
        MainWindow.setMinimumSize(QSize(800, 640))
        MainWindow.setMaximumSize(QSize(800, 640))
        font = QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"icon", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionLoad_2 = QAction(MainWindow)
        self.actionLoad_2.setObjectName(u"actionLoad_2")
        self.actionSave_2 = QAction(MainWindow)
        self.actionSave_2.setObjectName(u"actionSave_2")
        self.actionLoad1 = QAction(MainWindow)
        self.actionLoad1.setObjectName(u"actionLoad1")
        self.actionSave1 = QAction(MainWindow)
        self.actionSave1.setObjectName(u"actionSave1")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 640))
        self.centralwidget.setMaximumSize(QSize(800, 640))
        self.centralwidget.setBaseSize(QSize(640, 640))
        font1 = QFont()
        font1.setPointSize(12)
        self.centralwidget.setFont(font1)
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget_rating = QTabWidget(self.centralwidget)
        self.tabWidget_rating.setObjectName(u"tabWidget_rating")
        self.tab_info = QWidget()
        self.tab_info.setObjectName(u"tab_info")
        self.verticalLayout_2 = QVBoxLayout(self.tab_info)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_1 = QLabel(self.tab_info)
        self.label_1.setObjectName(u"label_1")
        font2 = QFont()
        font2.setPointSize(20)
        self.label_1.setFont(font2)
        self.label_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_1.setTextFormat(Qt.TextFormat.PlainText)
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_1)

        self.verticalSpacer = QSpacerItem(20, 489, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget_rating.addTab(self.tab_info, "")
        self.tab_rating_parameter = QWidget()
        self.tab_rating_parameter.setObjectName(u"tab_rating_parameter")
        self.tab_rating_parameter.setFont(font)
        self.horizontalLayout_5 = QHBoxLayout(self.tab_rating_parameter)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tab_rating_parameter_1 = QHBoxLayout()
        self.tab_rating_parameter_1.setObjectName(u"tab_rating_parameter_1")
        self.tabWidget_rating_parameter = QTabWidget(self.tab_rating_parameter)
        self.tabWidget_rating_parameter.setObjectName(u"tabWidget_rating_parameter")
        self.tabWidget_rating_parameter.setFont(font1)
        self.tab_parameter_vk = QWidget()
        self.tab_parameter_vk.setObjectName(u"tab_parameter_vk")
        self.verticalLayout_3 = QVBoxLayout(self.tab_parameter_vk)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.group_vk_ik = QVBoxLayout()
        self.group_vk_ik.setObjectName(u"group_vk_ik")
        self.label_vk_ik = QLabel(self.tab_parameter_vk)
        self.label_vk_ik.setObjectName(u"label_vk_ik")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_vk_ik.setFont(font3)
        self.label_vk_ik.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.group_vk_ik.addWidget(self.label_vk_ik)

        self.group_input_mean_vk_ik = QHBoxLayout()
        self.group_input_mean_vk_ik.setObjectName(u"group_input_mean_vk_ik")
        self.input_mean_vk_ik = QDoubleSpinBox(self.tab_parameter_vk)
        self.input_mean_vk_ik.setObjectName(u"input_mean_vk_ik")
        self.input_mean_vk_ik.setReadOnly(False)
        self.input_mean_vk_ik.setDecimals(4)
        self.input_mean_vk_ik.setMinimum(0.000100000000000)
        self.input_mean_vk_ik.setMaximum(99999.000000000000000)
        self.input_mean_vk_ik.setSingleStep(1.000000000000000)

        self.group_input_mean_vk_ik.addWidget(self.input_mean_vk_ik)

        self.checkbox_var_vk_ik = QCheckBox(self.tab_parameter_vk)
        self.checkbox_var_vk_ik.setObjectName(u"checkbox_var_vk_ik")
        self.checkbox_var_vk_ik.setAcceptDrops(False)

        self.group_input_mean_vk_ik.addWidget(self.checkbox_var_vk_ik)

        self.input_var_vk_ik = QDoubleSpinBox(self.tab_parameter_vk)
        self.input_var_vk_ik.setObjectName(u"input_var_vk_ik")
        self.input_var_vk_ik.setEnabled(False)
        self.input_var_vk_ik.setDecimals(4)
        self.input_var_vk_ik.setMaximum(999999.000000000000000)

        self.group_input_mean_vk_ik.addWidget(self.input_var_vk_ik)

        self.group_input_mean_vk_ik.setStretch(0, 3)
        self.group_input_mean_vk_ik.setStretch(2, 1)

        self.group_vk_ik.addLayout(self.group_input_mean_vk_ik)


        self.verticalLayout_3.addLayout(self.group_vk_ik)

        self.group_vk_m = QVBoxLayout()
        self.group_vk_m.setObjectName(u"group_vk_m")
        self.label_vk_m = QLabel(self.tab_parameter_vk)
        self.label_vk_m.setObjectName(u"label_vk_m")
        self.label_vk_m.setFont(font3)
        self.label_vk_m.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.group_vk_m.addWidget(self.label_vk_m)

        self.group_input_mean_vk_m = QHBoxLayout()
        self.group_input_mean_vk_m.setObjectName(u"group_input_mean_vk_m")
        self.input_mean_vk_m = QDoubleSpinBox(self.tab_parameter_vk)
        self.input_mean_vk_m.setObjectName(u"input_mean_vk_m")
        self.input_mean_vk_m.setDecimals(4)
        self.input_mean_vk_m.setMinimum(0.000100000000000)
        self.input_mean_vk_m.setMaximum(99999.000000000000000)

        self.group_input_mean_vk_m.addWidget(self.input_mean_vk_m)

        self.checkbox_var_vk_m = QCheckBox(self.tab_parameter_vk)
        self.checkbox_var_vk_m.setObjectName(u"checkbox_var_vk_m")

        self.group_input_mean_vk_m.addWidget(self.checkbox_var_vk_m)

        self.input_var_vk_m = QDoubleSpinBox(self.tab_parameter_vk)
        self.input_var_vk_m.setObjectName(u"input_var_vk_m")
        self.input_var_vk_m.setEnabled(False)
        self.input_var_vk_m.setDecimals(4)
        self.input_var_vk_m.setMaximum(999999.000000000000000)

        self.group_input_mean_vk_m.addWidget(self.input_var_vk_m)

        self.group_input_mean_vk_m.setStretch(0, 3)
        self.group_input_mean_vk_m.setStretch(2, 1)

        self.group_vk_m.addLayout(self.group_input_mean_vk_m)


        self.verticalLayout_3.addLayout(self.group_vk_m)

        self.group_vk_zk = QVBoxLayout()
        self.group_vk_zk.setObjectName(u"group_vk_zk")
        self.label_vk_zk = QLabel(self.tab_parameter_vk)
        self.label_vk_zk.setObjectName(u"label_vk_zk")
        self.label_vk_zk.setFont(font3)
        self.label_vk_zk.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.group_vk_zk.addWidget(self.label_vk_zk)

        self.group_input_mean_vk_zk = QHBoxLayout()
        self.group_input_mean_vk_zk.setObjectName(u"group_input_mean_vk_zk")
        self.input_mean_vk_zk = QDoubleSpinBox(self.tab_parameter_vk)
        self.input_mean_vk_zk.setObjectName(u"input_mean_vk_zk")
        self.input_mean_vk_zk.setDecimals(4)
        self.input_mean_vk_zk.setMinimum(0.000100000000000)
        self.input_mean_vk_zk.setMaximum(99999.000000000000000)

        self.group_input_mean_vk_zk.addWidget(self.input_mean_vk_zk)

        self.checkbox_var_vk_zk = QCheckBox(self.tab_parameter_vk)
        self.checkbox_var_vk_zk.setObjectName(u"checkbox_var_vk_zk")

        self.group_input_mean_vk_zk.addWidget(self.checkbox_var_vk_zk)

        self.input_var_vk_zk = QDoubleSpinBox(self.tab_parameter_vk)
        self.input_var_vk_zk.setObjectName(u"input_var_vk_zk")
        self.input_var_vk_zk.setEnabled(False)
        self.input_var_vk_zk.setDecimals(4)
        self.input_var_vk_zk.setMaximum(999999.000000000000000)

        self.group_input_mean_vk_zk.addWidget(self.input_var_vk_zk)

        self.group_input_mean_vk_zk.setStretch(0, 3)
        self.group_input_mean_vk_zk.setStretch(2, 1)

        self.group_vk_zk.addLayout(self.group_input_mean_vk_zk)


        self.verticalLayout_3.addLayout(self.group_vk_zk)

        self.group_vk_cty = QVBoxLayout()
        self.group_vk_cty.setObjectName(u"group_vk_cty")
        self.label_vk_cty = QLabel(self.tab_parameter_vk)
        self.label_vk_cty.setObjectName(u"label_vk_cty")
        self.label_vk_cty.setFont(font3)
        self.label_vk_cty.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.group_vk_cty.addWidget(self.label_vk_cty)

        self.group_input_mean_vk_cty = QHBoxLayout()
        self.group_input_mean_vk_cty.setObjectName(u"group_input_mean_vk_cty")
        self.input_mean_vk_cty = QDoubleSpinBox(self.tab_parameter_vk)
        self.input_mean_vk_cty.setObjectName(u"input_mean_vk_cty")
        self.input_mean_vk_cty.setDecimals(4)
        self.input_mean_vk_cty.setMinimum(0.000100000000000)
        self.input_mean_vk_cty.setMaximum(99999.000000000000000)

        self.group_input_mean_vk_cty.addWidget(self.input_mean_vk_cty)

        self.checkbox_var_vk_cty = QCheckBox(self.tab_parameter_vk)
        self.checkbox_var_vk_cty.setObjectName(u"checkbox_var_vk_cty")

        self.group_input_mean_vk_cty.addWidget(self.checkbox_var_vk_cty)

        self.input_var_vk_cty = QDoubleSpinBox(self.tab_parameter_vk)
        self.input_var_vk_cty.setObjectName(u"input_var_vk_cty")
        self.input_var_vk_cty.setEnabled(False)
        self.input_var_vk_cty.setDecimals(4)
        self.input_var_vk_cty.setMaximum(999999.000000000000000)

        self.group_input_mean_vk_cty.addWidget(self.input_var_vk_cty)

        self.group_input_mean_vk_cty.setStretch(0, 3)
        self.group_input_mean_vk_cty.setStretch(2, 1)

        self.group_vk_cty.addLayout(self.group_input_mean_vk_cty)


        self.verticalLayout_3.addLayout(self.group_vk_cty)

        self.group_vk_d = QVBoxLayout()
        self.group_vk_d.setObjectName(u"group_vk_d")
        self.label_vk_d = QLabel(self.tab_parameter_vk)
        self.label_vk_d.setObjectName(u"label_vk_d")
        self.label_vk_d.setFont(font3)
        self.label_vk_d.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.group_vk_d.addWidget(self.label_vk_d)

        self.group_input_mean_vk_d = QHBoxLayout()
        self.group_input_mean_vk_d.setObjectName(u"group_input_mean_vk_d")
        self.input_mean_vk_d = QDoubleSpinBox(self.tab_parameter_vk)
        self.input_mean_vk_d.setObjectName(u"input_mean_vk_d")
        self.input_mean_vk_d.setDecimals(4)
        self.input_mean_vk_d.setMinimum(0.000100000000000)
        self.input_mean_vk_d.setMaximum(99999.000000000000000)

        self.group_input_mean_vk_d.addWidget(self.input_mean_vk_d)

        self.checkbox_var_vk_d = QCheckBox(self.tab_parameter_vk)
        self.checkbox_var_vk_d.setObjectName(u"checkbox_var_vk_d")

        self.group_input_mean_vk_d.addWidget(self.checkbox_var_vk_d)

        self.input_var_vk_d = QDoubleSpinBox(self.tab_parameter_vk)
        self.input_var_vk_d.setObjectName(u"input_var_vk_d")
        self.input_var_vk_d.setEnabled(False)
        self.input_var_vk_d.setDecimals(4)
        self.input_var_vk_d.setMinimum(0.000100000000000)
        self.input_var_vk_d.setMaximum(999999.000000000000000)
        self.input_var_vk_d.setValue(0.000100000000000)

        self.group_input_mean_vk_d.addWidget(self.input_var_vk_d)

        self.group_input_mean_vk_d.setStretch(0, 3)
        self.group_input_mean_vk_d.setStretch(2, 1)

        self.group_vk_d.addLayout(self.group_input_mean_vk_d)


        self.verticalLayout_3.addLayout(self.group_vk_d)

        self.tabWidget_rating_parameter.addTab(self.tab_parameter_vk, "")
        self.tab_parameter_pmax = QWidget()
        self.tab_parameter_pmax.setObjectName(u"tab_parameter_pmax")
        self.verticalLayout = QVBoxLayout(self.tab_parameter_pmax)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.group_p_dn_max_q = QVBoxLayout()
        self.group_p_dn_max_q.setObjectName(u"group_p_dn_max_q")
        self.label_p_dn_max_q = QLabel(self.tab_parameter_pmax)
        self.label_p_dn_max_q.setObjectName(u"label_p_dn_max_q")
        self.label_p_dn_max_q.setFont(font3)
        self.label_p_dn_max_q.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.group_p_dn_max_q.addWidget(self.label_p_dn_max_q)

        self.group_input_mean_p_dn_max_q = QHBoxLayout()
        self.group_input_mean_p_dn_max_q.setObjectName(u"group_input_mean_p_dn_max_q")
        self.input_mean_p_dn_max_q = QDoubleSpinBox(self.tab_parameter_pmax)
        self.input_mean_p_dn_max_q.setObjectName(u"input_mean_p_dn_max_q")
        self.input_mean_p_dn_max_q.setDecimals(4)
        self.input_mean_p_dn_max_q.setMinimum(0.000100000000000)
        self.input_mean_p_dn_max_q.setMaximum(99999.000000000000000)

        self.group_input_mean_p_dn_max_q.addWidget(self.input_mean_p_dn_max_q)

        self.checkbox_var_p_dn_max_q = QCheckBox(self.tab_parameter_pmax)
        self.checkbox_var_p_dn_max_q.setObjectName(u"checkbox_var_p_dn_max_q")

        self.group_input_mean_p_dn_max_q.addWidget(self.checkbox_var_p_dn_max_q)

        self.input_var_p_dn_max_q = QDoubleSpinBox(self.tab_parameter_pmax)
        self.input_var_p_dn_max_q.setObjectName(u"input_var_p_dn_max_q")
        self.input_var_p_dn_max_q.setEnabled(False)
        self.input_var_p_dn_max_q.setDecimals(4)
        self.input_var_p_dn_max_q.setMaximum(999999.000000000000000)

        self.group_input_mean_p_dn_max_q.addWidget(self.input_var_p_dn_max_q)

        self.group_input_mean_p_dn_max_q.setStretch(0, 3)
        self.group_input_mean_p_dn_max_q.setStretch(2, 1)

        self.group_p_dn_max_q.addLayout(self.group_input_mean_p_dn_max_q)


        self.verticalLayout.addLayout(self.group_p_dn_max_q)

        self.group_p_dn_max_w = QVBoxLayout()
        self.group_p_dn_max_w.setObjectName(u"group_p_dn_max_w")
        self.label_p_dn_max_w = QLabel(self.tab_parameter_pmax)
        self.label_p_dn_max_w.setObjectName(u"label_p_dn_max_w")
        self.label_p_dn_max_w.setFont(font3)
        self.label_p_dn_max_w.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.group_p_dn_max_w.addWidget(self.label_p_dn_max_w)

        self.group_input_mean_p_dn_max_w = QHBoxLayout()
        self.group_input_mean_p_dn_max_w.setObjectName(u"group_input_mean_p_dn_max_w")
        self.input_mean_p_dn_max_w = QDoubleSpinBox(self.tab_parameter_pmax)
        self.input_mean_p_dn_max_w.setObjectName(u"input_mean_p_dn_max_w")
        self.input_mean_p_dn_max_w.setDecimals(4)
        self.input_mean_p_dn_max_w.setMinimum(0.000100000000000)
        self.input_mean_p_dn_max_w.setMaximum(99999.000000000000000)

        self.group_input_mean_p_dn_max_w.addWidget(self.input_mean_p_dn_max_w)

        self.checkbox_var_p_dn_max_w = QCheckBox(self.tab_parameter_pmax)
        self.checkbox_var_p_dn_max_w.setObjectName(u"checkbox_var_p_dn_max_w")

        self.group_input_mean_p_dn_max_w.addWidget(self.checkbox_var_p_dn_max_w)

        self.input_var_p_dn_max_w = QDoubleSpinBox(self.tab_parameter_pmax)
        self.input_var_p_dn_max_w.setObjectName(u"input_var_p_dn_max_w")
        self.input_var_p_dn_max_w.setEnabled(False)
        self.input_var_p_dn_max_w.setDecimals(4)
        self.input_var_p_dn_max_w.setMaximum(999999.000000000000000)

        self.group_input_mean_p_dn_max_w.addWidget(self.input_var_p_dn_max_w)

        self.group_input_mean_p_dn_max_w.setStretch(0, 3)
        self.group_input_mean_p_dn_max_w.setStretch(2, 1)

        self.group_p_dn_max_w.addLayout(self.group_input_mean_p_dn_max_w)


        self.verticalLayout.addLayout(self.group_p_dn_max_w)

        self.group_p_dn_max_mu = QVBoxLayout()
        self.group_p_dn_max_mu.setObjectName(u"group_p_dn_max_mu")
        self.label_p_dn_max_mu = QLabel(self.tab_parameter_pmax)
        self.label_p_dn_max_mu.setObjectName(u"label_p_dn_max_mu")
        self.label_p_dn_max_mu.setFont(font3)
        self.label_p_dn_max_mu.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.group_p_dn_max_mu.addWidget(self.label_p_dn_max_mu)

        self.group_input_mean_p_dn_max_mu = QHBoxLayout()
        self.group_input_mean_p_dn_max_mu.setObjectName(u"group_input_mean_p_dn_max_mu")
        self.input_mean_p_dn_max_mu = QDoubleSpinBox(self.tab_parameter_pmax)
        self.input_mean_p_dn_max_mu.setObjectName(u"input_mean_p_dn_max_mu")
        self.input_mean_p_dn_max_mu.setDecimals(4)
        self.input_mean_p_dn_max_mu.setMinimum(0.000100000000000)
        self.input_mean_p_dn_max_mu.setMaximum(99999.000000000000000)

        self.group_input_mean_p_dn_max_mu.addWidget(self.input_mean_p_dn_max_mu)

        self.checkbox_var_p_dn_max_mu = QCheckBox(self.tab_parameter_pmax)
        self.checkbox_var_p_dn_max_mu.setObjectName(u"checkbox_var_p_dn_max_mu")

        self.group_input_mean_p_dn_max_mu.addWidget(self.checkbox_var_p_dn_max_mu)

        self.input_var_p_dn_max_mu = QDoubleSpinBox(self.tab_parameter_pmax)
        self.input_var_p_dn_max_mu.setObjectName(u"input_var_p_dn_max_mu")
        self.input_var_p_dn_max_mu.setEnabled(False)
        self.input_var_p_dn_max_mu.setDecimals(4)
        self.input_var_p_dn_max_mu.setMaximum(999999.000000000000000)

        self.group_input_mean_p_dn_max_mu.addWidget(self.input_var_p_dn_max_mu)

        self.group_input_mean_p_dn_max_mu.setStretch(0, 3)
        self.group_input_mean_p_dn_max_mu.setStretch(2, 1)

        self.group_p_dn_max_mu.addLayout(self.group_input_mean_p_dn_max_mu)


        self.verticalLayout.addLayout(self.group_p_dn_max_mu)

        self.group_p_dn_max_pT = QVBoxLayout()
        self.group_p_dn_max_pT.setObjectName(u"group_p_dn_max_pT")
        self.label_p_dn_max_pT = QLabel(self.tab_parameter_pmax)
        self.label_p_dn_max_pT.setObjectName(u"label_p_dn_max_pT")
        self.label_p_dn_max_pT.setFont(font3)
        self.label_p_dn_max_pT.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.group_p_dn_max_pT.addWidget(self.label_p_dn_max_pT)

        self.group_input_mean_p_dn_max_pT = QHBoxLayout()
        self.group_input_mean_p_dn_max_pT.setObjectName(u"group_input_mean_p_dn_max_pT")
        self.input_mean_p_dn_max_pT = QDoubleSpinBox(self.tab_parameter_pmax)
        self.input_mean_p_dn_max_pT.setObjectName(u"input_mean_p_dn_max_pT")
        self.input_mean_p_dn_max_pT.setDecimals(4)
        self.input_mean_p_dn_max_pT.setMinimum(0.000100000000000)
        self.input_mean_p_dn_max_pT.setMaximum(99999.000000000000000)

        self.group_input_mean_p_dn_max_pT.addWidget(self.input_mean_p_dn_max_pT)

        self.checkbox_var_p_dn_max_pT = QCheckBox(self.tab_parameter_pmax)
        self.checkbox_var_p_dn_max_pT.setObjectName(u"checkbox_var_p_dn_max_pT")

        self.group_input_mean_p_dn_max_pT.addWidget(self.checkbox_var_p_dn_max_pT)

        self.input_var_p_dn_max_pT = QDoubleSpinBox(self.tab_parameter_pmax)
        self.input_var_p_dn_max_pT.setObjectName(u"input_var_p_dn_max_pT")
        self.input_var_p_dn_max_pT.setEnabled(False)
        self.input_var_p_dn_max_pT.setDecimals(4)
        self.input_var_p_dn_max_pT.setMaximum(999999.000000000000000)

        self.group_input_mean_p_dn_max_pT.addWidget(self.input_var_p_dn_max_pT)

        self.group_input_mean_p_dn_max_pT.setStretch(0, 3)
        self.group_input_mean_p_dn_max_pT.setStretch(2, 1)

        self.group_p_dn_max_pT.addLayout(self.group_input_mean_p_dn_max_pT)


        self.verticalLayout.addLayout(self.group_p_dn_max_pT)

        self.tabWidget_rating_parameter.addTab(self.tab_parameter_pmax, "")

        self.tab_rating_parameter_1.addWidget(self.tabWidget_rating_parameter)

        self.group_result_info = QVBoxLayout()
        self.group_result_info.setObjectName(u"group_result_info")
        self.image_calculation_p_formula = QLabel(self.tab_rating_parameter)
        self.image_calculation_p_formula.setObjectName(u"image_calculation_p_formula")
        self.image_calculation_p_formula.setFont(font3)
        self.image_calculation_p_formula.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.group_result_info.addWidget(self.image_calculation_p_formula)

        self.group_input_calc = QHBoxLayout()
        self.group_input_calc.setObjectName(u"group_input_calc")
        self.group_max_min_input = QVBoxLayout()
        self.group_max_min_input.setObjectName(u"group_max_min_input")
        self.group_max_min_input_2 = QHBoxLayout()
        self.group_max_min_input_2.setObjectName(u"group_max_min_input_2")
        self.label_min_calc_p = QLabel(self.tab_rating_parameter)
        self.label_min_calc_p.setObjectName(u"label_min_calc_p")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.label_min_calc_p.setFont(font4)

        self.group_max_min_input_2.addWidget(self.label_min_calc_p)

        self.label_max_calc_p = QLabel(self.tab_rating_parameter)
        self.label_max_calc_p.setObjectName(u"label_max_calc_p")
        self.label_max_calc_p.setFont(font4)

        self.group_max_min_input_2.addWidget(self.label_max_calc_p)


        self.group_max_min_input.addLayout(self.group_max_min_input_2)

        self.group_max_min_input_1 = QHBoxLayout()
        self.group_max_min_input_1.setObjectName(u"group_max_min_input_1")
        self.input_calc_min = QDoubleSpinBox(self.tab_rating_parameter)
        self.input_calc_min.setObjectName(u"input_calc_min")
        self.input_calc_min.setFont(font1)
        self.input_calc_min.setDecimals(4)
        self.input_calc_min.setMaximum(999999.000000000000000)

        self.group_max_min_input_1.addWidget(self.input_calc_min)

        self.input_calc_max = QDoubleSpinBox(self.tab_rating_parameter)
        self.input_calc_max.setObjectName(u"input_calc_max")
        self.input_calc_max.setFont(font1)
        self.input_calc_max.setDecimals(4)
        self.input_calc_max.setMaximum(999999.000000000000000)

        self.group_max_min_input_1.addWidget(self.input_calc_max)


        self.group_max_min_input.addLayout(self.group_max_min_input_1)


        self.group_input_calc.addLayout(self.group_max_min_input)

        self.btn_calcutation_parameter = QPushButton(self.tab_rating_parameter)
        self.btn_calcutation_parameter.setObjectName(u"btn_calcutation_parameter")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_calcutation_parameter.sizePolicy().hasHeightForWidth())
        self.btn_calcutation_parameter.setSizePolicy(sizePolicy)
        self.btn_calcutation_parameter.setFont(font3)

        self.group_input_calc.addWidget(self.btn_calcutation_parameter)


        self.group_result_info.addLayout(self.group_input_calc)

        self.group_result = QHBoxLayout()
        self.group_result.setObjectName(u"group_result")
        self.label_const_calculation_p_result = QLabel(self.tab_rating_parameter)
        self.label_const_calculation_p_result.setObjectName(u"label_const_calculation_p_result")
        font5 = QFont()
        font5.setPointSize(24)
        font5.setBold(True)
        self.label_const_calculation_p_result.setFont(font5)

        self.group_result.addWidget(self.label_const_calculation_p_result)

        self.calculation_p_result = QLabel(self.tab_rating_parameter)
        self.calculation_p_result.setObjectName(u"calculation_p_result")
        self.calculation_p_result.setFont(font5)

        self.group_result.addWidget(self.calculation_p_result)


        self.group_result_info.addLayout(self.group_result)

        self.group_result_info.setStretch(0, 1)

        self.tab_rating_parameter_1.addLayout(self.group_result_info)

        self.tab_rating_parameter_1.setStretch(0, 5)
        self.tab_rating_parameter_1.setStretch(1, 5)

        self.horizontalLayout_5.addLayout(self.tab_rating_parameter_1)

        self.tabWidget_rating.addTab(self.tab_rating_parameter, "")
        self.tab_rating_strucs = QWidget()
        self.tab_rating_strucs.setObjectName(u"tab_rating_strucs")
        self.tabWidget_rating.addTab(self.tab_rating_strucs, "")

        self.verticalLayout_4.addWidget(self.tabWidget_rating)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.tabWidget_rating, self.tabWidget_rating_parameter)
        QWidget.setTabOrder(self.tabWidget_rating_parameter, self.input_mean_vk_ik)
        QWidget.setTabOrder(self.input_mean_vk_ik, self.checkbox_var_vk_ik)
        QWidget.setTabOrder(self.checkbox_var_vk_ik, self.input_var_vk_ik)
        QWidget.setTabOrder(self.input_var_vk_ik, self.input_mean_vk_m)
        QWidget.setTabOrder(self.input_mean_vk_m, self.checkbox_var_vk_m)
        QWidget.setTabOrder(self.checkbox_var_vk_m, self.input_var_vk_m)
        QWidget.setTabOrder(self.input_var_vk_m, self.input_mean_vk_zk)
        QWidget.setTabOrder(self.input_mean_vk_zk, self.checkbox_var_vk_zk)
        QWidget.setTabOrder(self.checkbox_var_vk_zk, self.input_var_vk_zk)
        QWidget.setTabOrder(self.input_var_vk_zk, self.input_mean_vk_cty)
        QWidget.setTabOrder(self.input_mean_vk_cty, self.checkbox_var_vk_cty)
        QWidget.setTabOrder(self.checkbox_var_vk_cty, self.input_var_vk_cty)
        QWidget.setTabOrder(self.input_var_vk_cty, self.input_mean_vk_d)
        QWidget.setTabOrder(self.input_mean_vk_d, self.checkbox_var_vk_d)
        QWidget.setTabOrder(self.checkbox_var_vk_d, self.input_var_vk_d)
        QWidget.setTabOrder(self.input_var_vk_d, self.input_mean_p_dn_max_q)
        QWidget.setTabOrder(self.input_mean_p_dn_max_q, self.checkbox_var_p_dn_max_q)
        QWidget.setTabOrder(self.checkbox_var_p_dn_max_q, self.input_var_p_dn_max_q)
        QWidget.setTabOrder(self.input_var_p_dn_max_q, self.input_mean_p_dn_max_w)
        QWidget.setTabOrder(self.input_mean_p_dn_max_w, self.checkbox_var_p_dn_max_w)
        QWidget.setTabOrder(self.checkbox_var_p_dn_max_w, self.input_var_p_dn_max_w)
        QWidget.setTabOrder(self.input_var_p_dn_max_w, self.input_mean_p_dn_max_mu)
        QWidget.setTabOrder(self.input_mean_p_dn_max_mu, self.checkbox_var_p_dn_max_mu)
        QWidget.setTabOrder(self.checkbox_var_p_dn_max_mu, self.input_var_p_dn_max_mu)
        QWidget.setTabOrder(self.input_var_p_dn_max_mu, self.input_mean_p_dn_max_pT)
        QWidget.setTabOrder(self.input_mean_p_dn_max_pT, self.checkbox_var_p_dn_max_pT)
        QWidget.setTabOrder(self.checkbox_var_p_dn_max_pT, self.input_var_p_dn_max_pT)
        QWidget.setTabOrder(self.input_var_p_dn_max_pT, self.input_calc_min)
        QWidget.setTabOrder(self.input_calc_min, self.input_calc_max)
        QWidget.setTabOrder(self.input_calc_max, self.btn_calcutation_parameter)

        self.retranslateUi(MainWindow)

        self.tabWidget_rating.setCurrentIndex(1)
        self.tabWidget_rating_parameter.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ch\u01b0\u01a1ng tr\u00ecnh \u0111\u00e1nh gi\u00e1 \u0111\u1ed9 tin c\u1eady s\u00fang b\u1ed9 binh", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionLoad_2.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.actionSave_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionLoad1.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.actionSave1.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"CH\u01af\u01a0NG TR\u00ccNH \u0110\u00c1NH GI\u00c1 \u0110\u1ed8 TIN C\u1eacY \n"
"S\u00daNG B\u1ed8 BINH", None))
        self.tabWidget_rating.setTabText(self.tabWidget_rating.indexOf(self.tab_info), QCoreApplication.translate("MainWindow", u"Th\u00f4ng tin", None))
        self.label_vk_ik.setText(QCoreApplication.translate("MainWindow", u"Xung l\u01b0\u1ee3ng kh\u00ed thu\u1ed1c (Ik)", None))
        self.checkbox_var_vk_ik.setText("")
        self.label_vk_m.setText(QCoreApplication.translate("MainWindow", u"Kh\u1ed1i l\u01b0\u1ee3ng \u0111\u1ea7u \u0111\u1ea1n (m)", None))
        self.checkbox_var_vk_m.setText("")
        self.label_vk_zk.setText(QCoreApplication.translate("MainWindow", u"B\u1ec1 d\u00e0y ch\u00e1y t\u01b0\u01a1ng \u0111\u1ed1i (Zk)", None))
        self.checkbox_var_vk_zk.setText("")
        self.label_vk_cty.setText(QCoreApplication.translate("MainWindow", u"H\u1ec7 s\u1ed1 t\u00ednh c\u00f4ng th\u1ee9c y\u1ebfu", None))
        self.checkbox_var_vk_cty.setText("")
        self.label_vk_d.setText(QCoreApplication.translate("MainWindow", u"C\u1ee1 \u0111\u1ea1n (d)", None))
        self.checkbox_var_vk_d.setText("")
        self.tabWidget_rating_parameter.setTabText(self.tabWidget_rating_parameter.indexOf(self.tab_parameter_vk), QCoreApplication.translate("MainWindow", u"Theo v\u1eadn t\u1ed1c t\u1ea1i v\u1ecb tr\u00ed k", None))
        self.label_p_dn_max_q.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ecdng l\u01b0\u1ee3ng \u0111\u1ea1n \u0111\u1ea1n (q)", None))
        self.checkbox_var_p_dn_max_q.setText("")
        self.label_p_dn_max_w.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ecdng l\u01b0\u1ee3ng li\u1ec1u ph\u00f3ng (w)", None))
        self.checkbox_var_p_dn_max_w.setText("")
        self.label_p_dn_max_mu.setText(QCoreApplication.translate("MainWindow", u"H\u1ec7 s\u1ed1 \u1ea3nh h\u01b0\u1edfng c\u1ee7a tr\u1ecdng l\u01b0\u1ee3ng \u0111\u1ea1n", None))
        self.checkbox_var_p_dn_max_mu.setText("")
        self.label_p_dn_max_pT.setText(QCoreApplication.translate("MainWindow", u"\u00c1p su\u1ea5t thu\u1eadt trung b\u00ecnh l\u1edbn nh\u1ea5t", None))
        self.checkbox_var_p_dn_max_pT.setText("")
        self.tabWidget_rating_parameter.setTabText(self.tabWidget_rating_parameter.indexOf(self.tab_parameter_pmax), QCoreApplication.translate("MainWindow", u"Theo \u00e1p su\u1ea5t \u0111\u00e1y n\u00f2ng l\u1edbn nh\u1ea5t", None))
        self.image_calculation_p_formula.setText(QCoreApplication.translate("MainWindow", u"C\u00f4ng th\u1ee9c", None))
        self.label_min_calc_p.setText(QCoreApplication.translate("MainWindow", u"T\u1ed1i thi\u1ec3u", None))
        self.label_max_calc_p.setText(QCoreApplication.translate("MainWindow", u"T\u1ed1i \u0111a", None))
        self.btn_calcutation_parameter.setText(QCoreApplication.translate("MainWindow", u"T\u00ednh", None))
        self.label_const_calculation_p_result.setText(QCoreApplication.translate("MainWindow", u"K\u1ebft qu\u1ea3:", None))
        self.calculation_p_result.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget_rating.setTabText(self.tabWidget_rating.indexOf(self.tab_rating_parameter), QCoreApplication.translate("MainWindow", u"\u0110\u00e1nh gi\u00e1 theo tham s\u1ed1 thi\u1ebft k\u1ebf", None))
        self.tabWidget_rating.setTabText(self.tabWidget_rating.indexOf(self.tab_rating_strucs), QCoreApplication.translate("MainWindow", u"\u0110\u00e1nh gi\u00e1 theo k\u1ebft c\u1ea5u", None))
    # retranslateUi

