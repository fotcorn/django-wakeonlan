import wakeonlan

from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, reverse
from django.http import HttpResponseRedirect

from .forms import Form
from .models import Target

class WOLView(LoginRequiredMixin, FormView):
    form_class = Form
    template_name = 'index.html'

    def form_valid(self, form):
        target = form.cleaned_data['target']
        wakeonlan.send_magic_packet(target.mac_address, ip_address=target.ip_address)
        return HttpResponseRedirect(reverse('wol') + '?success')
