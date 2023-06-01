import tkinter as tk

# from platform import system
# import ttkbootstrap as ttk

from tkinter import ttk

# def mylabel(master, size, x, y, h, w, *args, **kwargs):
#     pass


def add_to_log(string):
    pass


# platformD = system()
# print(platformD)
# if platformD == 'Darwin':
#     logo_image = 'images/logo.icns'
# elif platformD == 'Windows':
#     logo_image = 'images/logo.ico'
# else:
#     logo_image = 'images/logo.xbm'

# from tkinter import font
# myfont = font.nametofont("TkDefaultFont")
# myfont.configure(family="Menlo", size=10)

# root RFpro window
window_RFproPE = tk.Tk()
window_RFproPE.title("RFproPE v1.0 rev0")

display_width = window_RFproPE.winfo_screenwidth()
display_height = window_RFproPE.winfo_screenheight()
width = 808
height = 412
txtwidth = 54
# window_RFproPE.iconbitmap("galliumsemi.ico")
window_RFproPE.geometry(f"{width}x{height}+100+100")
# window_RFproPE.minsize(width, height)
# window_RFproPE.maxsize(width, height)
window_RFproPE.resizable(False, False)

# window attributes
# window_RFproPE.attributes("-alpha", 0.9)  # transparancy
# window_RFproPE.attributes("-topmost", True)  # always on top
# window_RFproPE.attributes("-disable", True) # disable interaction with window. only Esc binding will work
# window_RFproPE.attributes("-fullscreen", True) # doesn't work with max sizes
# window_RFproPE.overrideredirect() # disable titlebar in MSwindows
# grip = ttk.Sizegrip(window_RFproPE)
# grip.pack()
# grip.place(relx=1, rely=1, anchor="se")


# MAIN FRAMES ==================
# main frame layout into Left, Right and Bottom side frames
widthLR = int(width / 2) - 2
bheight = 28
frmB = ttk.Frame(window_RFproPE, height=bheight)
frmB.pack(side="bottom", expand=True, fill="x")

frmL = ttk.Frame(window_RFproPE, width=widthLR, height=height - bheight)
frmL.pack(side="left", expand=True, fill="x")

frmR = ttk.Frame(window_RFproPE, width=widthLR, height=height - bheight)
frmR.pack(side="right", expand=True, fill="x")

# SUB FRAMES ==================
# Bottom frame layout division
frmButtonbar = ttk.Frame(
    frmB,
    width=width,
    height=bheight - 2,
    # borderwidth=1,
    # relief=tk.SUNKEN,
)
frmButtonbar.pack(side="top", expand=True, fill="x")

# Left frame layout division
frmMeas = ttk.Frame(
    frmL,
    width=widthLR,
    height=310,
    # borderwidth=1,
    # relief=tk.SUNKEN,
)
frmMeas.pack()  # expand=True, fill="x")

frmQlog = ttk.Frame(
    # frmL, width=widthLR, height=34, borderwidth=1, relief=tk.SUNKEN
    frmL,
    width=widthLR,
    height=34,
)
frmQlog.pack(expand=True, fill="x")

frmLog = ttk.Frame(frmL, width=widthLR, height=28)
frmLog.pack(expand=True, fill="x")


currentvar = tk.StringVar(value="System log (initialized)")
cmbLog = ttk.Combobox(
    frmLog, textvariable=currentvar, font=("Courier", 11), width=txtwidth
)
cmbLog.place(x=1, y=1)
logitems = list(cmbLog["values"])
logitems.append("test log 1")
cmbLog["values"] = logitems

# Right frame layout division
# frmHeader = ttk.Frame(frmR, width=widthLR, borderwidth=1, relief=tk.SUNKEN)
frmHeader = ttk.Frame(frmR, width=widthLR)
frmHeader.columnconfigure(0, weight=3, uniform="y")
frmHeader.columnconfigure((2, 4, 6), weight=1, uniform="y")
frmHeader.columnconfigure((1, 3, 5, 7), weight=3, uniform="y")
frmHeader.rowconfigure(tuple(range(4)), weight=1, uniform="y")
frmHeader.pack(side="top", expand=True, fill="both")

frmPSUbtns = ttk.Frame(frmR, width=widthLR)
frmPSUbtns.pack(expand=True, fill="both")

