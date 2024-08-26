# Residencia REST API

This project is a REST API designed for managing and consulting information about the residents of a residential facility. It is intended to be used by any frontend client to interact with the backend in a structured and efficient manner.

## Stack

- **Python**: Version >= 3.08
- **Django**: Version >= 5.0

## Requirements

- **PEP 8**: Code must adhere to Python's PEP 8 style guide.
- **Entities**: The application must include at least three entities: users, residents, and rooms.
- **Roles**: A basic role management system should be implemented, potentially including roles such as administrator and employee. Implementing this system is optional for the first version.
- **Postman**: The project should be delivered with a Postman JSON file that includes examples of all API functionalities.
- **Linters & Formatters**: Usage of Black Formatter and Pylance is suggested to maintain code quality.
- **Server Log**: The server terminal should be free from errors.
- **README**: A detailed README in Markdown format should be included.
- **Swagger**: Documentation should be prepared using Swagger, providing detailed information on how to make requests and example responses.
- **Language**: All documentation and code should be delivered in English.

## Optional

- **Database**: The choice of database is flexible.
- **Dependencies**: Additional dependencies may be used, provided they are explained and justified in the README.

## Presentation

The final deliverable should be a public code repository (e.g., GitLab) with the developed solution. The repository must include a README file explaining how to run the application, its architecture, structure, and any other relevant project information.

## Endpoints

The application should include the following verticals. The HTTP verbs for each endpoint are at the developer's discretion and should be justified in the README. Additionally, Swagger documentation is required.

### /api/user
- **Authentication**: Allows for logging in, logging out, and registering with basic authentication (username and password).
- **Profile Management**: Users should be able to edit their profiles and update their information. Required fields include phone number, email, and address.
- **User List**: Allows fetching a complete list of users, including details for each user.

### /api/residents
- **Resident List**: Allows listing all residents, ordered by name, with pagination support.
- **Resident Details**: Fetch details of a specific resident by ID.
- **Medical Information**: View and manage medical information (e.g., medical reports, diets) for each resident.
- **Room Occupancy**: Manage room occupancy by associating a resident with an available room.

### /api/rooms
- **Room List**: Display all rooms.
- **Room Status**: Identify which rooms are vacant and which are occupied.
- **Room Management**: Manage room occupancy through the resident's endpoint when creating or updating a resident's record.

### /api/activities
- **Activity List**: List all activities.
- **Create Activity**: Create a new activity.
- **Activity Details**: View details of specific activities.
- **Update Activity**: Update activity information.
- **Delete Activity**: Delete activities.

## Evaluation

This project evaluates three key areas:

1. **Object-Oriented Programming (OOP)**: Weight - 2
2. **Database Architecture and Design**: Weight - 2
3. **Backend Development with Django**: Weight - 5
4. **Collaboration and Presentation**: Weight - 1

## Contact

If you have any questions or need further clarification during the test, feel free to contact your assigned instructor.

## Documentation

The full API documentation is available in Swagger format. You can access it by visiting the `/docs/` endpoint after starting the server. The documentation includes detailed information on each endpoint, along with example requests and responses.

