import time
import wx

RED = [255, 64, 64]
GREEN = [0, 255, 0]
YELLOW = [255, 225, 0]
WINDOW_SIZE = (800, 400)
RELAY_BUTTON_SIZE = (65, 30)
DELAY_TIMER = 4000

class MyFrame(wx.Frame):
	def __init__(self, parent, title):
		super(MyFrame, self).__init__(parent, title =title, size = WINDOW_SIZE)
		self.panel = MyPanel(self)

		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
		menubar.Append(fileMenu, '&File')
		self.SetMenuBar(menubar)
				
		self.Bind(wx.EVT_MENU, self.onQuit, fileItem)

	def onQuit(self, event):
		self.Close()
 
 
class MyPanel(wx.Panel):
	def __init__(self, parent):
		super(MyPanel, self).__init__(parent)
		
		self.relay_list = []
		self.auto_release_1 = False
		self.auto_release_2 = False

		self.release_timer_1 = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.update, self.release_timer_1)

		self.release_timer_2 = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.update, self.release_timer_2)

		box = wx.StaticBox(self, -1, "     Power Control  ")
		self.bsizer = wx.StaticBoxSizer(box, wx.HORIZONTAL)
		
		box2 = wx.StaticBox(self, -1, "     Relay Control  ")
		self.bsizer2 = wx.StaticBoxSizer(box2, wx.VERTICAL)
		
		self.define_power_buttons()
		self.define_relay_buttons()
		#self.define_checkbox()
		
		border = wx.BoxSizer(wx.VERTICAL)
		border.Add(self.bsizer, 1, wx.ALL, 25)
		border.Add(self.bsizer2, 1, wx.ALL, 25)
		
		self.SetSizer(border)

	def define_power_buttons(self):
		self.dc300VBtn = wx.ToggleButton(self, label = "DC 300 V")
		self.dc300VBtn.SetBackgroundColour(RED)
		self.dc300VBtn.Bind(wx.EVT_TOGGLEBUTTON, self.onDC300V)
		
		self.ac230VBtn = wx.ToggleButton(self, label = "AC 230 V")
		self.ac230VBtn.SetBackgroundColour(RED)
		self.ac230VBtn.Bind(wx.EVT_TOGGLEBUTTON, self.onAC230V)
		
		self._24VBtn = wx.ToggleButton(self, label = "24 V")
		self._24VBtn.SetBackgroundColour(RED)
		self._24VBtn.Bind(wx.EVT_TOGGLEBUTTON, self.on24V)
		
		self.bsizer.Add(self.dc300VBtn, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10)
		self.bsizer.Add(self.ac230VBtn, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10)
		self.bsizer.Add(self._24VBtn, 0, wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT, 10)

	def define_relay_buttons(self):
		rel1 = wx.Button(self, label = "Rel 1", size=RELAY_BUTTON_SIZE)
		rel1.SetBackgroundColour(RED)
		rel1.SetFont(wx.Font(10, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.BOLD))
		rel1.realy_idx = 0
		rel1.state = False
		rel1.Bind(wx.EVT_BUTTON, self.onRelay)
		
		rel2 = wx.Button(self, label = "Rel 2", size=RELAY_BUTTON_SIZE)
		rel2.SetBackgroundColour(RED)
		rel2.SetFont(wx.Font(10, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.BOLD))
		rel2.realy_idx = 1
		rel2.state = False
		rel2.Bind(wx.EVT_BUTTON, self.onRelay)
		
		rel3 = wx.Button(self, label = "Rel 3", size=RELAY_BUTTON_SIZE)
		rel3.SetBackgroundColour(RED)
		rel3.SetFont(wx.Font(10, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.BOLD))
		rel3.realy_idx = 2
		rel3.state = False
		rel3.Bind(wx.EVT_BUTTON, self.onRelay)

		rel4 = wx.Button(self, label = "Rel 4", size=RELAY_BUTTON_SIZE)
		rel4.SetBackgroundColour(RED)
		rel4.SetFont(wx.Font(10, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.BOLD))
		rel4.realy_idx = 3
		rel4.state = False
		rel4.Bind(wx.EVT_BUTTON, self.onRelay)

		rel5 = wx.Button(self, label = "Rel 5", size=RELAY_BUTTON_SIZE)
		rel5.SetBackgroundColour(RED)
		rel5.SetFont(wx.Font(10, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.BOLD))
		rel5.realy_idx = 4
		rel5.state = False
		rel5.Bind(wx.EVT_BUTTON, self.onRelay)

		rel6 = wx.Button(self, label = "Rel 6", size=RELAY_BUTTON_SIZE)
		rel6.SetBackgroundColour(RED)
		rel6.SetFont(wx.Font(10, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.BOLD))
		rel6.realy_idx = 5
		rel6.state = False
		rel6.Bind(wx.EVT_BUTTON, self.onRelay)

		rel7 = wx.Button(self, label = "Rel 7", size=RELAY_BUTTON_SIZE)
		rel7.SetBackgroundColour(RED)
		rel7.SetFont(wx.Font(10, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.BOLD))
		rel7.realy_idx = 6
		rel7.state = False
		rel7.Bind(wx.EVT_BUTTON, self.onRelay)

		rel8 = wx.Button(self, label = "Rel 8", size=RELAY_BUTTON_SIZE)
		rel8.SetBackgroundColour(RED)
		rel8.SetFont(wx.Font(10, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.BOLD))
		rel8.realy_idx = 7
		rel8.state = False
		rel8.Bind(wx.EVT_BUTTON, self.onRelay)

		auto_release_cbox1 = wx.CheckBox(self, -1, 'Auto release')
		auto_release_cbox1.Bind(wx.EVT_CHECKBOX, self.onAutoRelease1)

		rel9 = wx.Button(self, label = "Rel 9", size=RELAY_BUTTON_SIZE)
		rel9.SetBackgroundColour(RED)
		rel9.SetFont(wx.Font(10, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.BOLD))
		rel9.realy_idx = 8
		rel9.state = False
		rel9.Bind(wx.EVT_BUTTON, self.onRelay)

		rel10 = wx.Button(self, label = "Rel 10", size=RELAY_BUTTON_SIZE)
		rel10.SetBackgroundColour(RED)
		rel10.SetFont(wx.Font(10, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.BOLD))
		rel10.realy_idx = 9
		rel10.state = False
		rel10.Bind(wx.EVT_BUTTON, self.onRelay)

		rel11 = wx.Button(self, label = "Rel 11", size=RELAY_BUTTON_SIZE)
		rel11.SetBackgroundColour(RED)
		rel11.SetFont(wx.Font(10, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.BOLD))
		rel11.realy_idx =10 
		rel11.state = False
		rel11.Bind(wx.EVT_BUTTON, self.onRelay)

		rel12 = wx.Button(self, label = "Rel 12", size=RELAY_BUTTON_SIZE)
		rel12.SetBackgroundColour(RED)
		rel12.SetFont(wx.Font(10, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.BOLD))
		rel12.realy_idx =11 
		rel12.state = False
		rel12.Bind(wx.EVT_BUTTON, self.onRelay)

		rel13 = wx.Button(self, label = "Rel 13", size=RELAY_BUTTON_SIZE)
		rel13.SetBackgroundColour(RED)
		rel13.SetFont(wx.Font(10, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.BOLD))
		rel13.realy_idx =12 
		rel13.state = False
		rel13.Bind(wx.EVT_BUTTON, self.onRelay)

		rel14 = wx.Button(self, label = "Rel 14", size=RELAY_BUTTON_SIZE)
		rel14.SetBackgroundColour(RED)
		rel14.SetFont(wx.Font(10, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.BOLD))
		rel14.realy_idx =13 
		rel14.state = False
		rel14.Bind(wx.EVT_BUTTON, self.onRelay)

		rel15 = wx.Button(self, label = "Rel 15", size=RELAY_BUTTON_SIZE)
		rel15.SetBackgroundColour(RED)
		rel15.SetFont(wx.Font(10, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.BOLD))
		rel15.realy_idx =14 
		rel15.state = False
		rel15.Bind(wx.EVT_BUTTON, self.onRelay)

		rel16 = wx.Button(self, label = "Rel 16", size=RELAY_BUTTON_SIZE)
		rel16.SetBackgroundColour(RED)
		rel16.SetFont(wx.Font(10, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.BOLD))
		rel16.realy_idx =15 
		rel16.state = False
		rel16.Bind(wx.EVT_BUTTON, self.onRelay)

		auto_release_cbox2 = wx.CheckBox(self, -1, 'Auto release')
		auto_release_cbox2.Bind(wx.EVT_CHECKBOX, self.onAutoRelease2)

		self.relay_list = [rel1, rel2, rel3, rel4, rel5, rel6, rel7, 
		                   rel8, rel9, rel10, rel11, rel12, rel13, 
				   rel14, rel15, rel16]

		relay_sizer1 = wx.BoxSizer(wx.HORIZONTAL)
		relay_sizer2 = wx.BoxSizer(wx.HORIZONTAL)

		relay_sizer1.Add(rel1, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10)
		relay_sizer1.Add(rel2, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10)
		relay_sizer1.Add(rel3, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10)
		relay_sizer1.Add(rel4, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10)
		relay_sizer1.Add(rel5, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10)
		relay_sizer1.Add(rel6, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10)
		relay_sizer1.Add(rel7, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10)
		relay_sizer1.Add(rel8, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10)
		relay_sizer1.Add(auto_release_cbox1, 0, wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT, 10)

		relay_sizer2.Add(rel9, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10)
		relay_sizer2.Add(rel10, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10)
		relay_sizer2.Add(rel11, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10)
		relay_sizer2.Add(rel12, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10)
		relay_sizer2.Add(rel13, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10)
		relay_sizer2.Add(rel14, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10)
		relay_sizer2.Add(rel15, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10)
		relay_sizer2.Add(rel16, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10)
		relay_sizer2.Add(auto_release_cbox2, 0, wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT, 10)
		
		self.bsizer2.Add(relay_sizer1, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10)
		self.bsizer2.Add(relay_sizer2, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 10)

	def define_checkbox(self):
		self.rb1 = wx.CheckBox(self, -1, 'Rel1')
		self.bsizer2.Add(self.rb1, 0, wx.TOP, 10)
		self.rb2 = wx.CheckBox(self, -1, 'Rel2')
		self.bsizer2.Add(self.rb2, 0, wx.TOP, 10)
		self.rb3 = wx.CheckBox(self, -1, 'Rel3')
		self.bsizer2.Add(self.rb3, 0, wx.TOP, 10)
		self.rb4 = wx.CheckBox(self, -1, 'Rel4')
		self.bsizer2.Add(self.rb4, 0, wx.TOP, 10)
		self.rb5 = wx.CheckBox(self, -1, 'Rel5')
		self.bsizer2.Add(self.rb5, 0, wx.TOP, 10)
 
	def onDC300V(self, event):
		state = event.GetEventObject().GetValue()
		
		if state == True:
		    # ON 
		    self.dc300VBtn.SetBackgroundColour(GREEN)
		
		else:
		    self.dc300VBtn.SetBackgroundColour(RED)
 
	def onAC230V(self, event):
		state = event.GetEventObject().GetValue()
		
		if state == True:
		    # ON 
		    self.ac230VBtn.SetBackgroundColour(GREEN)
		
		else:
		    self.ac230VBtn.SetBackgroundColour(RED)

	def on24V(self, event):
		state = event.GetEventObject().GetValue()
		
		if state == True:
		    # ON 
		    self._24VBtn.SetBackgroundColour(GREEN)
		
		else:
		    self._24VBtn.SetBackgroundColour(RED)


	def update(self, event):
		print('Update')
		print(time.ctime)

		if self.auto_release_1:
			for idx in range(0, 8):
				print(idx)
				self.relay_list[idx].SetBackgroundColour(RED)
				self.relay_list[idx].state = False
			self.release_timer_1.Stop()
		else:
			self.release_timer_1.Stop()

		if self.auto_release_2:
			for idx in range(8, 16):
				print(idx)
				self.relay_list[idx].SetBackgroundColour(RED)
				self.relay_list[idx].state = False
			self.release_timer_2.Stop()
		else:
			self.release_timer_2.Stop()

	def onRelay(self, event):
		idx = event.GetEventObject().realy_idx
		state = event.GetEventObject().state

		print('Relay: {}'.format(idx+1))

		if self.relay_list[idx].state == False:
			print('Greeen')

			if self.auto_release_1:
				self.release_timer_1.Start(DELAY_TIMER)

			self.relay_list[idx].SetBackgroundColour(GREEN)
			self.relay_list[idx].state = True

		elif self.relay_list[idx].state == True:
			print('Reeeed')

			if self.auto_release_2:
				self.release_timer_2.Start(DELAY_TIMER)

			self.relay_list[idx].SetBackgroundColour(RED)
			self.relay_list[idx].state = False

	def onAutoRelease1(self, event):
		cb = event.GetEventObject() 
		print(cb.GetLabel(),'1 is clicked:',cb.GetValue())
		self.auto_release_1 = cb.GetValue()
		self.release_timer_1.Start(DELAY_TIMER)

	def onAutoRelease2(self, event):
		cb = event.GetEventObject() 
		print(cb.GetLabel(),'2 is clicked:',cb.GetValue())
		self.auto_release_2 = cb.GetValue()
		self.release_timer_2.Start(DELAY_TIMER)
		


class MyApp(wx.App):
	def OnInit(self):
		self.frame = MyFrame(parent=None, title="Unicorn Controller")
		self.frame.Centre()
		self.frame.Show()
		return True
 
 
app = MyApp()
app.MainLoop()
