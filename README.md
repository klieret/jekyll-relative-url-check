# Jekyll: Enforce enforce URLs relative to site.baseurl

[![gh actions](https://github.com/klieret/jekyll-relative-url-check/actions/workflows/test.yaml/badge.svg)](https://github.com/klieret/jekyll-relative-url-check/actions)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/klieret/jekyll-relative-url-check/main.svg)](https://results.pre-commit.ci/latest/github/klieret/jekyll-relative-url-check/main)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![License](https://img.shields.io/github/license/klieret/jekyll-relative-url-check.svg)](https://github.com/klieret/jekyll-relative-url-check/blob/main/LICENSE.txt)
[![PR welcome](https://img.shields.io/badge/PR-Welcome-%23FF8300.svg)](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project)

A [pre-commit hook](https://pre-commit.com/) that enforces that all links
in a Jekyll project are relative to `{{ site.baseurl }}`.

The reasoning behind this is that links like `[link](/absolute/link)` will break if the site is not
directly deployed at `domain.com`, but e.g. at `user.github.io/projectname`.

## Examples

The following lines should raise errors:

Markdown:

```markdown
[link](/absolute/link)
![pic](/absolute/picture.png)
```

HTML:

```html
href="/absolute/link"
src="/absolute/picture.png"
```

## Installation & usage

### As a pre-commit hook

Include the following snippet in your pre-commit config

```yaml
repos:
-   repo: https://github.com/klieret/jekyll-relative-url-check
    rev: main
    hooks:
    -   id: jekyll-relative-url-check-html
    -   id: jekyll-relative-url-check-markdown
```

Afterwards run `pre-commit autoupdate` to replace `main` with the latest release.

### As a script

```bash
pip3 install .
jekyll-relative-url-check-html [FILE]...
jekyll-relative-url-check-markdown [FILE]...
```

## False positives

* Include `JEKYLL_RELATIVE_URL_CHECK_SKIP_FILE` in a file to skip checking the entire
file.
* Include `JEKYLL_RELATIVE_URL_CHECK_SKIP_LINE` in a line to skip checking it

## Implementation

Currently this hook only works by checking for several simple regular expressions.
