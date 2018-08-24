import wx
class MyFrame(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,-1,'hello word',size=(600,600))
        panel = wx.Panel(self)
        size = wx.BoxSizer(wx.HORIZONTAL)
        panel.SetSizer(size)
        txt = wx.StaticText(panel,-1,'submit')
        size.Add(txt,0,wx.TOP|wx.LEFT,100)
        self.button = wx.Button(panel,-1,"quit")
        size.Add(self.button,0,wx.TOP|wx.LEFT)
        self.button.Bind(wx.EVT_BUTTON, self.click, self.button, -1, -1)
        self.button.Bind(wx.EVT_ENTER_WINDOW, self.enter)
        self.button1 = wx.Button(panel,-1,"OK")
        self.button1.Bind(wx.EVT_BUTTON, self.ok)

        self.Centre()
    def enter(self,event):
        print ('enter window')
        self.button.SetLabel('dddd')
        event.Skip()
    def click(self,event):
        print( 'quit')
        dlg = wx.MessageDialog(None, u"消息对话框测试", u"标题信息", wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.Close(True)
        dlg.Destroy()
    def ok(self,event):
        print ('ok')
        text = wx.TextEntryDialog(None,u"请输入文本", u"标题信息")
        text.ShowModal()
        print(text.GetValue())
        event.Skip()
        #self.Close()
class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None)
        self.frame.Show(True)
        print ('init--',self.frame.GetId())
        return True

app = MyApp()
app.MainLoop()
