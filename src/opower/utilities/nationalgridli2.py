"""National Grid Long Island NY."""

import logging
from typing import Optional

import aiohttp

from .base import UtilityBase
from .oidchelper import async_auth_oidc

_LOGGER = logging.getLogger(__name__)


class NationalGridLI2(UtilityBase):
    """National Grid Long Island NY."""

    @staticmethod
    def name() -> str:
        """Return the name of the utility."""
        return "National Grid (Long Island)"

    @staticmethod
    def subdomain() -> str:
        """Return the opower.com subdomain for this utility."""
        return "ngli"

    @staticmethod
    def timezone() -> str:
        """Return the timezone."""
        return "America/New_York"

    BASE_URL = "https://login.nationalgrid.com"
    TENANT_ID = "0e1366c5-731c-42b3-90d3-508039d9e70f"
    POLICY = "B2C_1A_NationalGrid_convert_merge_signin"
    CLIENT_ID = "36488660-e86a-4a0d-8316-3df49af8d06d"
    REDIRECT_URI = "https://myaccount.nationalgrid.com/auth-landing"
    APPLICATION_URI = f"{BASE_URL}/"
    SCOPE_AUTH = "openid profile offline_access"
    SCOPE_ACCESS = f"{CLIENT_ID} openid profile offline_access"
    SELF_ASSERTED_ENDPOINT = "SelfAsserted"
    POLICY_CONFIRM_ENDPOINT = "api/CombinedSigninAndSignup/confirmed"

    @staticmethod
    async def async_login(
        session: aiohttp.ClientSession,
        username: str,
        password: str,
        optional_mfa_secret: Optional[str],
    ) -> Optional[str]:
        """Perform the login process and return an access token."""
        _LOGGER.debug("Starting login process for National Grid")
        return await async_auth_oidc(
            username,
            password,
            NationalGridLI2.BASE_URL,
            NationalGridLI2.TENANT_ID,
            NationalGridLI2.POLICY,
            NationalGridLI2.CLIENT_ID,
            NationalGridLI2.REDIRECT_URI,
            NationalGridLI2.SCOPE_AUTH,
            NationalGridLI2.SCOPE_ACCESS,
            NationalGridLI2.SELF_ASSERTED_ENDPOINT,
            NationalGridLI2.POLICY_CONFIRM_ENDPOINT,
        )
