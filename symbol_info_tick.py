import MetaTrader5 as mt5
from config import login_info

path=login_info["path"]
login=login_info["login"]    
server=login_info["server"]
password=login_info["password"]

# initializing connection with MetaTrader 5 Terminal 
if not mt5.initialize(path,login=login,server=server,password=password):
     print(f'Initialized failed, error code = {mt5.last_error()}')
     quit()

# function to use in the MT5 terminal 
# attempt to enable the display of the GBPUSD in MarketWatch
selected=mt5.symbol_select("GBPUSD",True)
if not selected:
    print("Failed to select GBPUSD")
    mt5.shutdown()
    quit()
 
# display the last GBPUSD tick
lasttick=mt5.symbol_info_tick("GBPUSD")
print(lasttick)
# display tick field values in the form of a list
print("Show symbol_info_tick(\"GBPUSD\")._asdict():")
symbol_info_tick_dict = mt5.symbol_info_tick("GBPUSD")._asdict()
for prop in symbol_info_tick_dict:
    print("  {}={}".format(prop, symbol_info_tick_dict[prop]))

# Terminating connection with the MetaTrader Terminal 5
mt5.shutdown()