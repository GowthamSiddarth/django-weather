from django.shortcuts import render


# Create your views here.
def home(request):
    import requests

    api_request = requests.get(
        "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=0620D809-DB96-499D-9416-B2244A45A0D3")
    try:
        api = api_request.json()
    except Exception as e:
        print(e)
        api = "Error..."

    return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})
