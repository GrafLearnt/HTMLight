from htmlight import h


def test_div():
    assert h.div("test") == "<div>test</div>"


def test_page():
    assert (
        h.html(
            h.head(
                h.title("Welcome to Our Website"),
                h.link(rel="stylesheet", href="styles.css"),
            ),
            h.body(
                h.header(
                    h.h1(
                        "Welcome to Our Website",
                        style=(
                            " color:"
                            " #333;"
                            " text-align:"
                            " center;"
                            " background-color:"
                            " #F0F0F0;"
                            " padding: 20px;"
                        ),
                    ),
                    h.p(
                        "Explore our amazing content",
                        style="font-size: 20px; color: #555;",
                    ),
                ),
                h.main(
                    h.h2("Featured Articles", style="color: #444; text-align: center;"),
                    h.article(
                        h.h3("Article 1", style="color: #0072d6;"),
                        h.p("This is the first article content", style="color: #666;"),
                    ),
                    h.article(
                        h.h3("Article 2", style="color: #00a86b;"),
                        h.p("This is the second article content", style="color: #666;"),
                    ),
                ),
                h.footer(
                    h.p(
                        "© 2023 Our Website",
                        style=(
                            "text-align: center;"
                            " background-color: #333;"
                            " color: #fff;"
                            " padding: 10px;"
                            " flex-shrink: 0;"
                            " background-color: #333;"
                            " position: absolute;"
                            " left: 0;"
                            " bottom: 0;"
                            " width: 100%;"
                            " overflow: hidden;"
                        ),
                    ),
                ),
            ),
            style="background-color: #f2f2f2; font-family: Arial, sans-serif;",
        )
        == """<html style="background-color: #f2f2f2; font-family: Arial, sans-serif;"><head><title>Welcome to Our Website</title><link rel="stylesheet" href="styles.css"/></head><body><header><h1 style=" color: #333; text-align: center; background-color: #F0F0F0; padding: 20px;">Welcome to Our Website</h1><p style="font-size: 20px; color: #555;">Explore our amazing content</p></header><main><h2 style="color: #444; text-align: center;">Featured Articles</h2><article><h3 style="color: #0072d6;">Article 1</h3><p style="color: #666;">This is the first article content</p></article><article><h3 style="color: #00a86b;">Article 2</h3><p style="color: #666;">This is the second article content</p></article></main><footer><p style="text-align: center; background-color: #333; color: #fff; padding: 10px; flex-shrink: 0; background-color: #333; position: absolute; left: 0; bottom: 0; width: 100%; overflow: hidden;">© 2023 Our Website</p></footer></body></html>"""
    )
