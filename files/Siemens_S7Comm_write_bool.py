import snap7, sys
import snap7.client as client
from snap7.util import *
from snap7.snap7types import *
from time import sleep
import argparse

def WriteOutput(dev,byte,bit,cmd):
	byte = int(byte)
	bit = int(bit)
	cmd = int(cmd)
	data = dev.read_area(areas['PA'],0,byte,1)
	set_bool(data,byte,bit,cmd)
	dev.write_area(areas['PA'],0,byte,data)

if __name__=="__main__":
	plc = snap7.client.Client()
	#plc.connect('192.168.222.41',0,1)
        #plc.connect('192.168.222.42',0,1)
        plc.connect('192.168.222.44',0,1)
        #sleep (1)
	if len(sys.argv)==4:
		sleep(0.2)
		WriteOutput(plc,sys.argv[1],sys.argv[2],sys.argv[3])
	else:
	  	print "Introduce los argumentos correctos!"



### Ejecucion CLI:
### 
### $python write_bool.py 0 0 0       ##Nº_byte Nº_bit 0/1
### 
### $for i in `seq 0 5`; do python write_bool.py 0 $i 0;done       ##Apagar todas las salidas
### 
### $for i in `seq 0 5`; do python write_bool.py 0 $i 1;done       ##Encender todas las salidas
### 
### En TIA Portal, el checkbox "habilitar comunicacion PUT/GET" debe estar marcado, de lo contrario no se podra escribir ni leer.

