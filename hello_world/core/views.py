from django.shortcuts import render

from django.http import JsonResponse

def index(request):
    return render(
        request,
        "index.html",
        {
            "title": "Django example",
        },
    )

def sponsor_income(request):
    if request.method == 'GET':
        people_to_be_sponsored = int(request.GET.get('people_to_be_sponsored'))
        in_household = int(request.GET.get('in_household'))
        household_size = int(people_to_be_sponsored + in_household)
        location = request.GET.get('location')

        if household_size == 2:
            poverty_guideline = 19720
        elif household_size == 3:
            poverty_guideline = 24860
        elif household_size == 4:
            poverty_guideline = 30000
        elif household_size == 5:
            poverty_guideline = 35140
        elif household_size == 6:
            poverty_guideline = 40280
        elif household_size == 7:
            poverty_guideline = 45420
        elif household_size == 8:
            poverty_guideline = 50560
        elif household_size > 8:
            poverty_guideline = 25650 + (household_size - 4) * 5140

        if location in ["Alaska", "Hawaii", "Guam", "Virgin Islands"]:
            poverty_guideline *= 1.15
        elif location == "Puerto Rico":
            poverty_guideline *= 1.5

        minimum_income = poverty_guideline * 1.25

        return JsonResponse({'minimum_income': minimum_income, 'location': location, 'household_size': household_size})

    return JsonResponse({'error': 'Please make sure you have read the instructions on determining household size before you begin. This is not a replacement for reading USCIS instructions for using income tables.'})



