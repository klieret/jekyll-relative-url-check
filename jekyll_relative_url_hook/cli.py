from typing import List
from pathlib import Path

# ours
from jekyll_relative_url_hook.html import HTMLRelativeURLHook
from jekyll_relative_url_hook.markdown import MarkdownRelativeURLHook


def html_pre_commit(files: List[str]):
    HTMLRelativeURLHook().check_files(map(Path, files))


def markdown_pre_commit(files: List[str]):
    MarkdownRelativeURLHook().check_files(map(Path, files))
