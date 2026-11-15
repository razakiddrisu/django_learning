from django.http import HttpResponse, JsonResponse

def home(request):
    return HttpResponse("Welcome to Mr Razaks website!")

def student_list(request):
    students = [
        {"id": 1, "name": "Razak", "course": "BSc IT"},
        {"id": 2, "name": "Ama", "course": "BSc II"},
    ]
    return JsonResponse(students, safe=False),