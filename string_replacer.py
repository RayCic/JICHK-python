#!/usr/bin/env python
#
# Copyright (c) 2022, Raimonds Cicans
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re


# Taken from https://stackoverflow.com/a/69195618
class StringReplacer:

    def __init__(self, replacements):
        patterns = sorted(replacements, key=len, reverse=True)
        self.replacements = [replacements[k] for k in patterns]
        self.pattern = re.compile('|'.join(("({})".format(p) for p in patterns)), re.IGNORECASE)

        def tr(matcher):
            index = next((index for index, value in enumerate(matcher.groups()) if value), None)
            return self.replacements[index]

        self.tr = tr

    def __call__(self, string):
        return self.pattern.sub(self.tr, string)
