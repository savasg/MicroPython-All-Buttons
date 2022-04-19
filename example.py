from buttons import butonlar
import time

def button_tick(buton, sure):
    print('buton %r %r ms süre ile basıldı' % (buton, sure))
    
BUTONLAR=butonlar([3,4,5], "button_tick", 100)

while True:
    time.sleep(0.2)