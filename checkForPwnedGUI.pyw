import wx
import wx.adv
import checkForPwnedShared
import os


class UI(wx.Frame):

    def __init__(self, parent, title):
        super(UI, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):

        self.SetInitialSize((385, 300))
        self.panel = wx.Panel(self)

        self.fileTxt = wx.StaticText(self.panel, -1, "File location:")
        self.fileBrowse = wx.FilePickerCtrl(self.panel, -1)

        self.nameColTxt = wx.StaticText(self.panel, -1, "Name Col:")
        self.nameColCtrl = wx.SpinCtrl(self.panel, -1)

        self.pwColTxt = wx.StaticText(self.panel, -1, "Password Col:")
        self.pwColCtrl = wx.SpinCtrl(self.panel, -1)

        self.headerColTxt = wx.StaticText(self.panel, -1, "Header Col:")
        self.headerColYes = wx.RadioButton(
            self.panel, -1, label='Yes', style=wx.RB_GROUP)
        self.headerColNo = wx.RadioButton(self.panel, -1, label='No')

        self.runButton = wx.Button(self.panel, -1, "Run")
        self.runButton.Bind(wx.EVT_BUTTON, self.runCheck)

        gridSizer = wx.GridSizer(rows=5, cols=3, hgap=10, vgap=10)

        radioSizer = wx.BoxSizer(wx.HORIZONTAL)
        radioSizer.Add(self.headerColYes, 0, wx.ALL, 5)
        radioSizer.Add(self.headerColNo, 0, wx.ALL, 5)

        fileSizer = wx.BoxSizer(wx.HORIZONTAL)
        nameColSizer = wx.BoxSizer(wx.HORIZONTAL)
        pwColSizer = wx.BoxSizer(wx.HORIZONTAL)
        headerColSizer = wx.BoxSizer(wx.HORIZONTAL)

        gridSizer.Add(self.fileTxt, 0, wx.ALL, 10)
        gridSizer.Add(self.fileBrowse, 1, wx.ALL | wx.ALIGN_LEFT, 10)
        gridSizer.Add((1, -1), proportion=1)

        gridSizer.Add(self.nameColTxt, 0, wx.ALL, 10)
        gridSizer.Add(self.nameColCtrl, 0, wx.ALL | wx.ALIGN_LEFT, 10)
        gridSizer.Add((1, -1), proportion=1)

        gridSizer.Add(self.pwColTxt, 0, wx.ALL, 10)
        gridSizer.Add(self.pwColCtrl, 0, wx.ALL | wx.ALIGN_LEFT, 10)
        gridSizer.Add((1, -1),  proportion=1)

        gridSizer.Add(self.headerColTxt, 0, wx.ALL, 10)
        gridSizer.Add(radioSizer, 0, wx.ALL | wx.ALIGN_LEFT, 10)
        gridSizer.Add((1, -1),  proportion=1)

        gridSizer.Add((1, -1),  proportion=1)
        gridSizer.Add((1, -1),  proportion=1)
        gridSizer.Add(self.runButton, 0, wx.ALL, 10)

        self.panel.SetSizerAndFit(gridSizer)

    def runCheck(self, event):
        try:
            if not os.path.isfile(self.fileBrowse.GetPath()):
                raise ValueError('Invalid file path. Please try again.')
            resp = checkForPwnedShared.checkCSV(self.fileBrowse.GetPath(
            ), self.nameColCtrl.GetValue(), self.pwColCtrl.GetValue(), self.headerColYes.GetValue())
            wx.MessageBox(resp, 'Pwned Results', wx.OK)
        except ValueError as e:
            wx.MessageBox(str(e), 'Pwned Results', wx.OK)


def main():

    app = wx.App()
    ex = UI(None, title='Check for Pwned')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
