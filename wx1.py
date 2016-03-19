import wx

class myApp(wx.App):
    def OnInit(self):
        wx.MessageBox("Hello pycoder_boy", "wxApp")
        return True

if __name__ == "__main__":
    app = myApp(False)
    app.MainLoop()