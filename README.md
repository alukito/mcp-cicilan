# mcp-cicilan

**mcp-cicilan** is a Mortgage and KPR (Kredit Pemilikan Rumah) MCP that provides tools to calculate monthly installments, remaining balance, and total interest paid for mortgage applications. It supports both fixed-rate and tiered-rate (bunga berjenjang) mortgages, commonly used in Indonesia.

## Features

- **Monthly Installment Calculation**: Compute monthly payments for both fixed and tiered interest rate mortgages.
- **Interest Paid Calculation**: Find out how much interest you have paid after a certain period.
- **Remaining Balance Calculation**: Check your outstanding loan balance at any point in your mortgage.

## Project Structure

```
main.py                      # Example usage and entry point
src/mcp_cicilan/
    installment.py           # Core mortgage calculation logic
    mcp_cicilan.py           # Tool definitions and FastMCP integration
```

## Tools

The following tools are available (see `src/mcp_cicilan/mcp_cicilan.py`):

### Fixed Rate Mortgage Tools

- `monthly_installment_fixed(principal, annual_interest, months)`
  - Calculate monthly installment for a fixed-rate mortgage.
- `interest_paid_fixed(principal, annual_interest, months, months_paid)`
  - Calculate total interest paid after a certain number of payments.
- `remaining_balance_fixed(principal, annual_interest, months, months_paid)`
  - Calculate remaining loan balance after a certain number of payments.

### Tiered Rate Mortgage Tools

- `monthly_installment_tiered(principal, annual_interests, months)`
  - Calculate monthly installment for a tiered-rate mortgage (multiple interest rates and tenures).
- `interest_paid_tiered(principal, annual_interests, months, months_paid)`
  - Calculate total interest paid for a tiered-rate mortgage after a certain number of payments.
- `remaining_balance_tiered(principal, annual_interests, months, months_paid)`
  - Calculate remaining balance for a tiered-rate mortgage after a certain number of payments.

### Utility

- `format_rupiah(amount)`
  - Format a number as Indonesian Rupiah.

## Example Usage

You can use the tools programmatically. See `main.py` for an example:

```python
import asyncio
from fastmcp import Client

client = Client("src/mcp_cicilan/mcp_cicilan.py")

async def call_tool():
    async with client:
        result = await client.call_tool("monthly_installment_fixed", {
            "principal": 1_000_000_000,
            "annual_interest": 0.06,
            "months": 192
        })
        print(result)

asyncio.run(call_tool())
```