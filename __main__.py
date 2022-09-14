#!/usr/bin/env python
#
# Copyright (c) 2022, Raimonds Cicans
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

import wx


class MainFrame(wx.Frame):
    """
    Main application's frame
    """

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(MainFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)

        # put some text with a larger bold font on it
        st = wx.StaticText(pnl, label="Jokes In Crazy Hiragana/Katakana")
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        # and create a sizer to manage the layout of child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        pnl.SetSizer(sizer)

        # create a menu bar
        self.make_menu_bar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to JICHK!")

    def make_menu_bar(self):
        file_menu = wx.Menu()
        next_item = file_menu.Append(-1, "&Next joke...\tCtrl-N", "Next joke")
        file_menu.AppendSeparator()
        exit_item = file_menu.Append(wx.ID_EXIT)

        help_menu = wx.Menu()
        about_item = help_menu.Append(wx.ID_ABOUT)

        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "&File")
        menu_bar.Append(help_menu, "&Help")
        self.SetMenuBar(menu_bar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.on_next_item, next_item)
        self.Bind(wx.EVT_MENU, self.on_exit_item, exit_item)
        self.Bind(wx.EVT_MENU, self.on_about_item, about_item)


    def on_exit_item(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


    def on_next_item(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")


    def on_about_item(self, event):
        """Display an About Dialog"""
        wx.MessageBox("Jokes In Crazy Hiragana/Katakana\n\nCopyright (c) 2022, Raimonds Cicans",
                      "About JICHK",
                      wx.OK | wx.ICON_INFORMATION | wx.CENTRE)


if __name__ == '__main__':
    app = wx.App()
    frm = MainFrame(None, title='Jokes In Crazy Hiragana/Katakana')
    frm.Show()
    app.MainLoop()
