from base import Layout
from .. import command, utils

class Fullscreen(Layout):
    """
        Just like the Max layout, but hides all Gaps and Bars.
    """
    name = "fullscreen"
    def __init__(self):
        Layout.__init__(self)
        self.clients = []

    def up(self):
        if self.clients:
            utils.shuffleUp(self.clients)
            self.group.layoutAll()
            self.group.focus(self.clients[0], False)

    def down(self):
        if self.clients:
            utils.shuffleDown(self.clients)
            self.group.layoutAll()
            self.group.focus(self.clients[0], False)

    def clone(self, group):
        c = Layout.clone(self, group)
        c.clients = []
        return c

    def add(self, c):
        self.clients.insert(0, c)

    def remove(self, c):
        self.clients.remove(c)
        if self.clients:
            return self.clients[0]

    def configure(self, c):
        if self.clients and c is self.clients[0]:
            c.place(
                self.group.screen.x,
                self.group.screen.y,
                self.group.screen.width,
                self.group.screen.height,
                0,
                None
            )
            c.unhide()
        else:
            c.hide()

    def info(self):
        d = Layout.info(self)
        d["clients"] = [i.name for i in self.clients]
        return d

    def cmd_down(self):
        """
            Switch down in the window list.
        """
        self.down()

    def cmd_up(self):
        """
            Switch up in the window list.
        """
        self.up()
