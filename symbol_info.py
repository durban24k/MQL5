import MetaTrader5 as mt5
from config import login_info

path=login_info["path"]
login=login_info["login"]    
server=login_info["server"]
password=login_info["password"]

if not mt5.initialize(path,login=login,server=server,password=password):
     print(f'Initialized failed, error code = {mt5.last_error()}')
     quit()

