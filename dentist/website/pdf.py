from io import BytesIO
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa 
from .views import appointment

def render_to_pdf(template_src, context_dic={}):
    template = get_template(template_src)
    html = template.render(context_dic)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def client(request):
    
    pdf = render_to_pdf('appointment_pdf.html', {'appointment': appointment})
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        content = "inline; filename=appointment.html"
        response['Content-Disposition'] = content
        return response
    return HttpResponse("not found")