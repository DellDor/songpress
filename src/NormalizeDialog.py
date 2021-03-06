# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug 25 2009)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import i18n
i18n.register('NormalizeDialog')
# -*- coding: utf-8 -*- 


###########################################################################
## Class NormalizeDialog
###########################################################################

class NormalizeDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Cleanup Chords"), pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.label1 = wx.StaticText( self, wx.ID_ANY, _(u"Notation:"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label1.Wrap( -1 )
		bSizer2.Add( self.label1, 0, wx.ALL, 5 )
		
		fromNotationChoices = []
		self.fromNotation = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, fromNotationChoices, 0 )
		self.fromNotation.SetSelection( 0 )
		bSizer2.Add( self.fromNotation, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();
		
		bSizer1.Add( m_sdbSizer1, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
		
		# Connect Events
		self.fromNotation.Bind( wx.EVT_CHOICE, self.OnFromNotation )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnFromNotation( self, event ):
		event.Skip()
	

