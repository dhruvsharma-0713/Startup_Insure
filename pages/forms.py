from django import forms

class ContactForm(forms.Form):
    # Define a consistent set of CSS classes for all fields
    tailwind_classes = "block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-600 focus:border-blue-600 sm:text-sm"

    company_name = forms.CharField(
        label="Company Name",
        widget=forms.TextInput(attrs={
            'class': tailwind_classes,
            'placeholder': 'Your Company Name'
        })
    )
    work_email = forms.EmailField(
        label="Work Email",
        widget=forms.EmailInput(attrs={
            'class': tailwind_classes,
            'placeholder': 'you@company.com'
        })
    )
    # The other fields like num_employees can be added here later
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            'class': tailwind_classes,
            'placeholder': 'Any specific questions?'
        }),
        required=False
    )