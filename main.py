import MetaTrader5 as mt5
from config import login_info

# initialize server variables (login details)
path=login_info["path"]
login=login_info["login"]
server=login_info["server"]
password=login_info["password"]

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
 
# establish MetaTrader 5 connection to a specified trading account
if not mt5.initialize(path,login=login,server=server,password=password):
    print("initialize() failed, error code =",mt5.last_error())
    quit()
 
# display data on connection status, server name and trading account
print(mt5.terminal_info())
# display data on MetaTrader 5 version
print(mt5.version())
 
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()