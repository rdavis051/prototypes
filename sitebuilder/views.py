import os
import datetime

from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template import Template
from django.utils._os import safe_join


from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
import datetime

BASE_DIR = os.path.dirname(__file__)

def get_page_or_404(name):
    """Return page content as a Django template or raise 404 error."""
    try:
        file_path = safe_join(settings.SITE_PAGES_DIRECTORY, name)
    except ValueError:
        raise Http404('Page Not Found')
    else:
        if not os.path.exists(file_path):
            raise Http404('Page Not Found')

    with open(file_path, 'r') as f:
        page = Template(f.read())

    return page


def page(request, slug='index'):
    """Render the requested page if found."""
    file_name = '{}.html'.format(slug)
    #print 'file_name: {0}'.format(file_name)
    page = get_page_or_404(file_name)
    context = {
        'slug': slug,
        'page': page,
    }
    if file_name == 'pdf_view.html':
        #print 'In if statement'
        pdf_view_response = pdf_view(request)
        return pdf_view_response
    else:
        return render(request, 'page.html', context)  

def pdf_view(request):
    # Gets the current date
    #print 'In pdf_view function'
    time_now = datetime.datetime.now()

    # Create a HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="summary_report.pdf"'

    # Create the PDF object, using the response object as its "file".
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 50, "This is from the bottom")
    p.drawString(100, 100, "Hello World.")
    p.setFont('Helvetica', 40, leading=None)
    p.drawCentredString(305, 500, "Certificate of Completion")
    p.setFont('Helvetica', 24, leading=None)
    p.drawCentredString(305, 450, "This certificate is presented to:")
    # Image of seal
    seal= os.path.join(BASE_DIR, 'static/images/SauceLogo_blk_HIRES.jpg')
    p.drawImage(seal, 235, 695, width=120, height=90)
    p.setFont('Helvetica', 12, leading=None)
    p.drawString(75, 650, time_now.strftime("%B %d, %Y"))

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    #print 'saved pdf'
    return response

