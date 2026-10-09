"""Pytest fixtures for the pdf-merger test suite.

The tests cover the pure merge logic only, never the tkinter GUI.
tkinter is stubbed out so the suite runs headless (e.g. in CI).
"""

import sys
from unittest.mock import MagicMock

_tk = MagicMock(name="tkinter")
_tk.filedialog = MagicMock(name="tkinter.filedialog")
_tk.messagebox = MagicMock(name="tkinter.messagebox")
sys.modules.setdefault("tkinter", _tk)
sys.modules.setdefault("tkinter.filedialog", _tk.filedialog)
sys.modules.setdefault("tkinter.messagebox", _tk.messagebox)
