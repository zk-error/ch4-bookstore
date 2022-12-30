#PermissionRequiredMixin con este podemos agregar nuestro permiso personalizado que hicimos llamado Can read all books
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views import View
from django.views.generic import ListView,DetailView,View
from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from django.shortcuts import render
from .models import Book,Categoria,Review,likes,bookview,Reserva
from .forms import formcomentarios

class BookListView(ListView):
    model = Book
    paginate_by = 10
    context_object_name = "book_list"
    template_name = "books/book_list.html"

    def get_queryset(self):
        queryset = self.model.objects.filter(cantidad__gte = 1)#gte es para mostrar los libros que tengan una cantidad minima de una gte es mayor o igual que 
        return queryset





# class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView): # new
#     model = Book
#     context_object_name = "book"
#     template_name = "books/book_detail.html"
#     login_url = "account_login"
#     permission_required = "books.special_status"  #aqui definimos el permiso extra 



class BookDetailView(View):
    template_name = "books/book_detail.html"

    def get_object(self, queryset=None): 
        try:
            instance = Book.objects.get(id=self.kwargs['pk'])
        except:
            pass
        return instance

    def get_context_data(self, **kwargs):
        context = {}
        
        context['listacomentarios'] = Review.objects.select_related().filter(book=self.kwargs['pk'])
        #context['listacomentarios'] =  Book.objects.all().prefetch_related('reviews__author',)
        context['book']=get_object_or_404(Book,pk=self.kwargs['pk'])
        context['form']=formcomentarios()
        return context


   
    def get(self,request,pk,*args, **kwargs):
        book=get_object_or_404(Book,pk=self.kwargs['pk'])
        if self.get_object().cantidad > 0: # que la cantidad de libros sea mayor a 0
            if request.user.is_authenticated: # esta condicion es para que solo usuarios autenticados se cuenten las vistas
                bookview.objects.get_or_create(usuariovistas=request.user,book=book)
            return render(request,self.template_name,self.get_context_data())
        return redirect('book_list')

    def post(self,request,pk,*args, **kwargs):
        form=formcomentarios()
        if request.method =='POST':
            form = formcomentarios(request.POST) 
            if form.is_valid():
                post = get_object_or_404(Book,pk=pk)
                form.author = request.user
                comentario = form.cleaned_data.get('review')
                p,created = Review.objects.get_or_create(author=form.author,book=post,review=comentario)
                p.save()
                return redirect('book_list')

class SearchResultsListView(ListView): 
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"
    def get_queryset(self): 
        query = self.request.GET.get("q") # esta el la variable name que pusimos en html que optine lo que buscamos
        return Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))


class Book_category(View):
    def get(self,request,slug,*args, **kwargs):
        #category_list = Categoria.objects.filter(slug=slug) #este no funciona
        category_list = Book.objects.filter(categoria=Categoria.objects.get(slug=slug))
        #category_list=Book.objects.all().filter(categoria=1) # este solo funciona con id
        con = {
            'list_category':category_list,
        }
        return render(request,'books/book_category.html',con)



class libros_reservados(LoginRequiredMixin,ListView):
    model = Reserva 
    context_object_name = "book_reservados_list"
    template_name = "books/libros_reservados.html"
    login_url = "account_login" # este es de loginrequieredmixin redirije al usuario si no esta registrado si no lo ponemos por defecto rederira al login si lo ponemos ponemos ponerle otra ruta ejem la de registrarse
    
    def get_queryset(self):
        queryset = self.model.objects.filter(estado = True,usuario = self.request.user)
        return queryset
#-----------------------------------------------------------likes y vistas-------------------------------------------
def like(request,pk):
    if request.user.is_authenticated:
        book = get_object_or_404(Book,pk=pk)
        like_qs = likes.objects.filter(user=request.user,book=book)
        if like_qs.exists():#si el usuario ya le dio like eliminalo
            like_qs[0].delete()
            return redirect('book_list')
        likes.objects.create(user=request.user,book=book)
        return redirect('book_list')
    return redirect('account_login')



def reservarlibro(request,pk):
    if request.user.is_authenticated:
        reservalibro = get_object_or_404(Book,pk=pk)
        Reserva.objects.create(
            usuario = request.user,
            libro=get_object_or_404(Book,pk=pk)
        )
    return redirect('libros_reservados')


