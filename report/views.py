import csv
# import tempfile

from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import get_user_model
# from weasyprint import HTML
# from django.template.loader import render_to_string

from newspaper.models import Post


User = get_user_model()

COLUMNS = [
    "first_name",
    "last_name",
    "username",
    "email",
    "is_staff",
    "is_active",
    "is_superuser",
    "last_login",
    "date_joined",
]


class UserReportView(View):
    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=users.csv"

        users = User.objects.all().only(*COLUMNS).values(*COLUMNS)

        writer = csv.DictWriter(response, fieldnames=users[0].keys())
        writer.writeheader()
        writer.writerows(users)

        return response

# class PostPdfFileView(View):
#     def get(self, request):
#         posts = Post.objects.all()
        
#         html_string = render_to_string("reports/posts.html", {"posts": posts})
#         html = HTML(string=html_string, base_url=request.build_absolute_uri())
#         result = html.write_pdf()
        
#         response = HttpResponse(content_type="application/pdf;")
#         response["Content-Disposition"] = "inline; filename=posts.pdf"
#         response["Content-Transfer-Encoding"] = "binary"
        
#         with tempfile.NamedTemporaryFile(delete=True) as output:
#             output.write(result)
#             output.flush()
            
#             with open(output.name, "rb") as f:
#                 response.write(f.read())
                
#         return response
    
# from django.http import HttpResponse
# from reportlab.pdfgen import canvas
# from django.views.generic import View

# class PostPdfFileView(View):
#     def get(self, request):
#         response = HttpResponse(content_type="application/pdf")
#         response["Content-Disposition"] = "inline; filename=posts.pdf"
        
#         p = canvas.Canvas(response)
        
#         # Example content (modify based on your posts data)
#         posts = Post.objects.all()
#         y = 800  # Starting y position on the PDF
#         for post in posts:
#             p.drawString(100, y, f"Title: {post.title}")
#             y -= 20  # Move down for next post
        
#         p.showPage()
#         p.save()
        
#         return response
