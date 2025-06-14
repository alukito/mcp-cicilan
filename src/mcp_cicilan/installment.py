import math
from typing import List
from decimal import *
import itertools

class FixedRateMortgage():
    def __init__(self, principal: int, annual_interest: float, months: int) -> None:
        self.principal = Decimal(principal)
        self.monthly_interest = Decimal(annual_interest) / 12
        self.months = months

    def monthly_installment(self) -> Decimal:
        # Calculate the monthly payment using the annuity formula
        monthly_payment = self.principal * (self.monthly_interest * (1 + self.monthly_interest) ** self.months) \
            / ((1 + self.monthly_interest) ** self.months - 1)
        return monthly_payment

    def remaining_balance(self, payments_made: int) -> Decimal: 
        remaining_balance = self.principal * ((1 + self.monthly_interest) ** self.months - (1 + self.monthly_interest) ** payments_made) / ((1 + self.monthly_interest) ** self.months - 1)
        return remaining_balance

    def interest_paid(self, payments_made: int) -> Decimal:
        total_paid = self.monthly_installment() * payments_made
        remaining_balance = self.remaining_balance(payments_made)
        
        return total_paid - (self.principal - remaining_balance)
        
class TieredRateMortgage():
    def __init__(self, principal: int, annual_interests: List[float], months: List[int]) -> None:
        self.fixed_mortgages = self.init_fixed_mortgages(principal, annual_interests, months)
        self.months = months

    def init_fixed_mortgages(self, principal: int, annual_interests: List[float], months: List[int]) -> List[FixedRateMortgage]:
        mortgages = []
        sum_months = sum(months)
        remaining = principal
        
        for interest, month in zip(annual_interests, months):
            frm = FixedRateMortgage(remaining, interest, sum_months)                    
            mortgages.append(frm)

            remaining = frm.remaining_balance(month)
            sum_months -= month

        return mortgages

    def monthly_installment(self) -> List[Decimal]:
        return [mortgage.monthly_installment() for mortgage in self.fixed_mortgages]

    def remaining_balance(self, payments_made: int) -> Decimal: 
        sum_month = 0
        for fm, month in zip(self.fixed_mortgages, self.months):
            sum_month += month
            if payments_made <= sum_month:
                return fm.remaining_balance(payments_made - sum_month + month)

        return Decimal(-1)

    def interest_paid(self, payments_made: int) -> Decimal:        
        sum_interest = 0
        for fm, month in zip(self.fixed_mortgages, self.months):
            if payments_made <= month:
                sum_interest += fm.interest_paid(payments_made)
                return sum_interest
            
            sum_interest += fm.interest_paid(month)            
            payments_made -= month