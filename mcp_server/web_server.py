import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
import requests
import json
from typing import Dict, List, Any, Optional
import aiohttp
from urllib.parse import urljoin, urlparse
import re
from dataclasses import dataclass, asdict
from mcp.server.fastmcp import FastMCP
from util.logger import get_logger
from config import TAVILY_CONFIG
from tavily import AsyncTavilyClient

logger = get_logger("WebServer")

mcp = FastMCP("ReAct Web Research Tools Server", port=8001)

# Global client variable - will be initialized in startup
tavily_client = None

async def initialize_tavily(): 
    global tavily_client
      
    try:
        tavily_client = AsyncTavilyClient(api_key=TAVILY_CONFIG["api_key"])
        return True
    except Exception as e:
        logger.error(f"Failed to initialize Tavily client: {e}")
        return False
    
def main():
    logger.info("Starting web server")
    
    async def startup():
        success = await initialize_tavily()
        logger.info("Tavily init ok")
    try:
        asyncio.run(startup())
        mcp.run(
            transport="streamable-http", 
        )
        logger.info("Server run ok")
    except KeyboardInterrupt:
        logger.info("\n Server stopped by user")
    except Exception as e:
        logger.info(f" Server error: {e}")

if __name__ == "__main__":
        main()

# main()