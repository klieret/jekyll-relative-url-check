from abc import ABC, abstractmethod
from pathlib import Path
from typing import Iterable


class RelativeURLHook(ABC):
    pass

    def check_file(self, file: Path):
        """Return False if issues were found, true if file is ok"""
        return self._check_file(file)

    def _check_file(self, file: Path):
        return self._check_text(file.read_text())

    def check_files(self, files: Iterable[Path]):
        return any(map(self._check_file, files))

    @abstractmethod
    def _check_text(self, text: str):
        pass
