from django.shortcuts import render
from django.http.response import HttpResponse


data = {
    "blogs": [
        {
            "id" : 1,
            "title": "Web Development Fundamentals",
            "image": "1-2.jpg",
            "is_active": True,
            "is_home": True,
            "description": "Unleash your creativity in the digital realm by mastering the art of web development. This course covers HTML, CSS, and JavaScript, providing you with the skills to create and design stunning websites from scratch."
        },
        {
            "id" : 2,
            "title": "Introduction to Python Programming",
            "image": "2-2.jpg",
            "is_active": True,
            "is_home": False,
            "description": "Dive into the world of programming with Python, a versatile and beginner-friendly language. Learn the fundamentals of Python, including variables, data types, control structures, and more, to kickstart your coding journey."
        },
        {
            "id" : 3,
            "title": "Cloud Computing and AWS Solutions",
            "image": "3-3.jpg",
            "is_active": False,
            "is_home": True,
            "description": " Explore the cloud computing landscape and become proficient in Amazon Web Services (AWS). Gain hands-on experience with cloud services, storage, and infrastructure management."
        },
        {
            "id" : 4,
            "title": "Full-Stack Web Development with JavaScript",
            "image": "4-4.jpg",
            "is_active": True,
            "is_home": True,
            "description": "Become a full-stack web developer by mastering the entire web development stack. Learn to build dynamic web applications with JavaScript, Node.js, and popular frontend libraries like React."
        },
    ]
}


# Create your views here.

def index(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request, "blog/blogs.html", context)

def blog_details(request, id):
    # blogs = data["blogs"]
    # selected_blog = None

    # for blog in blogs:
    #     if blog["id"] == id:
    #         selected_blog = blog

    blogs = data["blogs"]
    selected_blog = [blog for blog in blogs if blog["id"] == id ][0]

    return render(request, "blog/blog-details.html", {
        "blog": selected_blog,
    })
