from machine import Pin, Timer
import time, _thread, machine

class butonlar:
    def __init__(self, butonlar, _callback_fn, period):
        def _helper(t):
            for i in range(len(butonlar)):
                buton=Pin(self.butonlar[i], Pin.IN, Pin.PULL_UP)
                if buton.value()!=self.sonDurum[i]:
                    if(self.sonDurum[i]==False and buton.value()==True):
                        locals()[_callback_fn](i, time.ticks_ms()-self.sonZaman[i])
                    self.sonZaman[i]=time.ticks_ms()
                    self.sonDurum[i]=buton.value()
                    time.sleep(0.1)               
        self.butonlar=butonlar
        self.sonZaman=list()
        self.sonDurum=list()
        for i in range(len(butonlar)):
            self.sonZaman.append(time.ticks_ms())
            self.sonDurum.append(1)
        self.a = time.ticks_ms()
        tim1 = Timer(-1)
        tim1.init(period=period, callback=_helper)
