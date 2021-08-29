# std
import re
from typing import List

# ours
from jekyll_relative_url_hook.abstract import RelativeURLHook


class MarkdownRelativeURLHook(RelativeURLHook):
    def __init__(self):
        super().__init__()
        self.absolute_url_regexs: List[re.Pattern] = [
            re.compile(r"\[[^]]*]\(/[^)]*\)")
        ]

    def _check_text(self, text: str):
        found_any = False
        for line in text.split():
            found = set()
            for regex in self.absolute_url_regexs:
                found |= set(regex.findall(line))
            if found:
                print(
                    f"We believe we have found absolute URLS: {found} in this"
                    f"line: '{line}'"
                )
                found_any = True
        return not found_any
