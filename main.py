from machine import Pin, I2C, ADC, PWM
from time import sleep
from pico_i2c_lcd import I2cLcd
import utime

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
buzzer_pin = Pin(13, Pin.OUT)
buzzer = PWM(buzzer_pin)

pot_value = ADC(Pin(28))

number = int(input("Enter a number between 0 and 1023: "))

if number < 0 or number > 1023:
    print("Error: Please enter a number between 0 and 1023.")
else:
    print("Entered number:", number)

while True:
    sleep(1)
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr('Number: ')
    lcd.move_to(8, 0)
    lcd.putstr(str(number))
    pot_num = int(pot_value.read_u16() // 64.0615)
    print(pot_num)
    
    if number > pot_num:        
        lcd.move_to(0, 1)
        lcd.putstr('Buyuk Sayi')
        buzzer.freq(400)
        buzzer.duty_u16(3000)
        utime.sleep(0.5)
    else:
        buzzer.duty_u16(0)  # Turn off the buzzer if pot_num <= number
