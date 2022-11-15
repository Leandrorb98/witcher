from django.shortcuts import render
from django.views import View
from ejemplo.models import Persona
from ejemplo.forms import PersonaForm

class ListarPersonas(View):
    template_name = "ejemplo/lista_de_personas.html"

    def get(self, request):
        personas=Persona.objects.all()
        return render(request, self.template_name,{"personas": personas})

class CargarPersonas(View):
    template_name = "ejemplo/carga_de_personas.html"
    form_class = PersonaForm
    initial = {"nombre":"","apellido":"","fecha_de_nacimiento":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name,{"form": form})
    
    def post(self, request):
        form= self.form_class(request.POST)
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {"form":form})
        return render(request, self.template_name, {"form":form})
# Create your views here.
