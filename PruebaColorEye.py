# -*- coding: utf-8 -*-
import argparse
import time
from naoqi import ALProxy

def changeEyesColor(proxy, color):
    proxy.fadeRGB("FaceLeds", color, 1)

def turnOffEyes(proxy):
    proxy.off("FaceLeds")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Control de NAO para lectura de libros")
    parser.add_argument("--ip", type=str, required=True, help="Dirección IP del robot NAO")
    parser.add_argument("--port", type=int, default=9559, help="Puerto del robot NAO (por defecto es 9559)")
    args = parser.parse_args()
    leds = ALProxy("ALLeds", args.ip, args.port)
    color = 0x0000FF # Azul
    changeEyesColor(leds, color)
    time.sleep(5)
    turnOffEyes(leds)
    time.sleep(2)

    color = 0x00FF00 # Verde

    changeEyesColor(leds, color)
    time.sleep(5)
    turnOffEyes(leds)
