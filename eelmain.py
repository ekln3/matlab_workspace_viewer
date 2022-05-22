
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
            d[ws_var_name] = "<<Error getting value>>"
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




import eel

# loading files
import json
with open("ws.json", "r") as f:
    ws_str = json.load(f)

# in js functions
@eel.expose
def echo_in_python(msg):
    print(msg)

@eel.expose
def openvar(varname):
    eng.openvar(varname, nargout=0)


# eel init
eel.init("web")

eel.echo_in_js(ws_str)

eel.refresh_ws(ws_str)

# def refresh():
#     eel.refresh_ws(ws_str)
#     eel.sleep(0.5)
# print("spawn")
# eel.spawn(refresh)

# eel start
print("eel start")
eel.start("main.html")

