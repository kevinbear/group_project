# 📄 Login Page – Skill Analysis

## ✅ Skills Demonstrated

### 🧩 Django Template Inheritance & Blocks
- Extended the base template using:
  ```django
  {% extends "base.html" %}
  ```
- Defined content areas using template blocks like `{% block stylesheet %}` and `{% block placeholder %}`.
- Used `{% load static %}` to manage CSS file references.

### 🛡️ Secure Form Handling with CSRF
- Implemented CSRF protection using:
  ```django
  {% csrf_token %}
  ```
- Form data is securely submitted via `POST` to the login route using Django’s `{% url %}` tag.

### 🖼️ Static File Usage
- Loaded a custom stylesheet for the login page:
  ```html
  <link href="{% static 'css/signup.css' %}" rel="stylesheet" />
  ```

### 🧱 Responsive Layout with Bootstrap 5
- Applied grid system with `row`, `col`, and responsive sizing classes like `vh-100`.
- Used `d-flex`, `justify-content-between`, `position-relative`, and `text-center` for layout alignment.
- Included responsive hiding of left column on smaller screens using:
  ```css
  @media (max-width: 768px) { .left-column { display: none; } }
  ```

### 🎯 User Interface Enhancements
- Created a floating label login form using `form-floating` for each input.
- Styled form controls with dark theme overrides (custom `background-color`, `color`, `border`, etc).
- Integrated FontAwesome icons in input fields via `input-group-text`.

### 🧠 Interactive JavaScript
- Toggled password visibility with:
  ```javascript
  document.getElementById("togglePassword").addEventListener("click", ...)
  ```
- Included a Bootstrap toast structure for future alert display:
  ```html
  <div class="toast-body"> <!-- Error message --> </div>
  ```

---

## 🎨 Design Elements & Techniques

| Feature            | Description |
|--------------------|-------------|
| **Dark Mode Styling**   | Custom CSS for dark backgrounds, white text, and subtle borders. |
| **Floating Labels**     | Modern UX using `form-floating` to improve field clarity. |
| **Password Toggle**     | Enhances UX with show/hide toggle for password field. |
| **Mobile Responsiveness** | Left column hidden on small screens for better focus on the form. |
| **Bootstrap Toasts**    | Prepared for dynamic error or success notifications. |
| **Z-index Management**  | Controlled layer stacking for image and text overlay. |

---

## 📦 Tools & Technologies Used

| Tool/Library  | Purpose |
|---------------|---------|
| Django        | Backend framework and templating |
| HTML          | Page structure and form handling |
| CSS           | Styling including custom dark mode |
| Bootstrap 5   | Layout system and UI utilities |
| JavaScript    | Frontend interactivity (password toggle, toast init) |
| FontAwesome   | Icons inside form fields |
| Static files  | External CSS and image support |

