#i!/usr/bin/python

# Auther      : Heinz Samuelsson
# Date        : 2017-06-02
# File        : 
# Reference   : -
# Description :
#               
# Python ver  :

import wx
import trace
import logging

WINDOW_SIZE = (1035, 870)

HEADLINE = 10*' '+'Unicorn Tester'

# color codes
GREY  = (180, 180, 180)
BLACK = (0, 0, 0)


def print_const():
   app = wx.GetApp()
   #print app.frame.tabDownLoader.ser


class MainFrame(wx.Frame):
	def __init__(self, *args, **kwargs):
		wx.Frame.__init__(self, *args, **kwargs)

		pnl = wx.Panel(self)

		self.rb1 = wx.RadioButton(pnl, label='Value A', pos=(10, 10), style=wx.RB_GROUP)
		self.rb1.Bind(wx.EVT_RADIOBUTTON, self.SetVal)

		self.rb2 = wx.RadioButton(pnl, label='Value B', pos=(10, 30), style=wx.RB_GROUP)
		self.rb2.Bind(wx.EVT_RADIOBUTTON, self.SetVal)

		self.sb = self.CreateStatusBar(2)
		self.sb.SetStatusText("False", 0)
		self.sb.SetStatusText("False", 0)

		self.SetSize((210, 210))
		self.SetTitle('wx.RadioButton')

		self.Centre()

	def SetVal(self, e):
		state1 = str(self.rb1.GetValue())
		state2 = str(self.rb2.GetValue())
		self.sb.SetStatusText(state1, 0)
		self.sb.SetStatusText(state2, 0)

	def setup_alignment_sizer(self):
		statBoxSerial = wx.StaticBox(self, wx.ID_ANY, '  Alignment')
		statBoxSerial.SetBackgroundColour(GREY)
		statBoxSerial.SetForegroundColour(BLACK)
		statBoxSizer = wx.StaticBoxSizer(statBoxSerial, wx.HORIZONTAL)
		
		return statBoxSizer


class mainApp(wx.App):
   def OnInit(self):
       self.frame = MainFrame(None, -1, title=HEADLINE, style=wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX, size=WINDOW_SIZE)
       self.frame.Show()
       return True

if __name__ == '__main__':
    app = mainApp() 
    app.MainLoop()
