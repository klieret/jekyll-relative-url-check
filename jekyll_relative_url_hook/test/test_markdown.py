from jekyll_relative_url_hook.markdown import MarkdownRelativeURLHook


def test_regex():
    regex = MarkdownRelativeURLHook().absolute_url_regexs[0]
    yes = ['[asdf](/asdf)"']
    for y in yes:
        assert regex.findall(y)
    nos = ["", "nope", "[asdf](asdf)"]
    for no in nos:
        assert not regex.findall(no)
