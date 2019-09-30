# segurtasun-industriala

## Ariketak

## 1. Fasea: Fabrika sortu

Industria bateko fabrika simulatuko da. Bere PLC, HMI, sensore (tenperatura, ...), aktuadore (argi-led, pultsadore). Adibidez, PLC batek piezak egiten dituen makina bat kontrolatuko du, geldirik dagoenean argi gorri bat piztuko du, lanean dagoenean argi berdea eta pieza amaitzen duenean seinale bat (beste argi bat izan daiteke, edo buzz bat, ...). Beste PLC batek tenperatura eta humedadea kontrolatuko ditu. HMIak egongo dira prozesu guztiaren egoera azaltzeko (argien egoera, tenperatura, ) eta baita ere makinak gelditzeko eta hasieratzeko. Beste PLC batek piezak egiteko lehengaien egoera kontrolatuko du, zenbat dauden. Kamarak, RFID irakurgailuak, ... ere integratu daitezke.

### Open PLC

- PLC
- HMI

PLC eta HMI bat simulatu https://www.openplcproject.com. Raspberry Pi, Arduino, nodemcu, Linux,... erabiliz egin daiteke. Programa sinple bat egin: Led bat piztu/itzali.

1 - https://www.openplcproject.com/getting-started-rpi

2 - PLC programa egin: https://www.openplcproject.com/plcopen-editor

3 - HMI bat simulatu: https://www.openplcproject.com/reference-installing-scadabr

### Siemens

- S7-1200 PLC
- HMI

Siemens S7-1200 PLCa eta HMI instalatu eta konfiguratu. Argia itzali/Piztu aplikazioa egin.

### Node RED

Node red erabiliz datuak jaso (tenperatura, ...) eta data-base batean gorde

### OPC-UA

### Elastic search. Kibana. 

### ERP


## 2. Fasea: Fabrikaren segurtasun azterketa

ModBUS, SCADA, segmentazioa, TLS, OPC-UA

### SCADA. ModBUS. Segurtasuna

- ModBUS: https://en.wikipedia.org/wiki/Modbus
- http://www.modbus.org
- https://en.wikipedia.org/wiki/SCADA

SCADA eta ModBUS ulertu. Aurreko ariketetan ModBUS trafikoa aztertu eta protokoloaren arkitektura ulertu. Aldatzen saiatu. Segurtasunaren aldetik ondorioak atera.


### PLC-en segurtasuna. 

Siemens, simulatuak

