
import os
import wx
import wx.aui as aui


def load():
    
    frame = wx.Frame(None, wx.ID_ANY, title="SonicSim 0.1b", size=(800,800))
    mgr = aui.AuiManager(frame)
    mgr.GetArtProvider().SetColour(aui.AUI_DOCKART_BACKGROUND_COLOUR, 
                wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DFACE))
    mgr.GetArtProvider().SetColour(aui.AUI_DOCKART_INACTIVE_CAPTION_COLOUR,
                wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DFACE))   
    
    
    
    main_area_panel = wx.Panel(frame)
    main_area_panel.SetBackgroundColour('white')
    
    mgr.AddPane(main_area_panel, 
                        aui.AuiPaneInfo().Name("main_area_panel").CenterPane())    
    #
    
    
    # bmp_filename = "gripy_logo.jpg"
    # bmp = GripyBitmap(bmp_filename)
    # self._static_bmp = wx.StaticBitmap(self.main_area_panel, wx.ID_ANY, 
    #                             bmp, wx.Point(0, 0), 
    #                             bmp.GetSize()
    # )  
    

    #notebook = aui.AuiNotebook(main_area_panel)
    
    icon = wx.Icon("images/signal.bmp", wx.BITMAP_TYPE_ICO)       
    frame.SetIcon(icon)
    
    create_menu(frame)

    
    
    
    return frame



def create_menu(frame):
    menubar = wx.MenuBar()
    
    menu_model = wx.Menu()
    item_lm =  menu_model.Append(1001, "&Load model", "Load a model from file")
    frame.Bind(wx.EVT_MENU, on_open, id=1001)
    
    item_cm = menu_model.Append(-1, "&Create model", "Create a new model")
    item_cm.Enable(False)    
    menu_model.Append(-1, "&Save model", "Save a model to a file")
    menu_model.AppendSeparator()
    
    item_exit_app = menu_model.Append(wx.ID_EXIT, "Exit", "Exits aplication")

    #frame.Bind(wx.EVT_MENU, wx.App.g, id=wx.ID_EXIT)
    
    
    menubar.Append(menu_model, "Model")
    
  
    menu_sim = wx.Menu()  
    menu_sim.Append(-1, "Staggered grid", "")
    item_rsg = menu_sim.Append(-1, "Rotated Staggered grid", "")
    item_rsg.Enable(False)
    menubar.Append(menu_sim, "Simulation type")
    
    menu_about = wx.Menu()
    menubar.Append(menu_about, "About")
    
    
    frame.SetMenuBar(menubar)
    
    
    
    
    
    
    
    
#def frame_exit()
    
    
    
def on_open(*args, **kwargs):
    wildcard = "Load segmentated file (*.png)|*.png"
    try:
        fdlg = wx.FileDialog(wx.App.Get().GetTopWindow(), 
                             'Escolha o arquivo PGG', 
                             wildcard=wildcard, 
                             style=wx.FD_OPEN|wx.FD_FILE_MUST_EXIST
        )
        if fdlg.ShowModal() == wx.ID_OK:
            file_name = fdlg.GetFilename()
            dir_name = fdlg.GetDirectory()
            fdlg.Destroy()
        else:
            fdlg.Destroy()
            return
        fullfilename = os.path.join(dir_name, file_name)    
        #gripy_app = wx.App.Get()
        print(fullfilename)
    except Exception as e:
        print ('ERROR [on_open]:', str(e))
        raise   
    
    
    
    
    
    
    
    
    
    
    
    
    