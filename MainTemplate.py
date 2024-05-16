# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-370-gc831f1f7)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.grid

###########################################################################
## Class MainScreen
###########################################################################

class MainScreen ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 682,554 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel15 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel19 = wx.Panel( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self.m_panel19, wx.ID_ANY, u"Victoria State Accident Analyzing Tool", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer5.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel23 = wx.Panel( self.m_panel19, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer6 = wx.GridSizer( 0, 2, 5, 0 )

		self.m_panel10 = wx.Panel( self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.loadButton = wx.Button( self.m_panel10, wx.ID_ANY, u"Load Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.loadButton, 0, wx.ALL|wx.EXPAND, 5 )

		self.exportButton = wx.Button( self.m_panel10, wx.ID_ANY, u"Export Report", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.exportButton, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel10.SetSizer( gSizer3 )
		self.m_panel10.Layout()
		gSizer3.Fit( self.m_panel10 )
		gSizer6.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )

		self.searchbox = wx.SearchCtrl( self.m_panel23, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.searchbox.ShowSearchButton( True )
		self.searchbox.ShowCancelButton( False )
		gSizer6.Add( self.searchbox, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel23.SetSizer( gSizer6 )
		self.m_panel23.Layout()
		gSizer6.Fit( self.m_panel23 )
		bSizer5.Add( self.m_panel23, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel24 = wx.Panel( self.m_panel19, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_panel11 = wx.Panel( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		self.applyButton = wx.Button( self.m_panel11, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.applyButton, 0, wx.ALL|wx.EXPAND, 5 )

		regionListChoices = []
		self.regionList = wx.ComboBox( self.m_panel11, wx.ID_ANY, u"region", wx.DefaultPosition, wx.DefaultSize, regionListChoices, 0 )
		gSizer5.Add( self.regionList, 0, wx.ALL, 5 )


		self.m_panel11.SetSizer( gSizer5 )
		self.m_panel11.Layout()
		gSizer5.Fit( self.m_panel11 )
		gSizer4.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel12 = wx.Panel( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer61 = wx.GridSizer( 0, 4, 0, 0 )

		self.m_staticText14 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"start date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		gSizer61.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.startDateBox = wx.adv.DatePickerCtrl( self.m_panel12, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gSizer61.Add( self.startDateBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText15 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"end date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		gSizer61.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.endDateBox = wx.adv.DatePickerCtrl( self.m_panel12, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gSizer61.Add( self.endDateBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel12.SetSizer( gSizer61 )
		self.m_panel12.Layout()
		gSizer61.Fit( self.m_panel12 )
		gSizer4.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel24.SetSizer( gSizer4 )
		self.m_panel24.Layout()
		gSizer4.Fit( self.m_panel24 )
		bSizer5.Add( self.m_panel24, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel19.SetSizer( bSizer5 )
		self.m_panel19.Layout()
		bSizer5.Fit( self.m_panel19 )
		bSizer3.Add( self.m_panel19, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel20 = wx.Panel( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.dataTable = wx.grid.Grid( self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.dataTable.CreateGrid( 0, 0 )
		self.dataTable.EnableEditing( False )
		self.dataTable.EnableGridLines( True )
		self.dataTable.EnableDragGridSize( True )
		self.dataTable.SetMargins( 0, 0 )

		# Columns
		self.dataTable.AutoSizeColumns()
		self.dataTable.EnableDragColMove( False )
		self.dataTable.EnableDragColSize( False )
		self.dataTable.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.dataTable.AutoSizeRows()
		self.dataTable.EnableDragRowSize( False )
		self.dataTable.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.dataTable.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer8.Add( self.dataTable, 0, wx.ALL, 5 )


		self.m_panel20.SetSizer( bSizer8 )
		self.m_panel20.Layout()
		bSizer8.Fit( self.m_panel20 )
		bSizer3.Add( self.m_panel20, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel151 = wx.Panel( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3.Add( self.m_panel151, 1, wx.EXPAND |wx.ALL, 5 )

		self.goVisual = wx.Button( self.m_panel15, wx.ID_ANY, u"Make Visualisation Model", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.goVisual, 0, wx.ALL, 5 )


		self.m_panel15.SetSizer( bSizer3 )
		self.m_panel15.Layout()
		bSizer3.Fit( self.m_panel15 )
		bSizer2.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.loadButton.Bind( wx.EVT_BUTTON, self.load_data )
		self.exportButton.Bind( wx.EVT_BUTTON, self.export_report )
		self.searchbox.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.search )
		self.applyButton.Bind( wx.EVT_BUTTON, self.apply_filter )
		self.regionList.Bind( wx.EVT_COMBOBOX, self.region_list )
		self.goVisual.Bind( wx.EVT_BUTTON, self.go_visual )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def load_data( self, event ):
		event.Skip()

	def export_report( self, event ):
		event.Skip()

	def search( self, event ):
		event.Skip()

	def apply_filter( self, event ):
		event.Skip()

	def region_list( self, event ):
		event.Skip()

	def go_visual( self, event ):
		event.Skip()


