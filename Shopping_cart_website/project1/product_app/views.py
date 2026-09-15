from django.shortcuts import render
from . import data
# Create your views here.
def product_show(request):
    student_inforamtion = {
        "name": "rohit kumar",
        "age": 22,
        "hobbies": ["Cricket", "badminton", "chess"],
        "department": {
            "cs": "computer_science",
            "IT": "Information technology",
            "ECE": None,
        },
        "profession":"I am software engineer",
        "salary":50000
    }
    return render(request, "product.html", student_inforamtion)


def showId(request):
    return render(request, "showid.html")

def student_information(request):
    return render(request, "std_info.html", {"data":data})