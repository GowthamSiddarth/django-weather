from django.shortcuts import render


# Create your views here.
def home(request):
    import requests

    api_request = requests.get(
        "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=0620D809-DB96-499D-9416-B2244A45A0D3")
    try:
        api = api_request.json()

        if api[0]['Category']['Name'] == 'Good':
            category_desc = "(0-50) Air Quality is considered satisfactory and air pollution poses little or no risk."
            category_color = 'good'
        elif api[0]['Category']['Name'] == 'Moderate':
            category_desc = "(51-100) Air Quality is acceptable; however, for some pollutants there may be a moderate " \
                            "health concern for a very small number of people who are unusually sensitive to air " \
                            "pollution. "
            category_color = 'moderate'
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_desc = "(101-150) People with lung disease, older adults and children are at a greater risk from " \
                            "exposure to ozone, whereas persons with heart and lung disease, older adults and " \
                            "children are at greater risk from presence of particles in air. "
            category_color = 'usg'
        elif api[0]['Category']['Name'] == 'Unhealthy':
            category_desc = "(151-200) Everyone may begin to experience health effects; members of sensitive groups " \
                            "may experience more serious health effects. "
            category_color = 'unhealthy'
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_desc = "(201-300) Health alert: Everyone may experience more serious health effects."
            category_color = 'veryunhealthy'
        elif api[0]['Category']['Name'] == 'Hazardous':
            category_desc = "(301-500) Health warning of emergency situation. The entire population is more likely to " \
                            "be effected. "
            category_color = 'hazardous'
    except Exception as e:
        print(e)
        api = "Error..."

    return render(request, 'home.html', {'api': api, 'category_desc': category_desc, 'category_color': category_color})


def about(request):
    return render(request, 'about.html', {})
