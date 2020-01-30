from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

class ObjectDetailMixin:
    """
    Mixin for rendering Detail object.
    """
    model = None
    template = None
    def get(self,request,slug):
        """
        Overriding get method for viewing object.
        """
        obj = get_object_or_404(self.model,slug__iexact = slug)
        return render(request,self.template,context={self.model.__name__.lower():obj,'admin_object':obj,'detail':True})

    
class ObjectCreateMixin:
    """
    Mixin for Creating object.
    """
    model_form = None
    template = None

    def get(self,request):
        """
        Overriding get method for creating object.
        """
        form = self.model_form()
        return render(request,self.template,context={'form':form})

    def post(self,request):
        """
        Overriding post method for creating object.
        """
        bound_form = self.model_form(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template ,context = {'form':bound_form})

class ObjectUpdateMixin:
    """
    Mixin for Editing object.
    """
    model = None
    model_form = None
    template = None

    def get(self,request,slug):
        """
        Overriding get method for editing object.
        """
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request,self.template,context = {'form':bound_form,self.model.__name__.lower():obj})

    def post(self,request,slug):
        """
        Overriding post method for editing object.
        """
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST,instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request,self.template, context = {'form':bound_form,self.model.__name__.lower():obj})

class ObjectDeleteMixen:
    """
    Mixin for Deleting object.
    """
    model = None
    template = None
    redirect_url = None

    def get(self,request,slug):
        """
        Overriding get method for delete object.
        """
        obj = self.model.objects.get(slug__iexact = slug)
        return render(request,self.template,context = {self.model.__name__.lower(): obj})

    def post(self,request,slug):
        """
        Overriding post method for delete object.
        """
        obj = self.model.objects.get(slug__iexact = slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
