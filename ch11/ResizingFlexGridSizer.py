#! /usr/bin/env python
# coding:utf-8

import wx
from BlockWindow import BlockWindow

labels = 'one two three four five six seven eight nine'.split()

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Resizing Flex Grid Sizer')
        self.sizer = wx.FlexGridSizer(rows = 3, cols = 3, hgap = 5, vgap = 5)
        for label in labels:
            bw = BlockWindow(self, label = label)
            self.sizer.Add(bw, 0, 0)
        center = self.FindWindowByName('five')
        center.SetMinSize((150,50))
        self.sizer.AddGrowableCol(0,1)
        self.sizer.AddGrowableCol(1,2)
        self.sizer.AddGrowableCol(2,1)
        self.sizer.AddGrowableRow(0,1)
        self.sizer.AddGrowableRow(1,5)
        self.sizer.AddGrowableRow(2,1)
        self.sizer.SetFlexibleDirection(wx.VERTICAL)
        self.sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_ALL)
        #self.sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
        #self.sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        self.SetSizer(self.sizer)
        self.Fit()

class App(wx.App):
    def OnInit(self):
        self.f = TestFrame()
        self.f.Show()
        return True

if __name__ == "__main__":
    App().MainLoop()
