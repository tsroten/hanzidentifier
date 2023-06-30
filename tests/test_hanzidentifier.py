# -*- coding: utf-8 -*-
"""The test module for Hanzi Identifier."""

import unittest

import hanzidentifier


UNKNOWN = "Hello my name is Thomas."
SIMPLIFIED = "Thomas 说：你好！"
TRADITIONAL = "Thomas 說：你好！"
BOTH = "你好！"
MIXED = "Country in simplified: 国. Country in traditional: 國."


class TestIdentifyFunction(unittest.TestCase):
    def test_return_unknown(self):
        self.assertEqual(hanzidentifier.UNKNOWN, hanzidentifier.identify(UNKNOWN))

    def test_return_simplified(self):
        self.assertEqual(hanzidentifier.SIMPLIFIED, hanzidentifier.identify(SIMPLIFIED))

    def test_return_traditional(self):
        self.assertEqual(
            hanzidentifier.TRADITIONAL, hanzidentifier.identify(TRADITIONAL)
        )

    def test_return_both(self):
        self.assertEqual(hanzidentifier.BOTH, hanzidentifier.identify(BOTH))

    def test_return_mixed(self):
        self.assertEqual(hanzidentifier.MIXED, hanzidentifier.identify(MIXED))

    def test_count_chinese(self):
        self.assertEqual(
            hanzidentifier.count_chinese(BOTH),
            2,
        )
        self.assertEqual(
            hanzidentifier.count_chinese(SIMPLIFIED),
            3,
        )


class TestHelperFunctions(unittest.TestCase):
    def test_has_chinese(self):
        self.assertFalse(hanzidentifier.has_chinese(UNKNOWN))
        self.assertTrue(hanzidentifier.has_chinese(BOTH))

    def test_is_simplified(self):
        self.assertTrue(hanzidentifier.is_simplified(SIMPLIFIED))
        self.assertFalse(hanzidentifier.is_simplified(MIXED))
        self.assertTrue(hanzidentifier.is_simplified(BOTH))
        self.assertFalse(hanzidentifier.is_simplified(TRADITIONAL))
        self.assertFalse(hanzidentifier.is_simplified(UNKNOWN))

    def test_is_traditional(self):
        self.assertFalse(hanzidentifier.is_traditional(SIMPLIFIED))
        self.assertFalse(hanzidentifier.is_traditional(MIXED))
        self.assertTrue(hanzidentifier.is_traditional(BOTH))
        self.assertTrue(hanzidentifier.is_traditional(TRADITIONAL))
        self.assertFalse(hanzidentifier.is_traditional(UNKNOWN))
