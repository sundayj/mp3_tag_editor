import wx


class EditDialog(wx.Dialog):
    def __init__(self, mp3):
        title = f'Editing "{mp3.tag.title}"'
        super().__init__(parent=None, title=title)
        self.mp3 = mp3
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.artist = wx.TextCtrl(
            self, value=self.mp3.tag.artist)
        self.add_widgets('Artist', self.artist)
        self.album = wx.TextCtrl(
            self, value=self.mp3.tag.album)
        self.add_widgets('Album', self.album)
        self.title = wx.TextCtrl(
            self, value=self.mp3.tag.title)
        self.add_widgets('Title', self.title)
        btn_sizer = wx.BoxSizer()
        save_btn = wx.Button(self, label='Save')
        save_btn.Bind(wx.EVT_BUTTON, self.on_save)
        btn_sizer.Add(save_btn, 0, wx.ALL, 5)
        btn_sizer.Add(wx.Button(
            self, id=wx.ID_CANCEL), 0, wx.ALL, 5)
        self.main_sizer.Add(btn_sizer, 0, wx.CENTER)
        self.SetSizer(self.main_sizer)

    def add_widgets(self, label_text, text_ctrl):
        row_sizer = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self, label=label_text,
                              size=(50, -1))
        row_sizer.Add(label, 0, wx.ALL, 5)
        row_sizer.Add(text_ctrl, 1, wx.ALL | wx.EXPAND, 5)
        self.main_sizer.Add(row_sizer, 0, wx.EXPAND)

    def on_save(self, event):
        self.mp3.tag.artist = self.artist.GetValue()
        self.mp3.tag.album = self.album.GetValue()
        self.mp3.tag.title = self.title.GetValue()
        self.mp3.tag.save()
        self.Close()
