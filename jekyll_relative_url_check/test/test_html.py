from jekyll_relative_url_check.html import HTMLRelativeURLHook


def test_regex():
    o = HTMLRelativeURLHook()
    yes = ['href="/asdf"', "href='/asdf'"]
    for y in yes:
        assert not o._check_text(y), y
    nos = ["", "nope", "href="]
    for no in nos:
        assert o._check_text(no)
