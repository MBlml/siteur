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

        #Estado q0
        if (estado == "q0") & (moneda_insertada == "1"):
            estado_siguiente = "q1" 
        elif (estado == "q0") & (moneda_insertada == "2"):
            estado_siguiente = "q2"
        elif (estado == "q0") & (moneda_insertada == "5"):
            estado_siguiente = "q3"
        elif (estado == "q0") & (moneda_insertada == "10"):
            estado_siguiente = "q4"
        #Estado q1
        if (estado == "q1") & (moneda_insertada == "1"):
            estado_siguiente = "q5" 
        elif (estado == "q1") & (moneda_insertada == "2"):
            estado_siguiente = "q7"
        elif (estado == "q1") & (moneda_insertada == "5"):
            estado_siguiente = "q22"
        elif (estado == "q1") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q2
        if (estado == "q2") & (moneda_insertada == "1"):
            estado_siguiente = "q7" 
        elif (estado == "q2") & (moneda_insertada == "2"):
            estado_siguiente = "q6"
        elif (estado == "q2") & (moneda_insertada == "5"):
            estado_siguiente = "q18"
        elif (estado == "q2") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q3
        if (estado == "q3") & (moneda_insertada == "1"):
            estado_siguiente = "q19" 
        elif (estado == "q3") & (moneda_insertada == "2"):
            estado_siguiente = "q18"
        elif (estado == "q3") & (moneda_insertada == "5"):
            estado_siguiente = "λ"
        elif (estado == "q3") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q4
        if (estado == "q4") & (moneda_insertada == "1"):
            estado_siguiente = "λ (q4 = Terminal, regreso a q0)" 
        elif (estado == "q4") & (moneda_insertada == "2"):
            estado_siguiente = "λ (q4 = Terminal, regreso a q0)" 
        elif (estado == "q4") & (moneda_insertada == "5"):
            estado_siguiente = "λ (q4 = Terminal, regreso a q0)" 
        elif (estado == "q4") & (moneda_insertada == "10"):
            estado_siguiente = "λ (q4 = Terminal, regreso a q0)" 
        #Estado q5
        if (estado == "q5") & (moneda_insertada == "1"):
            estado_siguiente = "q7" 
        elif (estado == "q5") & (moneda_insertada == "2"):
            estado_siguiente = "q9"
        elif (estado == "q5") & (moneda_insertada == "5"):
            estado_siguiente = "q23"
        elif (estado == "q5") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q6
        if (estado == "q6") & (moneda_insertada == "1"):
            estado_siguiente = "q11" 
        elif (estado == "q6") & (moneda_insertada == "2"):
            estado_siguiente = "q8"
        elif (estado == "q6") & (moneda_insertada == "5"):
            estado_siguiente = "q21"
        elif (estado == "q6") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q7
        if (estado == "q7") & (moneda_insertada == "1"):
            estado_siguiente = "q9" 
        elif (estado == "q7") & (moneda_insertada == "2"):
            estado_siguiente = "q11"
        elif (estado == "q7") & (moneda_insertada == "5"):
            estado_siguiente = "q24"
        elif (estado == "q7") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q8
        if (estado == "q8") & (moneda_insertada == "1"):
            estado_siguiente = "q14" 
        elif (estado == "q8") & (moneda_insertada == "2"):
            estado_siguiente = "q10"
        elif (estado == "q8") & (moneda_insertada == "5"):
            estado_siguiente = "λ"
        elif (estado == "q8") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q9
        if (estado == "q9") & (moneda_insertada == "1"):
            estado_siguiente = "q11" 
        elif (estado == "q9") & (moneda_insertada == "2"):
            estado_siguiente = "q13"
        elif (estado == "q9") & (moneda_insertada == "5"):
            estado_siguiente = "q25"
        elif (estado == "q9") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q10
        if (estado == "q10") & (moneda_insertada == "1"):
            estado_siguiente = "q16" 
        elif (estado == "q10") & (moneda_insertada == "2"):
            estado_siguiente = "q12"
        elif (estado == "q10") & (moneda_insertada == "5"):
            estado_siguiente = "λ"
        elif (estado == "q10") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q11
        if (estado == "q11") & (moneda_insertada == "1"):
            estado_siguiente = "q13" 
        elif (estado == "q11") & (moneda_insertada == "2"):
            estado_siguiente = "q14"
        elif (estado == "q11") & (moneda_insertada == "5"):
            estado_siguiente = "q25"
        elif (estado == "q11") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q12
        if (estado == "q12") & (moneda_insertada == "1"):
            estado_siguiente = "λ (q12 = Terminal, regreso a q0)" 
        elif (estado == "q12") & (moneda_insertada == "2"):
            estado_siguiente = "λ (q12 = Terminal, regreso a q0)" 
        elif (estado == "q12") & (moneda_insertada == "5"):
            estado_siguiente = "λ (q12 = Terminal, regreso a q0)" 
        elif (estado == "q12") & (moneda_insertada == "10"):
            estado_siguiente = "λ (q12 = Terminal, regreso a q0)"
        #Estado q13
        if (estado == "q13") & (moneda_insertada == "1"):
            estado_siguiente = "q14" 
        elif (estado == "q13") & (moneda_insertada == "2"):
            estado_siguiente = "q15"
        elif (estado == "q13") & (moneda_insertada == "5"):
            estado_siguiente = "λ"
        elif (estado == "q13") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q14
        if (estado == "q14") & (moneda_insertada == "1"):
            estado_siguiente = "q14" 
        elif (estado == "q14") & (moneda_insertada == "2"):
            estado_siguiente = "q16"
        elif (estado == "q14") & (moneda_insertada == "5"):
            estado_siguiente = "λ"
        elif (estado == "q14") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q15
        if (estado == "q15") & (moneda_insertada == "1"):
            estado_siguiente = "q16" 
        elif (estado == "q15") & (moneda_insertada == "2"):
            estado_siguiente = "q17"
        elif (estado == "q15") & (moneda_insertada == "5"):
            estado_siguiente = "λ"
        elif (estado == "q15") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q16
        if (estado == "q16") & (moneda_insertada == "1"):
            estado_siguiente = "q17" 
        elif (estado == "q16") & (moneda_insertada == "2"):
            estado_siguiente = "λ"
        elif (estado == "q16") & (moneda_insertada == "5"):
            estado_siguiente = "λ"
        elif (estado == "q16") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q17
        if (estado == "q17") & (moneda_insertada == "1"):
            estado_siguiente = "λ (q17 = Terminal, regreso a q0)" 
        elif (estado == "q17") & (moneda_insertada == "2"):
            estado_siguiente = "λ (q17 = Terminal, regreso a q0)" 
        elif (estado == "q17") & (moneda_insertada == "5"):
            estado_siguiente = "λ (q17 = Terminal, regreso a q0)" 
        elif (estado == "q17") & (moneda_insertada == "10"):
            estado_siguiente = "λ (q17 = Terminal, regreso a q0)"
        #Estado q18
        if (estado == "q18") & (moneda_insertada == "1"):
            estado_siguiente = "q20" 
        elif (estado == "q18") & (moneda_insertada == "2"):
            estado_siguiente = "q21"
        elif (estado == "q18") & (moneda_insertada == "5"):
            estado_siguiente = "λ"
        elif (estado == "q18") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q19
        if (estado == "q19") & (moneda_insertada == "1"):
            estado_siguiente = "λ" 
        elif (estado == "q19") & (moneda_insertada == "2"):
            estado_siguiente = "q20"
        elif (estado == "q19") & (moneda_insertada == "5"):
            estado_siguiente = "λ"
        elif (estado == "q19") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q20
        if (estado == "q20") & (moneda_insertada == "1"):
            estado_siguiente = "λ" 
        elif (estado == "q20") & (moneda_insertada == "2"):
            estado_siguiente = "q12"
        elif (estado == "q20") & (moneda_insertada == "5"):
            estado_siguiente = "λ"
        elif (estado == "q20") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q21
        if (estado == "q21") & (moneda_insertada == "1"):
            estado_siguiente = "q12" 
        elif (estado == "q21") & (moneda_insertada == "2"):
            estado_siguiente = "λ"
        elif (estado == "q21") & (moneda_insertada == "5"):
            estado_siguiente = "λ"
        elif (estado == "q21") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q22
        if (estado == "q22") & (moneda_insertada == "1"):
            estado_siguiente = "q23" 
        elif (estado == "q22") & (moneda_insertada == "2"):
            estado_siguiente = "q24"
        elif (estado == "q22") & (moneda_insertada == "5"):
            estado_siguiente = "λ"
        elif (estado == "q22") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q23
        if (estado == "q23") & (moneda_insertada == "1"):
            estado_siguiente = "q24" 
        elif (estado == "q23") & (moneda_insertada == "2"):
            estado_siguiente = "q25"
        elif (estado == "q23") & (moneda_insertada == "5"):
            estado_siguiente = "λ"
        elif (estado == "q23") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q24
        if (estado == "q24") & (moneda_insertada == "1"):
            estado_siguiente = "q25" 
        elif (estado == "q24") & (moneda_insertada == "2"):
            estado_siguiente = "q26"
        elif (estado == "q24") & (moneda_insertada == "5"):
            estado_siguiente = "λ"
        elif (estado == "q24") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q25
        if (estado == "q25") & (moneda_insertada == "1"):
            estado_siguiente = "q26" 
        elif (estado == "q25") & (moneda_insertada == "2"):
            estado_siguiente = "λ"
        elif (estado == "q25") & (moneda_insertada == "5"):
            estado_siguiente = "λ"
        elif (estado == "q25") & (moneda_insertada == "10"):
            estado_siguiente = "λ"
        #Estado q26
        if (estado == "q26") & (moneda_insertada == "1"):
            estado_siguiente = "λ (q26 = Terminal, regreso a q0)"
            estado_siguiente =  "q0"
        elif (estado == "q26") & (moneda_insertada == "2"):
            estado_siguiente = "λ (q26 = Terminal, regreso a q0)"
            estado_siguiente =  "q0"
        elif (estado == "q26") & (moneda_insertada == "5"):
            estado_siguiente = "λ (q26 = Terminal, regreso a q0)" 
            estado_siguiente =  "q0"
        elif (estado == "q26") & (moneda_insertada == "10"):
            estado_siguiente = "λ (q26 = Terminal, regreso a q0)"
            estado_siguiente =  "q0"

        if estado_siguiente == "λ":
            estado_siguiente =  "q0"
        elif estado_siguiente == "λ (q26 = Terminal, regreso a q0)":
            estado_siguiente =  "q0"
        elif estado_siguiente == "λ (q17 = Terminal, regreso a q0)":
            estado_siguiente =  "q0"
        elif estado_siguiente == "λ (q12 = Terminal, regreso a q0)":
            estado_siguiente =  "q0"
        elif estado_siguiente == "λ (q4 = Terminal, regreso a q0)":
            estado_siguiente =  "q0"
        
        print("Total: $" + str(total))
        self.total_label.setText("$" + str(total))

        print("Viajes disponibles: " + str(viajes_disponibles))
        self.viajes_disponibles_label.setText(str(viajes_disponibles))

        print("Estados: " + estado + "->" + estado_siguiente)
        self.estados_label.setText("Actual: (" + estado + ") -> Siguiente: (" + estado_siguiente + ")")

        if total >= 100:
            self.limite_recarga()

    def cerrar(self):
        QMessageBox.information(self, "Recargar", "Se recargaron: $" + str(total) + " exitosamente!")
        main.close()

    def limite_recarga(self):
        QMessageBox.information(self, "Limite de recarga", "Haz llegado al limite, se recargaron: $" + str(total) + " exitosamente!")
        main.close()

app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()
sys.exit(app.exec_())
