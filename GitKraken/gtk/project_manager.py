#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# GitKraken - a git client for the GNOME desktop
# Copyright (c) 2011 - Kunal Sarkhel
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------

from gi.repository import Gtk as gtk
from dialogs import AddRepositoryDialog
from GitKraken.gtk import Views


class ProjectManager:
    """
    Project Manager that displays the projects and allows the user to add,
    group, and delete projects.
    """

    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file(Views.PROJECT_MANAGER_GLADE)

        self.window = self.builder.get_object("MainWindow")
        self.builder.connect_signals(self)

        self.initialize_ui()

    def initialize_ui(self):
        self.add_repo_dialog = AddRepositoryDialog()

    def quit_app(self, widget, event=None):
        gtk.main_quit()

    def open_add_repository_dialog(self, widget, event=None):
        #self.add_repo_dialog.show()
        results = self.add_repo_dialog.run()

    def main(self):
        self.window.show_all()
        gtk.main()
