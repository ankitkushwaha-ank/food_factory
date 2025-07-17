# 🍔 Food Factory

**Food Factory** is a powerful and user-friendly restaurant management system designed to streamline restaurant operations and enhance the customer experience. The platform includes features like online food ordering, table reservation, menu management, order tracking, and an intuitive admin dashboard.

---

## 🚀 Key Features

### 👨‍🍳 Restaurant Management (Admin)
- Add, update, or delete food items with categories and availability toggles
- View and manage all incoming orders
- Handle table reservations
- Access to a dashboard with food item analytics (optional)

### 🛒 Online Food Ordering (Customer)
- Browse digital menu with images, prices, and descriptions
- Add to cart and place orders
- Order status updates and confirmation system

### 📆 Table Reservation
- Customers can book tables for future dates
- Admin gets notified and sees reservation slots

### 📊 Admin Dashboard
- Real-time order tracking
- Reservation and feedback overview
- Easy-to-use menu management

---

## 🧑‍💻 Tech Stack

| Layer              | Technology                              |
|--------------------|------------------------------------------|
| **Frontend**       | HTML, CSS, JavaScript, Bootstrap/Tailwind |
| **Backend**        | Django (Python)                         |
| **Database**       | SQLite3 / MySQL                         |
| **Authentication** | Django Sessions & Login System          |
| **Templating**     | Django Templates                        |

---

## 📸 Screenshots

> Add your screenshots in the `screenshots/` folder and link them as shown below:

```markdown
![Homepage](screenshots/home.png)
![Menu](screenshots/menu.png)
![Cart](screenshots/cart.png)
![Admin Dashboard](screenshots/admin-dashboard.png)

# Clone the repository
git clone https://github.com/your-username/food-factory.git
cd food-factory

# Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser for admin access
python manage.py createsuperuser

# Start the development server
python manage.py runserver


food_factory/
├── restaurant/             # Core Django app
│   ├── models.py           # Models for menu, orders, reservations
│   ├── views.py            # Views for all endpoints
│   ├── forms.py            # Django forms for item and reservation inputs
│   ├── urls.py             # App-level URL routing
├── templates/              # HTML templates
│   ├── customer/           # Customer-facing views
│   └── admin/              # Admin dashboard views
├── static/                 # CSS, JS, and image files
├── media/                  # Uploaded images (e.g. menu photos)
├── manage.py
├── requirements.txt
└── README.md
