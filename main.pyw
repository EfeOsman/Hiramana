import os
from tkinter import *
from tkinter.tix import *
from tkinter import ttk, font
from playsound import playsound
class HiraMana:
	normal     = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん"
	dakuten    = "がぎぐげござじずぜぞだぢづでどばびぶべぼ"
	handakuten = "ぱぴぷぺぽ"
	romaji =    ['a',  'i', 'u','e','o',
				 'ka', 'ki','ku',   'ke',
				 'ko', 'sa','shi',  'su',
				 'se', 'so','ta',   'chi',
				 'tsu','te','to',   'na',
				 'ni', 'nu','ne',   'no',
				 'ha', 'hi','fu',   'he',
				 'ho', 'ma','mi',   'mu',
				 'me', 'mo','ya',   'yu',
				 'yo', 'ra','ri',   'ru',
				 're', 'ro','wa',   'wo',
				 'n',  'ga','gi',   'gu',
				 'ge', 'go','za',   'ji',
				 'zu', 'ze','zo',   'da',
				 'ji', 'zu','de',   'do',
				 'ba', 'bi','bu',   'be',
				 'bo', 'pa','pi',   'pu',
				 'pe', 'po']
	hiraganaMap = dict(zip(normal+dakuten+handakuten, romaji))
	romajiMap   = dict(zip(romaji, normal+dakuten+handakuten))
	def __init__(self, ):
		self.root = Tk()
		self.root.title("HiraMana")
		self.root.resizable(False, False)

		self._FONT = font.Font(family='Helvetica', size=22, weight='bold')
		self.widgets = {"Normal":    {"tabframe": None, "frame": None, "table": [None, None], "chartbuttons": []},
						"Dakuten":   {"tabframe": None, "frame": None, "table": [None, None], "chartbuttons": []},
						"Handakuten":{"tabframe": None, "frame": None, "table": [None, None], "chartbuttons": []}}
		self.tabControl = ttk.Notebook(self.root)
		self.balloon = Balloon(self.root,bg="white", title="Romaji")
		self.balloon.subwidget('message')['fg'] = "red"
		self.balloon.subwidget('message')['font'] = self._FONT
		for sub in self.balloon.subwidgets_all(): # Change background of balloon widget
			sub.config(bg='light grey')
		self.__initWidgets()

	def __initWidgets(self):
			
		def normalForm():
			self.widgets["Normal"]["tabframe"] = Frame(self.root)
			self.widgets["Normal"]["frame"]    = Frame(self.widgets["Normal"]["tabframe"], bg="gray")
			#Frame(self.widgets["Normal"]["tabframe"],bg="black").pack(side=LEFT, fill=BOTH)
			#Frame(self.widgets["Normal"]["tabframe"],bg="black").pack(side=TOP, fill=BOTH)
			for hc in self.normal:
				path = os.path.join("sounds",f"{self.hiraganaMap[hc]}.mp3") # Safe way of paths
				hiraButton = Button(self.widgets["Normal"]["frame"])
				hiraButton["text"] = hc
				hiraButton["font"] = self._FONT
				hiraButton["command"] = lambda path=path:playsound(path, False)# path=path->lambda looks up the variable name at the time the function is called 
				self.balloon.bind_widget(hiraButton, balloonmsg=self.hiraganaMap[hc])
				self.widgets["Normal"]["chartbuttons"].append(hiraButton)

		def dakutenForm():
			self.widgets["Dakuten"]["tabframe"] = Frame(self.root)
			self.widgets["Dakuten"]["frame"]    = Frame(self.widgets["Dakuten"]["tabframe"], bg="gray")
			for hc in self.dakuten:
				path = os.path.join("sounds",f"{self.hiraganaMap[hc]}.mp3") # Safe way of paths
				hiraButton = Button(self.widgets["Dakuten"]["frame"])
				hiraButton["text"] = hc
				hiraButton["font"] = self._FONT
				hiraButton["command"] = lambda path=path:playsound(path, False)# path=path->lambda looks up the variable name at the time the function is called 
				self.balloon.bind_widget(hiraButton, balloonmsg=self.hiraganaMap[hc])
				self.widgets["Dakuten"]["chartbuttons"].append(hiraButton)
		def handakutenForm():
			self.widgets["Handakuten"]["tabframe"] = Frame(self.root)
			self.widgets["Handakuten"]["frame"]    = Frame(self.widgets["Handakuten"]["tabframe"], bg="gray")
			for hc in self.handakuten:
				path = os.path.join("sounds",f"{self.hiraganaMap[hc]}.mp3") # Safe way of paths
				hiraButton = Button(self.widgets["Handakuten"]["frame"])
				hiraButton["text"] = hc
				hiraButton["font"] = self._FONT
				hiraButton["command"] = lambda path=path:playsound(path, False)# path=path->lambda looks up the variable name at the time the function is called 
				self.balloon.bind_widget(hiraButton, balloonmsg=self.hiraganaMap[hc])
				self.widgets["Handakuten"]["chartbuttons"].append(hiraButton)
		normalForm()
		dakutenForm()
		handakutenForm()

	def loop(self):
		def drawChart(widgets, chart):
			idx = 0
			for y in range(len(chart)):
				for x in range(len(chart[y])):
					if chart[y][x]:
						widgets[idx].grid(row = y, column = x)
						idx += 1			
		def normalForm():
			self.widgets["Normal"]["frame"].pack(fill=Y,expand=True,padx=10, pady=10)

			chart = [[1,1,1,1,1],
			         [1,1,1,1,1],
			         [1,1,1,1,1],
			         [1,1,1,1,1],
			         [1,1,1,1,1],
			         [1,1,1,1,1],
			         [1,1,1,1,1],
			         [1,0,1,0,1],
			         [1,1,1,1,1],
			         [1,0,0,0,1],
			         [1]]
			drawChart(self.widgets["Normal"]["chartbuttons"], chart)

		def dakutenForm():
			self.widgets["Dakuten"]["frame"].pack(fill=Y,expand=True,padx=10, pady=10)
			chart = [[1,1,1,1,1],
			         [1,1,1,1,1],
			         [1,1,1,1,1],
			         [1,1,1,1,1]]
			drawChart(self.widgets["Dakuten"]["chartbuttons"], chart)

		def handakutenForm():

			self.widgets["Handakuten"]["frame"].pack(fill=Y,expand=True,padx=10, pady=10)
			drawChart(self.widgets["Handakuten"]["chartbuttons"], [[1,1,1,1,1]])

		normalForm()
		dakutenForm()
		handakutenForm()
		self.tabControl.add(self.widgets["Normal"]["tabframe"],    text= "Normal Form")
		self.tabControl.add(self.widgets["Dakuten"]["tabframe"],   text= "Dakuten Form")
		self.tabControl.add(self.widgets["Handakuten"]["tabframe"],text= "Handakuten Form")
		self.tabControl.pack(expand = 1, fill ="both") 
		self.root.mainloop()

if __name__ == '__main__':
	hira = HiraMana()
	hira.loop()