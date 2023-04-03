import RPi.GPIO as GPIO
import sys
import atexit
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Set the GPIO pin number
led_GREEN = 7
led_RED= 8
led_YELLOW = 10

# Set the pin as output
GPIO.setup(led_GREEN, GPIO.OUT)
GPIO.setup(led_RED, GPIO.OUT)
GPIO.setup(led_BLUE, GPIO.OUT)


def window():
   app = QApplication(sys.argv)
   widget = QWidget()
   
   button1 = QPushButton(widget)
   button1.setText("RED")
   button1.move(64,32)
   button1.clicked.connect(button1_clicked)

   button2 = QPushButton(widget)
   button2.setText("GREEN")
   button2.move(64,64)
   button2.clicked.connect(button2_clicked)

   button3 = QPushButton(widget)
   button3.setText("YELLOW")
   button3.move(64,96)
   button3.clicked.connect(button3_clicked)

   widget.setGeometry(50,50,320,200)
   widget.setWindowTitle("TASK 5.2C")
   widget.show()
   sys.exit(app.exec_())

def goodbye(): #Called when we close the program to turn off LEDs
  GPIO.output(led_GREEN, GPIO.LOW) 
  GPIO.output(led_RED, GPIO.LOW)
  GPIO.output(led_YELLOW, GPIO.LOW)


atexit.register(goodbye) #When we close the program window run goodbye

def led(ledid):
  GPIO.output(led_GREEN, GPIO.LOW)
  GPIO.output(led_RED, GPIO.LOW)
  GPIO.output(led_YELLOW, GPIO.LOW)

  if ledid == "1":
    GPIO.output(led_GREEN, GPIO.HIGH)
  if ledid == "2":
    GPIO.output(led_RED, GPIO.HIGH)
  if ledid == "3":
    GPIO.output(led_YELLOW, GPIO.HIGH)
  

def button1_clicked():
   led("1")
def button2_clicked():
   led("2")  
def button3_clicked():
   led("3")   
   
if __name__ == '__main__':
   window()
