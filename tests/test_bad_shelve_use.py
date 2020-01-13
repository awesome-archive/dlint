#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadShelveUse(dlint.test.base.BaseTest):

    def test_bad_shelve_usage(self):
        python_node = self.get_ast_node(
            """
            import shelve
            """
        )

        linter = dlint.linters.BadShelveUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=2,
                col_offset=0,
                message=dlint.linters.BadShelveUseLinter._error_tmpl
            )
        ]

        assert result == expected


if __name__ == "__main__":
    unittest.main()
