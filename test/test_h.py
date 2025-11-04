from htmlight import h


def test_div():
    assert h.div("test") == "<div>test</div>"
