from django.shortcuts import render


# Helper methods
def get_category_desc_and_color(category_name):
    if category_name == 'Good':
        category_desc = "(0-50) Air Quality is considered satisfactory and air pollution poses little or no risk."
        category_color = 'good'
    elif category_name == 'Moderate':
        category_desc = "(51-100) Air Quality is acceptable; however, for some pollutants there may be a moderate " \
                        "health concern for a very small number of people who are unusually sensitive to air " \
                        "pollution. "
        category_color = 'moderate'
    elif category_name == "Unhealthy for Sensitive Groups":
        category_desc = "(101-150) People with lung disease, older adults and children are at a greater risk from " \
                        "exposure to ozone, whereas persons with heart and lung disease, older adults and " \
                        "children are at greater risk from presence of particles in air. "
        category_color = 'usg'
    elif category_name == 'Unhealthy':
        category_desc = "(151-200) Everyone may begin to experience health effects; members of sensitive groups " \
                        "may experience more serious health effects. "
        category_color = 'unhealthy'
    elif category_name == "Very Unhealthy":
        category_desc = "(201-300) Health alert: Everyone may experience more serious health effects."
        category_color = 'veryunhealthy'
    elif category_name == 'Hazardous':
        category_desc = "(301-500) Health warning of emergency situation. The entire population is more likely to " \
                        "be effected. "
        category_color = 'hazardous'

    return category_desc, category_color


# Create your views here.
def home(request):
    import requests

    try:
        if request.method == 'POST':
            zipcode = request.POST['zipcode']
            api_request = requests.get(
                "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode +
                "&distance=5&API_KEY=0620D809-DB96-499D-9416-B2244A45A0D3")
        else:
            api_request = requests.get(
                "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance"
                "=5&API_KEY=0620D809-DB96-499D-9416-B2244A45A0D3")
        api = api_request.json()
        category_desc, category_color = get_category_desc_and_color(api[0]['Category']['Name'])
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api': api, 'category_desc': category_desc, 'category_color': category_color})


def about(request):
    return render(request, 'about.html', {})
