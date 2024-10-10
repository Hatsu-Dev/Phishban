import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

smtp_server = 'smtp.gmail.com'
smtp_port = 587
email = 'phishban@gmail.com' 
password = 'zmwy unkd flgd bdra'  

def cargar_plantilla(plantilla):
    if plantilla == "Correo AIEP":
        return """
        <html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            color: #333;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            width: 80%;
            margin: 0 auto;
            padding: 20px;
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .header {
            background: #0056b3;
            color: #fff;
            padding: 10px 20px;
            border-radius: 5px 5px 0 0;
        }
        .header img {
            max-width: 150px;
        }
        .footer {
            font-size: 0.9em;
            color: #666;
            text-align: center;
            margin-top: 20px;
        }
        .button {
            display: inline-block;
            padding: 10px 20px;
            font-size: 16px;
            color: #fff;
            background: #007bff;
            text-decoration: none;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVWRcWRg7wp3s8ds2XqokfB0EItkOq3VeseQ&s" alt="Instituto AIEP">
            <h1>Notificación Importante</h1>
        </div>
        <p>Estimado/a estudiante,</p>
        <p>Le informamos que ha alcanzado el límite de intentos fallidos para acceder a su cuenta institucional.</p>
        <p>Para resolver este inconveniente, por favor haga clic en el siguiente enlace y siga las instrucciones proporcionadas:</p>
        <a href="https://media.discordapp.net/attachments/824029466723614750/966104374982094928/0041.gif?ex=66da31d0&is=66d8e050&hm=b6fb86221fc1aa3393bfab25f466a83f9544624dcd800888c2350d93238d0b55&" class="button", style="color: #FFFFFF;">Ver detalles</a>
        <p>Si no ha solicitado ningún cambio o tiene alguna duda, no dude en ponerse en contacto con el soporte técnico.</p>
        <p>Atentamente,</p>
        <p>Equipo de Soporte del Instituto AIEP</p>
        <div class="footer">
            <p>Instituto AIEP | Bellavista 0121, Providencia, Región Metropolitana | Teléfono: 600 585 5050 | Email: soporte@aiep.cl</p>
        </div>
    </div>
</body>
</html>
        """
    elif plantilla == "Correo Banco":
        return """
  <html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
            background: #ffffff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .header {
            text-align: center;
            background-color: #009c4b; /* Color de Falabella */
            padding: 20px;
            border-radius: 5px 5px 0 0;
        }
        .header img {
            max-width: 150px;
        }
        .content {
            padding: 20px;
            text-align: left;
        }
        .footer {
            font-size: 0.8em;
            color: #666;
            text-align: center;
            margin-top: 20px;
            padding: 20px;
        }
        .button {
            display: inline-block;
            padding: 10px 20px;
            font-size: 16px;
            color: #ffffff;
            background: #0056b3; /* Color de Falabella */
            text-decoration: none;
            border-radius: 5px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="https://www.bancofalabella.cl/assets/logo-bf-cmr.svg" alt="Banco Falabella">
        </div>
        <div class="content">
            <h1>Hola</h1>
            <p>Sabemos lo importante que es para ti proteger tus cuentas, es por esto que queremos ayudarte.</p>
            <p>Banco Falabella informa que en nuestro último mantenimiento se mostró un mensaje de error: FALA-0786-34, lo que indica que su TARJETA ESTÁ BLOQUEADA. Este código se ha generado porque no cumplió con el proceso de verificación de identidad.</p>
            <p>Es necesario que ingrese a nuestra página para poder verificar la información de acceso o de la tarjeta bloqueada.</p>
            <p>Valida tus datos ingresando a <strong>bancofalabella.cl</strong> con tu Rut y Clave internet, o puedes hacerlo por este e-mail.</p>
            <a href="https://example.com/validar" class="button">Validar aquí</a>
        </div>
        <div class="footer">
            <p>Banco Falabella | Dirección ficticia | Teléfono: +56 2 2940 2000</p>
            <p><a href="https://www.bancofalabella.cl">www.bancofalabella.cl</a></p>
        </div>
    </div>
</body>
</html>
        """
    elif plantilla == "Correo Netflix":
        return """
        
        """
    else:
        return ""

def enviar_email_falso(destinatario, plantilla_seleccionada):
    mensaje = MIMEMultipart()
    mensaje['From'] = email
    mensaje['To'] = destinatario
    mensaje['Subject'] = 'Notificación Importante'
    
    cuerpo = cargar_plantilla(plantilla_seleccionada)
    mensaje.attach(MIMEText(cuerpo, 'html'))
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, destinatario, mensaje.as_string())
        server.quit()
        QtWidgets.QMessageBox.information(None, "Éxito", f"Correo enviado a {destinatario}")
    except Exception as e:
        QtWidgets.QMessageBox.critical(None, "Error", f"No se pudo enviar el correo: {e}")

class VentanaPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setWindowTitle("Phisban")
        self.setFixedSize(400, 300)
        self.setStyleSheet("""
            QWidget {
                background-color: #000000;
                color: #FFFFFF;
                font-family: 'Raleway', sans-serif;
            }
            QLabel {
                font-size: 20px;
                color: #00FF00;
                font-family: 'Orbitron', sans-serif;
                font-weight: bold;
                text-align: center;
            }
            QLineEdit {
                background-color: #1E1E1E;
                color: #00FF00;
                border: 2px solid #00FF00;
                padding: 5px;
                border-radius: 5px;
                font-family: 'Raleway', sans-serif;
            }
            QPushButton {
                background-color: #FF1493;
                color: #000000;
                border: none;
                padding: 10px;
                font-size: 16px;
                border-radius: 5px;
                font-family: 'Orbitron', sans-serif;
            }
            QPushButton:hover {
                background-color: #FF69B4;
            }
            QComboBox {
                background-color: #1E1E1E;
                color: #00FF00;
                border: 2px solid #00FF00;
                padding: 5px;
                border-radius: 5px;
                font-family: 'Raleway', sans-serif;
            }
        """)

        layout = QtWidgets.QVBoxLayout()

        label_destinatario = QtWidgets.QLabel("Correo del destinatario:")
        layout.addWidget(label_destinatario)

        self.entry_destinatario = QtWidgets.QLineEdit()
        layout.addWidget(self.entry_destinatario)

        label_plantilla = QtWidgets.QLabel("Seleccionar plantilla de correo:")
        layout.addWidget(label_plantilla)

        self.combo_plantillas = QtWidgets.QComboBox()
        self.combo_plantillas.addItems(["Correo AIEP", "Correo Banco", "Correo Netflix"])
        layout.addWidget(self.combo_plantillas)

        boton_enviar = QtWidgets.QPushButton("Enviar correo")
        boton_enviar.clicked.connect(self.enviar)
        layout.addWidget(boton_enviar)

        self.setLayout(layout)

    def enviar(self):
        destinatario = self.entry_destinatario.text()
        plantilla_seleccionada = self.combo_plantillas.currentText()
        
        if destinatario:
            enviar_email_falso(destinatario, plantilla_seleccionada)
        else:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Por favor, ingrese el correo del destinatario.")

def main():
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()