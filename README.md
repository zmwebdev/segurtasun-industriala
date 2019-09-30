# segurtasun-industriala

## Ariketak

## 1. Fasea: Fabrika sortu

Industria bateko fabrika simulatuko da. Bere PLC, HMI, sensore (tenperatura, ...), aktuadore (argi-led, pultsadore). Adibidez, PLC batek piezak egiten dituen makina bat kontrolatuko du, geldirik dagoenean argi gorri bat piztuko du, lanean dagoenean argi berdea eta pieza amaitzen duenean seinale bat (beste argi bat izan daiteke, edo buzz bat, ...). Beste PLC batek tenperatura eta humedadea kontrolatuko ditu. HMIak egongo dira prozesu guztiaren egoera azaltzeko (argien egoera, tenperatura, ) eta baita ere makinak gelditzeko eta hasieratzeko. Beste PLC batek piezak egiteko lehengaien egoera kontrolatuko du, zenbat dauden. Kamarak, RFID irakurgailuak, ... ere integratu daitezke.

Gure fabrikari, WIFI sarea ere gehituko diogu. Baita ERP bat. VNC aukera ere kanpotik operadoreak konponketak egiteko. HMI-a VNC bidez kontrolatzeko aukera (remote HMI access).

Lehenengo fase honetan segurtasuna kontutan hartu gabeko diseinua egingo da. Erabilgarritasunari begira aukerak gehituko dira. 

Erabiliko dugun HW: 
- PLCak egiteko Siemens s7-1200(x2) eta Raspberry Pi (OpenPLC erabiliz simulatuz)
- HMIak egiteko Siemens(x2) eta HMI simulatzaileak. 
- "makinak", arduino edo raspberry pi-ekin simulatuko dira. 
- Sensore eta aktuadoreak

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

### Siemens PLC (24V) eta Raspberry Pi-Arduino (5V)

Gailuen arteko lotura. Nola pasa batetik bestera seinaleak.

### Node RED

Node red erabiliz datuak jaso (tenperatura, ...) eta data-base batean gorde

### OPC-UA

### Elastic search. Kibana. 

### ERP


## 2. Fasea: Fabrikaren segurtasun azterketa

Lehenengo fasean garatu dugun fabrikaren segurtasuna aztertuko da eta soluzioak inplementatuko dira. ModBUS, SCADA, segmentazioa, TLS, OPC-UA, WIFI, ...

### SCADA. ModBUS. Segurtasuna

- ModBUS: https://en.wikipedia.org/wiki/Modbus
- http://www.modbus.org
- https://en.wikipedia.org/wiki/SCADA

SCADA eta ModBUS ulertu. Aurreko ariketetan ModBUS trafikoa aztertu eta protokoloaren arkitektura ulertu. Aldatzen saiatu. Segurtasunaren aldetik ondorioak atera.


### PLC-en segurtasuna. 

Siemens, simulatuak

