import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton, QMessageBox
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
        global total, viajes_disponibles, estado, estado_siguiente
        estado_siguiente = "q0"
        estado = "q0"
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

    #Mostrar hora y fecha
    def displayTime(self):
        currentTime = QTime.currentTime()
        displayText = currentTime.toString('hh:mm:ss')
        self.reloj.setText(displayText)
        currentDate = QDateTime.currentDateTime()
        displayText = currentDate.toString('dd/mm/yyyy')
        self.fecha.setText(displayText)

    #Definicion y asignacion al insertar monedas
    def insert_coin(self):
        self.ComboBox_Monedas = QComboBox(self)
        self.ComboBox_Monedas.setStyleSheet("font: 75 12pt; color: rgb(255, 255, 255); background-color: rgb(0, 0, 0);")
        self.ComboBox_Monedas.setGeometry(550, 120, 71, 31)
        monedas = ['1','2','5','10']
        self.ComboBox_Monedas.addItems(monedas)
  
        boton_recargar = QPushButton("Insertar", self)
        boton_finalizar = QPushButton("Recargar", self)
        self.boton_recargar.clicked.connect(self.impresion)
        self.boton_finalizar.clicked.connect(self.cerrar)
          
        self.ingresado_label = QLabel(self)
        self.ingresado_label.setStyleSheet("font: 90 20pt;")
        self.ingresado_label.setGeometry(210, 160, 81, 21)
        self.ingresado_label.setText("$0")

        self.total_label = QLabel(self)
        self.total_label.setStyleSheet("font: 90 20pt;")
        self.total_label.setGeometry(210, 260, 81, 21)
        self.total_label.setText("$0")

        self.viajes_disponibles_label = QLabel(self)
        self.viajes_disponibles_label.setStyleSheet("font: 90 20pt;")
        self.viajes_disponibles_label.setGeometry(390, 310, 51, 21)
        self.viajes_disponibles_label.setText("0")

        self.estados_label = QLabel(self)
        self.estados_label.setStyleSheet("font: 90 12pt;")
        self.estados_label.setGeometry(210, 380, 335, 25)
        self.estados_label.setText(" ")
        
    def impresion(self):
        moneda = int(self.ComboBox_Monedas.currentText())
        moneda_insertada = self.ComboBox_Monedas.currentText()
        self.ingresado_label.setText("$" + moneda_insertada)
        print("Moneda insertada: $" + moneda_insertada)

        global total
        global viajes_disponibles
        global estado
        global estado_siguiente
        total = total + moneda
        viajes_disponibles = total / 10
        viajes_disponibles = int(viajes_disponibles) 
        estado = estado_siguiente

        if (estado == "q0") & (moneda_insertada == "1"):
            #estado = "q1"
            estado_siguiente = "q1" 
        elif (estado == "q0") & (moneda_insertada == "2"):
            #estado = "q2"
            estado_siguiente = "q2"
        elif (estado == "q0") & (moneda_insertada == "5"):
            #estado = "q5"
            estado_siguiente = "q5" 
        elif (estado == "q0") & (moneda_insertada == "10"):
            #estado = "q10"
            estado_siguiente = "q10" 
        elif (estado == "q1") & (moneda_insertada == "1"):
            #estado = "q2"
            estado_siguiente = "q2" 
        elif (estado == "q1") & (moneda_insertada == "2"):
            #estado = "q3"
            estado_siguiente = "q3" 
        elif (estado == "q2") & (moneda_insertada == "1"):
            #estado = "q3"
            estado_siguiente = "q3" 
        elif (estado == "q2") & (moneda_insertada == "2"):
            #estado = "q4"
            estado_siguiente = "q4"
        elif (estado == "q3") & (moneda_insertada == "1"):
            #estado = "q4"
            estado_siguiente = "q4" 
        elif (estado == "q3") & (moneda_insertada == "2"):
            #estado = "q5"
            estado_siguiente = "q5"
        elif (estado == "q3") & (moneda_insertada == "5"):
            #estado = "q8"
            estado_siguiente = "q8"
        elif (estado == "q4") & (moneda_insertada == "1"):
            #estado = "q5"
            estado_siguiente = "q5" 
        elif (estado == "q4") & (moneda_insertada == "2"):
            #estado = "q6"
            estado_siguiente = "q6" 
        elif (estado == "q5") & (moneda_insertada == "1"):
            #estado = "q6" 
            estado_siguiente = "q6"
        elif (estado == "q5") & (moneda_insertada == "2"):
            #estado = "q7" 
            estado_siguiente = "q7"
        elif (estado == "q5") & (moneda_insertada == "5"):
            #estado = "q10"
            estado_siguiente = "q10"
        elif (estado == "q6") & (moneda_insertada == "1"):
            #estado = "q7"
            estado_siguiente = "q7" 
        elif (estado == "q6") & (moneda_insertada == "2"):
            #estado = "q8"
            estado_siguiente = "q8"
        elif (estado == "q7") & (moneda_insertada == "1"):
            #estado = "q8"
            estado_siguiente = "q8"  
        elif (estado == "q7") & (moneda_insertada == "2"):
            #estado = "q9"
            estado_siguiente = "q9"
        elif (estado == "q8") & (moneda_insertada == "1"):
            #estado = "q9" 
            estado_siguiente = "q9"
        elif (estado == "q8") & (moneda_insertada == "2"):
            #estado = "q10" 
            estado_siguiente = "q10"
        elif (estado == "q9") & (moneda_insertada == "1"):
            #estado = "q10"
            estado_siguiente = "q10"
        elif (estado == "q9") & (moneda_insertada == "2"):
            #estado = "q10"
            estado_siguiente = "q1" 
        elif (estado == "q10") & (moneda_insertada == "1"):
            #estado = "q1"
            estado_siguiente = "q1"
        elif (estado == "q10") & (moneda_insertada == "2"):
            #estado = "q2"
            estado_siguiente = "q2"
        elif (estado == "q10") & (moneda_insertada == "5"):
            #estado = "q5"
            estado_siguiente = "q5"
        elif (estado == "q10") & (moneda_insertada == "10"):
            #estado = "q0"
            estado_siguiente = "q0"
        
        print("Total: $" + str(total))
        self.total_label.setText("$" + str(total))

        print("Viajes disponibles: " + str(viajes_disponibles))
        self.viajes_disponibles_label.setText(str(viajes_disponibles))

        print("Estados: " + estado + "->" + estado_siguiente)
        self.estados_label.setText("Actual: (" + estado + ") -> Siguiente: (" + estado_siguiente + ")")

    def cerrar(self):
        QMessageBox.information(self, "Recargar", "Se recargaron: $" + str(total) + " exitosamente!")
        main.close()

app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()
sys.exit(app.exec_())
