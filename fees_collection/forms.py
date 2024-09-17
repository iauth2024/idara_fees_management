from django import forms
from .models import Payment

# Form for Payment, linked to the Payment model
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['student', 'name', 'amount', 'receipt_no', 'receipt_type', 'date', 'created_by', 'payment_method', 'organization', 'year']
        labels = {
            'student': 'Admission Number',
            'name': 'Name',
            'amount': 'Amount Paid',
            'receipt_no': 'Receipt Number',
            'receipt_type': 'Receipt Type',
            'date': 'Date',
            'created_by': 'Created By',
            'payment_method': 'Payment Method',
            'organization': 'Organization',
            'year': 'Year',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

# Form for uploading files, such as Excel or CSV files
class UploadFileForm(forms.Form):
    file = forms.FileField(label='Select a file')

# Form for uploading payment data via Excel files
class PaymentUploadForm(forms.Form):
    excel_file = forms.FileField(label='Select Excel file')
