from django.contrib import messages
from allauth.account.views import SignupView
from allauth.account import app_settings


class CustomSignupView(SignupView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_message'] = " Join our vibrant plateform , to explore Madgascar genuinly"
        return context

    def form_valid(self, form):
        # add custom logic before saving
        response =  super().form_valid(form)

        if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
            messages.info(
                self.request, "please check you email to verify your account"
            )
        else:
            message.success(
                self.request,
                f"Welcome {form.cleaned_date['first_name']}! Your account has been created"
            )
        return response
