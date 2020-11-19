import datetime

from datetime import date
from datetime import timedelta

import matplotlib.units  as munits
import matplotlib.dates  as mdates
import matplotlib.pyplot as plt

from pydrive2.auth  import GoogleAuth
from pydrive2.drive import GoogleDrive

from kivy.uix.image   import Image
from kivy.uix.button  import Button
from kivy.core.window import Window

from kivymd.app import MDApp

from kivymd.uix.floatlayout import MDFloatLayout


##############################################################
##############################################################

class Graphs(MDFloatLayout):

    #################################################
    def __init__(self, **kwargs):
        super(Graphs, self).__init__(**kwargs)
        self.BStart = Button()
        self.iPic   = Image(source = 'Pic.png')
        return

    #################################################
    def Initialize(self):
        ##################################
        if(self.iPic.parent != None):
            self.remove_widget(self.iPic)
        ##################################
        self.size = Window.size
        Xc = int(self.width * 0.5)
        Yc = int(self.height * 0.5)
        ##################################
        Button_Width  = int(self.width / 7)
        Button_Height = int(self.height / 22)
        self.BStart.size_hint = (None, None)
        self.BStart.width     = Button_Width
        self.BStart.height    = Button_Height
        self.BStart.x         = Xc - int(self.BStart.width * 0.5)
        self.BStart.y         = Yc - int(self.BStart.height * 0.5)
        self.BStart.background_normal = ''
        self.BStart.background_color  = (0, 0.39, 0.49, 1)
        tmpDate = date.today()
        strDate = tmpDate.strftime("%a - %b %d")
        self.BStart.text = strDate
        ##################################
        self.iPic.size_hint = (None, None)
        self.iPic.keep_ratio = True
        self.iPic.allow_stretch = True
        self.iPic.width  = int(self.width * 0.9)
        self.iPic.height = int((self.iPic.width * 48) / 64)
        self.iPic.x = Xc - int(self.iPic.width * 0.5)
        self.iPic.y = Yc - int(self.iPic.height * 0.5)
        if(self.iPic.parent != None):
            self.remove_widget(self.iPic)
        ##################################
        self.Show_Graph()
        return
    
    #################################################
    def Press_Authenticate(self, instance):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        GDrive = GoogleDrive(gauth) # Google Drive Class Object
        return

    #################################################
    def Show_Graph(self):
        ##################################
        converter = mdates.ConciseDateConverter()
        munits.registry[datetime.date] = converter
        munits.registry[datetime.datetime] = converter
        ##################################
        EndDate = date.today()
        d = timedelta(days=6)
        date1 = EndDate - d
        d = timedelta(days=1)
        ##################################
        # MatPlotLib Bar Chart Code
        YMin = 0
        YMax = 0
        Y_calories = []
        X_days     = []
        ##################################
        for i in range(7):
            Y = i * 200
            Y_calories.append(Y)
            X_days.append(date1)
            date1 = date1 + d
            if(Y > YMax):
                YMax = Y
        ##################################
        plt.clf()
        plt.cla()
        plt.ylim(YMin, YMax)
        width1 = float(0.5)
        plt.bar(x=X_days, height=Y_calories, width=width1, label='eaten', zorder=2)
        strNum = 'Past ' + str(7) + ' Days'
        ##################################
        # Show the major grid lines
        plt.grid(b=True, which='major', color='#444444', linestyle='-', alpha=0.5, zorder=1)
        ##################################
        # Show the minor grid lines
        plt.minorticks_on()
        ##################################
        str1 = 'Calories Eaten each Day '
        plt.title(str1)
        plt.xlabel(strNum)
        plt.ylabel('Calories per Day')
        plt.gcf()
        plt.savefig(fname='./Pic.png', format='png', transparent=True)
        ##################################
        Y_calories.clear()
        X_days.clear()
        ##################################
        self.iPic.reload()
        if(self.iPic.parent == None):
            self.add_widget(self.iPic)
        ##################################
        return


##############################################################
##############################################################
        
class LayoutsApp(MDApp):

    def __init__(self, **kwargs):
        super(LayoutsApp, self).__init__(**kwargs)
        self.Obj1 = Graphs()
        return

    def build(self):
        LayoutsApp.title = 'MatPlotLib: Hello World'
        self.Obj1.Initialize()
        return self.Obj1

##############################################################
##############################################################
    
if __name__ == "__main__":
    LayoutsApp().run()

