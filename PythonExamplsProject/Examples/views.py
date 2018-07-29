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
    template_name = 'Python/Datatypes/datatypes.html'


class Bool(TemplateView):
    template_name = 'Python/Datatypes/bool.html'


class Numbers(TemplateView):
    template_name = 'Python/Datatypes/numbers.html'


class Strings(TemplateView):
    template_name = 'Python/Datatypes/strings.html'


class Lists(TemplateView):
    template_name = 'Python/Datatypes/lists.html'


class Tuples(TemplateView):
    template_name = 'Python/Datatypes/tuples.html'


class Sets(TemplateView):
    template_name = 'Python/Datatypes/sets.html'


class Dictionarys(TemplateView):
    template_name = 'Python/Datatypes/dictionarys.html'


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


class If_Elif_Elsestatement(TemplateView):
    template_name = 'Python/conditionalstatements/if_elif_else.html'


class NestedIfstatement(TemplateView):
    template_name = 'Python/conditionalstatements/nested_if.html'


class Loops(TemplateView):
    template_name = 'Python/Loops/loops.html'


class forloop(TemplateView):
    template_name = 'Python/Loops/for.html'


class whileloop(TemplateView):
    template_name = 'Python/Loops/while.html'


class functions(TemplateView):
    template_name = 'Python/Functions/functionwithparentheses.html'


class lambdaFun(TemplateView):
    template_name = 'Python/Functions/lambdaFunction.html'


class OOPs(TemplateView):
    template_name = 'Python/OOPS/oops.html'


class objs(TemplateView):
    template_name = 'Python/OOPS/object.html'


class cls(TemplateView):
    template_name = 'Python/OOPS/class.html'


class Inheritance(TemplateView):
    template_name = 'Python/OOPS/inheritance.html'


class Encap(TemplateView):
    template_name = 'Python/OOPS/Encap.html'


class Poly(TemplateView):
    template_name = 'Python/OOPS/PolyMor.html'


class FileHandling(TemplateView):
    template_name = 'Python/File Handling/filehandling.html'


class hello(TemplateView):
    template_name = 'helloworld/h1.html'


class sumodNum(TemplateView):
    template_name = 'AddofNum/addofnum.html'


class Even(TemplateView):
    template_name = 'Evennumbers/even.html'
