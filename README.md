# Jekyll relative URL hook

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/klieret/jekyll-relative-url-hook/main.svg)](https://results.pre-commit.ci/latest/github/klieret/jekyll-relative-url-hook/main)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![License](https://img.shields.io/github/license/klieret/jekyll-relative-url-hook.svg)](https://github.com/klieret/jekyll-relative-url-hook/blob/main/LICENSE.txt)
[![PR welcome](https://img.shields.io/badge/PR-Welcome-%23FF8300.svg)](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project)

A hook for [pre-commit](https://pre-commit.com/) that enforces that all links
in a Jekyll project are relative to `{{ site.baseurl }}`.

## Examples

The following constructions should raise errors:

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

The reasoning behind this is that these links will break if the site is not
directly deployed at `domain.com`, but e.g. at `user.github.io/projectname`.
In the latter case, the above links will resolve to `user.github.io/absolute/link`,
etc.

## False positives

* Include `JEKYLL_RELATIVE_URL_HOOK_SKIP_FILE` in a file to skip checking the entire
file.
* Include `JEKYLL_RELATIVE_URL_HOOK_SKIP_LINE` in a line to skip checking it
