# pi-bluetooth-obd
Connect Raspberry Pi with Bluetooth OBD adapter and collect real-time car data. 

Requirements:
* Car, I have a 2008 Volvo S40
* Raspberry Pi 3, which comes with Bluetooth adapter
* Bluetooth OBDII Scanner, I am using [BAFX Products 34t5 Bluetooth OBDII Scan Tool](https://www.amazon.com/gp/product/B005NLQAHS)

Step 1 - Install Softwares
* Install [Python OBD](http://python-obd.readthedocs.io/en/latest/): ```sudo pip3 install obd```
* Upgrade [pySerial](https://pythonhosted.org/pyserial/): ```sudo pip3 install --upgrade pyserial```
* Install Screen ```sudo apt-get install screen```

Step 2 - Connect OBD Adapater via Bluetooth
```
bluetoothctl
help <-- see all the commands
show
power on
pairable on
scan on <-- find OBDII and its MAC address
pair <mac_address> <-- enter pin 1234
trust <mac_address>
scan off
quit
```

Step 3 - Connect Car with Screen
```
screen /dev/rfcomm0
atz
atl1
ath1
atsp0 <-- use protocol auto, available protocols: 1, 2, 3, 4, 5, 6, 7, 8, 9, A
0100 <-- mode 01, pid 00, supported pids
```
If successfully connected to the car, 0100 will return something instead of "UNABLE TO CONNECT" or "CAN ERROR" or "BUS INIT: ...ERROR".

Step 4 - Connect Car with Python OBD
* Create a serial port: ```sudo rfcomm bind hci0 <mac_address>```
* Run the program: ```python3 obd_reader.py```
