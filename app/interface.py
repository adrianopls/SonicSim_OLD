# -*- coding: utf-8 -*-

import wx

import app

from classes.UIManager import UIManager



# def create_properties_dialog(obj_uid, size=None):
#     if not size:
#         size = (300, 330)
#     UIM = UIManager()
#     try:      
#         dlg = UIM.create('object_properties_dialog_controller')
#         #print(dlg)
#         dlg.obj_uid = obj_uid
#         dlg.view.SetSize(size)
#         dlg.view.ShowModal()            
#     except Exception as e:
#         print ('\nERROR create_properties_dialog:', e)
#         raise
#     finally:
#         UIM.remove(dlg.uid)    


"""
Load interface data.
"""
def load_application_UI_data(fullfilename):
    pass
    #UIM = UIManager()
    #UIM.load_application_state_from_file(fullfilename)


"""
Load interface data.
"""
def load_user_UI_data(fullfilename):
    pass
    #UIM = UIManager()
    #UIM.load_user_state_from_file(fullfilename)


"""
Save application structure UI data.
"""        
def save_UI_application_data(fullfilename):
    pass
    #UIM = UIManager()
    #UIM.save_application_state_to_file(fullfilename)
 
 
"""
Save user UI data.
"""        
def save_UI_user_data(fullfilename):
    pass
    #UIM = UIManager()
    #UIM.save_user_state_to_file(fullfilename)
    #UIM._save_state_to_file(self.UIM_file)     


"""
Loads Gripy Initial Interface (MainWindow and it's children).
"""
def load():
    #load_UI_file = True        
    load_UI_file = False
    
    gripy_app = wx.GetApp()
    #gripy_app = app.gripy_app.GripyApp.Get()
    
    if not gripy_app:
        raise Exception('ERRO grave.')
    
    
    UIM = UIManager()
    
    if load_UI_file:
        """
        Load basic app from file.            
        """
        load_application_UI_data(gripy_app._gripy_app_state.get('app_UI_file'))
        load_user_UI_data(gripy_app._gripy_app_state.get('user_UI_file'))
        mwc = UIM.list('main_window_controller')[0]      
    else:
        """
        Construct the application itself.
        """    
        mwc = UIM.create('main_window_controller', 
                         icon='images/signal.bmp',
                         size=(1000, 800),
                         pos=(100, 100),
                         #maximized=True,
                         title="SonicSim 0.1b"
        )

       # """

        # Menubar
        menubar_ctrl = UIM.create('menubar_controller', mwc.uid)
        
        

        mc_model = UIM.create('menu_controller', menubar_ctrl.uid, 
                                label=u"&Model")            
        UIM.create('menu_item_controller', mc_model.uid, 
                label="&Load model", 
                help="Load a model from file",
                id=wx.ID_OPEN,
                callback='app.menu_functions.on_open_model'
        )        
        UIM.create('menu_item_controller', mc_model.uid, 
                label="&Create model", 
                help="Create a new model",
                enabled=False
                #id=wx.ID_OPEN,
                #callback='app.menu_functions.on_open'
        )          
        UIM.create('menu_item_controller', mc_model.uid, 
                label="&Save model", 
                help="Save a model into file",
                enabled=False
                #id=wx.ID_OPEN,
                #callback='app.menu_functions.on_open'
        )         
        UIM.create('menu_item_controller', mc_model.uid, 
                        kind=wx.ITEM_SEPARATOR
        )    
        UIM.create('menu_item_controller', mc_model.uid, 
                label=u'Exit', 
                help=u'Exits application.',
                id=wx.ID_EXIT#,
                #callback='app.menu_functions.on_exit'
        )           
        
        
        mc_sim = UIM.create('menu_controller', menubar_ctrl.uid, 
                                label="Simulation type")                          
        UIM.create('menu_item_controller', mc_sim.uid, 
                label="Staggered grid"
                #callback='app.menu_functions.on_open'
        )             
        UIM.create('menu_item_controller', mc_sim.uid, 
                label="Rotated Staggered grid",
                enabled=False
                #callback='app.menu_functions.on_open'
        )              
 
        
        mc_about = UIM.create('menu_controller', menubar_ctrl.uid, 
                        label="About")    
        
 
        
#        UIM.create('tree_controller', mwc.uid)      
 
       
        
 #                 label=u'&Open', 
#                 help=u'Open GriPy Project (*.pgg)',
#                 id=wx.ID_OPEN,
#                 callback='app.menu_functions.on_open'
#         )       
        
