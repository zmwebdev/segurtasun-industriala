# segurtasun-industriala

## kontzeptuak

- https://en.wikipedia.org/wiki/Modbus
- http://www.modbus.org
- https://en.wikipedia.org/wiki/SCADA

 > a single-bit physical output is called a coil, and a single-bit physical input is called a discrete input or a contact
 

## 1. Fasea: Fabrika sortu

Industria bateko fabrika simulatuko da. Bere PLC, HMI, sensore (tenperatura, ...), aktuadore (argi-led, pultsadore). Adibidez, PLC batek piezak egiten dituen makina bat kontrolatuko du, geldirik dagoenean argi gorri bat piztuko du, lanean dagoenean argi berdea eta pieza amaitzen duenean seinale bat (beste argi bat izan daiteke, edo buzz bat, ...). Beste PLC batek tenperatura eta humedadea kontrolatuko ditu (slave device: nodemcu bat izan daiteke). HMIak egongo dira prozesu guztiaren egoera azaltzeko (argien egoera, tenperatura, ) eta baita ere makinak gelditzeko eta hasieratzeko. Beste PLC batek piezak egiteko lehengaien egoera kontrolatuko du, zenbat dauden. Kamarak, RFID irakurgailuak, BLE Bluetooth Low Energy device, Alexa(https://developer.amazon.com/es/docs/alexa-voice-service/set-up-raspberry-pi.html), echo(https://www.makeuseof.com/tag/diy-google-home-assistant-raspberry-pi/)... ere integratu daitezke. Fabrikak sosrtzen dituen datuak gordeko dira ondoren analizatu ahal izateko eta hauetatik AI erabiliz ikasteko. Aukera dado ere informazio hauek Cloud-ean gordetzeko (MQTT erabiliz datuak mugituz).

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

##### 1 - getting-started-rpi:

- https://www.openplcproject.com/getting-started-rpi

- Raspbian Buster Lite instalatu. IP static eman eman (https://raspberrypi.stackexchange.com/questions/37920/how-do-i-set-up-networking-wifi-static-ip-address, https://wiki.debian.org/NetworkConfiguration) eta ssh bidez konektatu ``` $sudo raspi-conf``` erabiliz. Hemendik aurrera gure PLCak sare konexioa eta argindarra bakarrik izango ditu eta ssh bidez konektatuko gara. ```$ssh pi@IP```

##### 2 - PLC programa egin:

https://www.openplcproject.com/plcopen-editor

https://www.element14.com/community/community/applications/industrial-automation-space/blog/2019/08/09/trying-out-openplc-on-a-raspberry-pi

**Hello World:**

![openplc-raspberry-helloworld-wire-schema](img/openplc-raspberry-helloworld-wire-schema.png)
![openplc-raspberry-helloworld-LD](img/openplc-raspberry-helloworld-LD.png)

**Hello World (Sarrera %X0.2 erabiliz. Kontuz! zirkuitua aurrekoaren ezberdinba da!!):**

![openplc_hello_world_lader_program2-circuit](img/openplc_hello_world_lader_program2-circuit.png)
![openplc_hello_world_lader_program2](img/openplc_hello_world_lader_program2.png)

**led piztu**

led-piztu-zirkuitoa             |  led-piztu-eskema
:-------------------------:|:-------------------------:
![led-piztu-zirkuitoa](img/led-botoia-plc-zirkuitoa.jpg)  |  ![led-piztu-eskema](img/led-botoia-plc-eskema.jpg)




##### 3 - HMI bat simulatu:

https://www.openplcproject.com/reference-installing-scadabr


#### Programa konplexuagoak egin

![OpenPLC_ariketak_simpleak.docx.pdf](plc-ariketak/OpenPLC_ariketak_simpleak.docx.pdf)

1 - Bi botoi. Batek piztu besteak itzaldu.

2 - Botoi berdinarekin, itzaldu eta piztu

#### PLC simulatuak sare batean konektatu eta elkarrekintza

PLC batetik beste PLC bat kontrolatu (nola? modbus?) 'slave device' MTU, IP, Software(linux, windows), 

- https://www.openplcproject.com/getting-started-modbus-io
- https://www.openplcproject.com/getting-started-esp8266

##### Beste OpenPLC bat instalatu



port number aldatu (makina berdinean bat baino gehiago instalatu behar badira)
```
Edit /webserver/ webserver.py line 2213 and change

app.run(debug=False, host='0.0.0.0', threaded=True, port=8080)

to

app.run(debug=False, host='0.0.0.0', threaded=True, port=[whatever-port-you'd-like])
```

### Siemens

- S7-1200 PLC. CPU 1212C AC/DC/Rly 6ES7 212-1HE40-0XB0 v4.2
- HMI

Ariketak:
 * Siemens S7-1200 PLCa eta HMI instalatu eta konfiguratu. Argia itzali/Piztu aplikazioa egin.
 * Siemens PLC (24V) eta Raspberry Pi-Arduino (5V): Gailuen arteko lotura. Nola pasa batetik bestera seinaleak.
 
#### TIA Portal

* New Project
* Add new device (S7-1200 PLC. CPU 1212C AC/DC/Rly 6ES7 212-1HE40-0XB0 v4.2)
* (PLC_1) Device configuration -> PROFINET interface -> Ethernet addresses -> (add new subnet) PN/IE_1; (IP Protocol) ip/mask
* (PLC_1) Device configuration -> Protection & Security -> (connection mechanisms) Permit access with PUT/GET ? (aztertu)
* (menu) online -> simulation -> start

#### S7. Profinet
- http://snap7.sourceforge.net/
- https://python-snap7.readthedocs.io/en/latest/
- 
#### Wireshark erabiliz
Wireshark erabiliz profinet - S7 protokoloa aztertu. https://wiki.wireshark.org/S7comm

#### Siemens HMI
TIA portal erabiliz siemens-eko HMI programatu

### Node RED. HMI
- https://nodered.org
- https://flows.nodered.org/node/node-red-contrib-modbus

Node red erabiliz datuak jaso/aldatu (tenperatura, ...)

### OPC-UA

### Elastic search. Kibana. 

### ERP


## 2. Fasea: Fabrikaren segurtasun azterketa

Lehenengo fasean garatu dugun fabrikaren segurtasuna aztertuko da eta soluzioak inplementatuko dira. ModBUS, SCADA, segmentazioa, TLS, OPC-UA, WIFI, MQTT, ...

### SCADA. ModBUS. Segurtasuna

SCADA eta ModBUS ulertu. Aurreko ariketetan ModBUS trafikoa aztertu eta protokoloaren arkitektura ulertu. Aldatzen saiatu. Segurtasunaren aldetik ondorioak atera.


#### Ariketa

1  - OpenPLC (raspberry pi) botoi-led sistemari ModBUS bezero bat erabiliz LED piztu/itzali:
* ModBUS protokoloa berrikusi. TCP/IP. 502 portua
* ModBUS bezero bat erabiliz konexio bat egin PLCarekin eta wireshark erabiliz 502 portua aztertu
    * https://sourceforge.net/projects/qmodmaster/
    * https://pymodbus.readthedocs.io/en/latest/readme.html

* ModBUS bezeroarekin LED-a piztu/itzali

Foro honetan ModBUS-en %IX sarrerak ezin dira aldatu programaren logikaren kontra. Baina sarrera hau %QX batean jarriz gero bai. horrela kanpotik aldatzeko aukera dago: - https://openplc.discussion.community/post/walk-through-of-hello-world-8461363?&trail=15

>One thing to note is that, if you look at the table, you will see that you can't write to inputs, which mean you can't change the value of the inputs. This is a definition of the Modbus protocol. Therefore, in the hello world example, you won't be able to change the state of the button because it is located in an input area (%IX0.0). To actually control the button, you will have to move it to an output address (can be %QX0.1 for example). This will not have any practical effect in your software besides the fact that you will be able to actually write, or force, the state of the button using Modbus

Gogoratu: 

 > a single-bit physical output is called a coil, and a single-bit physical input is called a discrete input or a contact

* Ondorioak atera

* irudiak

Openplc eta qModmaster     |  Openplc editor
:-------------------------:|:-------------------------:
![openplc-led-piztu-itzali](img/openplc_qmodmaster_led_piztu_itzali_QX00_QX01_2.png)  |  ![openplc-editor-led-piztu-itzali](img/openplceditor-led-piztu_itzali_QX00_QX01.png)

### PLC-en segurtasuna. 

Siemens, PLC simulatuak OpenPLC/raspberry pi (raspberry pi: default user/password: SSH is enabled and the default password for the 'pi' user has not been changed.This is a security risk - please login as the 'pi' user and type 'passwd' to set a new password. /// edo OpenPLC: This means that the first thing you must do after logging in for the first time is change the default username and password!)

ModBus: ```nmap -sS -T3 --top-ports 3000 167.99.132.140``` begiratu ITS kurtsoa.

## 3. Fasea: Smart Factory

Smart Factory baten proposamena, segurtasuna oinarritzat hartuta fabrika adimendu bat sortzea. Distributed secured factory using Blockchain.

### 4. HoneyPot

- https://www.incibe-cert.es/blog/guia-implantacion-honeypot-industrial

[incibe-cert_guia_implantacion_honeypot_industrial.pdf](doc/incibe-cert_guia_implantacion_honeypot_industrial.pdf)

- 
