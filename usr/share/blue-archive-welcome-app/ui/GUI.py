# =================================================================
# =          Original Authors: Brad Heffernan & Erik Dubois       =
# =          Forked and modified by: minhmc2007                   =
# =================================================================
import os
import getpass
from os.path import expanduser

# --- App Paths & Constants ---
APP_NAME = "blue-archive-welcome-app"
home = expanduser("~")
username = getpass.getuser()
user = "liveuser"
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

Settings = os.path.join(home, ".config", APP_NAME, "settings.conf")
dot_desktop = f"/usr/share/applications/{APP_NAME}.desktop"
autostart = os.path.join(home, ".config", "autostart", f"{APP_NAME}.desktop")

def GUI(self, Gtk, GdkPixbuf):
    self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
    self.vbox.set_border_width(10)
    self.add(self.vbox)

    # --- Header ---
    headerbar = Gtk.HeaderBar()
    headerbar.set_title("Blue Archive Linux")
    headerbar.set_subtitle("Welcome")
    headerbar.set_show_close_button(True)
    self.set_titlebar(headerbar)

    # --- Main Content ---
    pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(os.path.join(base_dir, "images/bal.png"), 200, 200)
    image = Gtk.Image().new_from_pixbuf(pixbuf)
    self.vbox.pack_start(image, False, False, 0)

    label_welcome = Gtk.Label(xalign=0.5)
    self.vbox.pack_start(label_welcome, False, False, 0)

    # Buttons change depending on session
    hbox_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox_buttons.set_halign(Gtk.Align.CENTER)
    self.vbox.pack_start(hbox_buttons, False, False, 10)

    if username == user:
        label_welcome.set_markup(f"<big><b>Welcome to the Live Session</b></big>")
        
        button_install = Gtk.Button(label="Install System")
        button_install.get_child().set_markup("<span size='large'><b>Install Blue Archive Linux</b></span>")
        button_install.connect("clicked", self.on_install_clicked)
        
        button_gparted = Gtk.Button(label="Partition Manager")
        button_gparted.connect("clicked", self.on_gparted_clicked)
        
        hbox_buttons.pack_start(button_gparted, False, False, 0)
        hbox_buttons.pack_start(button_install, True, True, 0)

    else:
        label_welcome.set_markup(f"<big><b>Welcome to Blue Archive Linux, {username}!</b></big>")
        label_info_text = Gtk.Label(label="This is your first login. You can disable this welcome screen below.")
        label_info_text.set_justify(Gtk.Justification.CENTER)
        self.vbox.pack_start(label_info_text, False, False, 0)

    # --- Footer ---
    hbox_footer = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    self.vbox.pack_end(hbox_footer, False, True, 0)

    check_autostart = Gtk.CheckButton(label="Show this window on startup")
    check_autostart.connect("toggled", self.startup_toggle)
    check_autostart.set_active(self.load_settings())
    if username != user:
        hbox_footer.pack_start(check_autostart, True, False, 0)

    # --- Credits Label ---
    credits_label = Gtk.Label()
    credits_label.set_markup("<small><i>Forked from ArcoLinux Welcome App by the ArcoLinux Team. Maintained by minhmc2007.</i></small>")
    credits_label.set_halign(Gtk.Align.END)
    hbox_footer.pack_end(credits_label, False, False, 0)
