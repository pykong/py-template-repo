from http import HTTPStatus

import httpx

from ..config import Config


def check_url(config: Config) -> bool | None:
    """Check if URL is reachable.

    Returns:
        bool | None: True if URL is reachable, False if not, None if URL is not set.

    """
    if not config.url:
        return None

    response = httpx.get(str(config.url))
    return response.status_code == HTTPStatus.OK