#         mc_edit = UIM.create('menu_controller', menubar_ctrl.uid, label=u"&Edit")
#         mc_well = UIM.create('menu_controller', menubar_ctrl.uid, label=u"&Well")
#         mc_precond = UIM.create('menu_controller', menubar_ctrl.uid, label=u"&Preconditioning")
#         mc_model = UIM.create('menu_controller', menubar_ctrl.uid, label=u"&Modeling")
#         mc_interp = UIM.create('menu_controller', menubar_ctrl.uid, label=u"&Interpretation")
# #        mc_infer = UIM.create('menu_controller', menubar_ctrl.uid, label=u"&Inference")
#         #mc_specdecom = UIM.create('menu_controller', menubar_ctrl.uid, label=u"&SpecDecom")
#         mc_tools = UIM.create('menu_controller', menubar_ctrl.uid, label=u"&Tools")
#         mc_plugins = UIM.create('menu_controller', menubar_ctrl.uid, label=u"&Plugins")
        
        
        
        
        # Project Menu
#         UIM.create('menu_item_controller', mc_project.uid, 
#                 label=u'&New project', 
#                 help=u'Create a new empty GriPy Project.',
#                 id=wx.ID_NEW,
#                 callback='app.menu_functions.on_new'
#         )
#         UIM.create('menu_item_controller', mc_project.uid, 
#                        kind=wx.ITEM_SEPARATOR
#         )
#         UIM.create('menu_item_controller', mc_project.uid, 
#                 label=u'&Open', 
#                 help=u'Open GriPy Project (*.pgg)',
#                 id=wx.ID_OPEN,
#                 callback='app.menu_functions.on_open'
#         )
#         UIM.create('menu_item_controller', mc_project.uid, 
#                 label=u'&Save', 
#                 help=u'Save GriPy Project',
#                 id=wx.ID_SAVE,
#                 callback='app.menu_functions.on_save'
#         )   
#         UIM.create('menu_item_controller', mc_project.uid, 
#                 label=u'&Save as', 
#                 help=u'Save GriPy Project with a new name',
#                 id=wx.ID_SAVEAS, 
#                 callback='app.menu_functions.on_save_as'
#         ) 
#         UIM.create('menu_item_controller', mc_project.uid, 
#                        kind=wx.ITEM_SEPARATOR
#         )
        
       
        
#         mc_import = UIM.create('menu_controller', mc_project.uid, 
#                                       label=u"&Import",
#                                       help=u"Import file"
#         )
        
        
        
#         UIM.create('menu_item_controller', mc_import.uid, 
#                 label=u"SEG-Y Well Gather", 
#                 help=u'Import a SEG-Y Seismic file as Well Gather',
#                 callback='app.menu_functions.on_import_segy_well_gather'
#         )  
#         UIM.create('menu_item_controller', mc_import.uid, 
#                 label=u"SEG-Y Seismic", 
#                 help=u'Import a SEG-Y Seismic file to current GriPy Project',
#                 callback='app.menu_functions.on_import_segy_seis'
#         )  
#         UIM.create('menu_item_controller', mc_import.uid, 
#                 label=u"SEG-Y Velocity", 
#                 help=u'Import a SEG-Y Velocity file to current GriPy Project',
#                 callback='app.menu_functions.on_import_segy_vel'
#         )  
#         mc_export = UIM.create('menu_controller', mc_project.uid, 
#                                       label=u"Export",
#                                       help=u"Export file"
#         )      
#         UIM.create('menu_item_controller', mc_export.uid, 
#                 label=u"LAS File", 
#                 help=u'Export a LAS file from a well in current GriPy Project',
#                 callback='app.menu_functions.on_export_las'
#         )
        
        
        
        
#         UIM.create('menu_item_controller', mc_project.uid, 
#                        kind=wx.ITEM_SEPARATOR
#         )
#         UIM.create('menu_item_controller', mc_project.uid, 
#                 label=u'Exit', 
#                 help=u'Exits GRIPy application.',
#                 id=wx.ID_EXIT,
#                 callback='app.menu_functions.on_exit'
#         )            
        
        
        
#         # Edit Menu
#         """
#         mc_partition = UIM.create('menu_controller', mc_edit.uid, 
#                                       label=u"&Partition",
#                                       help=u"Create / Edit Partition"
#         )
#         """
#         mc_rocktable = UIM.create('menu_controller', mc_edit.uid, 
#                                       label=u"&Rock Table",
#                                       help=u"Create / Edit RockTable"
#         )
#         UIM.create('menu_item_controller', mc_rocktable.uid, 
#                 label=u"New Rock Table", 
#                 help=u'New Rock Table',
#                 callback='app.menu_functions.on_new_rocktable'
#         )
#         UIM.create('menu_item_controller', mc_rocktable.uid, 
#                 label=u"Edit Rock Table", 
#                 help=u'Edit Rock Table',
#                 callback='app.menu_functions.on_edit_rocktable'
#         )

