from django.shortcuts import render

def jobs_list(request):
    return render(request, 'jobs/jobs_list.html')
