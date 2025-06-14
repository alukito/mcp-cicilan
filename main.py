import asyncio
from fastmcp import Client

client = Client("src/mcp_cicilan/mcp_cicilan.py")

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("monthly_installment_fixed", 
                                        {"principal": 1_000_000, 
                                         "annual_interest": 0.06,
                                         "months": 60
                                         })
        print(result)

asyncio.run(call_tool("Ford"))