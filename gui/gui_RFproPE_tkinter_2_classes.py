import tkinter as tk

# import ttkbootstrap as ttk

from tkinter import ttk
from tkinter import font
from tkinter import messagebox as mbx

myfont = ("Arial", 22)
# style = ttk.Style()
# print(style.theme_names())
# style.theme_use("classic")
# style.configure("new.TLabel", foreground="orange", font=myfont)
# style.map("new.TButton", foreground=[("pressed", "red"),("disabled", "yellow")])
# style.configure("TButton", padx=5, pady=5, foreground="#00F")
# style.configure("TLabel", foreground="blue")


class Equipment(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Equipment")
        self.geometry("500x250")
        ttk.Button(self, text="button").pack()
        ttk.Label(self, text="label1").pack()
        ttk.Label(self, text="label2").pack(expand=True)
        self.bind("<Escape>", lambda event: self.destroy())


class Root(tk.Tk):
    def __init__(self, title, size):
        # main setup
        width = size[0]
        height = size[1]

        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.change_titlebar_color()
        # self.minsize(size[0], size[1])
        # self.resizable(False, False)
        # self.tk.call("source", "gui/Azure/azure.tcl")
        # self.tk.call("set_theme", "light")

        # bottom frame -------------------------------------------------------
        bheight = 24
        self.bFrame = self.createFrame(self, width, bheight)
        self.bFrame.pack(side="bottom", fill="x")

        # widgets
        self.btnInitialize = self.createButton(self.bFrame, "Initialize")
        self.btnInitialize.pack(side="left", padx=1, pady=1)
        self.btnMeasure = self.createButton(self.bFrame, "Measure")
        self.btnMeasure.pack(side="left", padx=1, pady=1)

        def ask_yes_no():
            answer = mbx.askquestion("Title", "Yes or no?")
            print(answer)
            # mbx.showerror("Some error", "Here is some error")

        def create_window():
            global extra_window
            extra_window = Equipment()

        def close_window():
            extra_window.destroy()

        self.btnTest = self.createButton(self.bFrame, "Test")
        self.btnTest.configure(command=create_window)
        self.btnTest.pack(side="left", padx=2, pady=2)
        self.btnCloseTest = self.createButton(self.bFrame, "CloseTest")
        self.btnCloseTest.configure(command=close_window)
        self.btnCloseTest.pack(side="left", padx=2, pady=2)
        self.btnMessagebox = self.createButton(self.bFrame, "Messagebox")
        self.btnMessagebox.configure(command=ask_yes_no)
        self.btnMessagebox.pack(side="left", padx=2, pady=2)

        # left frame ---------------------------------------------------------
        widthLR = int(width / 2) - 0
        self.lFrame = self.createFrame(self, widthLR, height - bheight - 4)
        self.lFrame.pack(side="left", expand=True, fill="both")

        # Spar widgets
        self.notebook = ttk.Notebook(self.lFrame)
        self.notebook.pack()  # expand=True)

        self.tabSPAR = ttk.Frame(self.notebook)
        self.tabSPAR.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.tabSPAR.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")
        self.notebook.add(self.tabSPAR, text="Spar")
        self.Spar_lblPsrc = ttk.Label(
            self.tabSPAR, text="VNA Psource", foreground="#A50"
        ).grid(row=0, column=1, sticky="e")
        self.Spar_txtPsrc = ttk.Entry(self.tabSPAR, width=5).grid(
            row=0, column=2, sticky="ew"
        )
        self.Spar_lblPsrc_dBm = ttk.Label(self.tabSPAR, text="dBm").grid(
            row=0, column=3, sticky="w"
        )
        self.Spar_lblFstart = ttk.Label(self.tabSPAR, text="VNA Fstart").grid(
            row=1, column=1, sticky="e"
        )
        self.Spar_txtFstart = ttk.Entry(self.tabSPAR, width=5).grid(
            row=1, column=2, sticky="ew"
        )
        self.Spar_lblFstart_MHz = ttk.Label(self.tabSPAR, text="MHz").grid(
            row=1, column=3, sticky="w"
        )
        self.Spar_lblFstop = ttk.Label(self.tabSPAR, text="VNA Fstop").grid(
            row=2, column=1, sticky="e"
        )
        self.Spar_txtFstop = ttk.Entry(self.tabSPAR, width=5).grid(
            row=2, column=2, sticky="ew"
        )
        self.SparlblFstop_MHz = ttk.Label(self.tabSPAR, text="MHz").grid(
            row=2, column=3, sticky="w"
        )

        # AMxM widgets
        self.tabAMxM = ttk.Frame(self.notebook)
        ttk.Label(self.tabAMxM, text="VNA start").pack(side="left")
        ttk.Entry(self.tabAMxM).pack(side="left")
        ttk.Label(self.tabAMxM, text="[dBm]").pack(side="left")
        self.notebook.add(self.tabAMxM, text="AMxM")

        self.tabPCW = ttk.Frame(self.notebook)
        self.notebook.add(self.tabPCW, text="PCW")

        self.tabVBW = ttk.Frame(self.notebook)
        self.notebook.add(self.tabVBW, text="VBW")

        # right frame --------------------------------------------------------
        self.rFrame = self.createFrame(self, widthLR, height - bheight - 4)
        self.rFrame.pack(side="right", expand=True, fill="both")

        self.frmHeader = ttk.Frame(self.rFrame, width=widthLR)
        self.frmHeader.columnconfigure(0, weight=3, uniform="y")
        self.frmHeader.columnconfigure((2, 4, 6), weight=1, uniform="y")
        self.frmHeader.columnconfigure((1, 3, 5, 7), weight=3, uniform="y")
        self.frmHeader.rowconfigure(tuple(range(4)), weight=1, uniform="y")
        self.frmHeader.pack(side="top", expand=True, fill="both")

        self.frmPSUbtns = ttk.Frame(self.rFrame, width=widthLR)
        self.frmPSUbtns.pack(expand=True, fill="both")

        self.frmPSUfield = ttk.Frame(self.rFrame, width=widthLR)
        self.frmPSUfield.columnconfigure(0, weight=3, uniform="y")
        self.frmPSUfield.columnconfigure((2, 4, 6, 7), weight=1, uniform="y")
        self.frmPSUfield.columnconfigure((1, 3, 5), weight=3, uniform="y")
        self.frmPSUfield.rowconfigure(tuple(range(7)), weight=1, uniform="y")
        self.frmPSUfield.pack(side="top", expand=True, fill="x")

        self.frmAnnunciators = ttk.Frame(
            self.rFrame,
            width=widthLR,
            borderwidth=2,
            relief=tk.GROOVE,
        )
        self.frmAnnunciators.columnconfigure(
            (0, 1, 2, 3, 4, 5), weight=1, uniform="y"
        )
        self.frmAnnunciators.rowconfigure((0, 1), weight=1, uniform="y")
        self.frmAnnunciators.pack(side="top", expand=True, fill="x")

        # right frame header widgets
        self.lblComment = ttk.Label(
            self.frmHeader, text="Note:", anchor="e"
        ).grid(row=0, column=0, sticky="ew")
        self.txtComment = ttk.Entry(self.frmHeader, width=5).grid(
            row=0, column=1, columnspan=4, sticky="ew"
        )
        self.lblVd = ttk.Label(self.frmHeader, text="Vd[V]:", anchor="e").grid(
            row=0, column=5, columnspan=2, sticky="ew"
        )
        self.txtVd = ttk.Entry(self.frmHeader, width=5).grid(
            row=0, column=7, sticky="ew"
        )
        self.lblDevice = ttk.Label(
            self.frmHeader, text="Device:", anchor="e"
        ).grid(row=1, column=0, sticky="ew")
        self.txtDevice = ttk.Entry(self.frmHeader).grid(
            row=1, column=1, columnspan=4, sticky="ew"
        )
        self.lblPwr_dBm = ttk.Label(
            self.frmHeader, text="@Pwr[dBm]:", anchor="e"
        ).grid(row=1, column=5, columnspan=2, sticky="ew")
        self.txtPwr_dBm = ttk.Entry(self.frmHeader, width=5).grid(
            row=1, column=7, sticky="ew"
        )

        self.lblVgs1 = ttk.Label(
            self.frmHeader, text="Vgs[V].. 1:", anchor="e"
        ).grid(row=2, column=0, sticky="ew")
        self.txtVgs1 = ttk.Entry(self.frmHeader, width=5).grid(
            row=2, column=1, sticky="ew"
        )
        self.lblVgs2 = ttk.Label(self.frmHeader, text="2:", anchor="e").grid(
            row=2, column=2, sticky="ew"
        )
        self.txtVgs2 = ttk.Entry(self.frmHeader, width=5).grid(
            row=2, column=3, sticky="ew"
        )
        self.lblVgs3 = ttk.Label(self.frmHeader, text="3:", anchor="e").grid(
            row=2, column=4, sticky="ew"
        )
        self.txtVgs3 = ttk.Entry(self.frmHeader, width=5).grid(
            row=2, column=5, sticky="ew"
        )
        self.lblVgs4 = ttk.Label(self.frmHeader, text="4:", anchor="e").grid(
            row=2, column=6, sticky="ew"
        )
        self.txtVgs4 = ttk.Entry(self.frmHeader, width=5).grid(
            row=2, column=7, sticky="ew"
        )

        self.lblIgs1 = ttk.Label(
            self.frmHeader, text="Igs[A].. 1:", anchor="e"
        ).grid(row=3, column=0, sticky="ew")
        self.txtIgs1 = ttk.Entry(self.frmHeader, width=5).grid(
            row=3, column=1, sticky="ew"
        )
        self.lblIgs2 = ttk.Label(self.frmHeader, text="2:", anchor="e").grid(
            row=3, column=2, sticky="ew"
        )
        self.txtIgs2 = ttk.Entry(self.frmHeader, width=5).grid(
            row=3, column=3, sticky="ew"
        )
        self.lblIgs3 = ttk.Label(self.frmHeader, text="3:", anchor="e").grid(
            row=3, column=4, sticky="ew"
        )
        self.txtIgs3 = ttk.Entry(self.frmHeader, width=5).grid(
            row=3, column=5, sticky="ew"
        )
        self.lblIgs4 = ttk.Label(self.frmHeader, text="4:", anchor="e").grid(
            row=3, column=6, sticky="ew"
        )
        self.txtIgs4 = ttk.Entry(self.frmHeader, width=5).grid(
            row=3, column=7, sticky="ew"
        )

        # right frame PSU buttons widgets
        self.btnProgramPSUs = ttk.Button(
            self.frmPSUbtns, text="Program all PSU's"
        )
        self.btnProgramPSUs.pack(
            side="left", expand=True, fill="x", padx=2, pady=2
        )

        self.btnAutoSwitchPSUs = ttk.Button(
            self.frmPSUbtns, text="Switch enabled PSU's"
        )
        self.btnAutoSwitchPSUs.pack(
            side="left", padx=2, pady=2
        )  # , expand=True, fill="x")

        self.chkPSUsEnTgl = ttk.Button(self.frmPSUbtns, text="tgl")
        self.chkPSUsEnTgl.pack(
            side="left", expand=True, fill="x", padx=2, pady=2
        )

        # Right side frmPSUfield widgets
        self.lblPSU1 = ttk.Label(
            self.frmPSUfield, text="PSU1:", anchor="e"
        ).grid(row=0, column=0, sticky="ew")
        self.txtPSU1V = ttk.Entry(self.frmPSUfield, width=5).grid(
            row=0, column=1, sticky="ew"
        )
        self.lblPSU1V = ttk.Label(self.frmPSUfield, text="V", anchor="w").grid(
            row=0, column=2, sticky="ew"
        )
        self.txtPSU1A = ttk.Entry(self.frmPSUfield, width=5).grid(
            row=0, column=3, sticky="ew"
        )
        self.lblPSU1A = ttk.Label(self.frmPSUfield, text="A", anchor="w").grid(
            row=0, column=4, sticky="ew"
        )
        self.btnPSU1 = ttk.Button(self.frmPSUfield, text="PSU1")
        self.btnPSU1.grid(
            row=0, column=5, columnspan=2, padx=2, pady=2, sticky="e"
        )
        self.chkPSU1var = tk.StringVar(value=0)
        self.chkPSU1 = ttk.Checkbutton(
            self.frmPSUfield, text="", variable=self.chkPSU1var
        )
        self.chkPSU1.grid(row=0, column=7)

        self.lblPSU2 = ttk.Label(
            self.frmPSUfield, text="PSU2:", anchor="e"
        ).grid(row=1, column=0, sticky="ew")
        self.txtPSU2V = ttk.Entry(self.frmPSUfield, width=5).grid(
            row=1, column=1, sticky="ew"
        )
        self.lblPSU2V = ttk.Label(self.frmPSUfield, text="V", anchor="w").grid(
            row=1, column=2, sticky="ew"
        )
        self.txtPSU2A = ttk.Entry(self.frmPSUfield, width=5).grid(
            row=1, column=3, sticky="ew"
        )
        self.lblPSU2A = ttk.Label(self.frmPSUfield, text="A", anchor="w").grid(
            row=1, column=4, sticky="ew"
        )
        self.btnPSU2 = ttk.Button(self.frmPSUfield, text="PSU2")
        self.btnPSU2.grid(
            row=1, column=5, columnspan=2, padx=2, pady=2, sticky="e"
        )
        self.chkPSU2var = tk.StringVar(value=0)
        self.chkPSU2 = ttk.Checkbutton(
            self.frmPSUfield, text="", variable=self.chkPSU2var
        )
        self.chkPSU2.grid(row=1, column=7)

        self.lblPSU3 = ttk.Label(
            self.frmPSUfield, text="PSU3:", anchor="e"
        ).grid(row=2, column=0, sticky="ew")
        self.txtPSU3V = ttk.Entry(self.frmPSUfield, width=5).grid(
            row=2, column=1, sticky="ew"
        )
        self.lblPSU3V = ttk.Label(self.frmPSUfield, text="V", anchor="w").grid(
            row=2, column=2, sticky="ew"
        )
        self.txtPSU3A = ttk.Entry(self.frmPSUfield, width=5).grid(
            row=2, column=3, sticky="ew"
        )
        self.lblPSU3A = ttk.Label(self.frmPSUfield, text="A", anchor="w").grid(
            row=2, column=4, sticky="ew"
        )
        self.btnPSU3 = ttk.Button(self.frmPSUfield, text="PSU3")
        self.btnPSU3.grid(
            row=2, column=5, columnspan=2, padx=2, pady=2, sticky="ew"
        )
        self.chkPSU3var = tk.StringVar(value=0)
        self.chkPSU3 = ttk.Checkbutton(
            self.frmPSUfield, text="", variable=self.chkPSU3var
        )
        self.chkPSU3.grid(row=2, column=7)

        self.lblPSU4 = ttk.Label(
            self.frmPSUfield, text="PSU4:", anchor="e"
        ).grid(row=3, column=0, sticky="ew")
        self.txtPSU4V = ttk.Entry(self.frmPSUfield, width=5).grid(
            row=3, column=1, sticky="ew"
        )
        self.lblPSU4V = ttk.Label(self.frmPSUfield, text="V", anchor="w").grid(
            row=3, column=2, sticky="ew"
        )
        self.txtPSU4A = ttk.Entry(self.frmPSUfield, width=5).grid(
            row=3, column=3, sticky="ew"
        )
        self.lblPSU4A = ttk.Label(self.frmPSUfield, text="A", anchor="w").grid(
            row=3, column=4, sticky="ew"
        )
        self.btnPSU4 = ttk.Button(self.frmPSUfield, text="PSU4")
        self.btnPSU4.grid(
            row=3, column=5, columnspan=2, padx=2, pady=2, sticky="ew"
        )
        self.chkPSU4var = tk.StringVar(value=0)
        self.chkPSU4 = ttk.Checkbutton(
            self.frmPSUfield, text="", variable=self.chkPSU4var
        )
        self.chkPSU4.grid(row=3, column=7)

        self.lblPSU5 = ttk.Label(
            self.frmPSUfield, text="PSU5:", anchor="e"
        ).grid(row=4, column=0, sticky="ew")
        self.txtPSU5V = ttk.Entry(self.frmPSUfield, width=5).grid(
            row=4, column=1, sticky="ew"
        )
        self.lblPSU5V = ttk.Label(self.frmPSUfield, text="V", anchor="w").grid(
            row=4, column=2, sticky="ew"
        )
        self.txtPSU5A = ttk.Entry(self.frmPSUfield, width=5).grid(
            row=4, column=3, sticky="ew"
        )
        self.lblPSU5A = ttk.Label(self.frmPSUfield, text="A", anchor="w").grid(
            row=4, column=4, sticky="ew"
        )
        self.btnPSU5 = ttk.Button(self.frmPSUfield, text="PSU5")
        self.btnPSU5.grid(
            row=4, column=5, columnspan=2, padx=2, pady=2, sticky="ew"
        )
        self.chkPSU5var = tk.StringVar(value=0)
        self.chkPSU5 = ttk.Checkbutton(
            self.frmPSUfield, text="", variable=self.chkPSU5var
        )
        self.chkPSU5.grid(row=4, column=7)

        self.lblPSU6 = ttk.Label(
            self.frmPSUfield, text="PSU6:", anchor="e"
        ).grid(row=5, column=0, sticky="ew")
        self.txtPSU6V = ttk.Entry(self.frmPSUfield, width=5).grid(
            row=5, column=1, sticky="ew"
        )
        self.lblPSU6V = ttk.Label(self.frmPSUfield, text="V", anchor="w").grid(
            row=5, column=2, sticky="ew"
        )
        self.txtPSU6A = ttk.Entry(self.frmPSUfield, width=5).grid(
            row=5, column=3, sticky="ew"
        )
        self.lblPSU6A = ttk.Label(self.frmPSUfield, text="A", anchor="w").grid(
            row=5, column=4, sticky="ew"
        )
        self.btnPSU6 = ttk.Button(self.frmPSUfield, text="PSU6")
        self.btnPSU6.grid(
            row=5, column=5, columnspan=2, padx=2, pady=2, sticky="ew"
        )
        self.chkPSU6var = tk.StringVar(value=0)
        self.chkPSU6 = ttk.Checkbutton(
            self.frmPSUfield, text="", variable=self.chkPSU6var
        )
        self.chkPSU6.grid(row=5, column=7)

        self.lblPSUX = ttk.Label(
            self.frmPSUfield, text="PSUX:", anchor="e"
        ).grid(row=6, column=0, sticky="ew")
        self.txtPSUXV = ttk.Entry(self.frmPSUfield, width=5).grid(
            row=6, column=1, sticky="ew"
        )
        self.lblPSUXV = ttk.Label(self.frmPSUfield, text="V", anchor="w").grid(
            row=6, column=2, sticky="ew"
        )
        self.txtPSUXA = ttk.Entry(self.frmPSUfield, width=5).grid(
            row=6, column=3, sticky="ew"
        )
        self.lblPSUXA = ttk.Label(self.frmPSUfield, text="A", anchor="w").grid(
            row=6, column=4, sticky="ew"
        )
        self.btnPSUX = ttk.Button(self.frmPSUfield, text="PSUX")
        self.btnPSUX.grid(
            row=6, column=5, columnspan=2, padx=2, pady=2, sticky="ew"
        )
        self.chkPSUXvar = tk.StringVar(value=0)
        self.chkPSUX = ttk.Checkbutton(
            self.frmPSUfield, text="", variable=self.chkPSUXvar
        )
        self.chkPSUX.grid(row=6, column=7)

        # bindings
        self.bind("<Escape>", lambda event: self.destroy())
        # self.bind("<Configure>", lambda event: print(event))

    def createFrame(self, parent, width, height):
        return ttk.Frame(parent, borderwidth=1, relief=tk.GROOVE)

    def createLabel(self, parent, text):
        return ttk.Label(parent, text=text)

    def createButton(self, parent, text):
        return ttk.Button(parent, text=text)


width = 808
height = 412
txtwidth = 54

if __name__ == "__main__":
    RFproPE = Root("RFproPE v1.0 rev0", (width, height))
    # for font in font.families():
    #     print(font)
    RFproPE.mainloop()
