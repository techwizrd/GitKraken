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

from distutils.core import setup
from distutils.command.install_data import install_data
from subprocess import call

import glob
import os

### CONSTANTS ################################################################

DATA_DIR        = "share/gitkraken"
GLOBAL_ICON_DIR = "share/icons/hicolor"

print("""This install script has not been written yet.
Perhaps you would like to contribute?""")