frmPSUfield = ttk.Frame(frmR, width=widthLR)
frmPSUfield.columnconfigure(0, weight=3, uniform="y")
frmPSUfield.columnconfigure((2, 4, 6, 7), weight=1, uniform="y")
frmPSUfield.columnconfigure((1, 3, 5), weight=3, uniform="y")
frmPSUfield.rowconfigure(tuple(range(7)), weight=1, uniform="y")
frmPSUfield.pack(side="top", expand=True, fill="x")

frmAnnunciators = ttk.Frame(
    frmR,
    width=widthLR,
    borderwidth=2,
    relief=tk.GROOVE,
)
frmAnnunciators.columnconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="y")
frmAnnunciators.rowconfigure((0, 1), weight=1, uniform="y")
frmAnnunciators.pack(side="top", expand=True, fill="x")

# WIDGETS ==================
# Bottom side widgets
btnInitialize = ttk.Button(frmButtonbar, text="Initialize")
btnInitialize.pack(side="left")

btnMeasure = ttk.Button(frmButtonbar, text="Measure")
btnMeasure.pack(side="left")

# Left side widgets
# notebook(tab) widget
notebook = ttk.Notebook(frmMeas)

tabSPAR = ttk.Frame(notebook)
notebook.add(tabSPAR, text="Spar")

tabAMxM = ttk.Frame(notebook)
tabAMxMlabel1 = ttk.Label(tabAMxM, text="VNA start").pack(side="left")
tabAMxMpstart = ttk.Entry(tabAMxM).pack(side="left")
tabAMxMlabel2 = ttk.Label(tabAMxM, text="[dBm]").pack(side="left")
notebook.add(tabAMxM, text="AMxM")

tabPCW = ttk.Frame(notebook)
notebook.add(tabPCW, text="PCW")

tabVBW = ttk.Frame(notebook)
notebook.add(tabVBW, text="VBW")

notebook.pack(expand=True)

# quicklog widgets
lbl1Qlog = ttk.Label(
    frmQlog,
    text="Quicklog 1",
    foreground="maroon",
    font=("Courier", 11),
    width=txtwidth,
)
lbl1Qlog.place(x=1, y=1)
lbl2Qlog = ttk.Label(
    frmQlog,
    text="Quicklog 2",
    foreground="maroon",
    font=("Courier", 11),
    width=txtwidth,
)

# main log widget
lbl2Qlog.place(x=1, y=14)

# Right side frmHeader widgets
lblComment = ttk.Label(frmHeader, text="Note:", anchor="e").grid(
    row=0, column=0, sticky="ew"
)
txtComment = ttk.Entry(frmHeader, width=5).grid(
    row=0, column=1, columnspan=4, sticky="ew"
)
lblVd = ttk.Label(frmHeader, text="Vd[V]:", anchor="e").grid(
    row=0, column=5, columnspan=2, sticky="ew"
)
txtVd = ttk.Entry(frmHeader, width=5).grid(row=0, column=7, sticky="ew")
lblDevice = ttk.Label(frmHeader, text="Device:", anchor="e").grid(
    row=1, column=0, sticky="ew"
)
txtDevice = ttk.Entry(frmHeader).grid(
    row=1, column=1, columnspan=4, sticky="ew"
)
lblPwr_dBm = ttk.Label(frmHeader, text="@Pwr[dBm]:", anchor="e").grid(
    row=1, column=5, columnspan=2, sticky="ew"
)
txtPwr_dBm = ttk.Entry(frmHeader, width=5).grid(row=1, column=7, sticky="ew")

lblVgs1 = ttk.Label(frmHeader, text="Vgs[V].. 1:", anchor="e").grid(
    row=2, column=0, sticky="ew"
)
txtVgs1 = ttk.Entry(frmHeader, width=5).grid(row=2, column=1, sticky="ew")
lblVgs2 = ttk.Label(frmHeader, text="2:", anchor="e").grid(
    row=2, column=2, sticky="ew"
)
txtVgs2 = ttk.Entry(frmHeader, width=5).grid(row=2, column=3, sticky="ew")
lblVgs3 = ttk.Label(frmHeader, text="3:", anchor="e").grid(
    row=2, column=4, sticky="ew"
)
txtVgs3 = ttk.Entry(frmHeader, width=5).grid(row=2, column=5, sticky="ew")
lblVgs4 = ttk.Label(frmHeader, text="4:", anchor="e").grid(
    row=2, column=6, sticky="ew"
)
txtVgs4 = ttk.Entry(frmHeader, width=5).grid(row=2, column=7, sticky="ew")

