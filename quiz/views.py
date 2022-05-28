from django.shortcuts import render

# Create your views here.

def quiz(request):
    """ A view to render the customer quiz """
    return render(request, 'quiz/quiz.html')