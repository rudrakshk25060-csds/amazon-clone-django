from django.shortcuts import render
from . import data
# Create your views here.
def product_show(request):
    student_inforamtion = {
        "name": "rohit kumar",
        "age": 22,
        "hobbies": ["Cricket", "badminton", "chess"],
        "Student":["Rohit", "rohan"],
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
    count = 0
    for score in data.students_record:
        if(score["marks"]>=90):
            count = count +1
    return render(request, "std_info.html", {"data":data, "count":count})