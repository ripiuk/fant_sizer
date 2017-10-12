from unittest import mock

from fant_sizer import fant_sizer
from fant_sizer.fant_sizer import os


def test_results(monkeypatch):
    with mock.patch('os.walk') as mockwalk:
        mockwalk.return_value = [
            ('/foo', ('bar',), ('baz',)),
            ('/foo/bar', (), ('spam', 'eggs')),
        ]
        monkeypatch.setattr('fant_sizer.fant_sizer', os)
        assert fant_sizer.get_result('/some/path', False) == []
