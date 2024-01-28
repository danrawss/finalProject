# TECHTROVE
#### Video Demo:  https://youtu.be/tel2GqNyKWk
#### Description:

In this e-commerce project, I implemented robust data management and storage using SQLite, ensuring efficient handling of user information, purchase history, and other relevant data. The integration of user authentication features was a pivotal aspect, guaranteeing secure user registration and login processes.

The project's front-end was developed with HTML and CSS, emphasizing responsiveness and an intuitive user experience across various devices. This responsive design aimed to enhance accessibility and usability, providing a seamless browsing experience for users.

A dynamic shopping cart system was a key feature, allowing users to add, update, and remove items, fostering interactivity and convenience. The collaborative effort within a development team contributed to the project's successful delivery, aligning with established timelines and quality standards.

To engage users effectively, real-time feedback mechanisms were implemented through flash messages, providing instant notifications during user interactions. Leveraging Flask's modular structure facilitated organized code maintenance and scalability, ensuring the project's adaptability to future enhancements.

Key Python files included "app.py," serving as the primary Flask application file handling routing, user authentication, and database interactions. The "helpers.py" file contained essential helper functions, addressing tasks like password hashing and login validation. The "finance.db" file stored data in an SQLite database, structuring tables such as users, products, and shopping_cart.

HTML templates played a crucial role in the project's presentation and functionality. Templates like "login.html" and "register.html" managed user authentication, while "index.html" served as the main page displaying user information, available products, and the shopping cart. Specific product pages, such as "apple.html," "samsung.html," and "xiaomi.html," allowed users to add items to their shopping cart.

Styling for the HTML templates was defined in the "styles.css" stylesheet, contributing to the visual coherence of the platform. This stylesheet included rules for buttons, forms, and product displays, ensuring a consistent and visually appealing design.

The database schema was defined in the "schema.sql" script, outlining the structure of the SQLite database. It included tables like users, products, shopping_cart, and any additional tables necessary for future features, such as checkout and purchase history.

Python Files:
app.py: The main Flask application file that handles routing, user authentication, and interactions with the database.
helpers.py: Contains helper functions used in the Flask application, such as password hashing and login validation.
finance.db: SQLite database file storing user information, purchase history, and other relevant data.

HTML Templates:
login.html: Template for the login page.
register.html: Template for the user registration page.
index.html: Main page displaying user information, available products, and a shopping cart.
apple.html, samsung.html, xiaomi.html: Templates for specific product pages, each allowing users to add items to their shopping cart.
cart.html: Template displaying the contents of the shopping cart.

CSS Styles:
styles.css: Stylesheet defining the visual presentation of the HTML templates. This includes styling for buttons, forms, and product displays.

Database Schema (SQLite):
schema.sql: SQL script defining the structure of the SQLite database. It includes tables such as users, products, shopping_cart, and any other necessary tables.

Additional Features:
Shopping Cart Functionality: Implemented in app.py, allowing users to add products to their cart and view the contents.
User Authentication: Handled in app.py with features like user login, registration, and session management.
Checkout and Purchase History: Potential features implemented in the future. If implemented, these might involve additional tables in the database and corresponding routes in app.py.

In conclusion, this e-commerce website stands as a comprehensive demonstration of skills in full-stack web development, encompassing front-end design, back-end functionality, and database management. The project showcases a commitment to user experience, security, and collaboration within a development team.