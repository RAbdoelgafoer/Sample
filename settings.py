import json

"""
SettingsFile Import/Export handling

Importing/exporting test of JSON settingsfile
"""

# RFpro settingsfile name. JSON format
RFPROVERSION = "v1.0 r01"
RFPRODEFAULTSETTINGSFILE = ".RFproPE.json"
rfprosettingsfile = RFPRODEFAULTSETTINGSFILE

ctp = [  # cal table parameters of path losses
    "PwrA_Offset",
    "PwrB_Offset",
    "PwrC_Offset",
    "PwrD_Offset",
    "SA_Offset",
    "DateTime",
]

ctn = ["Amalia", "Dora"]  # cal table names

ctc = [  # cal table comments
    "10dB @Milmega 2-4GHz Output",
    "10dB @Milmega 0.8-2GHz Output",
]

ctf = [  # cal table frequencies
    {
        2110: [1, 2, 3, 2, 3, 7],
        2140: [4, 5, 6, 2, 3, 7],
        2180: [7, 8, 9, 2, 3, 7],
    },
    {
        3300: [1, 2, 3, 2, 3, 7],
        3500: [4, 5, 6, 2, 3, 7],
        3800: [7, 8, 9, 2, 3, 7],
    },
]

# building the settings file
rfproset = {  # adding settingsfile information
    "rfproversion": RFPROVERSION,
    "defaultsettingsfile": RFPRODEFAULTSETTINGSFILE,
    "settingsfiletoload": rfprosettingsfile,
}

# handling all cal tables
caltables = {}
for c, _ in enumerate(ctf):
    mydict = {}
    mydict.update({"comment": ctc[c]})
    for a in ctf[c]:
        ctf[c][a] = dict(zip(ctp, ctf[c][a]))
    mydict.update({"frequencies": ctf[c]})
    caltables.update({ctn[c]: mydict})
rfproset.update({"caltables": caltables})

# write json file
with open(rfprosettingsfile, "w") as json_file:
    json.dump(rfproset, json_file, indent=2)

# read back json file
with open(rfprosettingsfile, "r") as json_file:
    rfproset = json.load(json_file)

# print("RFpro version: ", rfproset["rfproversion"])
# print("RFpro default settings file: ", rfproset["defaultsettingsfile"])
# print("RFpro settingsfile to load: ", rfproset["settingsfiletoload"])
# print("RFpro cal tables: ", list(rfproset["caltables"]))
