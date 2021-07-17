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

import os
import binascii

from core.badges import badges

class GhostModule:
    def __init__(self, ghost):
        self.ghost = ghost
        self.badges = badges()

        self.details = {
            'name': "screenshot",
            'authors': ['enty8080'],
            'description': "Take device screenshot.",
            'usage': "screenshot <local_path>",
            'type': "managing",
            'args': 1,
            'needs_args': True,
            'needs_root': False,
            'comments': ""
        }

    def run(self, args):
        screenshot_filename = "/sdcard/" + str(binascii.hexlify(os.urandom(5))) + ".png"
        print(self.badges.G + "Taking screenshot...")
        self.ghost.send_command("shell", "screencap " + screenshot_filename, False, False)
        self.ghost.download(screenshot_filename, args)
        self.ghost.send_command("shell", "rm " + screenshot_filename, False, False)
