from typing import List
from pathlib import Path
import sys

# ours
from jekyll_relative_url_check.html import HTMLRelativeURLHook
from jekyll_relative_url_check.markdown import MarkdownRelativeURLHook


def html_pre_commit(files: List[str]):
    ret = HTMLRelativeURLHook().check_files(map(Path, files))
    if not ret:
        sys.exit(111)


def markdown_pre_commit(files: List[str]):
    ret = MarkdownRelativeURLHook().check_files(map(Path, files))
    if not ret:
        sys.exit(111)
