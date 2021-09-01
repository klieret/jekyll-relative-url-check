#!/usr/bin/env python3

# std
import subprocess
from pathlib import Path
import tempfile
import shutil
import random
from collections import defaultdict
import itertools
from typing import DefaultDict, Dict

# 3rd
import pytest

random.seed(a=123, version=2)

this_dir = Path(__file__).resolve().parent
main_dir = this_dir.parent

files: DefaultDict[str, Dict] = defaultdict(dict)
for state in ["failing", "passing"]:
    for suffix in ["markdown", "html"]:
        folder = this_dir / state / suffix
        files[state][suffix] = list(folder.iterdir())


def random_test(suffix, should_fail=False):
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmpdir = Path(tmpdirname)
        if should_fail:
            n_passing = random.randint(0, len(files["passing"][suffix]))
            n_failing = random.randint(1, len(files["failing"][suffix]))
        else:
            n_passing = random.randint(1, len(files["passing"][suffix]))
            n_failing = 0
        copy_files = random.choices(
            files["failing"][suffix], k=n_failing
        ) + random.choices(files["passing"][suffix], k=n_passing)
        print(copy_files)
        for f in copy_files:
            shutil.copy(f, tmpdir / f.name)
        subprocess.run(
            ["git", "init"],
            cwd=tmpdir,
        )
        subprocess.run(
            ["git", "config", "--global", "user.email", "you@example.com"],
            cwd=tmpdir,
        )
        subprocess.run(
            ["git", "config", "--global", "user.name", "you"],
            cwd=tmpdir,
        )
        subprocess.run(
            ["git", "add", "."],
            cwd=tmpdir,
        )
        subprocess.run(
            ["git", "commit", "-m", "test"],
            cwd=tmpdir,
        )
        exit_code = subprocess.run(
            [
                "pre-commit",
                "try-repo",
                str(main_dir.resolve()),
                f"jekyll-relative-url-check-{suffix}",
                "--verbose",
                "--all-files",
            ],
            cwd=tmpdir,
        ).returncode
        assert exit_code == 0 or should_fail, exit_code


@pytest.mark.parametrize(
    "suffix,should_fail", itertools.product(["markdown", "html"], [True, False])
)
def test_pre_commit(suffix, should_fail):
    for i in range(2):
        random_test(suffix=suffix, should_fail=should_fail)


@pytest.mark.parametrize(
    "suffix,failing", itertools.product(["markdown", "html"], [True, False])
)
def test_executable(suffix, failing):
    fs = "failing" if failing else "passing"
    these_files = files[fs][suffix]
    for f in these_files:
        rc = subprocess.run(
            [
                f"jekyll-relative-url-check-{suffix}",
                str(f),
            ],
        ).returncode
        assert rc == 0 or failing
