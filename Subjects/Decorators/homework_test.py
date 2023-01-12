import logging

from .homework import add, spam


def test_add(caplog):
    caplog.set_level(logging.NOTSET)

    result = add(1, 2)
    assert "homework" in caplog.text
    assert "DEBUG" in caplog.text
    assert "3" in caplog.text

    assert result == 3


def test_spam(caplog):
    caplog.set_level(logging.NOTSET)
    result = spam()

    assert "homework" in caplog.text
    assert "CRITICAL" in caplog.text
    assert "spam" in caplog.text
    # check the result
    assert result == "spam"
