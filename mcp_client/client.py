import aiohttp
import json
import asyncio
from typing import Dict, Any, Optional, List
from contextlib import AsyncExitStack
import sys
from datetime import datetime
from util.logger import get_logger
from config import MCP_CONFIG


from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
logger = get_logger(__name__)
    
class MCPClient:
    
    def __init__(self):
        self.server_url = None
        self.available_tools: List[Dict[str, Any]] = []
        self.tools_discovered = False
            
    async def _initialize_client(self, server: str):
        if self.tools_discovered:
            return 
        
        try:
            servers_config = MCP_CONFIG["servers"][server]
            self.server_url = servers_config["url"]
            
            logger.info(f"Initialize MCP Web Client of {server}server and URL: {self.server_url}")
            
            # discover tools
            async with streamablehttp_client(self.server_url) as (read, write, _):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    
                    response = await session.list_tools()
                    tools = response.tools
                    
                    self.available_tools = [{
                        "name": tool.name,
                        "description": tool.description,
                        "input_schema": tool.inputSchema
                    } for tool in tools]
                    
                    self.tools_discovered = True
                    logger.info(f"Discovered tools: {[tool.name for tool in tools]}")
                    
        except Exception as e:
            logger.error(f"Failed to discover tools: {e}")
            raise     source 