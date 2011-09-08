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
from GitKraken.gtk import Views


class AddRepositoryDialog:
    """Dialog to add repositories to the Project Manager"""

    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file(Views.ADD_REPO_DIALOG)

        self.initialize_ui()

    def initialize_ui(self):
        self.dialog = self.builder.get_object("add_repository_dialog")
        self.repo_name_entry =  self.builder.get_object("repo_name_entry")
        self.repo_location_button = self.builder.get_object("repo_location_button")
        self.builder.connect_signals(self)

    def show(self):
        self.dialog.show()

    def hide(self):
        self.dialog.hide()

    def run(self):
        return self.dialog.run()

    def on_response_event(self, widget, event=None):
        self.hide()
        return True

    def on_delete_event(self, widget, event=None):
        self.hide()
        return True

    def on_cancel_button_clicked_event(self, widget, event=None):
        self.hide()
        return True

    def on_file_set_event(self, widget, data=None):
        print data

    def on_ok_button_clicked_event(self, widget, event=None):
        repo_name_entry = self.repo_name_entry.get_text()
        #repo_location_button
