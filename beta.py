import wx
import wikipedia
import wolframalpha 
import pyttsx3
import speech_recognition as sr
from playsound import playsound

engine = pyttsx3.init()
rate = engine.getProperty('rate')   
print (rate)                       
engine.setProperty('rate', 150)
engine.say("Hello fucker !!")
engine.runAndWait()
class MyFrame(wx.Frame) :
    def __init__(self) :  
        wx.Frame.__init__(self,None,pos=wx.DefaultPosition, size=wx.Size(500,300),style=wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.MINIMIZE_BOX| wx.CLOSE_BOX | wx.CLIP_CHILDREN,title="Rayson :)")
        panel= wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl=wx.StaticText(panel,label="Hello Iam Rayson ,Your Sexy Assistant , How can i fuck you?",size = wx.Size(400,70))
        note=wx.StaticText(panel,label="Note : Keep Enter key pressed while you speak!!",size = wx.Size(400,70))
        my_sizer.Add(lbl, 0,wx.ALL,5)
        self.txt = wx.TextCtrl(panel,style= wx.TE_PROCESS_ENTER,size=(400,30)) 
        self.txt.SetFocus()
        self.txt.SetHint("Type anything ...")
        self.txt.Bind(wx.EVT_TEXT_ENTER,self.OnEnter)
        my_sizer.Add(self.txt,0,wx.ALL,5)
        my_sizer.Add(note,0,wx.ALL,5)
        panel.SetSizer(my_sizer)
        self.Show()
    def OnEnter(self, event) :
        input= self.txt.GetValue()
        input = input.lower()
        if input == 'xxx' :         
            engine.say("yyy")
            engine.runAndWait()
        elif input == 'zzz' :
            engine.say("aaa")
            engine.runAndWait()
        elif input == 'ooo' :
            engine.say("eee")
            engine.runAndWait()
        elif input == 'iii' :
            engine.say("eee")
            engine.runAndWait()
        elif input == '':
            r = sr.Recognizer()
            with sr.Microphone() as source :
                audio = r.listen(source)
                r.adjust_for_ambient_noise(source, duration=5)
            try :
                self.txt.SetValue(r.recognize_google(audio))
            except sr.UnknownValueError:
                print("I cant understand you")
            except sr.RequestError as e:
                print("Could not connect to the inernet; {0}",format(e))
        else :        
            try:
                app_id="WUGJEJ-2RERJEGKEE"
                client=wolframalpha.Client(app_id)
                res = client.query(input)
                answer = next(res.results).text
                print(answer)
                engine.say("The answer is :" +answer)
                engine.runAndWait()
            except:
                wikipedia.set_lang("en")
                engine.say("You Searched for :" +input)
                engine.runAndWait()
                print(wikipedia.summary(input , sentences=4))
                ans = wikipedia.summary(input)
                engine.say("The answer is :" +ans)
                engine.runAndWait()

        
        
            
if  __name__ == "__main__" :
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop() 