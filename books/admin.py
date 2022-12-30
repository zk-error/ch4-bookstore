from django.contrib import admin
from .models import Book,Review,Categoria,likes,Reserva,bookview
from .forms import ReservaForm

class ReviewInline(admin.TabularInline):
    model = Review
    
class BookAdmin(admin.ModelAdmin):
    inlines = [ReviewInline,]
    list_display = ("title", "author",)

class ReservaAdmin(admin.ModelAdmin):
    form = ReservaForm
    list_display = ('libro','usuario','fecha_creacion','fecha_vencimiento','estado')


admin.site.register(Book, BookAdmin)
admin.site.register(Categoria)
admin.site.register(Review)
admin.site.register(likes)
admin.site.register(Reserva,ReservaAdmin)
admin.site.register(bookview)