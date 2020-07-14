
import matplotlib.pyplot as plt

from kivy.core.window import Window

from kivy.uix.image import Image

from kivymd.app import MDApp

from kivymd.uix.floatlayout import MDFloatLayout


##############################################################
##############################################################

class Graphs(MDFloatLayout):

    #################################################
    def __init__(self, **kwargs):
        super(Graphs, self).__init__(**kwargs)
        self.LPad   = 0
        self.LWidth = 0
        self.Yc     = 0
        self.Xo     = 0
        self.iPic   = Image(source = 'Pic.png')
        return

    #################################################
    def Initialize(self):
        self.size = Window.size
        #############################################
        if(self.iPic.parent != None):
            self.remove_widget(self.iPic)
        #############################################
        self.LPad   = int(self.width * 0.05)
        self.LWidth = int(self.width * 0.9)
        self.Yc = int(self.height * 0.5)
        self.Xo = self.LPad
        #############################################
        self.Pie_CFP_Graph()
        return

    #################################################
    def Pie_CFP_Graph(self):
        #############################################
        # MatPlotLib code
        Pie_Labels = 'Cats', 'Monkeys', 'Dogs'
        Pie_Sizes  = [33, 10, 56]
        plt.clf()
        plt.cla()
        plt.pie(Pie_Sizes, labels=Pie_Labels, autopct='%1.1f%%')
        plt.axis('equal')
        plt.title("Hello World Pie Chart")
        plt.gcf()
        plt.savefig(fname='Pic.png', format='png', transparent=True)
        #############################################
        self.iPic.size_hint = (None, None)
        self.iPic.keep_ratio = True
        self.iPic.allow_stretch = True
        self.iPic.width  = self.LWidth
        self.iPic.height = int((self.iPic.width * 48) / 64)
        self.iPic.x = self.Xo
        self.iPic.y = self.Yc - int(self.iPic.height * 0.5)
        self.iPic.reload()
        if(self.iPic.parent == None):
            self.add_widget(self.iPic)
        #############################################
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

