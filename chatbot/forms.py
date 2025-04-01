from django import forms


class ChatForm(forms.Form):
    user_input = forms.CharField(
        label='Your Message',
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'with-icon',
            'placeholder': 'Type your message...',
            'style': (
                'background: url(/static/images/icon.png) no-repeat left center; ' +
                # Split the string to avoid exceeding the character limit
                'padding-left: 30px;'
                'padding-left: 30px;'
            )
        })
    )
