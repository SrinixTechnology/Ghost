#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020 EntySec
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

from core.badges import badges

class GhostModule:
    def __init__(self, ghost):
        self.ghost = ghost
        self.badges = badges()

        self.details = {
            'name': "wifi",
            'authors': ['enty8080'],
            'description': "Control device wifi service.",
            'usage': "wifi [on|off]",
            'type': "settings",
            'args': 1,
            'needs_args': True,
            'needs_root': False,
            'comments': ""
        }

    def run(self, args):
        if args in ['on', 'off']:
            if args == "on":
                self.ghost.send_command("shell", "svc wifi enable", False, False)
            else:
                self.ghost.send_command("shell", "svc wifi disable", False, False)
        else:
            print("Usage: " + self.usage)
