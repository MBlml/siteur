import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton
from PyQt5.QtCore import  QTimer, QTime, QDateTime, QDate
from PyQt5.uic import loadUi

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('siteur-interface.ui', self)
        self.setWindowTitle('Sistema Real | SITEUR')
        self.setFixedWidth(673)
        self.setFixedHeight(460)
        timer = QTimer(self)
        timer.timeout.connect(self.displayTime)
        timer.start(1000)
        global total
        global viajes_disponibles
        total = 0
        viajes_disponibles = 0
        self.insert_coin()

        #Imagenes de logotipos de base
        self.logo = QLabel(self)
        self.pixmap = QPixmap('logo.jpeg')
        self.logo.setPixmap(self.pixmap)
        self.logo.resize(181,121)
        self.logo.move(0,0)

        self.minimal = QLabel(self)
        self.pixmap = QPixmap('minimal.png')
        self.minimal.setPixmap(self.pixmap)
        self.minimal.resize(181,121)
        self.minimal.move(0,340)

        self.leyenda = QLabel(self)
        self.pixmap = QPixmap('leyenda.png')
        self.leyenda.setPixmap(self.pixmap)
        self.leyenda.resize(481,51)
        self.leyenda.move(190,410)

        self.insert_coin = QLabel(self)
        self.pixmap = QPixmap('insert_coin.png')
        self.insert_coin.setPixmap(self.pixmap)
        self.insert_coin.resize(41,81)
        self.insert_coin.move(500,120)

    def displayTime(self):
        currentTime = QTime.currentTime()
        displayText = currentTime.toString('hh:mm:ss')
        self.reloj.setText(displayText)
        currentDate = QDateTime.currentDateTime()
        displayText = currentDate.toString('dd/mm/yyyy')
        self.fecha.setText(displayText)

    def insert_coin(self):
        self.ComboBox_Monedas = QComboBox(self)
        self.ComboBox_Monedas.setStyleSheet("font: 75 12pt; color: rgb(255, 255, 255); background-color: rgb(0, 0, 0);")
        self.ComboBox_Monedas.setGeometry(550, 120, 71, 31)
        monedas = ['1','2','5','10']
        self.ComboBox_Monedas.addItems(monedas)
  
        boton_recargar = QPushButton("Mostrar contenido", self)
        self.boton_recargar.clicked.connect(self.impresion)
          
        self.ingresado_label = QLabel(self)
        self.ingresado_label.setStyleSheet("font: 90 20pt;")
        self.ingresado_label.setGeometry(210, 160, 81, 21)

        self.total_label = QLabel(self)
        self.total_label.setStyleSheet("font: 90 20pt;")
        self.total_label.setGeometry(210, 260, 81, 21)

        self.viajes_disponibles_label = QLabel(self)
        self.viajes_disponibles_label.setStyleSheet("font: 90 20pt;")
        self.viajes_disponibles_label.setGeometry(390, 310, 51, 21)
  
    def impresion(self):
        moneda = int(self.ComboBox_Monedas.currentText())
        moneda_insertada = self.ComboBox_Monedas.currentText()
        self.ingresado_label.setText("$" + moneda_insertada)
        print("Moneda insertada: $" + moneda_insertada)

        global total
        global viajes_disponibles
        total = total + moneda
        viajes_disponibles = total / 10
        viajes_disponibles = int(viajes_disponibles)  
        print("Total: $" + str(total))
        self.total_label.setText("$" + str(total))
        print("Viajes disponibles: " + str(viajes_disponibles))
        self.viajes_disponibles_label.setText(str(viajes_disponibles))
    
app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()
sys.exit(app.exec_())
