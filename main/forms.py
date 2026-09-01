from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='your name', max_length=100)
    
    '''
    def is_valid(self):
        print(self.cleaned_data)
        super().is_valid()
        print(self.cleaned_data)
    '''
