# -*- coding: utf-8 -*-

from .context import stravaAnalytics
from stravaAnalytics.util.data import Junk

from unittest import TestCase


class AdvancedTestSuite(TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(stravaAnalytics.hmm())

    def test_junk(self):
        j = Junk()
        self.assertEqual("we stuff", j.stuff())
