# Phase 1 ✔ API Call
# Phase 2 ✔ Structured Code
# Phase 3 ➜ File Storage
# Phase 4 ➜ Logging
# Phase 5 ➜ Unit Testing
# Phase 6 ➜ Convert to CLI tool
# Phase 7 ➜ Add configuration file
# Phase 8 ➜ Deploy or Dockerize

# # step:1 API call Beginners approch
# import requests
#
# url = "https://jsonplaceholder.typicode.com/users/1"
#
# headers = {
#     "user-agent": "Mozilla/5.0",
#     "Accept": "application/json"
# }
#
# response = requests.get(url, headers=headers)
# print(response.status_code)
#
# if response.status_code == 200:
#     print(response.json())
# else:
#     print(response.text)                   # Give me the raw response as plain text Don’t try to convert it into JSON
#
#
# # step:1 API call Intermediate approch
# import requests
#
# def fetch_employee(user_id):
#     url = f"https://jsonplaceholder.typicode.com/users/{user_id}"  # popular JSON url for Automation testing Is made specifically for testing
#
#     try:
#         response = requests.get(url)
#         return response.json()
#     except Exception:
#         print("Something went wrong while calling API")
#         return None
#
#
# employee = fetch_employee(1)
#
# if employee:
#     print("Name:", employee["name"])
#     print("Email:", employee["email"])
#
#
# # step:1 API call advanced production level approch:
# import requests
#
# def fetch_employee(user_id):
#     url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
#
#     try:
#         response = requests.get(url)
#
#         if response.status_code == 200:
#             return response.json()
#         else:
#             print("Error:", response.status_code)
#             return None
#
#     except requests.exceptions.RequestException as e:
#         print("Request failed:", e)
#         return None
#
#
# def main():
#     employee = fetch_employee(1)
#
#     if employee:
#         print("Employee Name:", employee["name"])
#         print("Email:", employee["email"])
#         print("Company:", employee["company"]["name"])
#
# if __name__ == "__main__":
#
# # STEP 2: Store API Data into a File (CSV)
#
#     import requests
#     import csv
#
#     def fetch_employee(user_id):
#         url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
#
#         try:
#             response = requests.get(url)
#             return response.json()
#         except Exception:
#             print("API call failed")
#             return None
#
#     employee = fetch_employee(1)
#
#     if employee:
#         name = employee["name"]
#         email = employee["email"]
#         company = employee["company"]["name"]
#
#         with open("employee_1.csv", "w", newline="") as file:
#             writer = csv.writer(file)
#
#             writer.writerow(["Name", "Email", "Company"])
#             writer.writerow([name, email, company])
#
#         print("Data saved successfully!")


# Updated Code (Multi-User Version – for 5 users Simple)
import requests
import csv

# def fetch_employee(user_id):
#     url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
#     try:
#         response = requests.get(url)
#         return response.json()
#     except Exception:
#         print(f"Failed to fetch user {user_id}")
#         return None
#
#
# with open("employees.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#
#     # Write header only once
#     writer.writerow(["Name", "Email", "Company"])
#
#     # Loop from 1 to 5
#     for user_id in range(1, 6):
#         employee = fetch_employee(user_id)
#
#         if employee:
#             name = employee["name"]
#             email = employee["email"]
#             company = employee["company"]["name"]
#
#             writer.writerow([name, email, company])
#
# print("All employee data saved successfully!")


#  Final Code (Dynamic approche for total employees of the company)
import requests
import csv

def fetch_employee(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    return response.json()

# Ask user how many employees to fetch
limit = int(input("Enter number of employees: "))

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow(["Name", "Email", "Company"])

    for i in range(1, limit + 1):
        emp = fetch_employee(i)
        # Stop if no valid data
        if not emp or "name" not in emp:
            print(f"No more users found after {i - 1}. Stopping...")
            break
        writer.writerow([
                emp["name"],
                emp["email"],
                emp["company"]["name"]
        ])


print("Data saved successfully!")



