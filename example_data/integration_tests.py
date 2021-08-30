#!/usr/bin/env python3

import subprocess
from pathlib import Path
import tempfile
import shutil
import random

this_dir = Path(__file__).resolve().parent
main_dir = this_dir.parent
failing_dir = this_dir / "failing"
passing_dir = this_dir / "passing"

failing_files = list(failing_dir.iterdir())
passing_files = list(passing_dir.iterdir())


def random_test(should_fail=False):
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmpdir = Path(tmpdirname)
        if should_fail:
            n_passing = random.randint(0, len(passing_files))
            n_failing = random.randint(1, len(failing_files))
        else:
            n_passing = random.randint(1, len(passing_files))
            n_failing = 0
        copy_files = random.choices(failing_files, k=n_failing) + random.choices(
            passing_files, k=n_passing
        )
        print(copy_files)
        for f in copy_files:
            shutil.copy(f, tmpdir / f.name)
        opt = subprocess.run(
            [
                "pre-commit",
                "try-repo",
                str(main_dir.resolve()),
                "jekyll-relative-url-check-markdown",
                "--verbose",
                "--all-files",
            ],
            cwd=tmpdir,
        )
        if should_fail:
            assert opt.returncode != 0
        else:
            assert opt.returncode == 0


random_test()
