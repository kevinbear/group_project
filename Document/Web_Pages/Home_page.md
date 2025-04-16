# Homepage Breakdown (`home.html` and corresponding view)

## 🧠 What the view does

1. **Checking if the user is logged in**:
   - If yes, you grab their name and role.
   - You store those in the context dictionary so the template can use them.
   - You also flash a message (like "Welcome back") using `messages.info`.

2. **Grabbing random menu items**:
   - You select 4 random `MenuItem` objects from your database.
   - These are passed into the template as `random_items`.

3. **Rendering the `home.html`**:
   - The view sends all that data to the template.

---

## 🌐 Template Walkthrough (`home.html`)

`home.html` is broken into sections:

### 1. Hero Section
- Big, full-screen image with a title: “Where every meal is a masterpiece.”
- A dropdown menu that links to breakfast, lunch, dinner (anchors like `#breakfast`, etc).

### 2. Floating Image Section
- Three stacked divs:
  - Omelette image (green background)
  - Pancake image (blue background)
  - Burger image (orange background)
- Each one is absolutely positioned on desktop and stacked nicely on mobile.
- Great for drawing attention!

### 3. Random Menu Items Section (`r2`)
- Looping through the `random_items` you passed from the view.
- Each menu item is shown in a card:
  - Image
  - Name, description
  - Quantity input with plus/minus
  - “Add to cart” button

### 4. Call-to-Action Section (`r3`)
- Large image background.
- Overlay text encouraging users to explore the full menu.
- A button that scrolls them down or takes them to another page.

### 5. Location Section (`r4`)
- Section title: “Visit Our Location”
- Uses Leaflet.js to render a map centered on CSUF.

---

## 📦 JavaScript

### Cart Functionality
The script listens for click events on all `.add-to-cart` buttons. When clicked:

- It grabs the item ID, name, price, and selected quantity.
- Sends a POST request to the `add_to_cart` endpoint using `fetch`.
- Uses the CSRF token to stay secure.
- On success, alerts the user and logs the updated cart.

```js
fetch("{% url 'add_to_cart' %}", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken
    },
    body: JSON.stringify({
        id: itemId,
        quantity: quantity,
        name: itemName,
        price: itemPrice
    })
})
```

## 🗺️ Leaflet Map Integration
```js
var map = L.map('map').setView([33.8825, -117.8850], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; OpenStreetMap'
}).addTo(map);

L.marker([33.8825, -117.8850]).addTo(map)
    .bindPopup("<b>California State University, Fullerton</b><br>800 N State College Blvd")
    .openPopup();
```