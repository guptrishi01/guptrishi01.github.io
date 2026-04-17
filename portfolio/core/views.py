from django.shortcuts import render
from django.http import Http404
from .projects_data import PROJECTS, get_project, get_projects_by_category
from .certifications_data import CERTIFICATIONS


def home(request):
    """Home / About Me page."""
    context = {
        "featured_projects": PROJECTS[:3],
        "years_coding": 5,
        "projects_count": len(PROJECTS),
    }
    return render(request, "core/home.html", context)


def certifications(request):
    """Certifications listing."""
    return render(request, "core/certifications.html", {
        "certifications": CERTIFICATIONS,
    })


def projects_index(request):
    """Overview of all projects split by category."""
    return render(request, "core/projects_index.html", {
        "academic_projects": get_projects_by_category("academic"),
        "personal_projects": get_projects_by_category("personal"),
    })


def project_detail(request, slug):
    """Detailed page for a single project."""
    project = get_project(slug)
    if not project:
        raise Http404("Project not found")
    return render(request, "core/project_detail.html", {"project": project})
