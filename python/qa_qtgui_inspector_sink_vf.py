#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import gr, gr_unittest
from gnuradio import blocks
import inspector_swig as inspector

class qa_qtgui_inspector_sink_vf (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # no signal processing done -> nothing to test
        self.tb.run ()
        # check data


if __name__ == '__main__':
    gr_unittest.run(qa_qtgui_inspector_sink_vf, "qa_qtgui_inspector_sink_vf.xml")
