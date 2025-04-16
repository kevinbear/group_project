# 📄 About Page – Skill Analysis

## ✅ Skills Demonstrated

### 🧩 Django Template Inheritance & Blocks
- Extended a base template using:
  ```django
  {% extends "base.html" %}
  ```
- Used `{% block placeholder %}` to inject content into the base layout.
- Loaded static files with `{% load static %}` to support image paths.

### 🖼️ Static File Handling
- Correctly referenced static images using Django’s static tag:
  ```django
  <img src="{% static 'image/about_right.jpg' %}" ... />
  ```

### 🧱 Responsive Layout with Bootstrap 5
- Leveraged Bootstrap grid system with:
  - `container`, `row`, and `col-md` for responsive layout.
  - `img-fluid`, `rounded`, `mx-auto`, `d-block` for image scaling and alignment.
- Used `justify-content-center` and `text-center` to neatly align group images and text.

### 🖋️ Content Structuring & Technical Writing
- Wrote clear documentation about the project:
  - Explained tools used: **Django**, **Python**, **HTML/CSS**.
  - Outlined key features: multiple tabs, menu sections, ordering system.
  - Provided contrast with Tkinter to highlight web tech choices.

### 🖼️ Group Member Visual Section
- Displayed a group image (probably an SVG team diagram or placeholder) using:
  ```django
  <img src="{% static 'image/ellipse-90.svg' %}" ... />
  ```
- Smart use of `vw` units for responsive scaling:
  ```css
  style="width: 75vw; height: auto"
  ```

---

## 📦 Tools & Technologies Used

| Tool/Library | Purpose |
|--------------|---------|
| Django       | Backend framework and templating |
| HTML         | Structure and content |
| CSS          | Custom styling |
| Bootstrap 5  | Responsive layout and UI utility classes |
| Static files | Image handling and assets |
