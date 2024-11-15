import requests
from config import COURSERA_ACCESS_TOKEN

def get_completed_courses():
    # Coursera API endpoint for accomplishments
    url = "https://api.coursera.org/api/accomplishments.v1"
    
    # Headers with authentication
    headers = {
        "Authorization": f"Bearer {COURSERA_ACCESS_TOKEN}",
        "Accept": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        data = response.json()
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching courses: {e}")
        return None

def main():
    courses = get_completed_courses()
    
    if courses:
        # Process and display the courses
        for course in courses.get('elements', []):
            print(f"Course Name: {course.get('name')}")
            print(f"Completion Date: {course.get('completionDate')}")
            print("-" * 50)

if __name__ == "__main__":
    main()