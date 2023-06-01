import tkinter as tk

# import ttkbootstrap as ttk
from tkinter import ttk

# from tkinter import font
# myfont = font.nametofont("TkDefaultFont")
# myfont.configure(family="Menlo", size=10)

# root RFpro window
width = 801
height = 401
window_RFproPE = tk.Tk()
window_RFproPE.title("RFproPE v1.0 rev0")
window_RFproPE.geometry(f"{width}x{height}")

# frames - Left side
frmL = ttk.Frame(window_RFproPE, width=int(width / 2) - 1)
frmL.pack(side="left", expand=True, fill="both")

frmMeas = ttk.Frame(
    frmL,
    width=int(width / 2) - 1,
    height=310,
    borderwidth=1,
    relief=tk.GROOVE,
)
frmMeas.pack(expand=True, fill="both")

frmQlog = ttk.Frame(frmL, width=int(width / 2) - 1)
frmQlog.pack(expand=True, fill="both")

frmLog = ttk.Frame(frmL, width=int(width / 2) - 1)
frmLog.pack(expand=True, fill="both")

frmInitializeMeasure = ttk.Frame(frmL, width=int(width / 2) - 1)
frmInitializeMeasure.pack(expand=True, fill="both")

# widgets
lbl1Qlog = ttk.Label(frmQlog, text="Quicklog 1", foreground="maroon", font=("Courier", 11))
lbl1Qlog.pack(expand=True, fill="both")
lbl2Qlog = ttk.Label(frmQlog, text="Quicklog 2", foreground="maroon", font=("Courier", 11))
lbl2Qlog.pack(expand=True, fill="both")

logstring = tk.StringVar(value="System log (initialized)")
cmbLog = ttk.Combobox(frmLog, textvariable=logstring, font=("Courier", 11))
cmbLog.pack(expand=True, fill="both")

btnInitialize = ttk.Button(frmInitializeMeasure, text="Initialize")
btnInitialize.pack(side="left", expand=True, fill="x", padx=2)

btnMeasure = ttk.Button(frmInitializeMeasure, text="Measure")
btnMeasure.pack(side="left", expand=True, fill="x", padx=2)

# frames - Right side
frmR = ttk.Frame(window_RFproPE, width=int(width / 2) - 1)
frmR.pack(side="right", expand=True, fill="both")

frmHeader = ttk.Frame(
    frmR,
    width=int(width / 2) - 1,
    height=150,
    borderwidth=1,
    relief=tk.GROOVE,
)
frmHeader.columnconfigure(0, weight=3, uniform="y")
frmHeader.columnconfigure((2, 4, 6), weight=1, uniform="y")
frmHeader.columnconfigure((1, 3, 5, 7), weight=3, uniform="y")
frmHeader.rowconfigure(tuple(range(4)), weight=1, uniform="y")
frmHeader.pack(expand=True, fill="both")

frmPSUfield = ttk.Frame(
    frmR, width=int(width / 2) - 1, borderwidth=1, relief=tk.GROOVE
)

frmPSUfield.columnconfigure(0, weight=3, uniform="y")
frmPSUfield.columnconfigure((2, 4, 6, 7), weight=1, uniform="y")
frmPSUfield.columnconfigure((1, 3, 5), weight=3, uniform="y")
frmPSUfield.rowconfigure(tuple(range(7)), weight=1, uniform="y")
frmPSUfield.pack(expand=True, fill="both")

frmPSUbuttons = ttk.Frame(
    frmR, width=int(width / 2) - 1, borderwidth=1, relief=tk.GROOVE
)
frmPSUbuttons.pack(expand=True, fill="both")

# frmHeader widgets
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

# frmPSUfield widgets
btnProgramPSUs = ttk.Button(frmPSUfield, text="Program all PSU's")
btnProgramPSUs.grid(row=0, column=0, columnspan=3, sticky="w")

