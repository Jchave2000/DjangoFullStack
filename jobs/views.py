from django.shortcuts import render, redirect
from .forms import JobApplicationForm

# View for the job application form
def job_application(request):
    if request.method == 'POST':
        # If the form has been submitted
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Redirect to a success page or back to the form with a success message
            return redirect('job_success')  # Adjust 'job_success' to your success page or URL
    else:
        # If the form is being displayed for the first time
        form = JobApplicationForm()

    # Render the form in the template
    return render(request, 'jobs/job_form.html', {'form': form})

#view for succsful submission
def job_success_view(request):
    return render(request, 'jobs/job_success.html')

def home(request):
    return render(request, 'jobs/index.html')

def menu(request):
    return render(request, 'jobs/menu.html')

def music(request):
    return render(request, 'jobs/music.html')