lblIgs1 = ttk.Label(frmHeader, text="Igs[A].. 1:", anchor="e").grid(
    row=3, column=0, sticky="ew"
)
txtIgs1 = ttk.Entry(frmHeader, width=5).grid(row=3, column=1, sticky="ew")
lblIgs2 = ttk.Label(frmHeader, text="2:", anchor="e").grid(
    row=3, column=2, sticky="ew"
)
txtIgs2 = ttk.Entry(frmHeader, width=5).grid(row=3, column=3, sticky="ew")
lblIgs3 = ttk.Label(frmHeader, text="3:", anchor="e").grid(
    row=3, column=4, sticky="ew"
)
txtIgs3 = ttk.Entry(frmHeader, width=5).grid(row=3, column=5, sticky="ew")
lblIgs4 = ttk.Label(frmHeader, text="4:", anchor="e").grid(
    row=3, column=6, sticky="ew"
)
txtIgs4 = ttk.Entry(frmHeader, width=5).grid(row=3, column=7, sticky="ew")

# Right side frmPSUBtns widgets
btnProgramPSUs = ttk.Button(frmPSUbtns, text="Program all PSU's")
btnProgramPSUs.pack(side="left", expand=True, fill="x")

btnAutoSwitchPSUs = ttk.Button(frmPSUbtns, text="Switch enabled PSU's")
btnAutoSwitchPSUs.pack(side="left")  # , expand=True, fill="x")

chkPSUsEnTgl = ttk.Button(frmPSUbtns, text="tgl")
chkPSUsEnTgl.pack(side="left", expand=True, fill="x")

# Right side frmPSUfield widgets
lblPSU1 = ttk.Label(frmPSUfield, text="PSU1:", anchor="e").grid(
    row=0, column=0, sticky="ew"
)
txtPSU1V = ttk.Entry(frmPSUfield, width=5).grid(row=0, column=1, sticky="ew")
lblPSU1V = ttk.Label(frmPSUfield, text="V", anchor="w").grid(
    row=0, column=2, sticky="ew"
)
txtPSU1A = ttk.Entry(frmPSUfield, width=5).grid(row=0, column=3, sticky="ew")
lblPSU1A = ttk.Label(frmPSUfield, text="A", anchor="w").grid(
    row=0, column=4, sticky="ew"
)
btnPSU1 = ttk.Button(frmPSUfield, text="PSU1")
btnPSU1.grid(row=0, column=5, columnspan=2, padx=2)
chkPSU1var = tk.StringVar(value=0)
chkPSU1 = ttk.Checkbutton(frmPSUfield, text="", variable=chkPSU1var)
chkPSU1.grid(row=0, column=7)

lblPSU2 = ttk.Label(frmPSUfield, text="PSU2:", anchor="e").grid(
    row=1, column=0, sticky="ew"
)
txtPSU2V = ttk.Entry(frmPSUfield, width=5).grid(row=1, column=1, sticky="ew")
lblPSU2V = ttk.Label(frmPSUfield, text="V", anchor="w").grid(
    row=1, column=2, sticky="ew"
)
txtPSU2A = ttk.Entry(frmPSUfield, width=5).grid(row=1, column=3, sticky="ew")
lblPSU2A = ttk.Label(frmPSUfield, text="A", anchor="w").grid(
    row=1, column=4, sticky="ew"
)
btnPSU2 = ttk.Button(frmPSUfield, text="PSU2")
btnPSU2.grid(row=1, column=5, columnspan=2, padx=2)
chkPSU2var = tk.StringVar(value=0)
chkPSU2 = ttk.Checkbutton(frmPSUfield, text="", variable=chkPSU2var)
chkPSU2.grid(row=1, column=7)

