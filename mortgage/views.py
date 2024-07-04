# views.py
from django.shortcuts import render
from .forms import MortgageForm
from .utils import MortgageCalculator

# views.py
def mortgage_calculator_view(request):
    if request.method == "POST":
        form = MortgageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            property_tax = (
                data.get("property_tax") if data.get("property_tax") is not None else 0
            )
            mip_pmi = data.get("mip_pmi") if data.get("mip_pmi") is not None else 0

            calculator = MortgageCalculator(
                interest_rate=data["interest_rate"],
                loan_term_years=data["loan_term_years"],
                property_value=data.get("property_value", 0),
                down_payment=data.get("down_payment", 0),
                property_tax=property_tax,
                mip_pmi=mip_pmi,
                additional_payments=data.get("additional_payments", []),
                initial_rent=data.get("initial_rent", 0),
                annual_rent_increase_percent=data.get(
                    "annual_rent_increase_percent", 0
                ),
            )

            schedule = calculator.amortization_schedule()
            context = {
                "schedule": schedule,
                "monthly_payment": calculator.monthly_payment,
                "loan_amount": calculator.loan_amount,
                "interest_rate": data["interest_rate"],
                "loan_term_years": data["loan_term_years"],
            }
            return render(request, "amortization_schedule.html", context)
    else:
        form = MortgageForm()
    return render(request, "mortgage_form.html", {"form": form})
