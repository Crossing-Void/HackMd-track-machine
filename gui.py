from Tkinter_template.base import Interface
from Tkinter_template.Assets.music import Music
from Tkinter_template.Assets.default_menu import canvas_cover
from Tkinter_template.Assets.default_dashboard import MusicPlayer


class Main(Interface):
    def __init__(self, title: str, icon=None, default_menu=True):
        super().__init__(title, icon, default_menu)
        self.canvas.config(bg='purple')
        self.__ini()

    def __ini(self):
        self.Musics = Music()
        self.Musicplayers = MusicPlayer(self.dashboard, self.Musics)
        self.default_menu.add_command(label="Covers", command=lambda: canvas_cover(
            self.canvas, self.canvas_side, self.side))


if __name__ == '__main__':
    app = Main("HackMd Tracking Machine", "favicon.ico")
    while True:
        app.canvas.update()
        app.Musicplayers.set_ball()
