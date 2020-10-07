
from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
import time
#Modbus TCP set up 
SERVER_HOST = "192.168.1.111"
SERVER_PORT = 502
#c = ModbusClient()
#c=FloatModbus()
#c.host(SERVER_HOST)
#c.port(SERVER_PORT)



var_alarm_up = True #initilize value 

class FloatModbus(ModbusClient):
    def read_float(self, addr, number=1):
        reg_l = self.read_holding_registers(addr, number * 2)
        if reg_l:
            #print(reg_l)
            return [utils.decode_ieee(f) for f in utils.word_list_to_long(reg_l)]
        else:
            reg_l=[16000,16000]
            return [utils.decode_ieee(f) for f in utils.word_list_to_long(reg_l)]

c = FloatModbus()
c.host(SERVER_HOST)
c.port(SERVER_PORT)

while True:
    
    # open or reconnect TCP to server
    if not c.is_open():
        if not c.open():
            print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))
    # if open() is ok, read register (modbus function 0x03)
    if c.is_open():
        # read 2 registers at address 0, store result in regs list
        #Modbus function READ_holding_REGISTERS (0x03)
        #regs_sts = c.read_float(1,10)
        regs_ws_hor = c.read_input_registers(1,1)
        #c.close()
       
        
    
    #Scale from integer to float
    #var_temp = regs_sts[1]
    #var_RH = regs_sts[1]
    
    #print("Current 1: ",int(var_temp),"A",'\n')
    #print("Current 2: ",var_RH,"A",'\n')
    ##var_A1=regs_sts[0]
    #print(regs_sts[3])
    ##print(regs_sts)
    print(int(regs_ws_hor[0])/10)
    print("**********************",'\n')
    time.sleep(2)


