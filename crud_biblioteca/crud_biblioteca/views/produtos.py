from django.shortcuts import render, redirect, get_object_or_404
from crud_biblioteca.models import produto
from django.forms import ModelForm
class produto_form(ModelForm):
    class Meta:
        model= produto
        fields= '__all__'
def lista(request):
    return render(request, 'produtos/lista.html', {
        'produtos': produto.objects.all()
    })
def novo(request):
    frm = produto_form(request.POST or None)
    if frm.is_valid():
        frm.save()
        return redirect('produtos.lista')
    return render(request, 'produtos/form.html', {
        'frm': frm,
        'titulo': 'Cadatrar produto'
    })
def editar(request, id):
    Produto = get_object_or_404(produto, pk=id)
    frm = produto_form(request.POST or None, instance=Produto)
    if frm.is_valid():
        frm.save()
        return redirect('produtos.lista')
    return render(request, 'produtos/form.html',{
        'frm':frm,
        'titulo': 'Editar produto'
    })
def excluir(request, id):
    Produto = get_object_or_404(produto, pk=id)
    frm = produto_form(request.POST or None, instance=Produto)
    Produto.delete()
    return redirect('produtos.lista')