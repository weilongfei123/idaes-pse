"""
Test Python notebooks in property example directories.

Generally, anything that requires a full optimization should be decorated with
`@pytest.mark.nocircleci()`, so our CircleCI tests don't take forever.
"""
# stdlib
import pathlib
# third party
# import pytest
# package
from idaes.util.testutil import run_notebook

__author__ = "Dan Gunter"


def notebook_path(dirname):
    return str((pathlib.Path("..") / dirname).absolute())


def test_module_2():
    assert run_notebook(
        notebook_path("Workshop_Module_2"), "Module_2_Flowsheet_DMF_Solution.ipynb"
    )
