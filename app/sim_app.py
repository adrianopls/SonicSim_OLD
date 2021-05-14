
import wx
from classes import class_register
from . import interface
#
from classes.UIManager import UIManager


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
        
        class_register.register_app_classes()
        
        self.load_app_interface()
        
        return True        
    
 
    def load_app_interface(self):

        if not wx.App.Get():
            raise Exception('ERROR: wx.App not found.')
            
        interface.load()
        mwc = interface.get_main_window_controller()
        mwc.Show()
        self.SetTopWindow(mwc.view)      

        
        
    #TODO: REMOVER ISSO!!    
    def get_manager_class(self, obj_tid):

        return UIManager    

    