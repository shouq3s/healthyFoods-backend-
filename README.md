# Project  and Repository Description
A Django REST Framework backend for managing healthy foods and drinks data.

What It Does:

- Provides food/drink data to frontend

- Handles user authentication (JWT)

## Tech Stack
- python
- django
- django rest frame work
- CORS
## Frontend Repository link:
[Healthy-Foods-frontend](https://git.generalassemb.ly/shouqAlbalawi/healthyFoods-frontend.git)
## Getting Started/Code Installation

To clone the project up and running on your local machine, follow these instructions:

#### 1. Clone the repo:
- `git clone https://git.generalassemb.ly/shouqAlbalawi/healthyFoods-frontend.git `
- `git clone https://git.generalassemb.ly/shouqAlbalawi/healthyFoods-backend`

#### 2.  Install backend dependencies:

- `pipenv install`
- `pipenv install django`
- `pipenv shell`
- `pipenv i django djangorestframework`
- `python manage.py makemigratin`
- `python manage.py migrate`
- `python manage.py createsuperuser`
#### 3. Start the backend server:
- `python manage.py runserver `

#### 4. In a new terminal, navigate to the frontend directory and install dependencies:
- `cd fronted_healthyfoods`
- `npm install`
- `npm install axios`
- `npm install react-router`
- `npm install bulma`
#### start the frontend server "
-`npm run dev `

### Routing table 
![Routingtable ](/images/Routing.png)

### ERD Diagram
![ERDDiagram ](/images/ERD%20Diagram.png)


## Future Improvements
- add eat time and workout module