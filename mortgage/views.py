# views.py
from django.shortcuts import render
from .forms import MortgageForm
from .utils import MortgageCalculator


def mortgage_view(request):
    if request.method == "POST":
        form = MortgageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            loan_amount = data["property_value"] - data["down_payment"]
            property_tax = (
                data.get("property_tax") if data.get("property_tax") is not None else 0
            )
            mip_pmi = data.get("mip_pmi") if data.get("mip_pmi") is not None else 0

            calculator = MortgageCalculator(
                loan_amount=loan_amount,
                interest_rate=data["interest_rate"],
                loan_term_years=data["loan_term_years"],
                property_value=data.get("property_value", 0),
                down_payment=data.get("down_payment", 0),
                property_tax=property_tax,
                mip_pmi=mip_pmi,
                initial_rent=data.get("initial_rent"),
                annual_rent_increase_percent=data.get("annual_rent_increase_percent"),
            )

            schedule = calculator.amortization_schedule()
            rent_schedule = calculator.calculate_rent_increase()

            context = {
                "schedule": schedule,
                "monthly_payment": calculator.monthly_payment,
                "loan_amount": loan_amount,
                "interest_rate": data["interest_rate"],
                "loan_term_years": data["loan_term_years"],
                "rent_schedule": rent_schedule,
            }
            return render(request, "amortization_schedule.html", context)
    else:
        form = MortgageForm()
    return render(request, "mortgage_form.html", {"form": form})


# views.py
def mortgage_view(request):
    if request.method == "POST":
        form = MortgageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            loan_amount = data["property_value"] - data["down_payment"]

            property_tax = (
                data.get("property_tax") if data.get("property_tax") is not None else 0
            )
            mip_pmi = data.get("mip_pmi") if data.get("mip_pmi") is not None else 0

            calculator = MortgageCalculator(
                loan_amount=loan_amount,
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
            print(schedule)
            context = {
                "schedule": schedule,
                "monthly_payment": calculator.monthly_payment,
                "loan_amount": loan_amount,
                "interest_rate": data["interest_rate"],
                "loan_term_years": data["loan_term_years"],
            }
            return render(request, "amortization_schedule.html", context)
    else:
        form = MortgageForm()
    return render(request, "mortgage_form.html", {"form": form})
