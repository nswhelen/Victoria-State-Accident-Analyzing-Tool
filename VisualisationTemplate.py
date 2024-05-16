# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-370-gc831f1f7)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Visualisation
###########################################################################

class Visualisation ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 682,554 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel15 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel19 = wx.Panel( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self.m_panel19, wx.ID_ANY, u"Visualisation Report", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer5.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel23 = wx.Panel( self.m_panel19, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer6 = wx.GridSizer( 2, 3, 5, 0 )

		self.exportVisual = wx.Button( self.m_panel23, wx.ID_ANY, u"Export Report", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.exportVisual, 0, wx.ALL|wx.EXPAND, 5 )

		self.loadRaw = wx.Button( self.m_panel23, wx.ID_ANY, u"Load Raw Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.loadRaw, 0, wx.ALL|wx.EXPAND, 5 )

		self.back = wx.Button( self.m_panel23, wx.ID_ANY, u"Back to Filter", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.back, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_panel111 = wx.Panel( self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer51 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button101 = wx.Button( self.m_panel111, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer51.Add( self.m_button101, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_panel131 = wx.Panel( self.m_panel111, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer81 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText161 = wx.StaticText( self.m_panel131, wx.ID_ANY, u"title", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )

		gSizer81.Add( self.m_staticText161, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.title = wx.TextCtrl(self.m_panel131, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		gSizer81.Add(self.title, 0, wx.ALL | wx.EXPAND, 5)

		self.m_panel131.SetSizer( gSizer81 )
		self.m_panel131.Layout()
		gSizer81.Fit( self.m_panel131 )
		gSizer51.Add( self.m_panel131, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel111.SetSizer( gSizer51 )
		self.m_panel111.Layout()
		gSizer51.Fit( self.m_panel111 )
		gSizer6.Add( self.m_panel111, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel121 = wx.Panel( self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer611 = wx.GridSizer( 0, 2, 0, 0 )

		xVariableChoices = []
		self.xVariable = wx.ComboBox( self.m_panel121, wx.ID_ANY, u"x-axis", wx.DefaultPosition, wx.DefaultSize, xVariableChoices, 0 )
		gSizer611.Add( self.xVariable, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		yVariableChoices = []
		self.yVariable = wx.ComboBox( self.m_panel121, wx.ID_ANY, u"y-axis", wx.DefaultPosition, wx.DefaultSize, yVariableChoices, 0 )
		gSizer611.Add( self.yVariable, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel121.SetSizer( gSizer611 )
		self.m_panel121.Layout()
		gSizer611.Fit( self.m_panel121 )
		gSizer6.Add( self.m_panel121, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel122 = wx.Panel(self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		gSizer811 = wx.GridSizer(0, 1, 0, 0)

		chartTypeChoices = []
		# Set the parent of wx.ComboBox to self.chartType
		self.chartType = wx.ComboBox(self.m_panel122, wx.ID_ANY, u"select a chart type", wx.DefaultPosition,
											 wx.DefaultSize, chartTypeChoices, 0)
		gSizer811.Add(self.chartType, 1, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

		self.m_panel122.SetSizer(gSizer811)
		self.m_panel122.Layout()
		gSizer811.Fit(self.m_panel122)
		gSizer6.Add(self.m_panel122, 1, wx.ALL | wx.EXPAND, 5)

		self.m_panel23.SetSizer(gSizer6)
		self.m_panel23.Layout()
		gSizer6.Fit(self.m_panel23)
		bSizer5.Add(self.m_panel23, 1, wx.EXPAND | wx.ALL, 5)

		# self.chartType = wx.Panel(self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		# gSizer811 = wx.GridSizer(0, 1, 0, 0)
		#
		# chartTypeChoices = []
		# # Set the parent of wx.ComboBox to self.chartType
		# self.chartTypeComboBox = wx.ComboBox(self.chartType, wx.ID_ANY, u"select a chart type", wx.DefaultPosition,
		# 									 wx.DefaultSize, chartTypeChoices, 0)
		# gSizer811.Add(self.chartTypeComboBox, 1, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)
		#
		# self.chartType.SetSizer(gSizer811)
		# self.chartType.Layout()
		# gSizer811.Fit(self.chartType)
		# gSizer6.Add(self.chartType, 1, wx.ALL | wx.EXPAND, 5)
		#
		# self.m_panel23.SetSizer( gSizer6 )
		# self.m_panel23.Layout()
		# gSizer6.Fit( self.m_panel23 )
		# bSizer5.Add( self.m_panel23, 1, wx.EXPAND |wx.ALL, 5 )



		self.m_panel19.SetSizer( bSizer5 )
		self.m_panel19.Layout()
		bSizer5.Fit( self.m_panel19 )
		bSizer3.Add( self.m_panel19, 1, wx.EXPAND |wx.ALL, 5 )

		self.visual_panel = wx.Panel(self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		bSizer3.Add(self.visual_panel, 1, wx.EXPAND | wx.ALL, 5)

		self.m_panel15.SetSizer(bSizer3)
		self.m_panel15.Layout()
		bSizer3.Fit(self.m_panel15)
		bSizer2.Add(self.m_panel15, 1, wx.EXPAND | wx.ALL, 5)

		self.SetSizer(bSizer2)
		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.exportVisual.Bind(wx.EVT_BUTTON, self.export_report)
		self.loadRaw.Bind(wx.EVT_BUTTON, self.load_data)
		self.back.Bind(wx.EVT_BUTTON, self.back_main)
		self.m_button101.Bind(wx.EVT_BUTTON, self.apply_visual_filter)
		self.xVariable.Bind(wx.EVT_COMBOBOX, self.x_variable)
		self.yVariable.Bind(wx.EVT_COMBOBOX, self.y_variable)
		self.chartType.Bind(wx.EVT_COMBOBOX, self.chart_type)

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def export_report( self, event ):
		event.Skip()

	def load_data( self, event ):
		event.Skip()

	def back_main( self, event ):
		event.Skip()

	def apply_visual_filter( self, event ):
		event.Skip()

	def x_variable( self, event ):
		event.Skip()

	def y_variable( self, event ):
		event.Skip()

	def chart_type( self, event ):
		event.Skip()


