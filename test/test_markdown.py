from jekyll_relative_url_check.markdown import MarkdownRelativeURLHook


def test_regex():
    o = MarkdownRelativeURLHook()
    yes = ['[asdf](/asdf)"', "![pic](/absolute/picture.png)"]
    for y in yes:
        assert not o._check_text(y)
    nos = ["", "nope", "[asdf](asdf)"]
    for no in nos:
        assert o._check_text(no)