#         UIM.create('menu_item_controller', mc_edit.uid, 
#                 label=u'&Well Plot', 
#                 help=u'Well Plot',
#                 callback='app.menu_functions.on_new_wellplot'
#         ) 
#         UIM.create('menu_item_controller', mc_edit.uid, 
#                 label=u'&Crossplot', 
#                 help=u'Crossplot',
#                 callback='app.menu_functions.on_new_crossplot'
#         )            
# #        UIM.create('menu_item_controller', mc_edit.uid, 
# #                label=u'&Rock', 
# #                help=u'Initialize rock model',
# #                callback='app.menu_functions.on_rock'
# #        )
# #        UIM.create('menu_item_controller', mc_edit.uid, 
# #                label=u'&Fluid', 
# #                help=u'Initialize fluid model',
# #                callback='app.menu_functions.on_fluid'
# #        )             
        
        
#         # Well Menu
#         UIM.create('menu_item_controller', 
#                    mc_well.uid, 
#                    label=u"New well",
#                    help=u"Create well",
#                    callback='app.menu_functions.on_create_well'
#         ) 
#         # Import Well
#         mc_import_well = UIM.create('menu_controller', 
#                                     mc_well.uid, 
#                                     label=u"&Import Well"
#         )
#         UIM.create('menu_item_controller', 
#                    mc_import_well.uid, 
#                    label=u"LAS File", 
#                    help=u'Import a LAS file to current GriPy Project',
#                    callback='app.menu_functions.on_import_las'
#         )
#         UIM.create('menu_item_controller', 
#                    mc_import_well.uid, 
#                    label=u"LIS File", 
#                    help=u'Import a LIS file to current GriPy Project',
#                    callback='app.menu_functions.on_import_lis'
#         )       

#         UIM.create('menu_item_controller', 
#                    mc_import_well.uid, 
#                    label=u"DLIS File", 
#                    help=u'Import a DLIS file to current GriPy Project',
#                    callback='app.menu_functions.on_import_dlis'
#         )  
#         UIM.create('menu_item_controller', 
#                    mc_import_well.uid, 
#                    label=u"ODT File", 
#                    help=u'Import a ODT file to current GriPy Project',
#                    callback='app.menu_functions.on_import_odt'
#         )        
     
#         #
#         UIM.create('menu_item_controller', mc_well.uid, 
#                        kind=wx.ITEM_SEPARATOR
#         )

#         UIM.create('menu_item_controller', mc_well.uid, 
#                 label=u"Create Synthetic Log",
#                 callback='app.menu_functions.on_create_synthetic'
#         )
        
        """
        ### Trabalho Roseane
        UIM.create('menu_item_controller', mc_well.uid, 
                       kind=wx.ITEM_SEPARATOR
        )
        
        UIM.create('menu_item_controller', mc_well.uid, 
                label=u'PoroPerm Cross-Plot',
                callback='app.menu_functions.create_poro_perm_xplot'
        )           
        
        UIM.create('menu_item_controller', mc_well.uid, 
                label=u'Winland Cross-Plot',
                callback='app.menu_functions.create_winland_xplot'
        )        
        UIM.create('menu_item_controller', mc_well.uid, 
                label=u'Stratigraphic Modified lorenz Plot (SMLP)',
                callback='app.menu_functions.create_SMLP_xplot'
        )        
        UIM.create('menu_item_controller', mc_well.uid, 
                label=u'Modified lorenz Plot (MLP)',
                callback='app.menu_functions.create_MLP_xplot'
        )          
        UIM.create('menu_item_controller', mc_well.uid, 
                label=u'Depth vs Acumulated KH',
                callback='app.menu_functions.create_Depth_vs_kHAcum_xplot'
        )      
        ### FIM - Trabalho Roseane
        """
        
        """
        # Inference Menu
        UIM.create('menu_item_controller', mc_infer.uid, 
                label=u"Avo PP", 
                callback='app.menu_functions.teste6'
        )  
        UIM.create('menu_item_controller', mc_infer.uid, 
                label=u"Avo PP-PS", 
                callback='app.menu_functions.teste7'
        )  
        """
        
#         # Interpretation Menu
#         mc_specdecom = UIM.create('menu_controller', mc_interp.uid,  
#                                       label=u"Spectral Decomposition",
#                                       help=u"Spectral Decomposition",
#         )
#         UIM.create('menu_item_controller', mc_specdecom.uid, 
#                 label=u"Continuous Wavelet Transform", 
#                 callback='app.menu_functions.on_cwt'
#         )          
#         mc_attributes = UIM.create('menu_controller', mc_interp.uid,  
#                                       label=u"Attributes",
#                                       help=u"Attributes",
#         )
#         UIM.create('menu_item_controller', mc_attributes.uid, 
#                 label=u"Phase Rotation", 
#                 callback='app.menu_functions.on_phase_rotation'
#         )

