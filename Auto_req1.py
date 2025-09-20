"""Requirement:
   Create a module name ACC Define ECU name ACC 
   channel and network shall be ACC vehicle network, 
   and baud rate is 250 kbps. 
   Output in display shall be
   ECU is connected to respective network at baud rate 

   and 
   run the script in command line or terminal
   comment the program
   Open the script in command line change baud rate to 500 kbps
   Run the code in idle lib
     """

#start of code
#ECU ACC detailed information
ECU_NAME = "ACC"
Channel_connected = 5
Network_connected = "ACC_Vehicle_network"
Baud_rate = 250

#output
print ("ECU name is %s" %ECU_NAME)
print("%s ECU is connected on channel %d and running on baud rate %d" %(ECU_NAME,))
