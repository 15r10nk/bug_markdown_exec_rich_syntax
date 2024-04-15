from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax
import pygments

console=Console(color_system="256")

console.print("[red] red")
console.print("[green] green")


console.print(Syntax(
"""
  code
- a
+ b
""","diff"))