btnAutoSwitchPSUs = ttk.Button(frmPSUfield, text="Switch PSU's on/off")
btnAutoSwitchPSUs.grid(row=0, column=3, columnspan=3, sticky="w")

btnPSUsEnable = ttk.Button(frmPSUfield, text="Toggle")
btnPSUsEnable.grid(row=0, column=6, columnspan=2)

lblPSU1 = ttk.Label(frmPSUfield, text="PSU1:", anchor="e").grid(
    row=1, column=0, sticky="ew"
)
txtPSU1V = ttk.Entry(frmPSUfield, width=5).grid(row=1, column=1, sticky="ew")
lblPSU1V = ttk.Label(frmPSUfield, text="V", anchor="w").grid(
    row=1, column=2, sticky="ew"
)
txtPSU1A = ttk.Entry(frmPSUfield, width=5).grid(row=1, column=3, sticky="ew")
lblPSU1A = ttk.Label(frmPSUfield, text="A", anchor="w").grid(
    row=1, column=4, sticky="ew"
)
btnPSU1 = ttk.Button(frmPSUfield, text="PSU1")
btnPSU1.grid(row=1, column=5, columnspan=2, padx=2)
chkPSU1var = tk.StringVar(value=0)
chkPSU1 = ttk.Checkbutton(frmPSUfield, text="", variable=chkPSU1var)
chkPSU1.grid(row=1, column=7)

lblPSU2 = ttk.Label(frmPSUfield, text="PSU2:", anchor="e").grid(
    row=2, column=0, sticky="ew"
)
txtPSU2V = ttk.Entry(frmPSUfield, width=5).grid(row=2, column=1, sticky="ew")
lblPSU2V = ttk.Label(frmPSUfield, text="V", anchor="w").grid(
    row=2, column=2, sticky="ew"
)
txtPSU2A = ttk.Entry(frmPSUfield, width=5).grid(row=2, column=3, sticky="ew")
lblPSU2A = ttk.Label(frmPSUfield, text="A", anchor="w").grid(
    row=2, column=4, sticky="ew"
)
btnPSU2 = ttk.Button(frmPSUfield, text="PSU2")
btnPSU2.grid(row=2, column=5, columnspan=2, padx=2)
chkPSU2var = tk.StringVar(value=0)
chkPSU2 = ttk.Checkbutton(frmPSUfield, text="", variable=chkPSU2var)
chkPSU2.grid(row=2, column=7)

lblPSU3 = ttk.Label(frmPSUfield, text="PSU3:", anchor="e").grid(
    row=3, column=0, sticky="ew"
)
txtPSU3V = ttk.Entry(frmPSUfield, width=5).grid(row=3, column=1, sticky="ew")
lblPSU3V = ttk.Label(frmPSUfield, text="V", anchor="w").grid(
    row=3, column=2, sticky="ew"
)
txtPSU3A = ttk.Entry(frmPSUfield, width=5).grid(row=3, column=3, sticky="ew")
lblPSU3A = ttk.Label(frmPSUfield, text="A", anchor="w").grid(
    row=3, column=4, sticky="ew"
)
btnPSU3 = ttk.Button(frmPSUfield, text="PSU3")
btnPSU3.grid(row=3, column=5, columnspan=2, padx=2)
chkPSU3var = tk.StringVar(value=0)
chkPSU3 = ttk.Checkbutton(frmPSUfield, text="", variable=chkPSU3var)
chkPSU3.grid(row=3, column=7)

