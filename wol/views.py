import wakeonlan

from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import Form

class WOLView(LoginRequiredMixin, FormView):
    form_class = Form
    template_name = 'index.html'

    def form_valid(self, form):
        target_pk = form.cleaned_data['target']
        target = get_object_or_404(Target, pk=target_pk)
        wakeonlan.send_magic_packet(target.mac_address)
        return reverse('wol') + '?success'
