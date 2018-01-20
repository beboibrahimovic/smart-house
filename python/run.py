# -*- coding: utf-8 -*-

#              +=======================================+
#              |..........    Smart-House    ..........|
#              +---------------------------------------+
#              |#Author: Mahmoud Ibrahim (Bebo)        |
#              |#Contact: www.fb.com/bebo.ibrahimovic  |
#              |#Mail: Bebo_mm42@hotmail.com           |
#              |#Phone: 01119214459                    |
#              +=======================================+

import sys
from PyQt4 import QtCore, QtGui
from smart_house import Ui_MainWindow
import serial
import time
import select

ser = serial.Serial('/dev/ttyACM0',9600)

class smartHouse(QtGui.QMainWindow):

	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		# Full Screen the app on start
		self.setWindowState(QtCore.Qt.WindowMaximized)
		
		self.timer = QtCore.QTimer(self)
		self.timer.setInterval(200)
		self.timer.timeout.connect(self.displayTime)
		self.timer.start()
		
		# Change Selected Tab color and background-color
		
		stylesheet = """ 
		QTabBar::tab:selected {color: rgb(85, 0, 255);background-color: rgb(255, 255, 0);}
		"""
		self.setStyleSheet(stylesheet)
		
		""" This is Reception Actions """
		
		# Radio Button4 'Intensity Manual' on and off
		self.ui.radioButton_7.toggled.connect(lambda:self.btnstate3(self.ui.radioButton_7))
		self.ui.radioButton_7.toggled.connect(lambda:self.btnstate4(self.ui.radioButton_7))
		
		# radioButton_6 with radioButton_14 "On Mode Auto Intensity" action
		self.ui.radioButton_6.toggled.connect(lambda:self.set16(self.ui.radioButton_6,self.ui.radioButton_14))
		self.ui.radioButton_14.toggled.connect(lambda:self.set16(self.ui.radioButton_6,self.ui.radioButton_14))
		
		# radioButton_6 with radioButton_15 "off Mode Auto Intensity" action
		self.ui.radioButton_6.toggled.connect(lambda:self.set17(self.ui.radioButton_6,self.ui.radioButton_15))
		self.ui.radioButton_15.toggled.connect(lambda:self.set17(self.ui.radioButton_6,self.ui.radioButton_15))
		
		# radioButton_13 with radioButton_14 "on Mode Full Intensity" action
		self.ui.radioButton_14.toggled.connect(lambda:self.set18(self.ui.radioButton_14,self.ui.radioButton_13))
		self.ui.radioButton_13.toggled.connect(lambda:self.set18(self.ui.radioButton_14,self.ui.radioButton_13))
		
		# radioButton_13 with radioButton_15 "Off Mode Full Intensity" action
		self.ui.radioButton_15.toggled.connect(lambda:self.set19(self.ui.radioButton_15,self.ui.radioButton_13))
		self.ui.radioButton_13.toggled.connect(lambda:self.set19(self.ui.radioButton_15,self.ui.radioButton_13))

		# radioButton_7 with radioButton_14 "On Mode Manual Intensity" action
		self.ui.radioButton_7.toggled.connect(lambda:self.set20(self.ui.radioButton_7,self.ui.radioButton_14))
		self.ui.radioButton_14.toggled.connect(lambda:self.set20(self.ui.radioButton_7,self.ui.radioButton_14))
		self.ui.horizontalSlider_3.valueChanged.connect(lambda:self.set20(self.ui.radioButton_7,self.ui.radioButton_14))
		
		# radioButton_7 with radioButton_15 "Off Mode Manual Intensity" action
		self.ui.radioButton_7.toggled.connect(lambda:self.set21(self.ui.radioButton_7,self.ui.radioButton_15))
		self.ui.radioButton_15.toggled.connect(lambda:self.set21(self.ui.radioButton_7,self.ui.radioButton_15))
		self.ui.horizontalSlider_3.valueChanged.connect(lambda:self.set21(self.ui.radioButton_7,self.ui.radioButton_15))
		
		# radioButton_16 "Door on" action
		self.ui.radioButton_16.toggled.connect(lambda:self.btnstate13(self.ui.radioButton_16))
		
		# radioButton_17 "Door off" action
		self.ui.radioButton_17.toggled.connect(lambda:self.btnstate14(self.ui.radioButton_17))
		
		""" End of Reception Actions """
		
		""" This is Dining Room Actions """
		
		# Radio Button4 'Intensity Manual' on and off
		self.ui.radioButton_36.toggled.connect(lambda:self.btnstate6(self.ui.radioButton_36))
		self.ui.radioButton_36.toggled.connect(lambda:self.btnstate7(self.ui.radioButton_36))
		
		# radioButton_35 with radioButton_40 "On Mode Auto Intensity" action
		self.ui.radioButton_35.toggled.connect(lambda:self.set23(self.ui.radioButton_35,self.ui.radioButton_40))
		self.ui.radioButton_40.toggled.connect(lambda:self.set23(self.ui.radioButton_35,self.ui.radioButton_40))
		
		# radioButton_35 with radioButton_41 "off Mode Auto Intensity" action
		self.ui.radioButton_35.toggled.connect(lambda:self.set24(self.ui.radioButton_35,self.ui.radioButton_41))
		self.ui.radioButton_41.toggled.connect(lambda:self.set24(self.ui.radioButton_35,self.ui.radioButton_41))
		
		# radioButton_37 with radioButton_40 "on Mode Full Intensity" action
		self.ui.radioButton_40.toggled.connect(lambda:self.set25(self.ui.radioButton_40,self.ui.radioButton_37))
		self.ui.radioButton_37.toggled.connect(lambda:self.set25(self.ui.radioButton_40,self.ui.radioButton_37))
		
		# radioButton_37 with radioButton_41 "Off Mode Full Intensity" action
		self.ui.radioButton_41.toggled.connect(lambda:self.set26(self.ui.radioButton_41,self.ui.radioButton_37))
		self.ui.radioButton_37.toggled.connect(lambda:self.set26(self.ui.radioButton_41,self.ui.radioButton_37))

		# radioButton_36 with radioButton_40 "On Mode Manual Intensity" action
		self.ui.radioButton_36.toggled.connect(lambda:self.set27(self.ui.radioButton_36,self.ui.radioButton_40))
		self.ui.radioButton_40.toggled.connect(lambda:self.set27(self.ui.radioButton_36,self.ui.radioButton_40))
		self.ui.horizontalSlider_7.valueChanged.connect(lambda:self.set27(self.ui.radioButton_36,self.ui.radioButton_40))
		
		# radioButton_36 with radioButton_41 "Off Mode Manual Intensity" action
		self.ui.radioButton_36.toggled.connect(lambda:self.set28(self.ui.radioButton_36,self.ui.radioButton_41))
		self.ui.radioButton_41.toggled.connect(lambda:self.set28(self.ui.radioButton_36,self.ui.radioButton_41))
		self.ui.horizontalSlider_7.valueChanged.connect(lambda:self.set28(self.ui.radioButton_36,self.ui.radioButton_41))
		
		# radioButton_38 "Window on" action
		self.ui.radioButton_38.toggled.connect(lambda:self.btnstate16(self.ui.radioButton_38))
		
		# radioButton_39 "Window off" action
		self.ui.radioButton_39.toggled.connect(lambda:self.btnstate17(self.ui.radioButton_39))
		
		""" End of Dining Room Actions """
		
		""" This is Office Actions """
		
		# radioButton_45 'Intensity Manual' on and off
		self.ui.radioButton_45.toggled.connect(lambda:self.btnstate19(self.ui.radioButton_45))
		self.ui.radioButton_45.toggled.connect(lambda:self.btnstate20(self.ui.radioButton_45))
		
		# radioButton_44 with radioButton_42 "On Mode Auto Intensity" action
		self.ui.radioButton_44.toggled.connect(lambda:self.set30(self.ui.radioButton_44,self.ui.radioButton_42))
		self.ui.radioButton_42.toggled.connect(lambda:self.set30(self.ui.radioButton_44,self.ui.radioButton_42))
		
		# radioButton_44 with radioButton_43 "off Mode Auto Intensity" action
		self.ui.radioButton_44.toggled.connect(lambda:self.set31(self.ui.radioButton_44,self.ui.radioButton_43))
		self.ui.radioButton_43.toggled.connect(lambda:self.set31(self.ui.radioButton_44,self.ui.radioButton_43))
		
		# radioButton_46 with radioButton_42 "on Mode Full Intensity" action
		self.ui.radioButton_42.toggled.connect(lambda:self.set32(self.ui.radioButton_42,self.ui.radioButton_46))
		self.ui.radioButton_46.toggled.connect(lambda:self.set32(self.ui.radioButton_42,self.ui.radioButton_46))
		
		# radioButton_46 with radioButton_43 "Off Mode Full Intensity" action
		self.ui.radioButton_43.toggled.connect(lambda:self.set33(self.ui.radioButton_43,self.ui.radioButton_46))
		self.ui.radioButton_46.toggled.connect(lambda:self.set33(self.ui.radioButton_43,self.ui.radioButton_46))

		# radioButton_45 with radioButton_42 "On Mode Manual Intensity" action
		self.ui.radioButton_45.toggled.connect(lambda:self.set34(self.ui.radioButton_45,self.ui.radioButton_42))
		self.ui.radioButton_42.toggled.connect(lambda:self.set34(self.ui.radioButton_45,self.ui.radioButton_42))
		self.ui.horizontalSlider_8.valueChanged.connect(lambda:self.set34(self.ui.radioButton_45,self.ui.radioButton_42))
		
		# radioButton_45 with radioButton_43 "Off Mode Manual Intensity" action
		self.ui.radioButton_45.toggled.connect(lambda:self.set35(self.ui.radioButton_45,self.ui.radioButton_43))
		self.ui.radioButton_43.toggled.connect(lambda:self.set35(self.ui.radioButton_45,self.ui.radioButton_43))
		self.ui.horizontalSlider_8.valueChanged.connect(lambda:self.set35(self.ui.radioButton_45,self.ui.radioButton_43))
		
		""" End of Office Actions """
		
		""" This is Room 1 Actions """
		
		# Radio Button4 'Intensity Manual' on and off
		self.ui.radioButton_4.toggled.connect(lambda:self.btnstate1(self.ui.radioButton_4))
		self.ui.radioButton_4.toggled.connect(lambda:self.btnstate2(self.ui.radioButton_4))
		
		# Change pushButton "Security Alarm" to disable
		self.ui.pushButton.setEnabled(False)
		
		# pushButton "Security Alarm" Action
		self.ui.pushButton.clicked.connect(lambda:self.toggleLED(self.ui.pushButton))
		
		# radioButton with radioButton1 "Auto Mode Auto Intensity" action
		self.ui.radioButton.toggled.connect(lambda:self.set(self.ui.radioButton,self.ui.radioButton1))
		self.ui.radioButton1.toggled.connect(lambda:self.set(self.ui.radioButton,self.ui.radioButton1))
		
		# radioButton with radioButton_2 "On Mode Auto Intensity" action
		self.ui.radioButton.toggled.connect(lambda:self.set2(self.ui.radioButton,self.ui.radioButton_2))
		self.ui.radioButton_2.toggled.connect(lambda:self.set2(self.ui.radioButton,self.ui.radioButton_2))
		
		# radioButton with radioButton_3 "off Mode Auto Intensity" action
		self.ui.radioButton.toggled.connect(lambda:self.set3(self.ui.radioButton,self.ui.radioButton_3))
		self.ui.radioButton_3.toggled.connect(lambda:self.set3(self.ui.radioButton,self.ui.radioButton_3))
		
		# radioButton_5 with radioButton1 "Auto Mode Full Intensity" action
		self.ui.radioButton1.toggled.connect(lambda:self.set4(self.ui.radioButton1,self.ui.radioButton_5))
		self.ui.radioButton_5.toggled.connect(lambda:self.set4(self.ui.radioButton1,self.ui.radioButton_5))
		
		# radioButton_5 with radioButton_2 "on Mode Full Intensity" action
		self.ui.radioButton_2.toggled.connect(lambda:self.set5(self.ui.radioButton_2,self.ui.radioButton_5))
		self.ui.radioButton_5.toggled.connect(lambda:self.set5(self.ui.radioButton_2,self.ui.radioButton_5))
		
		# radioButton_5 with radioButton_3 "Off Mode Full Intensity" action
		self.ui.radioButton_3.toggled.connect(lambda:self.set6(self.ui.radioButton_3,self.ui.radioButton_5))
		self.ui.radioButton_5.toggled.connect(lambda:self.set6(self.ui.radioButton_3,self.ui.radioButton_5))

		# radioButton_4 with radioButton1 "Auto Mode Manual Intensity" action
		self.ui.radioButton_4.toggled.connect(lambda:self.set7(self.ui.radioButton_4,self.ui.radioButton1))
		self.ui.radioButton1.toggled.connect(lambda:self.set7(self.ui.radioButton_4,self.ui.radioButton1))
		self.ui.horizontalSlider.valueChanged.connect(lambda:self.set7(self.ui.radioButton_4,self.ui.radioButton1))
		
		# radioButton_4 with radioButton_2 "On Mode Manual Intensity" action
		self.ui.radioButton_4.toggled.connect(lambda:self.set8(self.ui.radioButton_4,self.ui.radioButton_2))
		self.ui.radioButton_2.toggled.connect(lambda:self.set8(self.ui.radioButton_4,self.ui.radioButton_2))
		self.ui.horizontalSlider.valueChanged.connect(lambda:self.set8(self.ui.radioButton_4,self.ui.radioButton_2))
		
		# radioButton_4 with radioButton_3 "Off Mode Manual Intensity" action
		self.ui.radioButton_4.toggled.connect(lambda:self.set9(self.ui.radioButton_4,self.ui.radioButton_3))
		self.ui.radioButton_3.toggled.connect(lambda:self.set9(self.ui.radioButton_4,self.ui.radioButton_3))
		self.ui.horizontalSlider.valueChanged.connect(lambda:self.set9(self.ui.radioButton_4,self.ui.radioButton_3))
		
		# radioButton1_2 {Temperature on} Action
		self.ui.radioButton1_2.toggled.connect(lambda:self.set10(self.ui.radioButton1_2))
		
		# radioButton_10 {Temperature off} Action
		self.ui.radioButton_10.toggled.connect(lambda:self.set11(self.ui.radioButton_10))
		
		# pushButton_7 {Temperature Up} Action
		self.ui.pushButton_7.clicked.connect(lambda:self.set77(self.ui.pushButton_7))
		
		# pushButton_8 {Temperature Down} Action
		self.ui.pushButton_8.clicked.connect(lambda:self.set78(self.ui.pushButton_8))
		
		# pushButton_6 {Fan Speed } Action
		self.ui.pushButton_6.clicked.connect(lambda:self.set79(self.ui.pushButton_6))
		
		# pushButton_9 {Swing} Action
		self.ui.pushButton_9.clicked.connect(lambda:self.set13(self.ui.pushButton_9))
		
		# pushButton_2 {Mode} Action
		self.ui.pushButton_2.clicked.connect(lambda:self.set80(self.ui.pushButton_2))
		
		""" End of Room 1 Actions """
	
		""" This is Room 2 Actions """
		
		# radioButton_21 'Intensity Manual' on and off
		self.ui.radioButton_21.toggled.connect(lambda:self.btnstate22(self.ui.radioButton_21))
		self.ui.radioButton_21.toggled.connect(lambda:self.btnstate23(self.ui.radioButton_21))
		
		# radioButton_20 with radioButton_18 "On Mode Auto Intensity" action
		self.ui.radioButton_20.toggled.connect(lambda:self.set37(self.ui.radioButton_20,self.ui.radioButton_18))
		self.ui.radioButton_18.toggled.connect(lambda:self.set37(self.ui.radioButton_20,self.ui.radioButton_18))
		
		# radioButton_20 with radioButton_19 "off Mode Auto Intensity" action
		self.ui.radioButton_20.toggled.connect(lambda:self.set38(self.ui.radioButton_20,self.ui.radioButton_19))
		self.ui.radioButton_19.toggled.connect(lambda:self.set38(self.ui.radioButton_20,self.ui.radioButton_19))
		
		# radioButton_22 with radioButton_18 "on Mode Full Intensity" action
		self.ui.radioButton_18.toggled.connect(lambda:self.set39(self.ui.radioButton_18,self.ui.radioButton_22))
		self.ui.radioButton_22.toggled.connect(lambda:self.set39(self.ui.radioButton_18,self.ui.radioButton_22))
		
		# radioButton_22 with radioButton_19 "Off Mode Full Intensity" action
		self.ui.radioButton_19.toggled.connect(lambda:self.set40(self.ui.radioButton_19,self.ui.radioButton_22))
		self.ui.radioButton_22.toggled.connect(lambda:self.set40(self.ui.radioButton_19,self.ui.radioButton_22))

		# radioButton_21 with radioButton_18 "On Mode Manual Intensity" action
		self.ui.radioButton_21.toggled.connect(lambda:self.set41(self.ui.radioButton_21,self.ui.radioButton_18))
		self.ui.radioButton_18.toggled.connect(lambda:self.set41(self.ui.radioButton_21,self.ui.radioButton_18))
		self.ui.horizontalSlider_4.valueChanged.connect(lambda:self.set41(self.ui.radioButton_21,self.ui.radioButton_18))
		
		# radioButton_21 with radioButton_19 "Off Mode Manual Intensity" action
		self.ui.radioButton_21.toggled.connect(lambda:self.set42(self.ui.radioButton_21,self.ui.radioButton_19))
		self.ui.radioButton_19.toggled.connect(lambda:self.set42(self.ui.radioButton_21,self.ui.radioButton_19))
		self.ui.horizontalSlider_4.valueChanged.connect(lambda:self.set42(self.ui.radioButton_21,self.ui.radioButton_19))

		# radioButton1_3 {Certain Mode open} Action
		self.ui.radioButton1_3.toggled.connect(lambda:self.set43(self.ui.radioButton1_3))
		
		# radioButton_23 {Certain Mode close} Action
		self.ui.radioButton_23.toggled.connect(lambda:self.set44(self.ui.radioButton_23))
		
		# radioButton_24 {Certain Mode smart} Action
		self.ui.radioButton_24.toggled.connect(lambda:self.set45(self.ui.radioButton_24))
		
		""" End of Room 2 Actions """
	
		""" This is Room 3 Actions """
		
		# Change pushButton_3 "Fire-Secure" and pushButton_4 "Emergency-Off" to disable
		self.ui.pushButton_3.setEnabled(False)
		self.ui.pushButton_4.setEnabled(False)
		
		# pushButton_3 "Fire-Secure" Action
		self.ui.pushButton_3.clicked.connect(lambda:self.toggleLED3(self.ui.pushButton_3))
		
		# pushButton_4 "Emergency-off" Action
		self.ui.pushButton_4.clicked.connect(lambda:self.toggleLED4(self.ui.pushButton_4))
		
		# radioButton_76 'Intensity Manual' on and off
		self.ui.radioButton_76.toggled.connect(lambda:self.btnstate25(self.ui.radioButton_76))
		self.ui.radioButton_76.toggled.connect(lambda:self.btnstate26(self.ui.radioButton_76))
		
		# radioButton_75 with radioButton_73 "On Mode Auto Intensity" action
		self.ui.radioButton_75.toggled.connect(lambda:self.set47(self.ui.radioButton_75,self.ui.radioButton_73))
		self.ui.radioButton_73.toggled.connect(lambda:self.set47(self.ui.radioButton_75,self.ui.radioButton_73))
		
		# radioButton_75 with radioButton_74 "off Mode Auto Intensity" action
		self.ui.radioButton_75.toggled.connect(lambda:self.set48(self.ui.radioButton_75,self.ui.radioButton_74))
		self.ui.radioButton_74.toggled.connect(lambda:self.set48(self.ui.radioButton_75,self.ui.radioButton_74))
		
		# radioButton_77 with radioButton_73 "on Mode Full Intensity" action
		self.ui.radioButton_73.toggled.connect(lambda:self.set49(self.ui.radioButton_73,self.ui.radioButton_77))
		self.ui.radioButton_77.toggled.connect(lambda:self.set49(self.ui.radioButton_73,self.ui.radioButton_77))
		
		# radioButton_77 with radioButton_74 "Off Mode Full Intensity" action
		self.ui.radioButton_74.toggled.connect(lambda:self.set50(self.ui.radioButton_74,self.ui.radioButton_77))
		self.ui.radioButton_77.toggled.connect(lambda:self.set50(self.ui.radioButton_74,self.ui.radioButton_77))

		# radioButton_76 with radioButton_73 "On Mode Manual Intensity" action
		self.ui.radioButton_76.toggled.connect(lambda:self.set51(self.ui.radioButton_76,self.ui.radioButton_73))
		self.ui.radioButton_73.toggled.connect(lambda:self.set51(self.ui.radioButton_76,self.ui.radioButton_73))
		self.ui.horizontalSlider_13.valueChanged.connect(lambda:self.set51(self.ui.radioButton_76,self.ui.radioButton_73))
		
		# radioButton_76 with radioButton_74 "Off Mode Manual Intensity" action
		self.ui.radioButton_76.toggled.connect(lambda:self.set52(self.ui.radioButton_76,self.ui.radioButton_74))
		self.ui.radioButton_74.toggled.connect(lambda:self.set52(self.ui.radioButton_76,self.ui.radioButton_74))
		self.ui.horizontalSlider_13.valueChanged.connect(lambda:self.set52(self.ui.radioButton_76,self.ui.radioButton_74))

		# radioButton1_7 {Certain Mode open} Action
		self.ui.radioButton1_7.toggled.connect(lambda:self.set53(self.ui.radioButton1_7))
		
		# radioButton_78 {Certain Mode close} Action
		self.ui.radioButton_78.toggled.connect(lambda:self.set54(self.ui.radioButton_78))
		
		# radioButton_80 "Window on" action
		self.ui.radioButton_80.toggled.connect(lambda:self.btnstate27(self.ui.radioButton_80))
		
		# radioButton_81 "Window off" action
		self.ui.radioButton_81.toggled.connect(lambda:self.btnstate28(self.ui.radioButton_81))
		
		""" End of Room 3 Actions """
	
		""" This is Master Bedroom Actions """
		
		# radioButton_85 'Intensity Manual' on and off
		self.ui.radioButton_85.toggled.connect(lambda:self.btnstate30(self.ui.radioButton_85))
		self.ui.radioButton_85.toggled.connect(lambda:self.btnstate31(self.ui.radioButton_85))
		
		# radioButton_84 with radioButton_82 "On Mode Auto Intensity" action
		self.ui.radioButton_84.toggled.connect(lambda:self.set57(self.ui.radioButton_84,self.ui.radioButton_82))
		self.ui.radioButton_82.toggled.connect(lambda:self.set57(self.ui.radioButton_84,self.ui.radioButton_82))
		
		# radioButton_84 with radioButton_83 "off Mode Auto Intensity" action
		self.ui.radioButton_84.toggled.connect(lambda:self.set58(self.ui.radioButton_84,self.ui.radioButton_83))
		self.ui.radioButton_83.toggled.connect(lambda:self.set58(self.ui.radioButton_84,self.ui.radioButton_83))
		
		# radioButton_86 with radioButton_82 "on Mode Full Intensity" action
		self.ui.radioButton_82.toggled.connect(lambda:self.set59(self.ui.radioButton_82,self.ui.radioButton_86))
		self.ui.radioButton_86.toggled.connect(lambda:self.set59(self.ui.radioButton_82,self.ui.radioButton_86))
		
		# radioButton_86 with radioButton_83 "Off Mode Full Intensity" action
		self.ui.radioButton_83.toggled.connect(lambda:self.set60(self.ui.radioButton_83,self.ui.radioButton_86))
		self.ui.radioButton_86.toggled.connect(lambda:self.set60(self.ui.radioButton_83,self.ui.radioButton_86))

		# radioButton_85 with radioButton_82 "On Mode Manual Intensity" action
		self.ui.radioButton_85.toggled.connect(lambda:self.set61(self.ui.radioButton_85,self.ui.radioButton_82))
		self.ui.radioButton_82.toggled.connect(lambda:self.set61(self.ui.radioButton_85,self.ui.radioButton_82))
		self.ui.horizontalSlider_14.valueChanged.connect(lambda:self.set61(self.ui.radioButton_85,self.ui.radioButton_82))
		
		# radioButton_85 with radioButton_83 "Off Mode Manual Intensity" action
		self.ui.radioButton_85.toggled.connect(lambda:self.set62(self.ui.radioButton_85,self.ui.radioButton_83))
		self.ui.radioButton_83.toggled.connect(lambda:self.set62(self.ui.radioButton_85,self.ui.radioButton_83))
		self.ui.horizontalSlider_14.valueChanged.connect(lambda:self.set62(self.ui.radioButton_85,self.ui.radioButton_83))
		
		""" End of Master Bedroom Actions """
		
		""" This is Kitchen Actions """

		# Change pushButton_5 "Gas-Secure" to disable
		self.ui.pushButton_5.setEnabled(False)
		
		# pushButton_5 "Gas-Secure" Action
		self.ui.pushButton_5.clicked.connect(lambda:self.toggleLED6(self.ui.pushButton_5))
		
		# radioButton_87 "Light on" action
		self.ui.radioButton_87.toggled.connect(lambda:self.btnstate33(self.ui.radioButton_87))
		
		# radioButton_88 "Light off" action
		self.ui.radioButton_88.toggled.connect(lambda:self.btnstate34(self.ui.radioButton_88))
		
		""" End of Kitchen Actions """
		
		""" This is Garage Actions """

		# radioButton_89 "Door open" action
		self.ui.radioButton_89.toggled.connect(lambda:self.btnstate36(self.ui.radioButton_89))
		
		# radioButton_90 "Door close" action
		self.ui.radioButton_90.toggled.connect(lambda:self.btnstate37(self.ui.radioButton_90))
		
		# radioButton_95 "Door stop" action
		self.ui.radioButton_95.toggled.connect(lambda:self.btnstate48(self.ui.radioButton_95))
		
		""" End of Garage Actions """
	
		"""" This is Outside&Garden Actions """

		# radioButton_91 "Outside Light on" action
		self.ui.radioButton_91.toggled.connect(lambda:self.btnstate38(self.ui.radioButton_91))
		
		# radioButton_92 "Outside Light off" action
		self.ui.radioButton_92.toggled.connect(lambda:self.btnstate39(self.ui.radioButton_92))
		
		# radioButton_91 "Garden Light on" action
		self.ui.radioButton_93.toggled.connect(lambda:self.btnstate45(self.ui.radioButton_93))
		
		# radioButton_94 "Garden Light off" action
		self.ui.radioButton_94.toggled.connect(lambda:self.btnstate46(self.ui.radioButton_94))
		
		""" End of Outside&Garden Actions """
		
		""" Security Actions """
		
		# radioButton_11 "Security Level 1" action
		self.ui.radioButton_11.toggled.connect(lambda:self.btnstate10(self.ui.radioButton_11))
		
		# radioButton_25 "Security Level 2" action
		self.ui.radioButton_25.toggled.connect(lambda:self.btnstate42(self.ui.radioButton_25))
		
		# radioButton_12 "security off" action
		self.ui.radioButton_12.toggled.connect(lambda:self.btnstate11(self.ui.radioButton_12))

		""" End of Security Actions """
		
	"""	Reception  Fucntions """
	
	# Function for radioButton_7 'Intensity Manual'
	def btnstate3(self,b):
	    if b.isChecked() == True:
			self.ui.horizontalSlider_3.setEnabled(True)
			return True
	
	def btnstate4(self,b):
	    if b.isChecked() == False:
			self.ui.horizontalSlider_3.setEnabled(False)
	
	# Function for radioButton_6 with radioButton_14 "On Mode Auto Intensity"
	def set16(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "on Mode Auto Intensity in Reception"
				ser.write('RCPLAOn')
				
	# Function for radioButton_6 with radioButton_15 "off Mode Auto Intensity"
	def set17(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "off Mode Auto Intensity in Reception"
				ser.write('RCPLOff')
	
	# Function for radioButton_13 with radioButton_14 "on Mode Full Intensity"
	def set18(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "on Mode Full Intensity in Reception"
				ser.write('RCPLOn')
				
	# Function for radioButton_13 with radioButton_15 "Off Mode Full Intensity"
	def set19(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "Off Mode Full Intensity in Reception"
				ser.write('RCPLOff')
	
	# Function for radioButton_7 with radioButton_14 "On Mode Manual Intensity"
	def set20(self,b,c):
		if b.isChecked() == True:
			if c.isChecked() == True:
				ser.write('RCPLMOn')
				time.sleep(0.02)
				if self.ui.horizontalSlider_3.value() == 0:
					time.sleep(0.02)
					ser.write('RCPmlc000')
					#print "Manual Value is 0 with on mode in Reception"
				elif self.ui.horizontalSlider_3.value() == 1:
					time.sleep(0.02)
					ser.write('RCPmlc025')
					#print "Manual Value is 1 with on mode in Reception"
				elif self.ui.horizontalSlider_3.value() == 2:
					time.sleep(0.02)
					ser.write('RCPmlc050')
					#print "Manual Value is 2 with on mode in Reception"
				elif self.ui.horizontalSlider_3.value() == 3:
					time.sleep(0.02)
					ser.write('RCPmlc075')
					#print "Manual Value is 3 with on mode in Reception"
				elif self.ui.horizontalSlider_3.value() == 4:
					time.sleep(0.02)
					ser.write('RCPmlc100')
					#print "Manual Value is 4 with on mode in Reception"
				elif self.ui.horizontalSlider_3.value() == 5:
					time.sleep(0.02)
					ser.write('RCPmlc125')
					#print "Manual Value is 5 with on mode in Reception"
				elif self.ui.horizontalSlider_3.value() == 6:
					time.sleep(0.02)
					ser.write('RCPmlc150')
					#print "Manual Value is 6 with on mode in Reception"
				elif self.ui.horizontalSlider_3.value() == 7:
					time.sleep(0.02)
					ser.write('RCPmlc175')
					#print "Manual Value is 7 with on mode in Reception"
				elif self.ui.horizontalSlider_3.value() == 8:
					time.sleep(0.02)
					ser.write('RCPmlc200')
					#print "Manual Value is 8 with on mode in Reception"
				elif self.ui.horizontalSlider_3.value() == 9:
					time.sleep(0.02)
					ser.write('RCPmlc225')
					#print "Manual Value is 9 with on mode in Reception"
				elif self.ui.horizontalSlider_3.value() == 10:
					time.sleep(0.02)
					ser.write('RCPmlc255')
					#print "Manual Value is 10 with on mode in Reception"
				
				#print "Manual Value is " + str(self.ui.horizontalSlider_3.value()) + " with on mode in Reception"
	
	# Function for radioButton_7 with radioButton_15 "Off Mode Manual Intensity"
	def set21(self,b,c):
		if b.isChecked() == True:
			if c.isChecked() == True:
				#print "Manual Value is " + str(self.ui.horizontalSlider_3.value()) + " with off mode in Reception"
				ser.write('RCPLOff')
	
	# Function for radioButton_16 "Door on" action
	def btnstate13(self,b):
	    if b.isChecked() == True:
			#print "Door On"
			ser.write('OpenDoor')
			
	# Function for radioButton_17 "Door off" action
	def btnstate14(self,b):
	    if b.isChecked() == True:
			#print "Door Off"
			ser.write('CloseDoor')
	
	""" End of Reception Fucntios """
	
	"""	Dining Room  Fucntions """
	
	# Function for radioButton_36 'Intensity Manual'
	def btnstate6(self,b):
	    if b.isChecked() == True:
			self.ui.horizontalSlider_7.setEnabled(True)
			return True
	
	def btnstate7(self,b):
	    if b.isChecked() == False:
			self.ui.horizontalSlider_7.setEnabled(False)
	
	# Function for radioButton_35 with radioButton_40 "On Mode Auto Intensity"
	def set23(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "on Mode Auto Intensity in Dining Room"
				ser.write('DNLAOn')
				
	# Function for radioButton_35 with radioButton_41 "off Mode Auto Intensity"
	def set24(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "off Mode Auto Intensity in Dining Room"
				ser.write('DNLOff')
	
	# Function for radioButton_37 with radioButton_40 "on Mode Full Intensity"
	def set25(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "on Mode Full Intensity in Dining Room"
				ser.write('DNLOn')
				
	# Function for radioButton_37 with radioButton_41 "Off Mode Full Intensity"
	def set26(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "Off Mode Full Intensity in Dining Room"
				ser.write('DNLOff')
	
	# Function for radioButton_36 with radioButton_40 "On Mode Manual Intensity"
	def set27(self,b,c):
		if b.isChecked() == True:
			if c.isChecked() == True:
				ser.write('DNLMOn')
				time.sleep(0.02)
				if self.ui.horizontalSlider_7.value() == 0:
					time.sleep(0.02)
					ser.write('DN0mlc000')
					#print "Manual Value is 0 with on mode in Dining Room"
				elif self.ui.horizontalSlider_7.value() == 1:
					time.sleep(0.02)
					ser.write('DN0mlc025')
					#print "Manual Value is 1 with on mode in Dining Room"
				elif self.ui.horizontalSlider_7.value() == 2:
					time.sleep(0.02)
					ser.write('DN0mlc050')
					#print "Manual Value is 2 with on mode in Dining Room"
				elif self.ui.horizontalSlider_7.value() == 3:
					time.sleep(0.02)
					ser.write('DN0mlc075')
					#print "Manual Value is 3 with on mode in Dining Room"
				elif self.ui.horizontalSlider_7.value() == 4:
					time.sleep(0.02)
					ser.write('DN0mlc100')
					#print "Manual Value is 4 with on mode in Dining Room"
				elif self.ui.horizontalSlider_3.value() == 5:
					time.sleep(0.02)
					ser.write('DN0mlc125')
					#print "Manual Value is 5 with on mode in Dining Room"
				elif self.ui.horizontalSlider_7.value() == 6:
					time.sleep(0.02)
					ser.write('DN0mlc150')
					#print "Manual Value is 6 with on mode in Dining Room"
				elif self.ui.horizontalSlider_7.value() == 7:
					time.sleep(0.02)
					ser.write('DN0mlc175')
					#print "Manual Value is 7 with on mode in Dining Room"
				elif self.ui.horizontalSlider_7.value() == 8:
					time.sleep(0.02)
					ser.write('DN0mlc200')
					#print "Manual Value is 8 with on mode in Dining Room"
				elif self.ui.horizontalSlider_7.value() == 9:
					time.sleep(0.02)
					ser.write('DN0mlc225')
					#print "Manual Value is 9 with on mode in Dining Room"
				elif self.ui.horizontalSlider_7.value() == 10:
					time.sleep(0.02)
					ser.write('DN0mlc255')
					#print "Manual Value is 10 with on mode in Dining Room"
				
				#print "Manual Value is " + str(self.ui.horizontalSlider_7.value()) + " with on mode in Dining Room"
	
	# Function for radioButton_36 with radioButton_41 "Off Mode Manual Intensity"
	def set28(self,b,c):
		if b.isChecked() == True:
			if c.isChecked() == True:
				#print "Manual Value is " + str(self.ui.horizontalSlider_7.value()) + " with off mode in Dining Room"
				ser.write('DNLOff')
	
	# Function for radioButton_38 "Window on"
	def btnstate16(self,b):
	    if b.isChecked() == True:
			#print "Window On"
			ser.write('DNWOpen')
			
	# Function for radioButton_39 "Window off"
	def btnstate17(self,b):
	    if b.isChecked() == True:
			#print "Window Off"
			ser.write('DNWClose')
			
	""" End of Dining Room Fucntios """
	
	"""	Office  Fucntions """
	
	# Function for radioButton_45 'Intensity Manual'
	def btnstate19(self,b):
	    if b.isChecked() == True:
			self.ui.horizontalSlider_8.setEnabled(True)
			return True
	
	def btnstate20(self,b):
	    if b.isChecked() == False:
			self.ui.horizontalSlider_8.setEnabled(False)
	
	# Function for radioButton_44 with radioButton_42 "On Mode Auto Intensity"
	def set30(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "on Mode Auto Intensity in Office"
				ser.write('OFCLAOn')
				
	# Function for radioButton_44 with radioButton_43 "off Mode Auto Intensity"
	def set31(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "off Mode Auto Intensity in Office"
				ser.write('OFCLOff')
	
	# Function for radioButton_46 with radioButton_42 "on Mode Full Intensity"
	def set32(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "on Mode Full Intensity in Office"
				ser.write('OFCLOn')
				
	# Function for radioButton_46 with radioButton_43 "Off Mode Full Intensity"
	def set33(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "Off Mode Full Intensity in Office"
				ser.write('OFCLOff')
	
	# Function for radioButton_45 with radioButton_42 "On Mode Manual Intensity"
	def set34(self,b,c):
		if b.isChecked() == True:
			if c.isChecked() == True:
				ser.write('OFCLMOn')
				time.sleep(0.02)
				if self.ui.horizontalSlider_8.value() == 0:
					time.sleep(0.02)
					ser.write('OFCmlc000')
					#print "Manual Value is 0 with on mode in Office"
				elif self.ui.horizontalSlider_8.value() == 1:
					time.sleep(0.02)
					ser.write('OFCmlc025')
					#print "Manual Value is 1 with on mode in Office"
				elif self.ui.horizontalSlider_8.value() == 2:
					time.sleep(0.02)
					ser.write('OFCmlc050')
					#print "Manual Value is 2 with on mode in Office"
				elif self.ui.horizontalSlider_8.value() == 3:
					time.sleep(0.02)
					ser.write('OFCmlc075')
					#print "Manual Value is 3 with on mode in Office"
				elif self.ui.horizontalSlider_8.value() == 4:
					time.sleep(0.02)
					ser.write('OFCmlc100')
					#print "Manual Value is 4 with on mode in Office"
				elif self.ui.horizontalSlider_8.value() == 5:
					time.sleep(0.02)
					ser.write('OFCmlc125')
					#print "Manual Value is 5 with on mode in Office"
				elif self.ui.horizontalSlider_8.value() == 6:
					time.sleep(0.02)
					ser.write('OFCmlc150')
					#print "Manual Value is 6 with on mode in Office"
				elif self.ui.horizontalSlider_8.value() == 7:
					time.sleep(0.02)
					ser.write('OFCmlc175')
					#print "Manual Value is 7 with on mode in Office"
				elif self.ui.horizontalSlider_8.value() == 8:
					time.sleep(0.02)
					ser.write('OFCmlc200')
					#print "Manual Value is 8 with on mode in Office"
				elif self.ui.horizontalSlider_8.value() == 9:
					time.sleep(0.02)
					ser.write('OFCmlc225')
					#print "Manual Value is 9 with on mode in Office"
				elif self.ui.horizontalSlider_8.value() == 10:
					time.sleep(0.02)
					ser.write('OFCmlc255')
					#print "Manual Value is 10 with on mode in Office"
				
				#print "Manual Value is " + str(self.ui.horizontalSlider_8.value()) + " with on mode in Office"
	
	# Function for radioButton_45 with radioButton_43 "Off Mode Manual Intensity"
	def set35(self,b,c):
		if b.isChecked() == True:
			if c.isChecked() == True:
				#print "Manual Value is " + str(self.ui.horizontalSlider_8.value()) + " with off mode in Office"
				ser.write('OFCLOff')
	""" End of Office Functions """	
	
	"""	Room 1 Fucntions """
	
	# Function for radioButton with radioButton1 "Auto Mode Auto Intensity"
	def set(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "Auto Mode Auto Intensity"
				ser.write('R1LAA')
	# Function for radioButton with radioButton_2 "On Mode Auto Intensity"
	def set2(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "on Mode Auto Intensity"
				ser.write('R1LAOn')
	# Function for radioButton with radioButton_3 "off Mode Auto Intensity"
	def set3(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "off Mode Auto Intensity"
				ser.write('R1LOff')
	
	# Function for radioButton_5 with radioButton1 "Auto Mode Full Intensity"
	def set4(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "Auto Mode Full Intensity"
				ser.write('R1LFA')
	
	# Function for radioButton_5 with radioButton_2 "on Mode Full Intensity"
	def set5(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "on Mode Full Intensity"
				ser.write('R1LOn')
	# Function for radioButton_5 with radioButton_3 "Off Mode Full Intensity"
	def set6(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "Off Mode Full Intensity"
				ser.write('R1LOff')
	
				
	# Function for Radio Button4 'Intensity Manual'
	def btnstate1(self,b):
	    if b.isChecked() == True:
			self.ui.horizontalSlider.setEnabled(True)
			return True
	
	def btnstate2(self,b):
	    if b.isChecked() == False:
			self.ui.horizontalSlider.setEnabled(False)
	
	# Function For "Security Alarm" Action
	def toggleLED(self,b):
	    if b.pressed:
			#print "Security-alarm_off"
			ser.write('R1ALOff')
			self.ui.pushButton.setEnabled(False)
			self.ui.labe_6.setText('')
			self.ui.labe_6.setStyleSheet('QLabel {background-color: white; color: black;}')
			
	# Function for radioButton_4 with radioButton1 "Auto Mode Manual Intensity"
	def set7(self,b,c):
		if b.isChecked() == True:
			if c.isChecked() == True:
				ser.write('R1LMA')
				time.sleep(0.02)
				if self.ui.horizontalSlider.value() == 0:
					time.sleep(0.02)
					ser.write('R01mlc000')
					#print "Manual Value is 0 with auto mode"
				elif self.ui.horizontalSlider.value() == 1:
					time.sleep(0.02)
					ser.write('R01mlc025')
					#print "Manual Value is 1 with auto mode"
				elif self.ui.horizontalSlider.value() == 2:
					time.sleep(0.02)
					ser.write('R01mlc050')
					#print "Manual Value is 2 with auto mode"
				elif self.ui.horizontalSlider.value() == 3:
					time.sleep(0.02)
					ser.write('R01mlc075')
					#print "Manual Value is 3 with auto mode"
				elif self.ui.horizontalSlider.value() == 4:
					time.sleep(0.02)
					ser.write('R01mlc100')
					#print "Manual Value is 4 with auto mode"
				elif self.ui.horizontalSlider.value() == 5:
					time.sleep(0.02)
					ser.write('R01mlc125')
					#print "Manual Value is 5 with auto mode"
				elif self.ui.horizontalSlider.value() == 6:
					time.sleep(0.02)
					ser.write('R01mlc150')
					#print "Manual Value is 6 with auto mode"
				elif self.ui.horizontalSlider.value() == 7:
					time.sleep(0.02)
					ser.write('R01mlc175')
					#print "Manual Value is 7 with auto mode"
				elif self.ui.horizontalSlider.value() == 8:
					time.sleep(0.02)
					ser.write('R01mlc200')
					#print "Manual Value is 8 with auto mode"
				elif self.ui.horizontalSlider.value() == 9:
					time.sleep(0.02)
					ser.write('R01mlc225')
					#print "Manual Value is 9 with auto mode"
				elif self.ui.horizontalSlider.value() == 10:
					time.sleep(0.02)
					ser.write('R01mlc255')
					#print "Manual Value is 10 with auto mode"
				
				#print "Manual Value is " + str(self.ui.horizontalSlider.value()) + " with auto mode"
				
	# Function for radioButton_4 with radioButton_2 "On Mode Manual Intensity"
	def set8(self,b,c):
		if b.isChecked() == True:
			if c.isChecked() == True:
				ser.write('R1LMOn')
				time.sleep(0.02)
				if self.ui.horizontalSlider.value() == 0:
					time.sleep(0.02)
					ser.write('R01mlc000')
					#print "Manual Value is 0 with on mode"
				elif self.ui.horizontalSlider.value() == 1:
					time.sleep(0.02)
					ser.write('R01mlc025')
					#print "Manual Value is 1 with on mode"
				elif self.ui.horizontalSlider.value() == 2:
					time.sleep(0.02)
					ser.write('R01mlc050')
					#print "Manual Value is 2 with on mode"
				elif self.ui.horizontalSlider.value() == 3:
					time.sleep(0.02)
					ser.write('R01mlc075')
					#print "Manual Value is 3 with on mode"
				elif self.ui.horizontalSlider.value() == 4:
					time.sleep(0.02)
					ser.write('R01mlc100')
					#print "Manual Value is 4 with on mode"
				elif self.ui.horizontalSlider.value() == 5:
					time.sleep(0.02)
					ser.write('R01mlc125')
					#print "Manual Value is 5 with on mode"
				elif self.ui.horizontalSlider.value() == 6:
					time.sleep(0.02)
					ser.write('R01mlc150')
					#print "Manual Value is 6 with on mode"
				elif self.ui.horizontalSlider.value() == 7:
					time.sleep(0.02)
					ser.write('R01mlc175')
					#print "Manual Value is 7 with on mode"
				elif self.ui.horizontalSlider.value() == 8:
					time.sleep(0.02)
					ser.write('R01mlc200')
					#print "Manual Value is 8 with on mode"
				elif self.ui.horizontalSlider.value() == 9:
					time.sleep(0.02)
					ser.write('R01mlc225')
					#print "Manual Value is 9 with on mode"
				elif self.ui.horizontalSlider.value() == 10:
					time.sleep(0.02)
					ser.write('R01mlc255')
					#print "Manual Value is 10 with on mode"
				
				#print "Manual Value is " + str(self.ui.horizontalSlider.value()) + " with on mode"
	# Function for radioButton_4 with radioButton_3 "Off Mode Manual Intensity"
	def set9(self,b,c):
		if b.isChecked() == True:
			if c.isChecked() == True:
				#print "Manual Value is " + str(self.ui.horizontalSlider.value()) + " with off mode"
				ser.write('R1LOff')
	
	# Function for radioButton1_2 {Temperature on}
	def set10(self,b):
		if b.isChecked() == True:
			self.ui.pushButton_6.setEnabled(True)
			self.ui.pushButton_2.setEnabled(True)
			self.ui.pushButton_7.setEnabled(True)
			self.ui.pushButton_8.setEnabled(True)
			self.ui.pushButton_9.setEnabled(True)
			self.ui.labe_3.setStyleSheet('QLabel {background-color: red; color: white;}')
			self.ui.labe_11.setStyleSheet('QLabel {background-color: red; color: white;}')
			self.ui.labe_10.setStyleSheet('QLabel {background-color: red; color: white;}')
			self.ui.labe_12.setStyleSheet('QLabel {background-color: red; color: white;}')
			self.ui.labe_3.setText('24')
			self.ui.labe_11.setText('1')
			self.ui.labe_10.setText('Fan')
			self.ui.labe_12.setText('Off')
			ser.write('ACReset')
			time.sleep(0.02)
			ser.write('ACPowerOn')
			time.sleep(0.02)
			#print "Temperature is on"
			
	# Function for radioButton_10 {Temperature off} Action Function
	def set11(self,b):
		if b.isChecked() == True:
			self.ui.pushButton_6.setEnabled(False)
			self.ui.pushButton_2.setEnabled(False)
			self.ui.pushButton_7.setEnabled(False)
			self.ui.pushButton_8.setEnabled(False)
			self.ui.pushButton_9.setEnabled(False)
			ser.write('ACPowerOff')
			time.sleep(0.02)
			#print "Temperature is off"
	
	# Function for pushButton_7 {Temperature Up} Action
	def set77(self,b):
		temp = int(self.ui.labe_3.text())
		if b.pressed:
			temp = temp + 1
			if temp > 30:
				temp = 30
			time.sleep(0.02)
			self.ui.labe_3.setStyleSheet('QLabel {background-color: red; color: white;}')
			self.ui.labe_3.setText(str(temp))
			ser.write('ACTempUp')
			time.sleep(0.02)
	
	# Function for pushButton_8 {Temperature Down} Action
	def set78(self,b):
		temp = int(self.ui.labe_3.text())
		if b.pressed:
			temp = temp - 1
			if temp < 16:
				temp = 16
			time.sleep(0.02)
			self.ui.labe_3.setStyleSheet('QLabel {background-color: red; color: white;}')
			self.ui.labe_3.setText(str(temp))
			ser.write('ACTempDown')
			time.sleep(0.02)
			
	# Function for pushButton_6 {Fan Speed } Action
	def set79(self,b):
		if self.ui.labe_11.text() == '1' and b.pressed:
			self.ui.labe_11.setText('2')
			ser.write('ACFan')
			time.sleep(0.02)
		elif self.ui.labe_11.text() == '2' and b.pressed:
			self.ui.labe_11.setText('3')
			ser.write('ACFan')
			time.sleep(0.02)
		elif self.ui.labe_11.text() == '3' and b.pressed:
			self.ui.labe_11.setText('Auto')
			ser.write('ACFan')
			time.sleep(0.02)
		elif self.ui.labe_11.text() == 'Auto' and b.pressed:
			self.ui.labe_11.setText('1')
			ser.write('ACFan')
			time.sleep(0.02)
	
	# Function for pushButton_9 {Swing} Action
	def set13(self,b):
		if self.ui.labe_12.text() == 'Off' and b.pressed:
			self.ui.labe_12.setText('On')
			ser.write('ACSwing')
			time.sleep(0.02)
		elif self.ui.labe_12.text() == 'On' and b.pressed:
			self.ui.labe_12.setText('Off')
			ser.write('ACSwing')
			time.sleep(0.02)

	# Function for pushButton_2 {Mode} Action
	def set80(self,b):
		if self.ui.labe_10.text() == 'Fan' and b.pressed:
			self.ui.labe_10.setText('Cool')
			ser.write('ACMode')
			time.sleep(0.02)
		elif self.ui.labe_10.text() == 'Cool' and b.pressed:
			self.ui.labe_10.setText('Heat')
			ser.write('ACMode')
			time.sleep(0.02)
		elif self.ui.labe_10.text() == 'Heat' and b.pressed:
			self.ui.labe_10.setText('Dry')
			ser.write('ACMode')
			time.sleep(0.02)
		elif self.ui.labe_10.text() == 'Dry' and b.pressed:
			self.ui.labe_10.setText('Fan')
			ser.write('ACMode')
			time.sleep(0.02)
			
	""" End of Room 1 Fucntios """
	
	"""	Room 2 Fucntions """
	
	# Function for radioButton_21 'Intensity Manual'
	def btnstate22(self,b):
	    if b.isChecked() == True:
			self.ui.horizontalSlider_4.setEnabled(True)
			return True
	
	def btnstate23(self,b):
	    if b.isChecked() == False:
			self.ui.horizontalSlider_4.setEnabled(False)
	
	# Function for radioButton_20 with radioButton_18 "On Mode Auto Intensity"
	def set37(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "on Mode Auto Intensity in Room 2"
				ser.write('R2LAOn')
				
	# Function for radioButton_20 with radioButton_19 "off Mode Auto Intensity"
	def set38(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "off Mode Auto Intensity in Room 2"
				ser.write('R2LOff')
	
	# Function for radioButton_22 with radioButton_18 "on Mode Full Intensity"
	def set39(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "on Mode Full Intensity in Room 2"
				ser.write('R2LOn')
				
	# Function for radioButton_22 with radioButton_19 "Off Mode Full Intensity"
	def set40(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "Off Mode Full Intensity in Room 2"
				ser.write('R2LOff')
	
	# Function for radioButton_21 with radioButton_18 "On Mode Manual Intensity"
	def set41(self,b,c):
		if b.isChecked() == True:
			if c.isChecked() == True:
				ser.write('R2LMOn')
				time.sleep(0.02)
				if self.ui.horizontalSlider_4.value() == 0:
					time.sleep(0.02)
					ser.write('R02mlc000')
					#print "Manual Value is 0 with on mode in Room 2"
				elif self.ui.horizontalSlider_4.value() == 1:
					time.sleep(0.02)
					ser.write('R02mlc025')
					#print "Manual Value is 1 with on mode in Room 2"
				elif self.ui.horizontalSlider_4.value() == 2:
					time.sleep(0.02)
					ser.write('R02mlc050')
					#print "Manual Value is 2 with on mode in Room 2"
				elif self.ui.horizontalSlider_4.value() == 3:
					time.sleep(0.02)
					ser.write('R02mlc075')
					#print "Manual Value is 3 with on mode in Room 2"
				elif self.ui.horizontalSlider_4.value() == 4:
					time.sleep(0.02)
					ser.write('R02mlc100')
					#print "Manual Value is 4 with on mode in Room 2"
				elif self.ui.horizontalSlider_4.value() == 5:
					time.sleep(0.02)
					ser.write('R02mlc125')
					#print "Manual Value is 5 with on mode in Room 2"
				elif self.ui.horizontalSlider_4.value() == 6:
					time.sleep(0.02)
					ser.write('R02mlc150')
					#print "Manual Value is 6 with on mode in Room 2"
				elif self.ui.horizontalSlider_4.value() == 7:
					time.sleep(0.02)
					ser.write('R02mlc175')
					#print "Manual Value is 7 with on mode in Room 2"
				elif self.ui.horizontalSlider_4.value() == 8:
					time.sleep(0.02)
					ser.write('R02mlc200')
					#print "Manual Value is 8 with on mode in Room 2"
				elif self.ui.horizontalSlider_4.value() == 9:
					time.sleep(0.02)
					ser.write('R02mlc225')
					#print "Manual Value is 9 with on mode in Room 2"
				elif self.ui.horizontalSlider_4.value() == 10:
					time.sleep(0.02)
					ser.write('R02mlc255')
					#print "Manual Value is 10 with on mode in Room 2"
				
				#print "Manual Value is " + str(self.ui.horizontalSlider_4.value()) + " with on mode in Room 2"
	
	# Function for radioButton_21 with radioButton_19 "Off Mode Manual Intensity"
	def set42(self,b,c):
		if b.isChecked() == True:
			if c.isChecked() == True:
				#print "Manual Value is " + str(self.ui.horizontalSlider_4.value()) + " with off mode in Room 2"
				ser.write('R2LOff')
	
	# radioButton1_3 {Certain Mode open} Action
	def set43(self,b):
		if b.isChecked() == True:
			#print "Certain Mode is open"
			ser.write('R2CRCL')
				
	# radioButton_23 {Certain Mode close} Action
	def set44(self,b):
		if b.isChecked() == True:
			#print "Certain Mode is closed"
			ser.write('R2CROP')
				
	# radioButton_24 {Certain Mode smart} Action
	def set45(self,b):
		if b.isChecked() == True:
			#print "Certain Mode is smart"
			ser.write('R2CRSmart')
	
	""" End of Room 2 Functions """	
	
	"""	Room 3 Fucntions """
	
	# Function For "Fire-Secure" Action and enable Emergency-Off
	def toggleLED3(self,b):
	    if b.pressed:
			self.ui.pushButton_4.setEnabled(True)
			#print "Fire_secure"
			ser.write('FireSecure')
			self.ui.labe_22.setText('')
			self.ui.labe_22.setStyleSheet('QLabel {background-color: white; color: black;}')
			
	# Function for "Emergency-Off" action
	def toggleLED4(self,b):
	    if b.pressed:
			#print "Emergency_off"
			ser.write('EmergencyOff')
			self.ui.pushButton_3.setEnabled(False)
			self.ui.pushButton_4.setEnabled(False)
			
	# Function for radioButton_76 'Intensity Manual'
	def btnstate25(self,b):
	    if b.isChecked() == True:
			self.ui.horizontalSlider_13.setEnabled(True)
			return True
	
	def btnstate26(self,b):
	    if b.isChecked() == False:
			self.ui.horizontalSlider_13.setEnabled(False)
	
	# Function for radioButton_75 with radioButton_73 "On Mode Auto Intensity"
	def set47(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "on Mode Auto Intensity in Room 3"
				ser.write('R3LAOn')
				
	# Function for radioButton_75 with radioButton_74 "off Mode Auto Intensity"
	def set48(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "off Mode Auto Intensity in Room 3"
				ser.write('R3LOff')
	
	# Function for radioButton_77 with radioButton_73 "on Mode Full Intensity"
	def set49(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "on Mode Full Intensity in Room 3"
				ser.write('R3LOn')
				
	# Function for radioButton_77 with radioButton_74 "Off Mode Full Intensity"
	def set50(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "Off Mode Full Intensity in Room 3"
				ser.write('R3LOff')
	
	# Function for radioButton_76 with radioButton_73 "On Mode Manual Intensity"
	def set51(self,b,c):
		if b.isChecked() == True:
			if c.isChecked() == True:
				ser.write('R3LMOn')
				time.sleep(0.02)
				if self.ui.horizontalSlider_13.value() == 0:
					time.sleep(0.02)
					ser.write('R03mlc000')
					#print "Manual Value is 0 with on mode in Room 3"
				elif self.ui.horizontalSlider_13.value() == 1:
					time.sleep(0.02)
					ser.write('R03mlc025')
					#print "Manual Value is 1 with on mode in Room 3"
				elif self.ui.horizontalSlider_13.value() == 2:
					time.sleep(0.02)
					ser.write('R03mlc050')
					#print "Manual Value is 2 with on mode in Room 3"
				elif self.ui.horizontalSlider_13.value() == 3:
					time.sleep(0.02)
					ser.write('R03mlc075')
					#print "Manual Value is 3 with on mode in Room 3"
				elif self.ui.horizontalSlider_13.value() == 4:
					time.sleep(0.02)
					ser.write('R03mlc100')
					#print "Manual Value is 4 with on mode in Room 3"
				elif self.ui.horizontalSlider_13.value() == 5:
					time.sleep(0.02)
					ser.write('R03mlc125')
					#print "Manual Value is 5 with on mode in Room 3"
				elif self.ui.horizontalSlider_13.value() == 6:
					time.sleep(0.02)
					ser.write('R03mlc150')
					#print "Manual Value is 6 with on mode in Room 3"
				elif self.ui.horizontalSlider_13.value() == 7:
					time.sleep(0.02)
					ser.write('R03mlc175')
					#print "Manual Value is 7 with on mode in Room 3"
				elif self.ui.horizontalSlider_13.value() == 8:
					time.sleep(0.02)
					ser.write('R03mlc200')
					#print "Manual Value is 8 with on mode in Room 3"
				elif self.ui.horizontalSlider_13.value() == 9:
					time.sleep(0.02)
					ser.write('R03mlc225')
					#print "Manual Value is 9 with on mode in Room 3"
				elif self.ui.horizontalSlider_13.value() == 10:
					time.sleep(0.02)
					ser.write('R03mlc255')
					#print "Manual Value is 10 with on mode in Room 3"
				
				#print "Manual Value is " + str(self.ui.horizontalSlider_13.value()) + " with on mode in Room 3"
	
	# Function for radioButton_76 with radioButton_74 "Off Mode Manual Intensity"
	def set52(self,b,c):
		if b.isChecked() == True:
			if c.isChecked() == True:
				#print "Manual Value is " + str(self.ui.horizontalSlider_13.value()) + " with off mode in Room 3"
				ser.write('R3LOff')
	
	# radioButton1_7 {Certain Mode open} Action
	def set53(self,b):
		if b.isChecked() == True:
			#print "Certain Mode is open"
			ser.write('R3CROP')
				
	# radioButton_78 {Certain Mode close} Action
	def set54(self,b):
		if b.isChecked() == True:
			#print "Certain Mode is closed"
			ser.write('R3CRCL')
				
	# Function for radioButton_80 "Window on"
	def btnstate27(self,b):
	    if b.isChecked() == True:
			#print "Window On"
			ser.write('R3WOpen')
			
	# Function for radioButton_81 "Window off"
	def btnstate28(self,b):
	    if b.isChecked() == True:
			#print "Window Off"
			ser.write('R3WClose')
	
	""" End of Room 3 Functions """	
	
	"""	Master Bedroom  Fucntions """
	
	# Function for radioButton_85 'Intensity Manual'
	def btnstate30(self,b):
	    if b.isChecked() == True:
			self.ui.horizontalSlider_14.setEnabled(True)
			return True
	
	def btnstate31(self,b):
	    if b.isChecked() == False:
			self.ui.horizontalSlider_14.setEnabled(False)
	
	# Function for radioButton_84 with radioButton_82 "On Mode Auto Intensity"
	def set57(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "on Mode Auto Intensity in Master Bedroom"
				ser.write('MRLAOn')
				
	# Function for radioButton_84 with radioButton_83 "off Mode Auto Intensity"
	def set58(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "off Mode Auto Intensity in Master Bedroom"
				ser.write('MRLOff')
	
	# Function for radioButton_86 with radioButton_82 "on Mode Full Intensity"
	def set59(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "on Mode Full Intensity in Master Bedroom"
				ser.write('MRLOn')
				
	# Function for radioButton_86 with radioButton_83 "Off Mode Full Intensity"
	def set60(self,b,c):
	    if b.isChecked() == True:
			if c.isChecked() == True:
				#print "Off Mode Full Intensity in Master Bedroom"
				ser.write('MRLOff')
	
	# Function for radioButton_85 with radioButton_82 "On Mode Manual Intensity"
	def set61(self,b,c):
		if b.isChecked() == True:
			if c.isChecked() == True:
				ser.write('MRLMOn')
				time.sleep(0.02)
				if self.ui.horizontalSlider_14.value() == 0:
					time.sleep(0.02)
					ser.write('MR0mlc000')
					#print "Manual Value is 0 with on mode in Master Bedroom"
				elif self.ui.horizontalSlider_14.value() == 1:
					time.sleep(0.02)
					ser.write('MR0mlc025')
					#print "Manual Value is 1 with on mode in Master Bedroom"
				elif self.ui.horizontalSlider_14.value() == 2:
					time.sleep(0.02)
					ser.write('MR0mlc050')
					#print "Manual Value is 2 with on mode in Master Bedroom"
				elif self.ui.horizontalSlider_14.value() == 3:
					time.sleep(0.02)
					ser.write('MR0mlc075')
					#print "Manual Value is 3 with on mode in Master Bedroom"
				elif self.ui.horizontalSlider_14.value() == 4:
					time.sleep(0.02)
					ser.write('MR0mlc100')
					#print "Manual Value is 4 with on mode in Master Bedroom"
				elif self.ui.horizontalSlider_14.value() == 5:
					time.sleep(0.02)
					ser.write('MR0mlc125')
					#print "Manual Value is 5 with on mode in Master Bedroom"
				elif self.ui.horizontalSlider_14.value() == 6:
					time.sleep(0.02)
					ser.write('MR0mlc150')
					#print "Manual Value is 6 with on mode in Master Bedroom"
				elif self.ui.horizontalSlider_14.value() == 7:
					time.sleep(0.02)
					ser.write('MR0mlc175')
					#print "Manual Value is 7 with on mode in Master Bedroom"
				elif self.ui.horizontalSlider_14.value() == 8:
					time.sleep(0.02)
					ser.write('MR0mlc200')
					#print "Manual Value is 8 with on mode in Master Bedroom"
				elif self.ui.horizontalSlider_14.value() == 9:
					time.sleep(0.02)
					ser.write('MR0mlc225')
					#print "Manual Value is 9 with on mode in Master Bedroom"
				elif self.ui.horizontalSlider_14.value() == 10:
					time.sleep(0.02)
					ser.write('MR0mlc255')
					#print "Manual Value is 10 with on mode in Master Bedroom"
				
				#print "Manual Value is " + str(self.ui.horizontalSlider_14.value()) + " with on mode in Master Bedroom"
	
	# Function for radioButton_85 with radioButton_83 "Off Mode Manual Intensity"
	def set62(self,b,c):
		if b.isChecked() == True:
			if c.isChecked() == True:
				#print "Manual Value is " + str(self.ui.horizontalSlider_14.value()) + " with off mode in Master Bedroom"
				ser.write('MRLOff')
				
	""" End of Master Bedroom Functions """	
	
	"""	Kitchen  Fucntions """
	
	# Function For "Gas-Secure"
	def toggleLED6(self,b):
	    if b.pressed:
			#print "Gas-Secure"
			ser.write('GasSecure')
			self.ui.pushButton_5.setEnabled(False)
			self.ui.labe_25.setText('')
			self.ui.labe_25.setStyleSheet('QLabel {background-color: white; color: black;}')
	
	# Function for radioButton_87 "Light on"
	def btnstate33(self,b):
	    if b.isChecked() == True:
			#print "Light On"
			ser.write('KtnLOn')
			
	# Function for radioButton_88 "Light off"
	def btnstate34(self,b):
	    if b.isChecked() == True:
			#print "Light Off"
			ser.write('KtnLOff')
			
	""" End of Kitchen Functions """	
	
	"""	Garage  Fucntions """
	
	# Function for radioButton_89 "Door open"
	def btnstate36(self,b):
	    if b.isChecked() == True:
			#print "Door Open"
			ser.write('OpenGarage')
			
	# Function for radioButton_90 "Door close"
	def btnstate37(self,b):
	    if b.isChecked() == True:
			#print "Door Closed"
			ser.write('CloseGarage')
			
	# Function for radioButton_95 "Door stop"		
	def btnstate48(self,b):
	    if b.isChecked() == True:
			#print "Door stoped"
			ser.write('StopGarage')
			
	""" End of Garage Functions """	
	
	"""	Outside&Garden  Fucntions """
	
	# Function for radioButton_91 "Outside Light on"
	def btnstate38(self,b):
	    if b.isChecked() == True:
			#print "Outside Light On"
			ser.write('OUTLOn')
			
	# Function for radioButton_92 "Outside Light off"
	def btnstate39(self,b):
	    if b.isChecked() == True:
			#print "Outside Light Off"
			ser.write('OUTLOff')
			
	# Function for radioButton_91 "Garden Light on"
	def btnstate45(self,b):
	    if b.isChecked() == True:
			#print "Garden Light On"
			ser.write('Garden On')
			
	# Function for radioButton_94 "Garden Light off"
	def btnstate46(self,b):
	    if b.isChecked() == True:
			#print "Garden Light Off"
			ser.write('Garden Off')
			
	""" End of Outside&Garden Functions """	
	
	""" Security Functions """
	
	# Fucntion for security level 1 action
	def btnstate10(self,b):
	    if b.isChecked() == True:
			#print "security Level 1"
			ser.write('R1SOne')
	
	# Fucntion for security level 2 action
	def btnstate42(self,b):
	    if b.isChecked() == True:
			#print "security Level 2"
			ser.write('R1STwo')
			
	# Fucntion for security off action
	def btnstate11(self,b):
	    if b.isChecked() == True:
			#print "security off"
			ser.write('R1SOff')
			
	""" End of Security Functions """
	
	#Fucntion for Reading from Serial
	def displayTime(self):
		inp, outp, err = select.select([sys.stdin, ser], [], [], .2)

		# If the user has typed anything, send it to the Arduino:
		if sys.stdin in inp :
			line = sys.stdin.readline()
		# If the Arduino has printed anything, display it:
		if ser in inp :
			line = ser.readline().strip()
			""" Function for Security Alarm in Room 1 """
			if line == "Intrusion Alarm":
				# Change labe_6 "Alarm" Texte
				self.ui.labe_6.setText('Security Alram')
				# Change labe_6 "Alarm" backgroud color
				self.ui.labe_6.setStyleSheet('QLabel {background-color: red; color: white;}')
				self.ui.pushButton.setEnabled(True)
				
			""" Function for Fire Alarm in Room 3 """
			if line == "Fire Alarm":
				# Change labe_22 "Alarm" Texte
				self.ui.labe_22.setText('Fire Alarm')
				# Change labe_22 "Alarm" backgroud color
				self.ui.labe_22.setStyleSheet('QLabel {background-color: red; color: white;}')
				self.ui.pushButton_3.setEnabled(True)
				# Shut down Reception  Light
				time.sleep(0.3)
				self.ui.radioButton_15.setChecked(True)
				# Shut down Dining Room Light
				time.sleep(0.3)
				self.ui.radioButton_41.setChecked(True)
				# Shut down Office Light
				time.sleep(0.3)
				self.ui.radioButton_43.setChecked(True)
				# Shut down Room No.1 Light
				time.sleep(0.3)
				self.ui.radioButton_3.setChecked(True)
				# Shut down Room No.2 Light
				time.sleep(0.3)
				self.ui.radioButton_19.setChecked(True)
				# Shut down Room No.3 Light
				time.sleep(0.3)
				self.ui.radioButton_74.setChecked(True)
				# Shut down Master Bedroom Light
				time.sleep(0.3)
				self.ui.radioButton_83.setChecked(True)
				# Shut down Kitchen Light
				time.sleep(0.3)
				self.ui.radioButton_88.setChecked(True)
				
			"""Function for Gas-Leakage in Kitchen """
			if line == "GAS Leakage":
				# Change labe_25 "Alarm" Texte
				self.ui.labe_25.setText('GAS Alarm')
				# Change labe_25 "Alarm" backgroud color
				self.ui.labe_25.setStyleSheet('QLabel {background-color: red; color: white;}')
				self.ui.pushButton_5.setEnabled(True)
				
			""" Function for Temperature now is  in security """
			if line[0:4] == "Temp":
				# Change labe_13 "Temperatue now is" Texte
				self.ui.labe_13.setStyleSheet('QLabel {background-color: red; color: white;}')
				self.ui.labe_13.setText(line[4:])
				
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = smartHouse()
    MainWindow.show()
    sys.exit(app.exec_())
