from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class CircularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # CUSTOM PROPERTIES
        self.Tsuffix = '°C'
        self.Tmotor = 56
        self.Tbat = 30
        self.rpm = 0
        self.max_rpm = 6000
        self.A = 0
        self.max_A = 350
        self.SoC = 49
        self.width = 800
        self.height = 800
        self.progress_width = 100
        self.progress_rounded_cap = True
        self.progress_color = 0xAD0000
        self.font_family = "Segoe UI"
        self.font_size = 100
        self.Tfont_size = 25
        self.suffix = "%"
        self.text_color = 0xAD0000
        #BG
        self.enable_bg = True
        self.bg_color = 0x44475a
    

        # SET DEFAULT SIZE WITHOUT LAYOUT
        self.resize(self.width, self.height)
    
    # ADD DROPSHADOW
    def add_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setXOffset(0)
            self.shadow.setColor(QColor(255, 255, 255, 120))
            self.setGraphicsEffect(self.shadow)

    # SET VALUE
    def set_rpm(self, rpm):
        self.rpm = rpm
        self.repaint()# Render progress bar after change value

    # SET VALUE
    def set_A(self, A):
        self.A = A
        self.repaint()# Render progress bar after change value

    # SET VALUE
    def set_SoC(self, SoC):
        self.SoC = SoC
        self.repaint()# Render progress bar after change value

    # SET VALUE
    def set_Tmotor(self, Tmotor):
        self.Tmotor = Tmotor
        self.repaint()# Render progress bar after change value

    # SET VALUE
    def set_Tbat(self, Tbat):
        self.Tbat = Tbat
        self.repaint()# Render progress bar after change value


    # PAINT EVENT (DESIGN YOUR CIRCULAR PROGRESS HERE)
    def paintEvent(self, event):
        # SET PROGRESS PARAMETERS
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        rpm = self.rpm * 120 / self.max_rpm
        A = self.A * 120 / self.max_A

        # PAINTER
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing) # remove pixelared edges
        paint.setFont(QFont(self.font_family, self.font_size))

        # CREATE RECTANGLE
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        # PEN
        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)
        # Set Round Cap
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        # ENABLE BG
        if self.enable_bg:
            pen.setColor(QColor(self.bg_color))
            paint.setPen(pen)
            paint.drawArc(margin, margin, width, height, -120 * 16, -120 * 16)
            paint.drawArc(margin, margin, width, height, -60 * 16, 120 * 16)

        # CREATE ARC / CIRCULAR PROGRESS
        pen.setColor(QColor(self.progress_color))
        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, -120 * 16, -A * 16)
        paint.drawArc(margin, margin, width, height, -60 * 16, rpm * 16)

        # CREATE TEXT
        pen.setColor(QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect, Qt.AlignCenter, f"{self.SoC}{self.suffix}")

        # PEN
        Tpen = QPen()
        Tpen.setColor(QColor(self.text_color))
        paint.setPen(Tpen)
        paint.setFont(QFont(self.font_family, self.Tfont_size))
        paint.drawText(QPointF(450, 611), f"{self.Tmotor}{self.Tsuffix}")
        paint.drawText(QPointF(450, 661), f"{self.Tmotor}{self.Tsuffix}")


        # END
        paint.end()

    

    