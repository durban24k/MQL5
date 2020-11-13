import MetaTrader5 as mt5
import pandas as pd
from config import login_info

path=login_info["path"]
login=login_info["login"]    
server=login_info["server"]
password=login_info["password"]

if not mt5.initialize(path,login=login,server=server,password=password):
     print(f'Initialized failed, error code = {mt5.last_error()}')
     quit()

# Code for the function to happen/ Strategy or function call

# attempt to enable the display of the EURCAD in MarketWatch
selected=mt5.symbol_select("EURCAD.r",True)
if not selected:
    print("Failed to select EURCAD.r, error code =",mt5.last_error())
else:
    symbol_info=mt5.symbol_info("EURCAD.r")
    print(symbol_info)
    print("EURCAD: currency_base =",symbol_info.currency_base,"  currency_profit =",symbol_info.currency_profit,"  currency_margin =",symbol_info.currency_margin)
    print()
 
    # get symbol properties in the form of a dictionary
    print("Show symbol_info()._asdict():")
    symbol_info_dict = symbol_info._asdict()
    for prop in symbol_info_dict:
        print("  {}={}".format(prop, symbol_info_dict[prop]))
    print()
 
    # convert the dictionary into DataFrame and print
    df=pd.DataFrame(list(symbol_info_dict.items()),columns=['property','value'])
    print("symbol_info_dict() as dataframe:")
    print(df)

# Terminating the connection with the MetaTrader 5 terminal
mt5.shutdown()