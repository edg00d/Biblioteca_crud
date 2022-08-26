from django.shortcuts import render, redirect, get_object_or_404
from crud_biblioteca.models import categoria
from django.forms import ModelForm
class categoria_form(ModelForm):
    class Meta:
        model= categoria
        fields= '__all__'
def lista(request):
    return render(request, 'categorias/lista.html', {
        'categorias': categoria.objects.all()
    })
def novo(request):
    frm = categoria_form(request.POST or None)
    if frm.is_valid():
        frm.save()
        return redirect('categorias.lista')
    return render(request, 'categorias/form.html', {
        'frm': frm,
        'titulo': 'Cadastrar categoria'
    })
def editar(request, id):
    Categoria = get_object_or_404(categoria, pk=id)
    frm = categoria_form(request.POST or None, instance=Categoria)
    if frm.is_valid():
        frm.save()
        return redirect('categorias.lista')
    return render(request, 'categorias/form.html', {
        'frm': frm,
        'titulo': 'Editar categoria'
    })
def excluir(request, id):
    Categoria = get_object_or_404(categoria, pk=id)
    frm = categoria_form(request.POST or None, instance=Categoria)
    Categoria.delete()
    return redirect('categorias.lista')