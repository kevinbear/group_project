# 📄 Signup Page – Skill Analysis

## ✅ Skills Demonstrated

### 🧩 Django Template Inheritance & Blocks
- Extended the base layout using:
  ```django
  {% extends "base.html" %}
  ```
- Used `{% block stylesheet %}` to load page-specific CSS:
  ```html
  <link href="{% static 'css/signup.css' %}" rel="stylesheet" />
  ```
- Wrapped page content inside `{% block placeholder %}`.

### 🔐 Secure Form Handling with CSRF
- Included CSRF token for secure form submission:
  ```django
  {% csrf_token %}
  ```
- Form method set to `POST` with action pointing to the signup URL:
  ```django
  <form method="POST" action="{% url 'signup' %}">
  ```

### 🧱 Responsive Layout & Bootstrap Integration
- Used Bootstrap grid with `container-fluid`, `row`, and `col` classes.
- Implemented two-column layout:
  - Left: signup form
  - Right: image (`restaurant-image` class)
- Added responsiveness: image column hidden on small screens with media query.

### 🧑‍💻 Form Design & UX
- Used `form-floating` for modern label UX.
- Applied `input-group` with Bootstrap and FontAwesome icons for clarity.
- Enhanced password field with toggle visibility icon (`fa-eye`).

### 🎨 Custom Dark Theme Styling
- Custom dark mode for form fields:
  ```css
  background-color: #222;
  color: #fff;
  border-color: #555;
  ```
- Customized label behavior on focus and filled inputs using sibling combinators.
- Removed Bootstrap's white label background with:
  ```css
  .form-floating > label::after {
    background-color: transparent;
  }
  ```

### 🧠 Interactive JavaScript Features
- Implemented password visibility toggle using JS:
  ```javascript
  document.getElementById("togglePassword").addEventListener("click", ...)
  ```
- Dynamically switches icon between `fa-eye` and `fa-eye-slash`.

### ⚠️ Error Handling Display
- Used Django template logic to loop through form errors and display them in a styled alert:
  ```django
  {% if form.errors %}
    <div class="alert alert-warning"> ... </div>
  {% endif %}
  ```

---

## 🎨 Design Elements & Techniques

| Feature               | Description |
|-----------------------|-------------|
| **Floating Labels**   | Improves form clarity and modern feel. |
| **FontAwesome Icons** | Used in `input-group-text` for visual cues. |
| **Dark Mode Styling** | Enhances visual comfort and custom UI feel. |
| **Responsive Layout** | Two-column layout collapses gracefully on mobile. |
| **Password Toggle**   | Enhances usability and user trust. |
| **Form Validation Feedback** | Error messages shown via alert system. |

---

## 📦 Tools & Technologies Used

| Tool/Library  | Purpose |
|---------------|---------|
| Django        | Backend framework and template engine |
| HTML          | Form structure and semantics |
| CSS           | Custom dark theme and responsive adjustments |
| Bootstrap 5   | Grid layout, utility classes, form components |
| JavaScript    | Password toggle interactivity |
| FontAwesome   | Icons in form fields |
| Static files  | External CSS and image loading |
