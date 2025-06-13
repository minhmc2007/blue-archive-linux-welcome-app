#!/usr/bin/env python3
# =================================================================
# =          Original Authors: Brad Heffernan & Erik Dubois       =
# =          Forked and modified by: minhmc2007                   =
# =================================================================
import gi
import os
import subprocess
import threading
import shutil

import ui.GUI as GUI
from ui.MessageDialog import MessageDialog

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf, GLib

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

class Main(Gtk.Window):
    def __init__(self):
        super(Main, self).__init__(title="Blue Archive Linux Welcome")
        self.set_border_width(10)
        self.set_default_size(700, 450)
        self.set_icon_from_file(os.path.join(base_dir, "images/bal-icon.png"))
        self.set_position(Gtk.WindowPosition.CENTER)

        config_dir = os.path.join(GUI.home, ".config", GUI.APP_NAME)
        if not os.path.exists(config_dir):
            os.makedirs(config_dir)
            with open(GUI.Settings, "w") as f:
                f.write("autostart=True")
            if os.path.isfile(GUI.dot_desktop):
                shutil.copy(GUI.dot_desktop, GUI.autostart)

        self.calamares_polkit = "/usr/bin/calamares"
        self.session = os.environ.get("XDG_SESSION_TYPE")

        GUI.GUI(self, Gtk, GdkPixbuf)

    def on_install_clicked(self, widget):
        if shutil.which(self.calamares_polkit):
            subprocess.Popen([self.calamares_polkit, "-d"])
        else:
            self.show_message_dialog("Installer Not Found", "Calamares installer not found at\n/usr/bin/calamares")

    def on_gparted_clicked(self, widget):
        if shutil.which("gparted"):
            subprocess.Popen(["pkexec", "gparted"])
        else:
            self.show_message_dialog("GParted Not Found", "Please install 'gparted' package to use this feature.")

    def startup_toggle(self, widget):
        if widget.get_active():
            if os.path.isfile(GUI.dot_desktop):
                os.makedirs(os.path.dirname(GUI.autostart), exist_ok=True)
                shutil.copy(GUI.dot_desktop, GUI.autostart)
        else:
            if os.path.isfile(GUI.autostart):
                os.unlink(GUI.autostart)
        self.save_settings(widget.get_active())

    def save_settings(self, state):
        with open(GUI.Settings, "w") as f:
            f.write(f"autostart={state}")

    def load_settings(self):
        if os.path.isfile(GUI.Settings):
            with open(GUI.Settings, "r") as f:
                line = f.readline()
                if "autostart" in line:
                    return line.split("=")[1].strip().capitalize() == "True"
        return True

    def show_message_dialog(self, title, message):
        dialog = MessageDialog(parent=self, title=title, message=message)
        dialog.run()
        dialog.destroy()

if __name__ == "__main__":
    w = Main()
    w.connect("delete-event", Gtk.main_quit)
    w.show_all()
    Gtk.main()
