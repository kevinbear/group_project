# 🔍 404 Error Page – Skill Analysis

## ✅ Skills Demonstrated

### 🧩 Django Template Inheritance
- Used `{% extends "base.html" %}` to inherit from a common base template.
- Utilized `{% block %}` tags (`headerfile` and `placeholder`) to inject page-specific content.

### 📁 Static File Management
- Loaded static files using `{% load static %}`.
- Included CSS and JavaScript specific to the 404 page:
  ```django
  <link href="{% static 'css/404.css' %}" rel="stylesheet" />
  <script src="{% static 'js/404.js' %}"></script>
  ```

### 🎨 Front-End Styling (Bootstrap + Custom Styles)
- Used Bootstrap 5 utility classes for layout and styling:
  - `container-fluid`, `d-flex`, `justify-content-center`, `align-items-center`
  - `col-md`, `text-center`, `text-white`, `p-5`, `fw-bold`, `fs-4`
- Applied a semi-transparent background using inline CSS.
- Styled interactive elements like the button with Bootstrap: `btn btn-primary text-white rounded-pill`.

### ✨ Visual Flair with Emojis & Animations
- Used emojis creatively for a playful tone: 🍕 🍔 🌮 🍩 🍟 🍗 🍎
- Added unique class names like `melting-text` and `melting-background` (presumably styled in `404.css`) for animated or themed effects.

### 🧭 Django URL Routing
- Created a button that uses Django’s `{% url %}` tag to dynamically link to the home page:
  ```django
  <a href="{% url 'home' %}">Return to Home Page</a>
  ```

---