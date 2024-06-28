from django import forms


class MortgageForm(forms.Form):
    property_value = forms.FloatField(
        label="Property Value", min_value=0, required=False
    )
    down_payment = forms.FloatField(label="Down Payment", min_value=0, required=False)

    interest_rate = forms.FloatField(
        label="Interest Rate (%)", min_value=0, max_value=100, required=True
    )
    loan_term_years = forms.IntegerField(
        label="Loan Term (years)", min_value=1, required=True
    )

    property_tax = forms.FloatField(
        label="Annual Property Tax", min_value=0, required=False
    )
    mip_pmi = forms.FloatField(label="Monthly MIP/PMI", min_value=0, required=False)
    initial_rent = forms.FloatField(label="Initial Rent", min_value=0, required=True)
    annual_rent_increase_percent = forms.FloatField(
        label="Annual Rent Increase (%)", min_value=0, max_value=100, required=True
    )
