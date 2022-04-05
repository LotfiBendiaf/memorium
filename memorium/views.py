from unicodedata import category
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import Category, Memory

# Create your views here.

def gallery(request):
    return render (request, 'photos/gallery.html')

def memory(request):
    return render (request, 'photos/memory.html')

def addMemory(request):
    return render (request, 'photos/add_memory.html')

class MemoryListView(ListView): 
    model = Memory
    template_name = 'photos/gallery.html'

    def get_context_data(self, **kwargs):
        category = self.request.GET.get('category')
        if category == None:
            memories = Memory.objects.all()
        else:
            memories = Memory.objects.filter(category__name=category)

        print("Category : ", category)
        context = super(MemoryListView, self).get_context_data(**kwargs)
        context.update({
            'categories': Category.objects.all(),
            'memories': memories
        })
        return context

class MemoryDetailView(DetailView):
    model = Memory
    template_name = 'photos/memory.html'
    fields = ['title', 'author', 'body']

class MemoryCreateView(CreateView): 
    model = Memory
    template_name = 'photos/add_memory.html'
    fields = ('title', 'memory', 'category', 'description',)


    def form_valid(self, form): 
        if self.request.method == 'POST':
            data = self.request.POST

            if data['category'] != '':
                category = Category.objects.get(id=data['category'])
            elif data['new_category'] != '':
                category, created = Category.objects.get_or_create(name=data['new_category'])
            else:
                category = None

        form.instance.category = category

        form.instance.author = self.request.user 
        return super().form_valid(form)


class MemoryUpdateView(UpdateView):
    model = Memory
    fields = ('title', 'category', 'description', )
    template_name = 'photos/edit_memory.html'
    success_url = "/" 

    def form_valid(self, form): 
        if self.request.method == 'POST':
            data = self.request.POST

            if data['category'] != '':
                category = Category.objects.get(id=data['category'])
            elif data['new_category'] != '':
                category, created = Category.objects.get_or_create(name=data['new_category'])
            else:
                category = None

        form.instance.category = category
        return super().form_valid(form)

    def get_success_url(self):         
        return reverse_lazy('memory', args = (self.object.id,))

class MemoryDeleteView(DeleteView):
    model = Memory
    template_name = 'photos/delete_memory.html'
    success_url = reverse_lazy('gallery')

