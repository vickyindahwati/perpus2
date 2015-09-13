from django import forms
from django.contrib.auth.models import User
from buku2.models import Book, Category, Pengarang, UserProfile

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)


class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the book.")
    sinopsis = forms.CharField(widget = forms.Textarea, help_text="Please enter the sinopsis of the book.")
    
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Book

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