#         UIM.create('menu_item_controller', mc_attributes.uid, 
#                 label=u"Hilbert Attributes", 
#                 callback='app.menu_functions.on_hilbert_attributes'
#         )             
        
#         # Modeling Menu  
#         UIM.create('menu_item_controller', mc_model.uid, 
#                 label=u"Create 2/3 layers model", 
#                 callback='app.menu_functions.on_create_model'
#         )   
#         UIM.create('menu_item_controller', mc_model.uid,
#                        kind=wx.ITEM_SEPARATOR
#         )        
#         UIM.create('menu_item_controller', mc_model.uid,
#                 label=u"Aki-Richards PP", 
#                 callback='app.menu_functions.on_akirichards_pp'
#         )      
#         UIM.create('menu_item_controller', mc_model.uid, 
# 				label=u"Reflectivity Method", 
# 				callback='app.menu_functions.ReflectivityModel'
#         )
#         #UIM.create('menu_item_controller', mc_model.uid,
#         #               kind=wx.ITEM_SEPARATOR
#         #) 
#         #UIM.create('menu_item_controller', mc_model.uid,
#         #        label=u"Poisson ratio", 
#         #        callback='app.menu_functions.on_poisson_ratio'
#         #)            


#         # Tools Menu
#         UIM.create('menu_item_controller', mc_tools.uid, 
#                 label="Coding Console", help=u"Gripy Coding Console", 
#                 callback='app.menu_functions.on_coding_console'
#         )  
#         #


#         """
#         # Debug Menu
#         UIM.create('menu_item_controller', mc_debug.uid, 
#                 label=u"Load Wilson Synthetics", 
#                 callback='app.menu_functions.on_load_wilson'
#         )  
           
#         UIM.create('menu_item_controller', mc_debug.uid, 
#                 label=u"Load Stack North Viking Data", 
#                 callback='app.menu_functions.teste10'
#         )   
#         UIM.create('menu_item_controller', mc_debug.uid, 
#                 label=u"Teste 11", 
#                 callback='app.menu_functions.teste11'
#         ) 
     
#         UIM.create('menu_item_controller', mc_debug.uid, 
#                 label=u'Calc Well Time from Depth curve', 
#                 callback='app.menu_functions.calc_well_time_from_depth'
#         ) 
 
#         UIM.create('menu_item_controller', mc_debug.uid, 
#                        kind=wx.ITEM_SEPARATOR
#         )
        
#         UIM.create('menu_item_controller', mc_debug.uid, 
#                 label="Load Teste 2019", 
#                 callback='app.menu_functions.on_load_teste_2019'
#         )  
#         """
        
#         # Fim Main Menu Bar

       

#         # Object Manager TreeController                                                          
#         UIM.create('tree_controller', mwc.uid)                            
            
#         # Main ToolBar 
#         tbc = UIM.create('toolbar_controller', mwc.uid)
#         UIM.create('toolbartool_controller', tbc.uid,
#                        label=u"New project", 
#                        bitmap='new_file-30.png',
#                        help='New project', 
#                        long_help='Start a new Gripy project, closes existing',
#                        callback='app.menu_functions.on_new'
#         )            
#         UIM.create('toolbartool_controller', tbc.uid,
#                        label=u"Abrir projeto", 
#                        bitmap='open_folder-30.png',
#                        help='Abrir projeto', 
#                        long_help='Abrir projeto GriPy',
#                        callback='app.menu_functions.on_open'
#         )
#         UIM.create('toolbartool_controller', tbc.uid,
#                        label=u"Salvar projeto", 
#                        bitmap='save_close-30.png',
#                        help='Salvar projeto', 
#                        long_help='Salvar projeto GriPy',
#                        callback='app.menu_functions.on_save'
#         )
#         UIM.create('toolbartool_controller', tbc.uid,
#                        label=u"Well Plot", 
#                        bitmap='oil_rig-30.png',
#                        help='Well Plot', 
#                        long_help='Well Plot',
#                        callback='app.menu_functions.on_new_wellplot'
#         )
#         UIM.create('toolbartool_controller', tbc.uid,
#                        label=u"Crossplot", 
#                        bitmap='scatter_plot-30.png',
#                        help='Crossplot', 
#                        long_help='Crossplot',
#                        callback='app.menu_functions.on_new_crossplot'
#         )               


#         # StatusBar
#         UIM.create('statusbar_controller', mwc.uid, 
#             label='Bem vindo ao ' + \
#             app.gripy_app.GripyApp.Get()._gripy_app_state.get('app_display_name')
#         )  
        
        
        

    # _do_initial_tests()




def get_main_window_controller():    
    UIM = UIManager()
    mwc = UIM.list('main_window_controller')[0]   
    return mwc
   
    
    
"""
Funcao reservada para alguns testes 
"""
def _do_initial_tests():
    pass
   

  

