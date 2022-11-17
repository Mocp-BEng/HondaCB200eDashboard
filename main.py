import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# IMPORT UIS
from ui_main import Ui_MainWindow
from ui_splash_screen import Ui_SplashScreen
from circular_progress import CircularProgress

# GLOBALS 
counter_rpm = 0
counter_A = 0
counter_SoC = 0
counter_Tmotor = 0
counter_Tbat = 0

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.ui.Tbat = 88

        # REMOVE TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)

        # IMPORT CIRCULAR PROGRESS
        self.progress = CircularProgress()
        self.progress.width = 800
        self.progress.height = 800
        self.progress.value = 50
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.add_shadow(False)
        self.progress.setParent(self.ui.centralwidget)
        self.progress.show()

        # QTIMER
        self.timerrpm = QTimer()
        self.timerrpm.timeout.connect(self.updaterpm)
        self.timerrpm.start(1)

        # QTIMER
        self.timerA = QTimer()
        self.timerA.timeout.connect(self.updateA)
        self.timerA.start(25)

        # QTIMER
        self.timerSoC = QTimer()
        self.timerSoC.timeout.connect(self.updateSoC)
        self.timerSoC.start(100)

        # QTIMER
        self.timerTmotor = QTimer()
        self.timerTmotor.timeout.connect(self.updateTmotor)
        self.timerTmotor.start(100)

        # QTIMER
        self.timerTbat = QTimer()
        self.timerTbat.timeout.connect(self.updateTbat)
        self.timerTbat.start(50)

        self.show()

    # UPDATE PROGRESS BAR 
    def updaterpm(self):
        global counter_rpm
        # SET VALUE TO PROGRESS BAR
        self.progress.set_rpm(counter_rpm)
        # CLOSE SPLASH SCREEN AND OPEN MAIN APP
        if counter_rpm >= 6000:
            # STOP TIMER
            counter_rpm = 0
        # INCRESE COUNTER
        counter_rpm += 1

    # UPDATE PROGRESS BAR 
    def updateA(self):
        global counter_A
        # SET VALUE TO PROGRESS BAR
        self.progress.set_A(counter_A)
        # CLOSE SPLASH SCREEN AND OPEN MAIN APP
        if counter_A >= 350:
            # STOP TIMER
            counter_A = 0
        # INCRESE COUNTER
        counter_A += 1

    # UPDATE PROGRESS BAR 
    def updateSoC(self):
        global counter_SoC
        # SET VALUE TO PROGRESS BAR
        self.progress.set_SoC(counter_SoC)
        # CLOSE SPLASH SCREEN AND OPEN MAIN APP
        if counter_SoC >= 100:
            # STOP TIMER
            counter_SoC = 0
        # INCRESE COUNTER
        counter_SoC += 1
    
    # UPDATE PROGRESS BAR 
    def updateTmotor(self):
        global counter_Tmotor
        # SET VALUE TO PROGRESS BAR
        self.progress.set_Tmotor(counter_Tmotor)
        # CLOSE SPLASH SCREEN AND OPEN MAIN APP
        if counter_Tmotor >= 100:
            # STOP TIMER
            counter_Tmotor = 0
        # INCRESE COUNTER
        counter_Tmotor += 1
    
    # UPDATE PROGRESS BAR 
    def updateTbat(self):
        global counter_Tbat
        # SET VALUE TO PROGRESS BAR
        self.progress.set_Tbat(counter_Tbat)
        # CLOSE SPLASH SCREEN AND OPEN MAIN APP
        if counter_Tbat >= 100:
            # STOP TIMER
            counter_Tbat = 0
        # INCRESE COUNTER
        counter_Tbat += 1

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec())
