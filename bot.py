#HXXEQK-Q6UTV3APKR
import wx
import wolframalpha
import wikipedia
import pyttsx3 as pk
engine = pk.init()
engine.say("welcome my buddy nice to see you :),I HOPE YOU ARE FINE")
engine.say("HELLO MY NAME 'bhanu' THE PERSIONAL ASSISTANT OF 'THUDI BHANU PRASAD',HOW CAN I HELP YOU?")
engine.say("enter any thing in the box,i will give you the meaning")
engine.runAndWait()
class My_Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,
        pos=wx.DefaultPosition,size=wx.Size(600,100),
        style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
        wx.CLOSE_BOX | wx.CLIP_CHILDREN,
        title="MY-BHANU")
        panel=wx.Panel(self)
        my_sizer=wx.BoxSizer(wx.VERTICAL)
        lbl=wx.StaticText(panel,label="HELLO MY NAME IS 'bhanu' THE PERSIONAL ASSISTANT OF 'THUDI BHANU PRASAD'HOW CAN I HELP YOU?")
        my_sizer.Add(lbl,0,wx.ALL,5)
        self.txt=wx.TextCtrl(panel,style=wx.TE_PROCESS_ENTER,size=(500,60))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER,self.OnEnter)
        my_sizer.Add(self.txt,0,wx.ALL,5)
        panel.SetSizer(my_sizer)
        self.Show()
    def OnEnter(self,event):
        input=self.txt.GetValue()
        input=input.lower()
        try:
            engine = pk.init()
            app_id='HXXEQK-Q6UTV3APKR'
            client=wolframalpha.Client(app_id)
            res=client.query(input)
            answer=next(res.results).text
            print(answer)
            engine.say("the answer is "+answer)
            engine.runAndWait()
        except:
            engine =pk.init()
            engine.say("okay,i am  searched for "+input)
            print(wikipedia.summary(input))
            engine.runAndWait()
if __name__=="__main__":
    app=wx.App(True)
    frame=My_Frame()
    app.MainLoop()
