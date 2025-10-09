import random
from fastmcp import FastMCP

# Create a FastMCP server instance
mcp=FastMCP(name='Demo Server')


@mcp.tool
def roll_dice(n_dice: int = 1) -> list[int]:
    """ Roll n_dice 6-sided dice and return the results. """
    return [random.randint(1,6) for i in range(n_dice)]

@mcp.tool
def add_numbers(a: float, b:float) -> float:
    return a+b

@mcp.tool
def sub_numbers(a: float, b:float) -> float:
    return a-b

@mcp.tool
def divide_numbers(a: float, b:float) -> float:
    if b==0: return 0
    return a/b

@mcp.tool
def mult_numbers(a: float, b:float) -> float:
    return a*b


if __name__ == "__main__":
    mcp.run()
