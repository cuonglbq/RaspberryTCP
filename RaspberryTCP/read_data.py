#check GIT

import blynklib
from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
import time
#-----------define value------------------
init_connect = True
init_read = False
var_Compare=0
list_Buffer1=[]
list_Buffer2=[]
list_Buffer3=[]
list_buffer4=[]
list_buffer5=[]
list_Buffer=[]
list_Buffer_Start=[]
list_Buffer_Final=[]
count = 0
list_String_IVT1=[19,22,22,19,18,22,22,20,20,19,22,19,22,22,22]
list_Data_F=[]
flag_read_Current=True
flag_read_Weather=False
data_Weather=0
keep_Alarm=False
var_alarm_up = False #initilize value
"""
ip_Device=["192.168.1.151","192.168.1.152","192.168.1.153","192.168.1.154","192.168.1.155","192.168.1.156",
           "192.168.1.157","192.168.1.158","192.168.1.159","192.168.1.160","192.168.1.161","192.168.1.162",
           "192.168.1.163","192.168.1.164","192.168.1.165","192.168.1.166"]
"""
ip_Device=["192.168.1.151"]
name_Device=["IVT1.1","IVT1.2","IVT2.1","IVT2.2","IVT3.1","IVT3.2","IVT4.1","IVT4.2","IVT5.1","IVT5.2","IVT6.1","IVT6.2","IVT7.1","IVT7.2","IVT8.1","IVT8.2"]
#-----------end define value -------------
class FloatModbusClient(ModbusClient):
    def read_float(self , address, number=1):
        reg_l = self.read_holding_registers(address,number * 2)
        if reg_l:
            return [utils.decode_ieee(f) for f  in utils.word_list_to_long(reg_l)]
        else:
            reg_l = [16000,16000]
            return [utils.decode_ieee(f) for f  in utils.word_list_to_long(reg_l)]    
c = FloatModbusClient()
def Connect_MbTCP(ip,func,reg_addr,reg_nb):
    SERVER_HOST = ip
    SERVER_PORT = 502
    #c = ModbusClient()
    c.host(SERVER_HOST)
    c.port(SERVER_PORT)

    if not c.is_open():
        if not c.open():
            print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))
    if c.is_open():
        init_read = True
    if init_read==True:
        if func==3:
            regs_data = c.read_float(reg_addr,reg_nb)
            #find_MaxMin(regs_data)
            #print(regs_data)
            return regs_data
        if func==4:
            regs_data=c.read_input_registers(reg_addr,reg_nb)
            return regs_data
            c.close()
        else:
            print("PLS! choose FunctionCod")


def find_MaxMin(data):
    max_data=max(data)
    var_Compare=(max_data*10)/100
    print(var_Compare)
    for y in data:
        if y<max_data-var_Compare:
            print("Lost Current at")



#Blynk set up
BLYNK_AUTH = 'yJrIM13raUXVjmYPoGxIyd2LYdOSs0w3'
blynk = blynklib.Blynk(BLYNK_AUTH)

#Weather data
@blynk.handle_event('read V0')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, data_Weather[0]/10)

#SCB1 normalized current 
@blynk.handle_event('read V1')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, list_Data_F[0])

#SCB2 normalized current 
@blynk.handle_event('read V2')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, list_Data_F[1])

#SCB3 normalized current 
@blynk.handle_event('read V3')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, list_Data_F[2])

#SCB4 normalized current 
@blynk.handle_event('read V4')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, list_Data_F[3])

#SCB5 normalized current 
@blynk.handle_event('read V5')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, list_Data_F[4])

#SCB6 normalized current 
@blynk.handle_event('read V6')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, list_Data_F[5])

#SCB7 normalized current 
@blynk.handle_event('read V7')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, list_Data_F[6])

#SCB8 normalized current 
@blynk.handle_event('read V8')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, list_Data_F[7])

#SCB9 normalized current 
@blynk.handle_event('read V9')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, list_Data_F[8])

#SCB10 normalized current 
@blynk.handle_event('read V10')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, list_Data_F[9])

#SCB11 normalized current 
@blynk.handle_event('read V11')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, list_Data_F[10])

