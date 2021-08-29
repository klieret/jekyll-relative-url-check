# Jekyll relative URL hook

A hook for [pre-commit](https://pre-commit.com/) that enforces that all links
in a Jekyll project are relative to `{{ site.baseurl }}`.

For examples, the following constructions should raise errors:

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
In the latter case, the aboce links will resolve to `user.github.io/absolute/link`,
etc.