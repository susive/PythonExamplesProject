from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'index.html'


class UseofPython(TemplateView):
    template_name = 'useofpython.html'


class WhyPython(TemplateView):
    template_name = 'whypython.html'


class Variablediclration(TemplateView):
    template_name = 'Python/variable.html'


class DataTypes(TemplateView):
    template_name = 'Python/datatypes.html'


class Bool(TemplateView):
    template_name = 'Python/bool.html'


class Numbers(TemplateView):
    template_name = 'Python/numbers.html'


class Strings(TemplateView):
    template_name = 'Python/strings.html'


class Lists(TemplateView):
    template_name = 'Python/lists.html'


class Tuples(TemplateView):
    template_name = 'Python/tuples.html'


class Sets(TemplateView):
    template_name = 'Python/sets.html'


class Dictionarys(TemplateView):
    template_name = 'Python/dictionarys.html'


class Conversions(TemplateView):
    template_name = 'Python/conversionbetweendatatypes.html'


class Conditionalstatements(TemplateView):
    template_name = 'Python/conditionalstatements/conditionalstatements.html'


class Ifstatement(TemplateView):
    template_name = 'Python/conditionalstatements/if.html'


class Elsestatements(TemplateView):
    template_name = 'Python/conditionalstatements/else.html'


class ElIfstatements(TemplateView):
    template_name = 'Python/conditionalstatements/elif.html'


class If_Elsestatements(TemplateView):
    template_name = 'Python/conditionalstatements/if_else.html'


class If_Elifstatement(TemplateView):
    template_name = 'Python/conditionalstatements/if_elif.html'


class If_Elif_Elsestatement(TemplateView):
    template_name = 'Python/conditionalstatements/if_elif_else.html'


class NestedIfstatement(TemplateView):
    template_name = 'Python/conditionalstatements/nested_if.html'


class Loops(TemplateView):
    template_name = 'Python/Loops/loops.html'


class hello(TemplateView):
    template_name = 'helloworld/h1.html'


class sumodNum(TemplateView):
    template_name = 'AddofNum/addofnum.html'


class Even(TemplateView):
    template_name = 'Evennumbers/even.html'


