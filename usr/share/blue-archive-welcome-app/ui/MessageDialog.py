import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MessageDialog(Gtk.MessageDialog):
    def __init__(self, parent, title, message):
        super().__init__(
            transient_for=parent,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text=title,
        )
        self.format_secondary_text(message)
