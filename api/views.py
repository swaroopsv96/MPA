import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# POST endpoint
@csrf_exempt
def post_employee(request):
    employee_data = json.loads(request.body)
    with open('data.txt', 'r+') as file:
        data = json.load(file)
        # Generate the next ID
        next_id = max(employee['id'] for employee in data) + 1 if data else 1
        # Create the new employee entry
        new_employee = {
            'id': next_id,
            'employee_name': employee_data['employee_name'],
            'employee_salary': employee_data['employee_salary'],
            'employee_age': employee_data['employee_age']
        }
        # Append the new employee entry to the existing data
        data.append(new_employee)
        # Move the file cursor to the beginning to overwrite the contents
        file.seek(0)
        # Write the updated data to the file
        json.dump(data, file, indent=4)
        # Truncate the remaining contents in case the new data is smaller than the existing content
        file.truncate()
    return HttpResponse('Employee added successfully', status=201)


# GET endpoint by employee ID
def get_employee(request, employee_id):
    with open('data.txt', 'r') as file:
        data = json.load(file)
    for employee in data:
        if employee['id'] == employee_id:
            return JsonResponse(employee)
    return HttpResponse('Employee not found', status=404)

# GET endpoint to return all employees sorted by salary
def get_sorted_employees(request):
    with open('data.txt', 'r') as file:
        data = json.load(file)
    sorted_employees = sorted(data, key=lambda x: x['employee_salary'], reverse=True)
    return JsonResponse(sorted_employees, safe=False)


