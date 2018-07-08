from django.views.generic import TemplateView



class HomePage(TemplateView):
    template_name = 'index.html'


class hello(TemplateView):
    template_name = 'helloworld/h1.html'


class sumodNum(TemplateView):
    template_name = 'AddofNum/addofnum.html'


class Even(TemplateView):
    template_name = 'Evennumbers/even.html'

