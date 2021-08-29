from jekyll_relative_url_hook.html import HTMLRelativeURLHook


def test_regex():
    regex = HTMLRelativeURLHook().absolute_url_regexs[0]
    yes = ['href="/asdf"']
    for y in yes:
        assert regex.findall(y)
    nos = ['', 'nope', 'href=']
    for no in nos:
        assert not regex.findall(no)
