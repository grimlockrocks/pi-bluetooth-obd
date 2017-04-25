import obd

# OBD setup
obd.logger.setLevel(obd.logging.DEBUG)

# Connect to OBDII adapter
ports = obd.scan_serial()
print("Ports: ")
print(ports)

connection = obd.OBD(ports[0])
print("Connection status: ")
print(connection.status())

# Print supported commands
commands = connection.supported_commands
print("Supported commands: ")
for command in commands:
  print(command.name)

# Send a command
while True:
  command = input("Enter command (type 'quit' to exit): ")
  if (command == "quit"):
    break
  try:
    res = connection.query(obd.commands[command])
    print(res.value)
  except Exception as ex:
    print("Error: " + str(ex))

# Close the connection
connection.close()
