#libraries
from fastmcp import FastMCP

mcp = FastMCP(name = "Calculator")


mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers.
    
    args: a (float): the first number.
          b (float): the second number.
    returns: float: The product of the two numbers.
    """
    return a * b

mcp.tool(
    name = "add"
    description = "Add two numbers."
    tags = ("math", "arithmetic")
)

def add_numbers(x: float, y:)