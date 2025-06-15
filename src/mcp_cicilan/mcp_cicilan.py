from fastmcp import FastMCP
from installment import FixedRateMortgage, TieredRateMortgage
from typing import Annotated, List
from pydantic import Field
from decimal import Decimal

mcp = FastMCP(
    name="Mortgage and KPR Assistant",
    instructions="""This provide tools to calculate monthly installment, remaining balance 
    and total interest paid of mortgage application (called Kredit Pemilikan Rumah / KPR in
    Indonesian).
    """,
)

@mcp.tool
def monthly_installment_fixed(
    principal: Annotated[int, Field(description="the loan amount")],
    annual_interest: Annotated[float, Field(description="annual interest in decimal. Divide by 100 if using percentage.")], 
    months: Annotated[int, Field(description="the loan tenure in months.")]
) -> int:
    """Calculate monthly installment using fixed rate mortgage."""
    
    fxm = FixedRateMortgage(principal, annual_interest, months)
    return fxm.monthly_installment()    

@mcp.tool
def interest_paid_fixed(
    principal: Annotated[int, Field(description="the loan amount")],
    annual_interest: Annotated[float, Field(description="annual interest in decimal. Divide by 100 if using percentage.")], 
    months: Annotated[int, Field(description="the loan tenure in months.")],
    months_paid: Annotated[int, Field(description="number of monthly payments the installment has been paid to.")]
) -> int:
    """Calculate the amount of interests paid after a certain period. 
    This assumes the mortgage is using fixed rate."""
    
    fxm = FixedRateMortgage(principal, annual_interest, months)
    return fxm.interest_paid(months_paid)

@mcp.tool
def remaining_balance_fixed(
    principal: Annotated[int, Field(description="the loan amount")],
    annual_interest: Annotated[float, Field(description="annual interest in decimal. Divide by 100 if using percentage.")], 
    months: Annotated[int, Field(description="the loan tenure in months.")],
    months_paid: Annotated[int, Field(description="number of monthly payments the installment has been paid to.")]
) -> int:
    """Calculate the remaining balance after a certain period. 
    This assumes the mortgage is using fixed rate."""
    
    fxm = FixedRateMortgage(principal, annual_interest, months)
    return fxm.remaining_balance(months_paid)

@mcp.tool
def monthly_installment_tiered(
    principal: Annotated[int, Field(description="the loan amount")],
    annual_interests: Annotated[List[float], Field(description="list of annual interest in decimal. Divide by 100 if using percentage.")],
    months: Annotated[List[int], Field(description="list of loan tenures in months.")],
) -> int:
    """Calculate monthly installment using tiered rate mortgage (Bunga berjenjang in Indonesian).
    This is characterized by multiple interests and multiple tenures."""
    trm = TieredRateMortgage(principal, annual_interests, months)
    return trm.monthly_installment()     

@mcp.tool
def interest_paid_tiered(
    principal: Annotated[int, Field(description="the loan amount")],
    annual_interests: Annotated[List[float], Field(description="list of annual interest in decimal. Divide by 100 if using percentage.")],
    months: Annotated[List[int], Field(description="list of loan tenures in months.")],
    months_paid: Annotated[int, Field(description="number of monthly payments the installment has been paid to.")]
) -> int:
    """Calculate the amount of interests paid after a certain period. 
    This assumes the mortgage is using tiered rate with multiple interests and tenures."""

    fxm = TieredRateMortgage(principal, annual_interests, months)
    return fxm.interest_paid(months_paid) 

@mcp.tool
def remaining_balance_tiered(
    principal: Annotated[int, Field(description="the loan amount")],
    annual_interests: Annotated[List[float], Field(description="list of annual interest in decimal. Divide by 100 if using percentage.")],
    months: Annotated[List[int], Field(description="list of loan tenures in months.")],
    months_paid: Annotated[int, Field(description="number of monthly payments the installment has been paid to.")]
) -> int:
    """Calculate the remaining balance after a certain period. 
    This assumes the mortgage is using tiered rate with multiple interests and tenures."""
    
    fxm = TieredRateMortgage(principal, annual_interests, months)
    return fxm.remaining_balance(months_paid) 

@mcp.tool
def format_rupiah(amount: str) -> str:
    """Format money amount in Rupiah"""
    
    return format(Decimal(amount))

def main():
    mcp.run()

if __name__ == "__main__":
    main()
