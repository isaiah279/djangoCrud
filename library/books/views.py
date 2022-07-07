from django.shortcuts import render,redirect
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse
from subscribe import views

# Create your views here
def index(request):
    shelf=Book.objects.all()
    return render(request,'books/library.html',{'shelf':shelf})
def upload(request):
    upload=BookCreate()
    if request.method=="POST":
        upload=BookCreate(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""Your form is wrong ,reload on<a href={{url :'index'}}>reload</a>""")
    else:
        return render (request,'books/upload_form.html',{'upload_form':upload})
def update_book(request,book_id):
    #The request it self and id number. The id number is used to identify the object which is to be edited
    id=book_id
    book_id=int(book_id)
    
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    
    book_form = BookCreate(request.POST or None, instance = book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('index')
    return render(request, 'books/upload_form.html', {'upload_form':book_form})
def delete_book(request,book_id):
    book_id = int(book_id)
    # checks wheathe id if valid or not.
    try:
        book_sel = Book.objects.get(id = book_id)
    #The queryset book.objects.get(id = book_id) will check for the books having an id equal to book_id.
    except Book.DoesNotExist:
        return redirect('index/')
    book_sel.delete()
    return redirect('index/')

#UPDATE FUCTION
#If the object exists it will return the
# form filled with the object’s information in it.
# The user can change the form again. In this case, there
# will be no creation of new object .