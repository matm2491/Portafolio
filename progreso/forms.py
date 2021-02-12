from django import forms

class CommentsUsers(forms.Form):
    name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    title = forms.CharField(label='Titulo', required=True)
    comment = forms.CharField(label='Comentario',widget=forms.Textarea  ,required=True)

