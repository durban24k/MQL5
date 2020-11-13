import MetaTrader5 as mt5
from config import login_info

path=login_info["path"]
login=login_info["login"]    
server=login_info["server"]
password=login_info["password"]

# establishing connection with the MetaTrader 5 terminal
if not mt5.initialize(path,login=login,server=server,password=password):
     print(f'Initialized failed, error code = {mt5.last_error()}')
     quit()

# attempt to enable the display of the EURUSD symbol in MarketWatch
selected=mt5.symbol_select("EURUSD",True)
if not selected:
    print("Failed to select EURUSD")
    mt5.shutdown()
    quit()
 
# display EURUSD symbol properties
symbol_info=mt5.symbol_info("EURUSD")
if symbol_info!=None:
    # display the terminal data 'as is'    
    print(symbol_info)
    print("EURUSD: spread =",symbol_info.spread,"  digits =",symbol_info.digits)
    # display symbol properties as a list
    print("Show symbol_info(\"EURUSD\")._asdict():")
    symbol_info_dict = mt5.symbol_info("EURUSD")._asdict()
    for prop in symbol_info_dict:
        print("  {}={}".format(prop, symbol_info_dict[prop]))
 
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()