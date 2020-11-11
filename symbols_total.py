# In this we shall have a script that gets all the financial symbols in MT5 terminal
import MetaTrader5 as mt5
from config import login_info

path=login_info["path"]
login=login_info["login"]    
server=login_info["server"]
password=login_info["password"]

if not mt5.initialize(path,login=login,server=server,password=password):
     print(f'Initialized failed, error code = {mt5.last_error()}')
     quit()

symbols=mt5.symbols_total()
if symbols>0:
     print(f'Total Symbols = {symbols}')
else:
     print(f'Symbols not found')

mt5.shutdown()