#
# Project:   retdec-python
# Copyright: (c) 2015 by Petr Zemek <s3rvac@gmail.com> and contributors
# License:   MIT, see the LICENSE file for more details
#

"""Tests for the :mod:`retdec.exceptions` module."""

import unittest

from retdec.exceptions import AuthenticationError
from retdec.exceptions import MissingAPIKeyError
from retdec.exceptions import UnknownAPIError


class MissingAPIKeyErrorTests(unittest.TestCase):
    """Tests for :class:`retdec.exceptions.MissingAPIKeyError`."""

    def test_has_correct_description(self):
        ex = MissingAPIKeyError()
        self.assertIn('API key', str(ex))
        self.assertIn('RETDEC_API_KEY', str(ex))


class AuthenticationErrorTests(unittest.TestCase):
    """Tests for :class:`retdec.exceptions.AuthenticationError`."""

    def test_has_correct_description(self):
        ex = AuthenticationError()
        self.assertIn('API key', str(ex))
        self.assertIn('failed', str(ex))


class UnknownAPIErrorTests(unittest.TestCase):
    """Tests for :class:`retdec.exceptions.UnknownAPIError`."""

    def test_has_correct_attributes(self):
        ex = UnknownAPIError(401, 'message', 'description')
        self.assertEqual(ex.code, 401)
        self.assertEqual(ex.message, 'message')
        self.assertEqual(ex.description, 'description')

    def test_str_gives_description(self):
        ex = UnknownAPIError(401, 'message', 'description')
        self.assertEqual(str(ex), 'description')
