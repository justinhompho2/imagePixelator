from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import FileResponse
from django.template import loader

from .models import Document
from .forms import DocumentForm

import ImagePixelator.ImagePixelator as IP
import os
from io import StringIO
from io import BytesIO
import base64

# Codes copied from https://github.com/axelpale/minimal-django-file-upload-example
# Check https://stackoverflow.com/questions/5871730/how-to-upload-a-file-in-django

def homepage(request):
    
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        if request.POST.get('download') == "":
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            ip = ""
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            altip = ip.replace(".", "-")
            altip = altip + ".png"
            try:
                with open(altip, "rb") as f:
                    return FileResponse(open(altip, "rb"), as_attachment=True, filename="Export.png")
            except IOError:
                return redirect('homepage')
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():

            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            ip = ""
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            altip = ip.replace(".", "-")
            altip = altip + ".png"

            img_doc = request.FILES['docfile']
            pixel_size = request.POST.get('pixelsize')
            # newdoc = Document(docfile=request.FILES['docfile'])
            newdoc = Document(docfile=img_doc)

            # img = Image.open(img_doc)
            # imgSmall = img.resize((64, 64))
            # result = imgSmall.resize(img.size,Image.NEAREST)
            result = IP.Pixelator2(img_doc, 10)
            if pixel_size != '':
                result = IP.Pixelator2(img_doc, int(pixel_size))

            buffer_png = BytesIO()
            result.save(buffer_png, 'png')
            result.save(altip)

            # Original example uses database here, need to modify
            # newdoc.save()
            # Redirect to the document list after POST
            form = DocumentForm()
            documents = Document.objects.all()
            context = {
                'img_str': base64.b64encode(buffer_png.getvalue()).decode('utf-8'),
                'documents': documents, 'form': form, 'message': message
            }

            return render(request, 'index.html', context=context)
            

            # image_data = img_doc.read()
            # return response
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'index.html', context)
    """
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
    """
