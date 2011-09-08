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

"""
Contains all the views for GitKraken
"""

import os


class Views:
    """Contains all the views for GitKraken"""

    current_path = os.path.dirname(os.path.abspath(__file__))

    PROJECT_MANAGER_GLADE = os.path.join(current_path, "project_manager.glade")
    ADD_REPO_DIALOG = os.path.join(current_path, "add_repository_dialog.glade")
