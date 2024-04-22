import requests
import sys


def fetch_employee_and_todos(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee data
    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print(f"Error: Failed to retrieve data for employee ID {employee_id}")
        return

    employee = employee_response.json()
    employee_name = employee['name']

    # Fetch TODOs data
    todos_url = f"{base_url}/todos"
    todos_response = requests.get(todos_url, params={"userId": employee_id})
    if todos_response.status_code != 200:
        print(f"Error: Failed to retrieve TODOs for employee ID {employee_id}")
        return

    todos = todos_response.json()
    completed_tasks = [todo for todo in todos if todo['completed']]
    number_of_done_tasks = len(completed_tasks)
    total_tasks = len(todos)

    # Print the output
    print(f"Employee {employee_name} is done with "
          f"tasks({number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    fetch_employee_and_todos(employee_id)