lblPSU3 = ttk.Label(frmPSUfield, text="PSU3:", anchor="e").grid(
    row=2, column=0, sticky="ew"
)
txtPSU3V = ttk.Entry(frmPSUfield, width=5).grid(row=2, column=1, sticky="ew")
lblPSU3V = ttk.Label(frmPSUfield, text="V", anchor="w").grid(
    row=2, column=2, sticky="ew"
)
txtPSU3A = ttk.Entry(frmPSUfield, width=5).grid(row=2, column=3, sticky="ew")
lblPSU3A = ttk.Label(frmPSUfield, text="A", anchor="w").grid(
    row=2, column=4, sticky="ew"
)
btnPSU3 = ttk.Button(frmPSUfield, text="PSU3")
btnPSU3.grid(row=2, column=5, columnspan=2, padx=2)
chkPSU3var = tk.StringVar(value=0)
chkPSU3 = ttk.Checkbutton(frmPSUfield, text="", variable=chkPSU3var)
chkPSU3.grid(row=2, column=7)

lblPSU4 = ttk.Label(frmPSUfield, text="PSU4:", anchor="e").grid(
    row=3, column=0, sticky="ew"
)
txtPSU4V = ttk.Entry(frmPSUfield, width=5).grid(row=3, column=1, sticky="ew")
lblPSU4V = ttk.Label(frmPSUfield, text="V", anchor="w").grid(
    row=3, column=2, sticky="ew"
)
txtPSU4A = ttk.Entry(frmPSUfield, width=5).grid(row=3, column=3, sticky="ew")
lblPSU4A = ttk.Label(frmPSUfield, text="A", anchor="w").grid(
    row=3, column=4, sticky="ew"
)
btnPSU4 = ttk.Button(frmPSUfield, text="PSU4")
btnPSU4.grid(row=3, column=5, columnspan=2, padx=2)
chkPSU4var = tk.StringVar(value=0)
chkPSU4 = ttk.Checkbutton(frmPSUfield, text="", variable=chkPSU4var)
chkPSU4.grid(row=3, column=7)

lblPSU5 = ttk.Label(frmPSUfield, text="PSU5:", anchor="e").grid(
    row=4, column=0, sticky="ew"
)
txtPSU5V = ttk.Entry(frmPSUfield, width=5).grid(row=4, column=1, sticky="ew")
lblPSU5V = ttk.Label(frmPSUfield, text="V", anchor="w").grid(
    row=4, column=2, sticky="ew"
)
txtPSU5A = ttk.Entry(frmPSUfield, width=5).grid(row=4, column=3, sticky="ew")
lblPSU5A = ttk.Label(frmPSUfield, text="A", anchor="w").grid(
    row=4, column=4, sticky="ew"
)
btnPSU5 = ttk.Button(frmPSUfield, text="PSU5")
btnPSU5.grid(row=4, column=5, columnspan=2, padx=2)
chkPSU5var = tk.StringVar(value=0)
chkPSU5 = ttk.Checkbutton(frmPSUfield, text="", variable=chkPSU5var)
chkPSU5.grid(row=4, column=7)

lblPSU6 = ttk.Label(frmPSUfield, text="PSU6:", anchor="e").grid(
    row=5, column=0, sticky="ew"
)
txtPSU6V = ttk.Entry(frmPSUfield, width=5).grid(row=5, column=1, sticky="ew")
lblPSU6V = ttk.Label(frmPSUfield, text="V", anchor="w").grid(
    row=5, column=2, sticky="ew"
)
txtPSU6A = ttk.Entry(frmPSUfield, width=5).grid(row=5, column=3, sticky="ew")
lblPSU6A = ttk.Label(frmPSUfield, text="A", anchor="w").grid(
    row=5, column=4, sticky="ew"
)
btnPSU6 = ttk.Button(frmPSUfield, text="PSU6")
btnPSU6.grid(row=5, column=5, columnspan=2, padx=2)
chkPSU6var = tk.StringVar(value=0)
chkPSU6 = ttk.Checkbutton(frmPSUfield, text="", variable=chkPSU6var)
chkPSU6.grid(row=5, column=7)

