import MetaTrader5 as mt5 
from config import login_info

# Initialize variables
path=login_info["path"]
login=login_info["login"]    
server=login_info["server"]
password=login_info["password"]

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize(path,login=login,server=server,password=password):
    print("initialize() failed, error code =",mt5.last_error())
    quit()
 
# get all symbols
symbols=mt5.symbols_get()
print('Symbols: ', len(symbols))
count=0
# display the first five ones
for s in symbols:
    count+=1
    print("{}. {}".format(count,s.name))
    if count==5: break
print()
 
# get symbols containing RU in their names
ru_symbols=mt5.symbols_get("*RU*")
print('len(*RU*): ', len(ru_symbols))
for s in ru_symbols:
    print(s.name)
print()
 
# get symbols whose names do not contain USD, EUR, JPY and GBP
group_symbols=mt5.symbols_get(group="*,!*USD*,!*EUR*,!*JPY*,!*GBP*")
print('len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):', len(group_symbols))
for s in group_symbols:
    print(s.name,":",s)
 
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()