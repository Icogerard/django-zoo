from django.shortcuts import render, get_object_or_404
from .models import Category, Animal
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


class Staff_Required_Mixin():
    """
    Este Mixin requerira que el usuario sea miembro del staf
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(Staff_Required_Mixin, self).dispatch(request, *args, **kwargs)





def animal_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    animals = Animal.objects.filter(extinct=False)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        animals = animals.filter(category=category)
    return render(request,
                  'zoo/animal/list.html',
                  {'category': category,
                   'categories': categories,
                   'animals': animals})
    def dispatch(self, reques, *args, **kwargs):
        print(request.user)
    return super()

def animal_detail(request, id, slug):
    animal = get_object_or_404(Animal,
                                id=id,
                                slug=slug,
                                extinct=False)
    return render(request,'zoo/animal/detail.html',{'animal': animal})



