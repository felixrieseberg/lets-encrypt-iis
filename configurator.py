"""IIS Configuration"""
import logging
import os
import re
import shutil
import socket
import subprocess
import sys

import zope.interface

from letsencrypt.acme import challenges

from letsencrypt.client import achallenges
from letsencrypt.client import constants
from letsencrypt.client import errors
from letsencrypt.client import interfaces
from letsencrypt.client import le_util
from letsencrypt.client import reverter

class IISConfigurator(object):
    # pylint: disable=too-many-instance-attributes,too-many-public-methods
    """IIS configurator.

    .. warning:: This plugin is a stub!

    :ivar config: Configuration.
    :type config: :class:`~letsencrypt.client.interfaces.IConfig`

    :ivar str save_notes: Human-readable config change notes

    :ivar reverter: saves and reverts checkpoints
    :type reverter: :class:`letsencrypt.client.reverter.Reverter`

    """
    zope.interface.implements(interfaces.IAuthenticator, interfaces.IInstaller)

    description = "IIS"

    def __init__(self, config):
        """Initialize an IIS Configurator.
        """
        self.config = config

    def prepare():
        """Prepare the installer.

         Finish up any additional initialization.

         :raises letsencrypt.client.errors.LetsEncryptMisconfigurationError`:
             when full initialization cannot be completed.
         :raises letsencrypt.errors.LetsEncryptNoInstallationError`:
             when the necessary programs/files cannot be located.

        """

    def get_all_names():
        """Returns all names that may be authenticated."""

    def deploy_cert(domain, cert, key, cert_chain=None):
        """Deploy certificate.

        :param str domain: domain to deploy certificate
        :param str cert: certificate filename
        :param str key: private key filename

        """

    def enhance(domain, enhancement, options=None):
        """Perform a configuration enhancement.

        :param str domain: domain for which to provide enhancement
        :param str enhancement: An enhancement as defined in
            :const:`~letsencrypt.client.constants.ENHANCEMENTS`
        :param options: Flexible options parameter for enhancement.
            Check documentation of
            :const:`~letsencrypt.client.constants.ENHANCEMENTS`
            for expected options for each enhancement.

        """

    def supported_enhancements():
        """Returns a list of supported enhancements.

        :returns: supported enhancements which should be a subset of
            :const:`~letsencrypt.client.constants.ENHANCEMENTS`
        :rtype: :class:`list` of :class:`str`

        """

    def get_all_certs_keys():
        """Retrieve all certs and keys set in configuration.

        :returns: tuples with form `[(cert, key, path)]`, where:

            - `cert` - str path to certificate file
            - `key` - str path to associated key file
            - `path` - file path to configuration file

        :rtype: list

        """

    def save(title=None, temporary=False):
        """Saves all changes to the configuration files.

        Both title and temporary are needed because a save may be
        intended to be permanent, but the save is not ready to be a full
        checkpoint

        :param str title: The title of the save. If a title is given, the
            configuration will be saved as a new checkpoint and put in a
            timestamped directory. `title` has no effect if temporary is true.

        :param bool temporary: Indicates whether the changes made will
            be quickly reversed in the future (challenges)

        """

    def rollback_checkpoints(rollback=1):
        """Revert `rollback` number of configuration checkpoints."""

    def view_config_changes():
        """Display all of the LE config changes."""

    def config_test():
        """Make sure the configuration is valid."""

    def restart():
        """Restart or refresh the server content."""

    ##-------------------------------------------------------------------------------
    # IAuthenticator
    ##-------------------------------------------------------------------------------
    
    def get_chall_pref(domain):
        """Return list of challenge preferences.

        :param str domain: Domain for which challenge preferences are sought.

        :returns: List of challege types (subclasses of
            :class:`letsencrypt.acme.challenges.Challenge`) with the most
            preferred challenges first. If a type is not specified, it means the
            Authenticator cannot perform the challenge.
        :rtype: list

        """ 

    def perform(achalls):
        """Perform the given challenge.

        :param list achalls: Non-empty (guaranteed) list of
            :class:`~letsencrypt.client.achallenges.AnnotatedChallenge`
            instances, such that it contains types found within
            :func:`get_chall_pref` only.

        :returns: List of ACME
            :class:`~letsencrypt.acme.challenges.ChallengeResponse` instances
            or if the :class:`~letsencrypt.acme.challenges.Challenge` cannot
            be fulfilled then:

            ``None``
              Authenticator can perform challenge, but not at this time.
            ``False``
              Authenticator will never be able to perform (error).

        :rtype: :class:`list` of
            :class:`letsencrypt.acme.challenges.ChallengeResponse`

        """

    def cleanup(achalls):
        """Revert changes and shutdown after challenges complete.

        :param list achalls: Non-empty (guaranteed) list of
            :class:`~letsencrypt.client.achallenges.AnnotatedChallenge`
            instances, a subset of those previously passed to :func:`perform`.

        """

    def more_info():
        """Human-readable string to help the user.

        Should describe the steps taken and any relevant info to help the user
        decide which Authenticator to use.

        """