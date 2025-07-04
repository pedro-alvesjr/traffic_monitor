# Traffic Monitor API

A REST API built with Django and Django REST Framework for monitoring road traffic on local road segments.

## Features

- Full CRUD for road segments (`RoadSegment`)
- Full CRUD for average speed readings (`TrafficReading`)
- Dynamic traffic intensity calculation based on speed
- Total readings count per segment
- User-based permissions:
  - **Admin**: can create, edit, and delete
  - **Anonymous**: read-only access
- Admin interface via Django Admin
- Interactive API documentation at `/api/docs`

## How to Run the Project

### Prerequisites

- Python 3.12 or higher
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pedro-alvesjr/traffic_monitor
   cd traffic_monitor
   ```

2. *(Optional)* Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

   or

   ```bash
   source venv/bin/activate  # On Linux/macOS
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply the migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Useful Endpoints:

- API (road segments): [`/api/roadsegments/`]
- API (readings): [`/api/readings/`]
- Swagger Documentation: [`/api/docs/`]
- Django Admin: [`/admin/`]
