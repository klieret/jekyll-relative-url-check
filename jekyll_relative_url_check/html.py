# std
import re
from typing import List

# ours
from jekyll_relative_url_check.abstract import RelativeURLHook


class HTMLRelativeURLHook(RelativeURLHook):
    def __init__(self):
        super().__init__()
        self.absolute_url_regexs: List[re.Pattern] = list(
            map(
                re.compile,
                [
                    r'href="/[^"]*"',
                    r"href='/[^']*'",
                    r'src="/[^"]*"',
                    r"src='/[^']*'",
                ],
            )
        )  # type: ignore
