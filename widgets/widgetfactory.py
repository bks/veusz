# widget factory
# tools to generate any type of plot widget you want

#    Copyright (C) 2004 Jeremy S. Sanders
#    Email: Jeremy Sanders <jeremy@jeremysanders.net>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
##############################################################################

# $Id$

class WidgetFactory:
    """Class to help produce any type of widget you want by name."""

    def __init__(self):
        """Initialise the class."""
        self.regwidgets = {}

    def register(self, classobj):
        """Register a class with the factory."""
        self.regwidgets[classobj.typename] = classobj

    def makeWidget(self, widgetname, *args, **optargs):
        """Make a new widget of the appropriate type."""
        return self.regwidgets[widgetname]( *args, **optargs )

    def listWidgets(self):
        """Return an array of the widgets the factory can make."""
        names = self.regwidgets.keys()
        names.sort()
        return names

# singleton
thefactory = WidgetFactory()
