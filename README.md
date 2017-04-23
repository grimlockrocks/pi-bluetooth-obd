# pi-bluetooth-obd
Connect Raspberry Pi with Bluetooth OBD adapter and collect real-time car data. 

Requirements:
* Car, I have a 2008 Volvo S40
* Raspberry Pi 3, which comes with Bluetooth adapter
* Bluetooth OBDII Scanner, I am using [BAFX Products 34t5 Bluetooth OBDII Scan Tool](https://www.amazon.com/gp/product/B005NLQAHS)

Step 1 - Install Softwares
* Install [Python OBD](http://python-obd.readthedocs.io/en/latest/): ```sudo pip3 install obd```
* Upgrade [pySerial](https://pythonhosted.org/pyserial/): ```sudo pip3 install --upgrade pyserial```

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
Step 3 - Connect Car
