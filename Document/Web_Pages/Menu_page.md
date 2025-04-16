# 📄 Menu Page with Bootstrap Tabs & Cart Integration – Skill Analysis

## ✅ Skills Demonstrated

### 🧩 Django Template Foundation
- Extended base layout:
  ```django
  {% extends "base.html" %}
  {% load static %}
  ```
- Used context variables to render menu items (`breakfast_items`, `lunch_items`, `dinner_items`) dynamically.

---

### 🍽️ Bootstrap UI Integration
- Integrated Bootstrap tab system:
  ```html
  <ul class="nav nav-tabs" id="menuTab">
    <li class="nav-item"><button class="nav-link active" data-bs-target="#breakfast">...</button></li>
    ...
  </ul>
  ```
- Used `tab-pane` classes to organize content inside tabs. Each section (`#breakfast`, `#lunch`, `#dinner`) is toggled by the navbar above.

---

### 💳 Menu Cards with Quantity Select & Add to Cart
- For each item, displayed a fully responsive card with:
  - Image
  - Name
  - Optional combo price
  - Description
  - Price
  - Quantity selector (`+`, `-`, and number input)
  - "Add to Cart" button
- Example markup:
  ```html
  <div class="btn-group">
    <button type="button" class="btn btn-primary">-</button>
    <input type="number" class="text-center" value="1" min="1">
    <button type="button" class="btn btn-primary">+</button>
  </div>
  <button class="btn btn-success add-to-cart" data-id="..." data-name="..." data-price="...">
    <i class="fas fa-shopping-cart"> Add to Cart</i>
  </button>
  ```

---

### 🧠 Empty State UX
- Gracefully handled empty sections with placeholder cards:
  ```html
  <h5 class="card-title">No [meal] items available.</h5>
  ```

---

### ⚙️ JavaScript Functionality

#### ✅ Bootstrap Tab Trigger on Page Load
- Automatically switches to the correct tab based on `window.location.hash`:
  ```js
  document.addEventListener("DOMContentLoaded", function () {
    const hash = window.location.hash;
    ...
  });
  ```

#### 🛒 Add-to-Cart AJAX POST
- Captures quantity, item details and sends JSON payload via `fetch()`:
  ```js
  fetch("{% url 'add_to_cart' %}", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken
    },
    body: JSON.stringify({ id, quantity, name, price })
  });
  ```
- Includes `csrf_token` for secure POST requests.
- Uses `dataset` attributes to collect item info.

---

## 📦 Tools & Technologies Used

| Tool/Library    | Purpose                              |
|-----------------|--------------------------------------|
| Django          | Backend, templating, data context    |
| Bootstrap 5     | Responsive tabs, layout, styling     |
| FontAwesome     | Icons for meal types and cart button |
| Vanilla JS      | DOM interaction, tab toggling, AJAX  |
| Django URLs     | Secure cart handling with CSRF       |

---

## ✨ Enhancement Suggestions

1. **Make + / - Buttons Functional:**
   - Currently, the plus/minus buttons are static. Add click handlers to increment/decrement quantity values dynamically.

2. **Feedback UI:**
   - Instead of `alert("Item added to cart!")`, consider using a toast or in-page notification for better UX.

3. **Disable Add to Cart on Empty Input:**
   - Prevent users from adding items with invalid quantity (0, blank, etc.).

4. **Partial Template Refactor:**
   - Consider moving the repeated card HTML into a partial like:
     ```django
     {% include "partials/menu_card.html" with item=item %}
     ```

---

