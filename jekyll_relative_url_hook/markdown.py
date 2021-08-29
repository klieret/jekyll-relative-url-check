# std
import re
from typing import List
from pathlib import Path

# ours
from jekyll_relative_url_hook.abstract import RelativeURLHook


class MarkdownRelativeURLHook(RelativeURLHook):
    def __init__(self):
        super().__init__()
        self.absolute_url_regexs: List[re.Pattern] = [re.compile("\[[^]]*]\(/[^)]*\)")]

    def _check_file(self, file: Path):
        found_any = False
        for line in file.read_text().split():
            found = set()
            for regex in self.absolute_url_regexs:
                found |= set(regex.findall(line))
            if found:
                print(
                    f"We believe we have found absolute URLS: {found} in this"
                    f"line: '{line}' of {file}"
                )
                found_any = True
        return not found_any
