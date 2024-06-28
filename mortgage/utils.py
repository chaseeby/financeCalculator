from typing import List, Dict


# utils.py
# utils.py
# utils.py
class MortgageCalculator:
    def __init__(
        self,
        loan_amount,
        interest_rate,
        loan_term_years,
        property_value=0,
        down_payment=0,
        property_tax=0,
        mip_pmi=0,
        additional_payments=[],
        initial_rent=0,
        annual_rent_increase_percent=0,
    ):
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.loan_term_years = loan_term_years
        self.property_value = property_value
        self.down_payment = down_payment
        self.property_tax = property_tax if property_tax is not None else 0
        self.mip_pmi = mip_pmi if mip_pmi is not None else 0
        self.additional_payments = additional_payments if additional_payments else []
        self.initial_rent = initial_rent
        self.annual_rent_increase_percent = annual_rent_increase_percent
        self.monthly_payment = self.calculate_monthly_payment()

    @property
    def monthly_property_tax(self):
        return (self.property_tax or 0) / 12

    def calculate_monthly_payment(self):
        principal_payment = (
            self.loan_amount
            * (self.interest_rate / 100 / 12)
            / (1 - (1 + self.interest_rate / 100 / 12) ** (-self.loan_term_years * 12))
        )
        return principal_payment + (self.mip_pmi or 0) + self.monthly_property_tax

    def amortization_schedule(self):
        schedule = []
        remaining_balance = self.loan_amount
        total_paid = 0
        total_rent_paid = 0
        current_rent = self.initial_rent
        monthly_rent_increase = self.annual_rent_increase_percent / 100 / 12

        for month in range(1, self.loan_term_years * 12 + 1):
            interest_payment = remaining_balance * (self.interest_rate / 100 / 12)
            principal_payment = (
                self.monthly_payment
                - interest_payment
                - self.mip_pmi
                - self.monthly_property_tax
            )

            if principal_payment > remaining_balance:
                principal_payment = remaining_balance

            remaining_balance -= principal_payment
            monthly_total = self.monthly_payment + sum(self.additional_payments)
            total_paid += monthly_total

            # Increment rent
            total_rent_paid += current_rent
            current_rent += current_rent * monthly_rent_increase

            schedule.append(
                {
                    "Month": month,
                    "Principal": round(principal_payment, 2),
                    "Interest": round(interest_payment, 2),
                    "Remaining_Balance": round(remaining_balance, 2),
                    "Total_Paid": round(total_paid, 2),
                    "Total_Rent_Paid": round(total_rent_paid, 2),
                }
            )

            if remaining_balance <= 0:
                break

        return schedule

    def calculate_rent_increase(self):
        rent_schedule = []
        current_rent = self.initial_rent

        for month in range(1, self.loan_term_years * 12 + 1):
            if (
                month % 12 == 1 and month != 1
            ):  # Increase rent at the beginning of each year
                current_rent += current_rent * (self.annual_rent_increase_percent / 100)
            rent_schedule.append(current_rent)

        return rent_schedule
