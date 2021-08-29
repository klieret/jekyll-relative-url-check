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
