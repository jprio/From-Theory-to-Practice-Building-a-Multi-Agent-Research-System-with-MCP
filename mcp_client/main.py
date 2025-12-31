from mcp.client.session import ClientSession
from mcp.client.sse import sse_client
from typing import Any
import sys
import os
from urllib.parse import urlparse
import asyncio
import asyncio
from fastmcp import Client, FastMCP
from fastmcp.server.auth.providers.github import GitHubProvider


def print_items(name: str, result: Any) -> None:
    """Print items with formatting.

    Args:
        name: Category name (tools/resources/prompts)
        result: Result object containing items list
    """
    print("", f"Available {name}:", sep="\n")
    items = getattr(result, name)
    if items:
        for item in items:
            print(" *", item)
    else:
        print("No items available")


"""
async def main(server_url: str):
    if urlparse(server_url).scheme not in ("http", "https"):
        print("Error: Server URL must start with http:// or https://")
        sys.exit(1)

    try:
        async with sse_client(server_url) as streams:
            async with ClientSession(streams[0], streams[1]) as session:
                await session.initialize()
                print("Connected to MCP server at", server_url)
                print_items("tools", (await session.list_tools()))
                print_items("resources", (await session.list_resources()))
                print_items("prompts", (await session.list_prompts()))

    except Exception as e:
        print(f"Error connecting to server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main("https://vague-lime-quokka.fastmcp.app/mcp"))

"""

# GitHub OAuth
os.environ["FASTMCP_SERVER_AUTH"]="fastmcp.server.auth.providers.github.GitHubProvider"
os.environ["FASTMCP_SERVER_AUTH_GITHUB_CLIENT_ID"]="Iv23liw8DCEbMSLF3CpL"
os.environ["FASTMCP_SERVER_AUTH_GITHUB_CLIENT_SECRET"]="fcd69ccdbbc99eab80f58eb76f1a20eeb79d13d7"

client = Client("https://vague-lime-quokka.fastmcp.app/mcp", auth="fmcp_w-7O2rWBpJbW8_NfjRSPGjrc80zg60AuZ_HlSoLuTU4")

async def main():
    async with client:
        # Ensure client can connect
        await client.ping()

        # List available operations
        tools = await client.list_tools()
        print(tools)
        resources = await client.list_resources()
        prompts = await client.list_prompts()

        # Ex. execute a tool call
        result = await client.call_tool("echo_tool", {"text": "value"})
        result = await client.call_tool("test4", {"query": "value"})
        print(result)

asyncio.run(main())