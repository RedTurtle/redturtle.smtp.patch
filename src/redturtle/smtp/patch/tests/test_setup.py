# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID
from redturtle.smtp.patch.testing import (
    REDTURTLE_SMTP_PATCH_INTEGRATION_TESTING  # noqa: E501,
)

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that redturtle.smtp.patch is properly installed."""

    layer = REDTURTLE_SMTP_PATCH_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if redturtle.smtp.patch is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'redturtle.smtp.patch'))

    def test_browserlayer(self):
        """Test that IRedturtleSmtpPatchLayer is registered."""
        from redturtle.smtp.patch.interfaces import (
            IRedturtleSmtpPatchLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IRedturtleSmtpPatchLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = REDTURTLE_SMTP_PATCH_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['redturtle.smtp.patch'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if redturtle.smtp.patch is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'redturtle.smtp.patch'))

    def test_browserlayer_removed(self):
        """Test that IRedturtleSmtpPatchLayer is removed."""
        from redturtle.smtp.patch.interfaces import \
            IRedturtleSmtpPatchLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IRedturtleSmtpPatchLayer,
            utils.registered_layers())
