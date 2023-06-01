import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        self.pnl = wx.Panel(self)
        # wx.Font object initialization
        font = wx.Font(
            11,
            wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL,
            underline=False,
            faceName="Microsoft Sans Serif",
        )

        # CREATE BUTTON AT POINT (20, 20)
        self.st = wx.Button(
            self.pnl,
            id=1,
            label="Initialize PCW",
            pos=(20, 40),
            size=(190, 60),  # wx.DefaultSize
            name="cmd_InitPCW",
        )
        # SET FONT FOR LABEL
        self.st.SetFont(font)
        self.SetSize((350, 250))
        self.SetTitle("wx.Button")
        self.Centre()


def main():
    app = wx.App()
    ex = Example(None, title="Font test")
    ex.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()

# class Example(wx.Frame):
#     def __init__(self, *args, **kwargs):
#         super(Example, self).__init__(*args, **kwargs)
#         self.InitUI()
#
#     def InitUI(self):
#         self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
#         self.pnl = wx.Panel(self)
#         # wx.Font object initialization
#         font = wx.Font(12, wx.FONTFAMILY_MODERN, 0, 90, underline=False,
#                        faceName="")
#
#         # CREATE BUTTON AT POINT (20, 20)
#         self.st = wx.Button(self.pnl, id=1, label="Button", pos=(20, 20),
#                             size=wx.DefaultSize,  name="button")
#         # SET FONT FOR LABEL
#         self.st.SetFont(font)
#         self.SetSize((350, 250))
#         self.SetTitle('wx.Button')
#         self.Centre()
#
#
# def main():
#     app = wx.App()
#     ex = Example(None)
#     ex.Show()
#     app.MainLoop()
#
#
# if __name__ == '__main__':
#     main()
