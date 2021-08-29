from pathlib import Path
from typing import Iterable


class RelativeURLHook:
    def __init__(self):
        self.absolute_url_regexs = []

    def check_file(self, file: Path):
        """Return False if issues were found, true if file is ok"""
        return self._check_file(file)

    def _check_file(self, file: Path):
        return self._check_text(file.read_text(), context=f"(in file {file})")

    def check_files(self, files: Iterable[Path]):
        return all(map(self._check_file, files))

    def _check_text(self, text: str, context=""):
        """Check text

        Args:
            text: Text to check
            context: String to be printed in issues found in this text that
                gives additional context (where is this text from, e.g. which
                file are we checking?)

        Returns:

        """
        found_any = False
        for line in text.split():
            found = set()
            for regex in self.absolute_url_regexs:
                found |= set(regex.findall(line))
            if found:
                print(
                    f"We believe we have found absolute URLS: {found} in this "
                    f"line: '{line}' ({context})"
                )
                found_any = True
        return not found_any
