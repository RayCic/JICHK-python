#!/usr/bin/env python
#
# Copyright (c) 2022, Raimonds Cicans
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import wx
from wx.lib import sized_controls


# Install a custom displayhook to keep Python from setting the global
# _ (underscore) to the value of the last evaluated expression.
# If we don't do this, our mapping of _ to gettext can get overwritten.
# This is useful/needed in interactive debugging with PyShell.
def _display_hook(obj):
    """
    Custom display hook to prevent Python stealing '_'.
    """

    if obj is not None:
        print(repr(obj))


# Add translation macro to builtin similar to what gettext does.
_ = wx.GetTranslation

# ---------------------------------------------------------------------------
class CustomDialog(sized_controls.SizedDialog):

    def __init__(self, settings, *args, **kwargs):
        super(CustomDialog, self).__init__(*args, **kwargs)
        self.settings = settings
        self.SetClientSize(wx.Size(1000, 700))
        pane = self.GetContentsPane()

        values = [_("Hiragana"), _("Katakana")]
        self.rbox = wx.RadioBox(pane, label=_("Alphabet"),
                                          choices=values, style=wx.RA_SPECIFY_COLS)
        self.rbox.SetSelection(settings["alphabet"])

        self.list = wx.ListCtrl(pane, -1, style=wx.LC_REPORT)
        headers = ["-", "A / А", "I / И", "U / У", "E / Э", "O / О"]
        for i, j in enumerate(headers):
                self.list.InsertColumn(col=i, heading=j, format=wx.LIST_FORMAT_CENTER)

        data = [
            ["",        "あ / ア", "い / イ", "う / ウ", "え / エ", "お / オ"],
            ["K- / К-", "か / カ", "き / キ", "く / ク", "け / ケ", "こ / コ"],
            ["S- / С-", "さ / サ", "し / シ", "す / ス", "せ / セ", "そ / ソ"],
            ["T- / Т-", "た / タ", "ち / チ", "つ / ツ", "て / テ", "と / ト"],
            ["N- / Н-", "な / ナ", "に / ニ", "ぬ / ヌ", "ね / ネ", "の / ノ"],
            ["H- / Х-", "は / ハ", "ひ / ヒ", "ふ / フ", "へ / ヘ", "ほ / ホ"],
            ["M- / М-", "ま / マ", "み / ミ", "む / ム", "め / メ", "も / モ"],
            ["R- / Р-", "ら / ラ", "り / リ", "る / ル", "れ / レ", "ろ / ロ"],
            ["W- / В-", "わ / ワ", "",        "",       "",       "を / ヲ"],
            ["",        "",       "",        "ん / ン", "",       ""      ],
        ]

        for y, x in enumerate(data):
            index = self.list.InsertItem(y, x[0])
            for i in range(1, 6):
                self.list.SetItem(index, i, x[i])

        pane_btns = sized_controls.SizedPanel(pane)
        pane_btns.SetSizerType('horizontal')

        button_ok = wx.Button(pane_btns, wx.ID_OK, label='OK')
        button_ok.Bind(wx.EVT_BUTTON, self.on_ok)

        button_ok = wx.Button(pane_btns, wx.ID_CANCEL, label='Cancel')
        button_ok.Bind(wx.EVT_BUTTON, self.on_cancel)

        self.Fit()

    def on_ok(self, event):
        self.settings["alphabet"] = self.rbox.GetSelection()
        self.EndModal(wx.ID_OK)

    def on_cancel(self, event):
        self.EndModal(wx.ID_CANCEL)

    def get_settings(self):
        return self.settings


# ---------------------------------------------------------------------------


class MainFrame(wx.Frame):
    """
    Main application's frame
    """

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(MainFrame, self).__init__(*args, **kw)

        self.settings = {"alphabet": 0}

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
        self.SetStatusText(_("Welcome to JICHK!"))

    # -----------------------------------------------------------------------

    def make_menu_bar(self):
        file_menu = wx.Menu()
        next_item = file_menu.Append(-1, _("&Next joke...\tCtrl-N"), _("Next joke"))
        file_menu.AppendSeparator()
        pref_item = file_menu.Append(wx.ID_PREFERENCES)
        file_menu.AppendSeparator()
        exit_item = file_menu.Append(wx.ID_EXIT)

        help_menu = wx.Menu()
        about_item = help_menu.Append(wx.ID_ABOUT)

        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, _("&File"))
        menu_bar.Append(help_menu, _("&Help"))
        self.SetMenuBar(menu_bar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.on_next_item, next_item)
        self.Bind(wx.EVT_MENU, self.on_pref_item, pref_item)
        self.Bind(wx.EVT_MENU, self.on_exit_item, exit_item)
        self.Bind(wx.EVT_MENU, self.on_about_item, about_item)

    def on_exit_item(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)

    def on_next_item(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")

    def on_pref_item(self, event):
        """Say hello to the user."""
        settings_dialog = CustomDialog(self.settings, None, title=_("Preferences"))
        result = settings_dialog.ShowModal()
        if result == wx.ID_OK:
            self.settings = settings_dialog.get_settings()
        settings_dialog.Destroy()

    def on_about_item(self, event):
        """Display an About Dialog"""
        wx.MessageBox(_("Jokes In Crazy Hiragana/Katakana\n\nCopyright (c) 2022, Raimonds Cicans"),
                      _("About JICHK"),
                      wx.OK | wx.ICON_INFORMATION | wx.CENTRE)


# ---------------------------------------------------------------------------

class MyApp(wx.App):
    locale = None
    language = "LANGUAGE_DEFAULT"

    def OnInit(self):
        # Set Current directory to the one containing this file
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        self.SetAppName('JICHK')

        self.init_i18n()

        # Create the main window
        frm = MainFrame(None, title=_("Jokes In Crazy Hiragana/Katakana"))
        self.SetTopWindow(frm)

        frm.Show()

        return True

    def init_i18n(self):
        """
        ...
        """

        # Set locale for wxWidgets.
        # You would define wx.Locale in your wx.App.OnInit class.
        # Setup the Locale
        self.locale = wx.Locale(getattr(wx, self.language))
        path = os.path.abspath("./locale") + os.path.sep
        self.locale.AddCatalogLookupPathPrefix(path)
        self.locale.AddCatalog(self.GetAppName())


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
