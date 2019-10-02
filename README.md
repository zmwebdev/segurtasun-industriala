# segurtasun-industriala

## Ariketak

## 1. Fasea: Fabrika sortu

Industria bateko fabrika simulatuko da. Bere PLC, HMI, sensore (tenperatura, ...), aktuadore (argi-led, pultsadore). Adibidez, PLC batek piezak egiten dituen makina bat kontrolatuko du, geldirik dagoenean argi gorri bat piztuko du, lanean dagoenean argi berdea eta pieza amaitzen duenean seinale bat (beste argi bat izan daiteke, edo buzz bat, ...). Beste PLC batek tenperatura eta humedadea kontrolatuko ditu (slave device: nodemcu bat izan daiteke). HMIak egongo dira prozesu guztiaren egoera azaltzeko (argien egoera, tenperatura, ) eta baita ere makinak gelditzeko eta hasieratzeko. Beste PLC batek piezak egiteko lehengaien egoera kontrolatuko du, zenbat dauden. Kamarak, RFID irakurgailuak, BLE Bluetooth Low Energy device, ... ere integratu daitezke. Fabrikak sosrtzen dituen datuak gordeko dira ondoren analizatu ahal izateko eta hauetatik AI erabiliz ikasteko. Aukera dado ere informazio hauek Cloud-ean gordetzeko (MQTT erabiliz datuak mugituz).

Gure fabrikari (Smart Factory), WIFI sarea ere gehituko diogu. Baita ERP bat. VNC aukera ere kanpotik operadoreak konponketak egiteko. HMI-a VNC bidez kontrolatzeko aukera (remote HMI access). 

Lehenengo fase honetan segurtasuna kontutan hartu gabeko diseinua egingo da. Erabilgarritasunari begira aukerak gehituko dira. 

Erabiliko dugun HW: 
- PLCak egiteko Siemens s7-1200(x2) eta Raspberry Pi (OpenPLC erabiliz simulatuz)
- HMIak egiteko Siemens(x2) eta HMI simulatzaileak. 
- "makinak", arduino edo raspberry pi-ekin simulatuko dira. 
- Sensore eta aktuadoreak
- Cloud

### Open PLC

- PLC
- HMI
- https://www.openplcproject.com/reference
- https://openplc.discussion.community/post/my-first-project-9671952

PLC eta HMI bat simulatu https://www.openplcproject.com. Raspberry Pi, Arduino, nodemcu, Linux,... erabiliz egin daiteke. 

#### Programa sinple bat egin: Led bat piztu/itzali.

1 - https://www.openplcproject.com/getting-started-rpi

- Raspbian Buster Lite instalatu. IP static eman eman (https://wiki.debian.org/NetworkConfiguration) eta ssh bidez konektatu ``` $sudo raspi-conf``` erabiliz. Hemendik aurrera gure PLCak sare konexioa eta argindarra bakarrik izango ditu eta ssh bidez konektatuko gara. ```$ssh pi@IP```

2 - PLC programa egin: https://www.openplcproject.com/plcopen-editor

3 - HMI bat simulatu: https://www.openplcproject.com/reference-installing-scadabr

#### Programa konplexuagoak egin

#### PLC simulatuak sare batean konektatu eta elkarrekintza

PLC batetik beste PLC bat kontrolatu (nola? modbus?) 'slave device' MTU, IP

- https://www.openplcproject.com/getting-started-modbus-io
- https://www.openplcproject.com/getting-started-esp8266


### Siemens

- S7-1200 PLC
- HMI

Siemens S7-1200 PLCa eta HMI instalatu eta konfiguratu. Argia itzali/Piztu aplikazioa egin.

- Siemens PLC (24V) eta Raspberry Pi-Arduino (5V): Gailuen arteko lotura. Nola pasa batetik bestera seinaleak.

### Node RED

Node red erabiliz datuak jaso (tenperatura, ...) eta data-base batean gorde

### OPC-UA

### Elastic search. Kibana. 

### ERP


## 2. Fasea: Fabrikaren segurtasun azterketa

Lehenengo fasean garatu dugun fabrikaren segurtasuna aztertuko da eta soluzioak inplementatuko dira. ModBUS, SCADA, segmentazioa, TLS, OPC-UA, WIFI, MQTT, ...

### SCADA. ModBUS. Segurtasuna

- ModBUS: https://en.wikipedia.org/wiki/Modbus
- http://www.modbus.org
- https://en.wikipedia.org/wiki/SCADA

SCADA eta ModBUS ulertu. Aurreko ariketetan ModBUS trafikoa aztertu eta protokoloaren arkitektura ulertu. Aldatzen saiatu. Segurtasunaren aldetik ondorioak atera.


### PLC-en segurtasuna. 

Siemens, PLC simulatuak OpenPLC/raspberry pi (raspberry pi: default user/password: SSH is enabled and the default password for the 'pi' user has not been changed.This is a security risk - please login as the 'pi' user and type 'passwd' to set a new password. /// edo OpenPLC: This means that the first thing you must do after logging in for the first time is change the default username and password!)

ModBus: ```nmap -sS -T3 --top-ports 3000 167.99.132.140``` begiratu ITS kurtsoa

## 3. Fasea: Smart Factory

Smart Factory baten proposamena, segurtasuna oinarritzat hartuta fabrika adimendu bat sortzea. Distributed secured factory using Blockchain.

