# Bookymark
**Bookymark**

Hello, my name is Nada Mohamed Hassan, and I’m from Egypt, currently living in Port Said. I’m a dedicated student pursuing a degree in Electronics and Communications Engineering. My passion for technology and problem-solving has driven me to explore various fields in programming and web development, which inspired me to create my final project: "Bookymark."

Bookymark is a website designed to help users easily manage and organize their favorite online links. In today’s world, where we constantly access information from a wide range of sources, keeping track of useful and important links can become overwhelming. My platform offers users the ability to register, log in, and efficiently categorize their bookmarks into different groups, such as work-related, study resources, or personal interests. This organizational structure makes it simple for users to retrieve specific links when they need them.

I developed this project using a combination of HTML, CSS, JavaScript, SQL, and Flask. These technologies allowed me to create a user-friendly interface that focuses on a clean, responsive design, ensuring a smooth and intuitive experience on both desktop and mobile devices. Beyond basic bookmark management, Bookymark offers additional features such as the ability to add, edit, and delete bookmarks, as well as advanced search and sorting options. This ensures that users can quickly find the links they are looking for, even as their collection of bookmarks grows.

One of my primary goals with this project is to deliver a practical, user-centric tool that simplifies the way people manage online information. I’m committed to continuously improving Bookymark by adding new features, enhancing its usability, and expanding its functionality based on user feedback.

This project represents not only my technical skills but also my ability to identify and solve real-world challenges through software development. I'm excited about the potential impact of Bookymark and am eager to continue learning and developing my expertise in the field of web development.


## Table of Contents

- [Features](#features)
- [Routes](#routes)
- [Technologies Used](#technologies-used)
- [Database Schema](#database-schema)
- [CSS and JavaScript](#css-and-javascript)
- [Conclusion](#conclusion)

---

## Features

- **User Authentication**: Register, log in, and log out with secure sessions.
- **Bookmark Management**: Add, edit, delete, and manage bookmarks.
- **Categorization**: Classify bookmarks into different categories like work, study, university, or other.
- **Search and Filter**: Search bookmarks and sort them alphabetically or by frequency of use.
- **Bookmark Icons**: Add images to bookmarks for a visual representation.
- **Bookmark Stats**: View bookmark usage statistics and manage favorite bookmarks.


---


## Routes

- **/** - Home page: Displays the main welcome page for Bookymark with options for login and registration.
- **/login** - User login: Allows users to log in using their credentials.
- **/register** - User registration: Enables new users to register an account.
- **/logout** - User logout: Logs users out and redirects them to the home page.
- **/bookmark** - View and manage bookmarks: Shows the user's bookmarks and provides options to manage them.
- **/add** - Add a new bookmark: Allows users to add a new bookmark to their list.
- **/edit/<id>** - Edit a bookmark: Allows users to edit an existing bookmark based on its ID.
- **/delete/<id>** - Delete a bookmark: Deletes a bookmark with the given ID from the user's list.
- **/search** - Search bookmarks: Enables users to search for bookmarks based on keywords.
- **/sort** - Sort bookmarks: Provides options to sort bookmarks alphabetically or by frequency of use.


---


## Technologies Used

- **Flask**: A micro web framework for Python, used for building the web application.
- **SQLite**: A lightweight database used for storing user data and bookmarks.
- **HTML**: The standard markup language for creating web pages.
- **CSS**: A style sheet language used for describing the presentation of the web pages.
- **JavaScript**: A programming language used for client-side scripting to enhance user interaction.
- **Bootstrap**: A front-end framework for developing responsive and mobile-first websites.


---

## Database Schema

The database for the Bookymark application consists of the following tables:

### Users Table
| Column      | Type      | Description                         |
|-------------|-----------|-------------------------------------|
| id          | INTEGER   | Primary key, unique user identifier |
| username    | TEXT      | Unique username for the user       |
| password    | TEXT      | Hashed password for secure login    |
| email       | TEXT      | User's email address                |

### Bookmarks Table
| Column      | Type      | Description                         |
|-------------|-----------|-------------------------------------|
| id          | INTEGER   | Primary key, unique bookmark identifier |
| user_id     | INTEGER   | Foreign key referencing Users table |
| url         | TEXT      | The URL of the bookmark             |
| name        | TEXT      | The name or title of the bookmark   |
| category    | TEXT      | Category of the bookmark (work, study, etc.) |
| created_at  | DATETIME  | Timestamp of when the bookmark was created |

### Usage
- **Users Table**: Stores user account information, including hashed passwords for security.
- **Bookmarks Table**: Stores bookmarks linked to users, allowing for management and categorization.


---

## CSS and JavaScript

This project utilizes CSS and JavaScript for styling and interactive features.

### CSS
- **Styling Framework**: The application uses [Bootstrap](https://getbootstrap.com/) for responsive design and pre-defined styles. It helps in creating a clean and modern user interface.
- **Custom Styles**: Additional custom styles are provided in `styles.css`, which includes:
  - Layout adjustments
  - Color schemes
  - Button and form styling
  - Hover effects

### JavaScript
- **Functionality**: JavaScript is used to enhance user experience through:
  - Form validation: Ensures that user input is valid before submission.
  - Dynamic content: Updates the bookmark list dynamically without refreshing the page.
  - Search and Filter: Allows users to search for specific bookmarks and filter them based on categories.
  - Sorting: Implements sorting of bookmarks by name or frequency of use.

### Libraries
- [jQuery](https://jquery.com/): Used for easier DOM manipulation and event handling.
- [Axios](https://axios-http.com/): Used for making HTTP requests to the server.

Make sure to include links to the relevant CSS and JavaScript files in your HTML templates to ensure proper functionality.


---


## Conclusion

Thank you for exploring the Bookymark project! This web application provides a seamless experience for managing your bookmarks, complete with user authentication and robust features for organization and categorization. We hope this project inspires you to enhance your own web development skills and consider contributing to its future improvements. If you have any questions or suggestions, feel free to reach out!


﻿# Media_player_
This Python project is a versatile media player designed to provide a seamless audio and video playback experience..
