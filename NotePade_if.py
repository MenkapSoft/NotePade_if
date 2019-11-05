# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NotePade.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QFontDialog







class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 664)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imaces/imaces/logo_cok_amacli_menkapsoft.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 40, 611, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_edit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.text_edit.setObjectName("text_edit")
        self.verticalLayout.addWidget(self.text_edit)
        self.splitter = QtWidgets.QSplitter(self.verticalLayoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.opn_btn = QtWidgets.QPushButton(self.splitter_2)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imaces/imaces/Open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.opn_btn.setIcon(icon1)
        self.opn_btn.setObjectName("opn_btn")
        self.clr_btn = QtWidgets.QPushButton(self.splitter_2)

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/imaces/imaces/Actions-edit-clear-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clr_btn.setIcon(icon2)
        self.clr_btn.setObjectName("clr_btn")
        self.sav_btn = QtWidgets.QPushButton(self.splitter_2)

        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/imaces/imaces/Save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sav_btn.setIcon(icon3)
        self.sav_btn.setObjectName("sav_btn")
        self.verticalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 21))
        self.menubar.setObjectName("menubar")
        self.menuDosya = QtWidgets.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDosya")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        MainWindow.setMenuBar(self.menubar)
        self.toolBarFile = QtWidgets.QToolBar(MainWindow)
        self.toolBarFile.setFocusPolicy(QtCore.Qt.NoFocus)
        self.toolBarFile.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBarFile.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBarFile.setObjectName("toolBarFile")

        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarFile)
        self.toolBarEdit = QtWidgets.QToolBar(MainWindow)
        self.toolBarEdit.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBarEdit.setObjectName("toolBarEdit")

        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarEdit)
        self.toolBarExit = QtWidgets.QToolBar(MainWindow)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBarExit.sizePolicy().hasHeightForWidth())
        self.toolBarExit.setSizePolicy(sizePolicy)
        self.toolBarExit.setFocusPolicy(QtCore.Qt.TabFocus)
        self.toolBarExit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.toolBarExit.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBarExit.setObjectName("toolBarExit")

        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarExit)
        self.toolBarStatusbar = QtWidgets.QToolBar(MainWindow)
        self.toolBarStatusbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBarStatusbar.setObjectName("toolBarStatusbar")

        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBarStatusbar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setAutoFillBackground(False)
        self.statusBar.setObjectName("statusBar")

        MainWindow.setStatusBar(self.statusBar)
        self.actionNew = QtWidgets.QAction(MainWindow)

        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/imaces/imaces/new-file-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon4)
        self.actionNew.setWhatsThis("")
        self.actionNew.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.actionNew.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionNew.setIconVisibleInMenu(True)
        self.actionNew.setPriority(QtWidgets.QAction.NormalPriority)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setCheckable(False)
        self.actionExit.setEnabled(True)

        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/imaces/imaces/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon5)
        self.actionExit.setObjectName("actionExit")
        self.actionMenkapSoft = QtWidgets.QAction(MainWindow)
        self.actionMenkapSoft.setIcon(icon)
        self.actionMenkapSoft.setObjectName("actionMenkapSoft")
        self.actionFont = QtWidgets.QAction(MainWindow)

        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/imaces/imaces/Fonts-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFont.setIcon(icon6)
        self.actionFont.setObjectName("actionFont")
        self.menuDosya.addAction(self.actionNew)
        self.menuDosya.addAction(self.actionOpen)
        self.menuDosya.addAction(self.actionSave)
        self.menuDosya.addSeparator()
        self.menuDosya.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionFont)
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.toolBarFile.addAction(self.actionNew)
        self.toolBarFile.addAction(self.actionOpen)
        self.toolBarFile.addAction(self.actionSave)
        self.toolBarEdit.addAction(self.actionFont)
        self.toolBarExit.addAction(self.actionExit)
        self.toolBarStatusbar.addAction(self.actionMenkapSoft)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MenkapSoft"))
        self.opn_btn.setText(_translate("MainWindow", "Open"))
        self.clr_btn.setText(_translate("MainWindow", "Clear"))
        self.sav_btn.setText(_translate("MainWindow", "Save"))
        self.menuDosya.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.toolBarFile.setWindowTitle(_translate("MainWindow", "File"))
        self.toolBarEdit.setWindowTitle(_translate("MainWindow", "Edit"))
        self.toolBarExit.setWindowTitle(_translate("MainWindow", "Exit"))
        self.toolBarStatusbar.setWindowTitle(_translate("MainWindow", "MenkapSoft"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+F4"))
        self.actionMenkapSoft.setText(_translate("MainWindow", "MenkapSoft"))
        self.actionMenkapSoft.setToolTip(_translate("MainWindow", "MenkapSoft"))
        self.actionFont.setText(_translate("MainWindow", "Font"))

    # clicked 
        
        self.actionExit.triggered.connect(self.exit)
        self.clr_btn.clicked.connect(self.clear_text)
        self.sav_btn.clicked.connect(self.save_text)
        self.actionSave.triggered.connect(self.save_text)
        self.opn_btn.clicked.connect(self.open_text)
        self.actionOpen.triggered.connect(self.open_text)
        self.actionFont.triggered.connect(self.font_changer)
        self.actionNew.triggered.connect(self.new_text)


   
    
    def font_changer(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.text_edit.setFont(font)
       
    def new_text(self):
        self.text_edit.clear()
    
    def open_text(self):
        
        filename, ok = QFileDialog.getOpenFileName(None, 'Open File', os.getenv('HOME'))
        if ok:
            with open(filename[0], 'r') as f:
                file_text = f.read()
                self.text_edit.setText(file_text)

    def save_text(self):
        filename, ok = QFileDialog.getSaveFileName(None, 'Save File', os.getenv('HOME'))
        if ok:
            with open(filename[0], 'w') as f:
                my_text = self.text_edit.toPlainText()
                f.write(my_text)
        
        
    def clear_text(self):
        self.text_edit.clear()
      
    def exit(self,MainWindow):
        sys.exit()


# import imaces_rc
import imaces


    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
