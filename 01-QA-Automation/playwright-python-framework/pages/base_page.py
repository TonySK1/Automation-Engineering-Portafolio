from urllib.parse import urljoin

from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url.rstrip("/")

    def navigate(self, path: str = "") -> None:
        """
        Navigate to a relative application path.
        """
        if path.startswith(("http://", "https://")):
            raise ValueError("Only relative paths are allowed")

        url = urljoin(f"{self.base_url}/", path.lstrip("/"))

        self.page.goto(url)

    def get_tittle(self) -> str:
        """
        Return the current document title
        """
        return self.page.title()

    def get_current_url(self) -> str:
        """
        Return the current page URL
        """
        return self.page.url
