# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import redturtle.smtp.patch


class RedturtleSmtpPatchLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=redturtle.smtp.patch)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'redturtle.smtp.patch:default')


REDTURTLE_SMTP_PATCH_FIXTURE = RedturtleSmtpPatchLayer()


REDTURTLE_SMTP_PATCH_INTEGRATION_TESTING = IntegrationTesting(
    bases=(REDTURTLE_SMTP_PATCH_FIXTURE,),
    name='RedturtleSmtpPatchLayer:IntegrationTesting',
)


REDTURTLE_SMTP_PATCH_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(REDTURTLE_SMTP_PATCH_FIXTURE,),
    name='RedturtleSmtpPatchLayer:FunctionalTesting',
)


REDTURTLE_SMTP_PATCH_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        REDTURTLE_SMTP_PATCH_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='RedturtleSmtpPatchLayer:AcceptanceTesting',
)
