from django.views.generic import TemplateView


class hello(TemplateView):
    template_name = 'helloworld/h1.html'


class HomePage(TemplateView):
    template_name = 'index.html'
