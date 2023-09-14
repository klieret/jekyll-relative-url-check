from typing import List, Union
from pathlib import Path
import sys

# ours
from jekyll_relative_url_check.html import HTMLRelativeURLHook
from jekyll_relative_url_check.markdown import MarkdownRelativeURLHook


def html_pre_commit(files: Union[List[str], None] = None):
    if files is None:
        files = sys.argv[1:]
    ret = HTMLRelativeURLHook().check_files(map(Path, files))
    if not ret:
        sys.exit(111)


def markdown_pre_commit(files: Union[List[str], None] = None):
    if files is None:
        files = sys.argv[1:]
    ret = MarkdownRelativeURLHook().check_files(map(Path, files))
    if not ret:
        sys.exit(111)
