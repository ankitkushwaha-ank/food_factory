# ðŸ” Food Factory

**Food Factory** is a powerful and user-friendly restaurant management system designed to streamline restaurant operations and enhance the customer experience. The platform includes features like online food ordering, table reservation, menu management, order tracking, and an intuitive admin dashboard.

---

## ðŸš€ Key Features

### ðŸ‘¨â€ðŸ³ Restaurant Management (Admin)
- Add, update, or delete food items with categories and availability toggles
- View and manage all incoming orders
- Handle table reservations
- Access to a dashboard with food item analytics (optional)

### ðŸ›’ Online Food Ordering (Customer)
- Browse digital menu with images, prices, and descriptions
- Add to cart and place orders
- Order status updates and confirmation system

### ðŸ“† Table Reservation
- Customers can book tables for future dates
- Admin gets notified and sees reservation slots

### ðŸ“Š Admin Dashboard
- Real-time order tracking
- Reservation and feedback overview
- Easy-to-use menu management

---

## ðŸ§‘â€ðŸ’» Tech Stack

| Layer              | Technology                              |
|--------------------|------------------------------------------|
| **Frontend**       | HTML, CSS, JavaScript, Bootstrap/Tailwind |
| **Backend**        | Django (Python)                         |
| **Database**       | SQLite3 / MySQL                         |
| **Authentication** | Django Sessions & Login System          |
| **Templating**     | Django Templates                        |

---

## ðŸ“¸ Screenshots

> Add your screenshots in the `screenshots/` folder and link them as shown below:

```markdown
![Homepage](screenshots/home.png)
![Menu](screenshots/menu.png)
![Cart](screenshots/cart.png)
![Admin Dashboard](screenshots/admin-dashboard.png)
```

---

## âš™ï¸ Installation & Setup

### âœ… Prerequisites
- Python 3.8+
- Git
- Virtualenv (recommended)

### ðŸ› ï¸ Setup Steps

```bash
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
```

Then visit `http://127.0.0.1:8000/` in your browser.

---

## ðŸ“‚ Folder Structure

```
food_factory/
â”œâ”€â”€ restaurant/             # Core Django app
â”‚   â”œâ”€â”€ models.py           # Models for menu, orders, reservations
â”‚   â”œâ”€â”€ views.py            # Views for all endpoints
â”‚   â”œâ”€â”€ forms.py            # Django forms for item and reservation inputs
â”‚   â”œâ”€â”€ urls.py             # App-level URL routing
â”œâ”€â”€ templates/              # HTML templates
â”‚   â”œâ”€â”€ customer/           # Customer-facing views
â”‚   â””â”€â”€ admin/              # Admin dashboard views
â”œâ”€â”€ static/                 # CSS, JS, and image files
â”œâ”€â”€ media/                  # Uploaded images (e.g. menu photos)
â”œâ”€â”€ manage.py
â”œâ”€â”€ requirements.txt
â””â”€â”€ README.md
```

---

## ðŸ‘¥ User Roles

### ðŸ”¸ Admin (Restaurant Owner)
- Manage menu items and categories
- Monitor and process customer orders
- Handle table reservations and feedback

### ðŸ”¸ Customer
- Browse menu and place food orders
- Book tables in advance
- Track order status

---

## ðŸ§ª Testing

To run unit tests:

```bash
python manage.py test
```

---

## ðŸ“„ License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## ðŸ™‹â€â™‚ï¸ Author & Contributors

- **Your Name** â€“ Full Stack Developer  
- Additional contributors (if any)

---

## ðŸ“¬ Contact

For questions or suggestions:

- ðŸ“§ Email: your-email@example.com  
- ðŸ“± Phone: +91-XXXXXXXXXX  
- ðŸŒ Website: [https://yourwebsite.com](https://yourwebsite.com)  
- ðŸ”— GitHub: [https://github.com/your-username](https://github.com/your-username)

---

## ðŸ™Œ Acknowledgements

- Django Framework  
- Bootstrap / Tailwind CSS  
- Open Source Libraries  
- Real-world restaurant workflows for inspiration