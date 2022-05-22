
#%%
import matlab.engine

names = matlab.engine.find_matlab()
print(names)

eng = matlab.engine.connect_matlab(names[0])
print(eng)

#%%

def get_wsdict(_eng=None):
    if _eng is None:
        global eng
    else:
        eng = _eng
    
    d = {}
    ws_vars = eng.who()
    for ws_var_name in ws_vars:
        try:
            d[ws_var_name] = eng.workspace[ws_var_name]
            #print(ws_var_name)
        except:
            print("Error:", ws_var_name)
            d[ws_var_name] = "Error"
    return d

ws = get_wsdict()
ws_str = {}
for ws_var_name in ws:
    ws_str[ws_var_name] = str(ws[ws_var_name])

import json
with open("ws.json", "w") as f:
    json.dump(ws_str, f, indent=4)


#%%


#%%