#SCB12 normalized current 
@blynk.handle_event('read V12')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, list_Data_F[11])

#SCB13 normalized current 
@blynk.handle_event('read V13')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, list_Data_F[12])

#SCB14 normalized current 
@blynk.handle_event('read V14')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, list_Data_F[13])

#SCB15 normalized current 
@blynk.handle_event('read V15')
def read_virtual_pin_handler(pin) :
    blynk.virtual_write(pin, list_Data_F[14])

###########################################################
# infinite loop that waits for event
###########################################################
def read_weather():
    data=Connect_MbTCP("192.168.1.111",4,1,1)
    return data

def Alarm(value_Alarm):
    
    if value_Alarm == True and keep_Alarm==False:
        blynk.notify(alarm_msg)
        blynk.email("cuonglbq@geccom.vn", alarm_msg , "https://shorturl.at/hDTY2")
        #blynk.notify('Alarm SET!')
        #blynk.email("cuonglbq@geccom.vn", "Sensor Temperature & Humidity", "https://drive.google.com/file/d/1SzKMVdSz59slXK4rYwqK5kk_zL_PKdxi/view?usp=sharing");
        value_Alarm = False
        keep_Alarm=True
    if value_Alarm == False:
        blynk.notify('Alarm CLEAR!')
        keep_Alarm=False
    


while True:
    blynk.run()
    if flag_read_Weather == True:
        data_Weather=read_weather()
           
        #read SCB current only if irradiance is more than 400W/m2   
        if((data_Weather[0]/10)>400):
            flag_read_Current = True
            flag_read_Weather=False
        else:
            flag_read_Current = False
            flag_read_Weather=True
            print("Low Irradian"+str(data_Weather[0]))
        time.sleep(1)
            
        
        
#    blynk.run()

#    for x in ip_Device:
#        print(x)
#        a=Connect_MbTCP(x,3,1,10)
#        print(a)
#        print("***********************")
#        time.sleep(5)
    
    if flag_read_Current == True:
        data=Connect_MbTCP("192.168.1.151",3,1,14)
        if len(data)>1:
            list_Buffer.append(data)
            count=count+1;
            time.sleep(1)
        if count==5:
            count=0
            count_len_Subbuff=len(list_Buffer[1]) # <------ dem so data trong mang 1 cua buffer
            count_len_Buff=len(list_Buffer) # <-------------dem so data trong mang =5
            for a in range(int(count_len_Subbuff)):
                for b in range(count_len_Buff):
                    list_Buffer_Start.append(list_Buffer[b][a])
                
                list_Buffer_Final.append(max(list_Buffer_Start))
                list_Buffer_Start=[]
           
            list_Buffer=[]
            
            for u in range(len(list_Buffer_Final)):
                d=list_Buffer_Final[u]/list_String_IVT1[u]
                list_Data_F.append(d)
                d=0
            print(list_Data_F)
            max_data=max(list_Data_F)
            var_Compare=(max_data*5)/100
            print(str(var_Compare) + " - " + str(max_data))
            for y in list_Data_F:
                if y<max_data-var_Compare:
                    b=list_Data_F.index(y)+1 //shift from index 0 to index 1 - SCB index starts from 1
                    print("Low Current at SCB No:  " + str(b))
                    
                    alarm_msg = "Low Current at SCB No:  " + str(b) //alarm msg
                    var_alarm_up == True
                    Alarm(var_alarm_up)
                                 
                else:
                    var_alarm_up == False
                    Alarm(var_alarm_up)
            flag_read_Weather=True
                
                  
        list_Data_F=[] 
        
        list_Buffer_Final=[]
        

def Alarm_thermal():
    if var_RH  > 80.0 and var_alarm_up == True: 
        blynk.notify('Humidity high alarm SET!')
        blynk.email("cuonglbq@geccom.vn", "Sensor Temperature & Humidity", "https://drive.google.com/file/d/1SzKMVdSz59slXK4rYwqK5kk_zL_PKdxi/view?usp=sharing");
        var_alarm_up = False

    if var_alarm_up == False and var_RH < 75.0:
        blynk.notify('Humidity high alarm CLEAR!')
        var_alarm_up = True


        #var_alarm_up = True
