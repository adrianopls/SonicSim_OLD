
import wx

from classes.ui import interface

class SimApp(wx.App):
    
    def __init__(self):
        #
        _redirect =  False
        _filename = None
        _useBestVisual = False
        _clearSigInt = True
        #
        super().__init__(_redirect, _filename, 
                                       _useBestVisual, _clearSigInt
        ) 
        
        
    def OnInit(self):
        self.load_app_interface()
        return True        
    
 
    def load_app_interface(self):
        if not wx.App.Get():
            raise Exception('ERROR: wx.App not found.')    
        mwc = interface.load()
        mwc.Show()
        
        self.SetTopWindow(mwc)     