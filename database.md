# Rebuind database
### Step 1: Delete the database file
```bash
rm db.sqlite3
```

### Step 2: Remove all previous migrations (optional but helpful)
```bash
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
```
This deletes all auto-generated migration files, but keeps __init__.py so Django still treats them as packages.

### Step 3: Rebuild everything from scratch
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Create new superuser
```bash
python manage.py createsuperuser
```

# Create Super User and CustomUser
### Step 1: Login Admin Panel
#### [Login Page](http://127.0.0.1:8000/admin/login/?next=/admin/)
#### [Admin Page](http://127.0.0.1:8000/admin/)

### Step 2: Create other superuser by using admin panel
1. Add other member in our group
2. Eamil address is school address
3. Password is `project7`

### Step 3: Run generate_dummy_data
Create dummy data to database
```bash
python manage.py generate_dummy_data
```

# Build our MenuItem Database
### Step 1: Create breakfast menu item

#### Breakfast List: ['Pancakes', 'French Toast', 'Waffles', 'Omelette', '2 Eggs & Bacon or Sausage', 'Maple Oatmeal', 'Fruit Bowl']
---
+ Pancakes – Fluffy, golden pancakes served with butter and warm maple syrup.
+ French Toast – Thick slices of brioche dipped in cinnamon-vanilla egg batter, griddled to perfection.
+ Waffles – Crisp on the outside, soft on the inside – our classic Belgian waffles come with syrup and butter.
+ Omelette – A hearty three-egg omelette filled with your choice of cheese, veggies, and meats.
+ 2 Eggs & Bacon or Sausage – Two farm-fresh eggs cooked your way, served with crispy bacon or savory sausage.
+ Maple Oatmeal – Warm and wholesome oats simmered with maple syrup, topped with brown sugar and cinnamon.
+ Fruit Bowl – A refreshing mix of seasonal fruits, perfect as a light breakfast or a sweet side.
---
+ Pancakes – $6.99 Add $4.99 for combo
+ French Toast – $7.99 Add $4.99 for combo
+ Waffles – $7.99 Add $4.99 for combo
+ Omelette – $9.99
+ 2 Eggs & Bacon or Sausage – $8.49
+ Maple Oatmeal – $5.49
+ Fruit Bowl – $6.59
---
All images in `/static/image/breakfast`, but still need manual upload to the admin panel > Menu items

### Step 2: Create lunch menu item
#### Lunch List: ['Grilled Chicken Sandwich', 'BLT Sandwich', 'Ham and Swiss Sandwich', 'Caesar Salad', 'CA Cobb Salad', 'Cheeseburger', 'Spaghetti', 'Tomato Basil Soup', 'Chicken Soup']
---
+ Grilled Chicken Sandwich – Tender grilled chicken breast with lettuce, tomato, and mayo on a toasted bun.
+ BLT Sandwich – Crispy bacon, fresh lettuce, and juicy tomato layered between toasted bread with mayo.
+ Ham and Swiss Sandwich – Classic deli-style sandwich with smoked ham, Swiss cheese, and mustard on your choice of bread.
+ Caesar Salad – Crisp romaine lettuce tossed with creamy Caesar dressing, croutons, and parmesan cheese.
+ California Cobb Salad – A vibrant mix of greens topped with grilled chicken, avocado, bacon, egg, tomato, and blue cheese crumbles.
+ Cheeseburger – A juicy grilled beef patty topped with melted cheddar cheese, lettuce, tomato, pickles, and onions, served on a toasted bun with your choice of sauce.
+ Spaghetti – Classic spaghetti pasta served with savory marinara sauce and grated parmesan.
+ Tomato Basil Soup – Smooth, rich tomato soup infused with fresh basil — comfort in a bowl.
+ Chicken Soup – A hearty blend of tender chicken, vegetables, and noodles in warm, flavorful broth.
---
+ Grilled Chicken Sandwich - $8.99
+ BLT Sandwich - $9.99
+ Ham and Swiss Sandwich - $7.99
+ Caesar Salad - $9.99
+ CA Cobb Salad - $15.99
+ Cheeseburger - $16.49
+ Spaghetti - $14.99
+ Tomato Basil Soup - $6.99
+ Chicken Soup - $7.99
---
All images in `/static/image/lunch`, but still need manual upload to the admin panel > Menu items

### Step 3: Create dinner menu item
#### Dinner List: ['Filet Mignon', 'New York Strip Steak', 'Grilled Salmon', 'Grilled Halibut', 'Pasta Alfredo', 'Pesto Penne', 'Lamb Chops with Side Salad', 'Caesar Salad', 'Apple Walnut Salad']
---
+ Filet Mignon – A tender, premium-cut filet grilled to your liking, served with a side of seasonal vegetables.
+ New York Strip Steak – Juicy and flavorful, this classic steak is seared to perfection and paired with your choice of side.
+ Grilled Salmon – Wild-caught salmon grilled with a touch of lemon and herbs, served with roasted vegetables.
+ Grilled Halibut – Light and flaky halibut fillet grilled and served with a garlic butter glaze and fresh sides.
+ Pasta Alfredo – Creamy Alfredo sauce tossed with fettuccine pasta and topped with parmesan — rich and comforting.
+ Pesto Penne – Penne pasta tossed in house-made basil pesto with cherry tomatoes and grated cheese.
+ Lamb Chops with Side Salad – Succulent lamb chops seasoned and grilled, served with a fresh garden side salad.
+ Lobser – Succulent lobster tail meat, pan-seared in garlic herb butter, served with grilled asparagus and creamy mashed potatoes.
+ Apple Walnut Salad – Mixed greens with sliced apples, candied walnuts, blue cheese, and a light vinaigrette.
---
+ Filet Mignon - $27.99
+ NY Strip Steak - $25.99
+ Grilled Salmon - $23.49
+ Grilled Halibut - $23.49
+ Pasta Alfredo - $17.99
+ Pesto Penne - $18.99
+ Lamb Chops with Side Salad - 34.99
+ Lobster - $32.99
+ Apple Walnut Salad - $11.99
---
All images in `/static/image/dinner`, but still need manual upload to the admin panel > Menu items

# Backup working sqlite database
1. Order Table have majority issue right now
2. I need to backup all data before I delete other table
3. Backup working database
```bash
python manage.py dumpdata restaurant.MenuItem --indent 2 > menuitem_backup.json
python manage.py dumpdata restaurant.GuestOrder --indent 2 > guestorder_backup.json
python manage.py dumpdata restaurant.CustomUser --indent 2 > customuser_backup.json
python manage.py dumpdata restaurant.UserProfile --indent 2 > userprofile_backup.json
```
4. Reset the database
```bash
rm db.sqlite3
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

python manage.py makemigrations
python manage.py migrate
```
5. Restore backed up data
```bash
python manage.py loaddata menuitem_backup.json
python manage.py loaddata guestorder_backup.json
python manage.py loaddata customuser_backup.json
python manage.py loaddata userprofile_backup.json
``` 