lblPSU4 = ttk.Label(frmPSUfield, text="PSU4:", anchor="e").grid(
    row=4, column=0, sticky="ew"
)
txtPSU4V = ttk.Entry(frmPSUfield, width=5).grid(row=4, column=1, sticky="ew")
lblPSU4V = ttk.Label(frmPSUfield, text="V", anchor="w").grid(
    row=4, column=2, sticky="ew"
)
txtPSU4A = ttk.Entry(frmPSUfield, width=5).grid(row=4, column=3, sticky="ew")
lblPSU4A = ttk.Label(frmPSUfield, text="A", anchor="w").grid(
    row=4, column=4, sticky="ew"
)
btnPSU4 = ttk.Button(frmPSUfield, text="PSU4")
btnPSU4.grid(row=4, column=5, columnspan=2, padx=2)
chkPSU4var = tk.StringVar(value=0)
chkPSU4 = ttk.Checkbutton(frmPSUfield, text="", variable=chkPSU4var)
chkPSU4.grid(row=4, column=7)

lblPSU5 = ttk.Label(frmPSUfield, text="PSU5:", anchor="e").grid(
    row=5, column=0, sticky="ew"
)
txtPSU5V = ttk.Entry(frmPSUfield, width=5).grid(row=5, column=1, sticky="ew")
lblPSU5V = ttk.Label(frmPSUfield, text="V", anchor="w").grid(
    row=5, column=2, sticky="ew"
)
txtPSU5A = ttk.Entry(frmPSUfield, width=5).grid(row=5, column=3, sticky="ew")
lblPSU5A = ttk.Label(frmPSUfield, text="A", anchor="w").grid(
    row=5, column=4, sticky="ew"
)
btnPSU5 = ttk.Button(frmPSUfield, text="PSU5")
btnPSU5.grid(row=5, column=5, columnspan=2, padx=2)
chkPSU5var = tk.StringVar(value=0)
chkPSU5 = ttk.Checkbutton(frmPSUfield, text="", variable=chkPSU5var)
chkPSU5.grid(row=5, column=7)

lblPSU6 = ttk.Label(frmPSUfield, text="PSU6:", anchor="e").grid(
    row=6, column=0, sticky="ew"
)
txtPSU6V = ttk.Entry(frmPSUfield, width=5).grid(row=6, column=1, sticky="ew")
lblPSU6V = ttk.Label(frmPSUfield, text="V", anchor="w").grid(
    row=6, column=2, sticky="ew"
)
txtPSU6A = ttk.Entry(frmPSUfield, width=5).grid(row=6, column=3, sticky="ew")
lblPSU6A = ttk.Label(frmPSUfield, text="A", anchor="w").grid(
    row=6, column=4, sticky="ew"
)
btnPSU6 = ttk.Button(frmPSUfield, text="PSU6")
btnPSU6.grid(row=6, column=5, columnspan=2, padx=2)
chkPSU6var = tk.StringVar(value=0)
chkPSU6 = ttk.Checkbutton(frmPSUfield, text="", variable=chkPSU6var)
chkPSU6.grid(row=6, column=7)

lblPSUX = ttk.Label(frmPSUfield, text="PSUX:", anchor="e").grid(
    row=7, column=0, sticky="ew"
)
txtPSUXV = ttk.Entry(frmPSUfield, width=5).grid(row=7, column=1, sticky="ew")
lblPSUXV = ttk.Label(frmPSUfield, text="V", anchor="w").grid(
    row=7, column=2, sticky="ew"
)
txtPSUXA = ttk.Entry(frmPSUfield, width=5).grid(row=7, column=3, sticky="ew")
lblPSUXA = ttk.Label(frmPSUfield, text="A", anchor="w").grid(
    row=7, column=4, sticky="ew"
)
btnPSUX = ttk.Button(frmPSUfield, text="PSUX")
btnPSUX.grid(row=7, column=5, columnspan=2, padx=2)
chkPSUXvar = tk.StringVar(value=0)
chkPSUX = ttk.Checkbutton(frmPSUfield, text="", variable=chkPSUXvar)
chkPSUX.grid(row=7, column=7)


# bindings
window_RFproPE.bind("<Escape>", lambda event: window_RFproPE.quit())

if __name__ == "__main__":
    window_RFproPE.mainloop()
