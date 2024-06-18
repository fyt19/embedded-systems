"""
kullanıcıdan input alacak bu inputa göre lcd ekrana bu sayıyı yazdıracak, kullanıcıdan bir işlem alacak + veya * işlemi olacak şekilde. Bu işlemlerden sonra ise bu işlemi lcd ekrana yazacak kod
"""

from machine import Pin, I2C
from time import sleep
from pico_i2c_lcd import I2cLcd
import utime

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

number1 = int(input("Enter a number: "))
process = input("Enter a process: (+ or *)")
number2 = int(input("Enter a number: "))

if process == '+':
  result = number1 + number2
  lcd.move_to(0, 0)
  lcd.putstr(f"{number1} {process} {number2} = {result}")
  
elif process == '*':
  result = number1 * number2
  lcd.move_to(0, 0)
  lcd.putstr(f"{number1} {process} {number2} = {result}")  
  
else:
  lcd.move_to(0, 0)
  lcd.putstr("farklı bir işlem yaptınız!!")  
