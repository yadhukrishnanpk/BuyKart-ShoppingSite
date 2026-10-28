# BuyKart 🛒

BuyKart is a full-featured e-commerce and marketplace web application built with **Django** and **Django REST Framework (DRF)**. It features user authentication, item listings, category management, an internal messaging/conversation system between buyers and sellers, a user dashboard, staff category administration, and a fully featured RESTful API.

## 🌟 Key Features

* **Core & Authentication:** User signup, login, logout, and landing page management.
* **Item Marketplace:** Browse, create, edit, search (using multi-field Django `Q` objects), and filter items by category.
* **Related Items Discovery:** Recommends unsold related items in the same category on item detail pages.
* **Buyer-Seller Messaging:** Integrated real-time messaging and conversation history between buyers and sellers regarding item inquiries.
* **User Dashboard & Item Management:** Dedicated seller dashboard to manage, update, or delete personal listings.
* **Staff Category Administration:** Admin/staff-restricted actions for creating, editing, and deleting item categories (`@staff_member_required`).
* **RESTful API (DRF):** Full API exposure for Categories, Items, Conversations, Messages, and Users with granular permissions and JWT/Session authentication.
* **Cloud Storage Integration:** Cloudinary integration for handling user-uploaded media files and static assets in production.
* **Docker Support:** Containerized setup via `Dockerfile` and `.dockerignore`.

---

## 📁 Project Structure

```
buykart/
├── API/             # REST API endpoints, serializers, and ViewSets
├── buykart/         # Project configuration (settings, root URLs, WSGI/ASGI)
├── conversation/    # Buyer-seller chat & messaging module
├── core/            # Main landing page, auth views, static files & global templates
├── dashboard/       # User dashboard and informational pages (About, Terms, etc.)
├── item/            # Products, categories, forms, views & marketplace logic
├── media/           # Local media uploads (item images)
├── templates/       # Global error pages (400, 403, 404, 500)
├── Dockerfile       # Container build configuration
├── manage.py        # Django CLI utility
├── requirements.txt # Project dependencies
└── project_structure.txt
```

---

## 🛠️ Tech Stack & Dependencies

* **Backend Framework:** Django 6.x
* **REST API:** Django REST Framework (DRF) & SimpleJWT
* **Database:** PostgreSQL / SQLite (configured via `dj-database-url`)
* **Storage:** Cloudinary (`django-cloudinary-storage`)
* **Styling & UI:** Tailwind CSS (configured in form widgets & responsive templates)
* **Containerization:** Docker

---

## 📊 Database Models

### 1. `item` App

* **Category:**
  * `name`: CharField (max 255)
* **Item:**
  * `category`: ForeignKey -> `Category`
  * `name`: CharField (max 255)
  * `description`: TextField
  * `price`: FloatField
  * `image`: ImageField
  * `is_sold`: BooleanField
  * `created_by`: ForeignKey -> `User`
  * `created_at`: DateTimeField

### 2. `conversation` App

* **Conversation:**
  * `item`: ForeignKey -> `Item`
  * `members`: ManyToManyField -> `User`
  * `created_at`: DateTimeField
  * `modified_at`: DateTimeField
* **ConversationMessage:**
  * `conversation`: ForeignKey -> `Conversation`
  * `content`: TextField
  * `created_by`: ForeignKey -> `User`
  * `created_at`: DateTimeField

---

## 📝 Django Views & Routes (`item` App)

| View Function | Access Level | Description |
| :--- | :--- | :--- |
| `items(request)` | Public | Browse all items with search query (`Q` filter) and category filter. |
| `detail(request, pk)` | Public | View detailed item specifications along with up to 3 related unsold items. |
| `newItem(request)` | Authenticated | Allows registered users to post a new item for sale. |
| `editItem(request, pk)` | Item Owner | Allows item creators to update item metadata or mark as sold. |
| `delete(request, pk)` | Item Owner | Deletes an item and redirects to the user's dashboard. |
| `manage_categories(request)`| Staff Only | Lists all item categories for administration. |
| `add_category(request)` | Staff Only | Form view to add a new marketplace category. |
| `edit_category(request, pk)`| Staff Only | Form view to edit an existing category name. |
| `delete_category(request, pk)`| Staff Only | Removes a category from the database. |

---

## 📋 Django Forms Summary

All forms use Tailwind CSS utility classes embedded in the widget attributes for consistent styling.

* **`SignupForm`** (`core/forms.py`): Extends `UserCreationForm` with `username`, `email`, `password1`, `password2`.
* **`LoginForm`** (`core/forms.py`): Extends standard `AuthenticationForm`.
* **`NewitemForm`** (`item/forms.py`): Creates new product listings (`category`, `name`, `description`, `price`, `image`).
* **`EdititemForm`** (`item/forms.py`): Updates existing listings with an additional `is_sold` checkbox.
* **`CategoryForm`** (`item/forms.py`): Handles creation and editing of item categories.
* **`ConversationMessageForm`** (`conversation/forms.py`): Textarea widget configured for dynamic chat responses.

---

## 🔌 REST API Reference & Endpoints

All API endpoints are implemented using DRF `ModelViewSet`s with nested serialization for clean responses.

| Endpoint | ViewSet | Authentication & Permissions | Description |
| :--- | :--- | :--- | :--- |
| `/api/categories/` | `CategoryViewSet` | Read: Any / Write: Authenticated | Manage item categories |
| `/api/items/` | `ItemViewSet` | Read: Any / Write: Authenticated | Browse, search, and list products |
| `/api/users/` | `UserViewSet` | Read: Any / Write: Authenticated | Retrieve public user info |
| `/api/conversations/` | `ConversationViewSet` | Session Auth & Authenticated | Access user's active chat conversations |
| `/api/messages/` | `ConversationmessageViewset` | Session Auth & Authenticated | Access user's conversation messages |

---



> **Disclaimer:** This project is developed for **educational purposes**. It serves as a learning project to demonstrate multi-app architecture in Django, RESTful API development with Django REST Framework (DRF), database relations, Role-Based Access Control (RBAC) and user authentication workflows.