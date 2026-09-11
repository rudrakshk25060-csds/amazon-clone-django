from django.shortcuts import render

# Create your views here.
def product_show(request):
    student_inforamtion = {
        "name": "Rohit",
        "age": 30,
        "hobbies":["Cricket", "badminton", "chess"],
        "department": {
            "cs":"computer_science",
            "IT": "Information technology",
            "ECE": None
        }
    }
    return render(request, 'product.html', student_inforamtion)

def showId(request):
    return render(request, 'showid.html')