lblPSUX = ttk.Label(frmPSUfield, text="PSUX:", anchor="e").grid(
    row=6, column=0, sticky="ew"
)
txtPSUXV = ttk.Entry(frmPSUfield, width=5).grid(row=6, column=1, sticky="ew")
lblPSUXV = ttk.Label(frmPSUfield, text="V", anchor="w").grid(
    row=6, column=2, sticky="ew"
)
txtPSUXA = ttk.Entry(frmPSUfield, width=5).grid(row=6, column=3, sticky="ew")
lblPSUXA = ttk.Label(frmPSUfield, text="A", anchor="w").grid(
    row=6, column=4, sticky="ew"
)
btnPSUX = ttk.Button(frmPSUfield, text="PSUX")
btnPSUX.grid(row=6, column=5, columnspan=2, padx=2)
chkPSUXvar = tk.StringVar(value=0)
chkPSUX = ttk.Checkbutton(frmPSUfield, text="", variable=chkPSUXvar)
chkPSUX.grid(row=6, column=7)


# Right side frmAnnunciators widgets
# -----------------------------------------------------------------------------
def toggle_chkPstartLvl():
    global chkPstartLvlVar
    if chkPstartLvlVar:
        chkPstartLvlVar = False
        chkPstartLvl["foreground"] = "gray"
        chkPstartLvl["background"] = "lightgray"
    else:
        chkPstartLvlVar = True
        chkPstartLvl["foreground"] = "black"
        chkPstartLvl["background"] = "lightgreen"


chkPstartLvlVar = tk.BooleanVar(value=False)
chkPstartLvl = tk.Checkbutton(
    frmAnnunciators,
    indicatoron=0,
    text="PstartLvl",
    font=("Arial", 11),
    variable=chkPstartLvlVar,
    command=lambda: toggle_chkPstartLvl(),
    borderwidth=2,
    justify="center",
)
chkPstartLvl.grid(row=0, column=0, ipadx=2, ipady=1, sticky="nsew")
toggle_chkPstartLvl()
# -----------------------------------------------------------------------------


def toggle_chkSingleFreq():
    global chkSingleFreqVar
    if chkSingleFreqVar:
        chkSingleFreqVar = False
        chkSingleFreq["foreground"] = "gray"
        chkSingleFreq["background"] = "lightgray"
    else:
        chkSingleFreqVar = True
        chkSingleFreq["foreground"] = "black"
        chkSingleFreq["background"] = "lightgreen"


chkSingleFreqVar = tk.BooleanVar(value=False)
chkSingleFreq = tk.Checkbutton(
    frmAnnunciators,
    indicatoron=0,
    text="1-Freq",
    font=("Arial", 11),
    variable=chkSingleFreqVar,
    command=lambda: toggle_chkSingleFreq(),
    borderwidth=2,
    justify="center",
)
chkSingleFreq.grid(row=0, column=1, ipadx=2, ipady=1, sticky="nsew")
toggle_chkSingleFreq()
# -----------------------------------------------------------------------------

# BINDINGS
window_RFproPE.bind("<Escape>", lambda event: window_RFproPE.quit())
cmbLog.bind("<Button>", lambda event: print("Selected"))  # on mouseclick

# MENUS
mainmenu = tk.Menu(window_RFproPE)
window_RFproPE.configure(menu=mainmenu)

settingsmenu = tk.Menu(mainmenu, tearoff=False)
mainmenu.add_cascade(label="Settings", menu=settingsmenu)
settingsmenu.add_command(label="Export", command=lambda: print("Exported"))
settingsmenu.add_command(
    label="Export as", command=lambda: print("Exported as...")
)
settingsmenu.add_command(label="Import", command=lambda: print("Imported"))
settingsmenu.add_separator()
settingsmenu_autosave = tk.StringVar(value="on")
settingsmenu.add_checkbutton(
    label="Autosave",
    onvalue="on",
    offvalue="off",
    variable=settingsmenu_autosave,
)

calibration_menu = tk.Menu(mainmenu, tearoff=False)
mainmenu.add_cascade(label="Cal", menu=calibration_menu)
calibration_menu.add_command(
    label="Freq list", command=lambda: print("Opened freq list")
)
calibration_menu.add_command(
    label="Cal settings", command=lambda: print("Opened cal settings")
)
calibration_menu.add_command(
    label="Calibrate", command=lambda: print("Opened cal wizard")
)

helpmenu = tk.Menu(mainmenu, tearoff=False)
mainmenu.add_cascade(label="Help", menu=helpmenu)

if __name__ == "__main__":
    window_RFproPE.mainloop()
