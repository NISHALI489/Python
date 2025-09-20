#ACC Node details information
ECU_NAME = "ACC"                    #ECU name assigned
channel_connected = 1               #Channel added
Baud_rate = 2500                    #Baude rate running for ECU
Network_type = "ACC_CAN_Network"
print("ECU name is %s" %ECU_NAME)
print("%s ECU is connected to channel %d and running at baud rate %d" %(ECU_NAME, channel_connected, Baud_rate))
