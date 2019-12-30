from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView


from .forms import LoginForm,RegisterForm

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = '/'


    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        #  当 校验错误的 时候
        return self.render_to_response(self.get_context_data(form=form))


    def form_valid(self, form):
        #  当 校验正确的时候
        return HttpResponseRedirect(self.get_success_url())

    # def form_valid(self, form):
    #     """If the form is valid, redirect to the supplied URL."""
    #     return HttpResponseRedirect(self.get_success_url())
    #
    # def form_invalid(self, form):
    #     """If the form is invalid, render the invalid form."""
    #     return self.render_to_response(self.get_context_data(form=form))


class ResterView(FormView):
    form_class = RegisterForm
    template_name = 'accounts/registration_form.html'
    def form_valid(self, form):
        if form.is_valid():
            user = form.save(False)
            user.is_active = False
            user.source = 'Register'
            user.save(True)
            return HttpResponseRedirect('/')
        else:
            return self.render_to_response({
                'form': form
            })
