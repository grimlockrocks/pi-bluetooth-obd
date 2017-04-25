import obd
import boto3
import threading

# Update DynamoDB table
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("telematics")

def upload(speed, fuel):
  table.put_item(
    Item={
      "id": "1",
      "speed": speed,
      "fuel": fuel
    }
  )
  print("Updated DynamoDB")

# OBD setup
obd.logger.setLevel(obd.logging.DEBUG)

# Connect to OBDII adapter
ports = obd.scan_serial()
connection = obd.OBD(ports[0])

# Scheduler 
def repeat():
  threading.Timer(10.0, repeat).start()
  speedCmd = connection.query(obd.commands.SPEED)
  speedVal = str(speedCmd.value)
  fuelCmd = connection.query(obd.commands.FUEL_LEVEL)
  fuelVal = str(fuelCmd.value)
  print("Speed: " + speedVal + ", fuel: " + fuelVal)
  upload(speedVal, fuelVal)

repeat()

