from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FileUploadForm



def landing_page(request):
    return render(request, 'landing_page.html')


# Create your views here.
@login_required
def home(request):
    message = ''
    if request.method == 'POST':
        # 4 SUM REAZON TO JEST KURDE BRIAN NIE WIEM CZEMU ZJADŁO MI TO
        # DZIEŃ ŻYCIA I NAWET NIE CHCE WIEDZIEĆ SKĄD TO SIĘ BIRZE
        file = request.FILES['braian']

        handle_uploaded_file(file)
        # form = FileUploadForm(request.POST, request.FILES)
        # valid = form.is_valid()
        # # handle_uploaded_file(request.FILES['file'])
        # if valid:
            # Process the file here, e.g., saving it to a model or the filesystem

            # form.save()
        #     message = 'File uploaded successfully'
        # else:
        #     message = f'Upload failed{form.errors}'
        #     print(form.errors)

    else:
        form = FileUploadForm()
    return render(request, "braian.html",{'message': message})

def handle_uploaded_file(f):
    with open('media/file_uploads/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def about(request):
    return render(request, "about.html")