from pygments import highlight
from pygments.lexers import CppLexer
from pygments.formatters import TerminalFormatter
from pygments.styles import get_style_by_name

def _tui_text_highlight(text):
    return highlight(text, CppLexer(), TerminalFormatter(style=get_style_by_name('dracula')))
