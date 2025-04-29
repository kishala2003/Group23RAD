# StreamVision

"StreamVision" is a modern, user-friendly streaming web application that offers unlimited movies, TV shows, and animations. Users can browse featured content, search for their favorite titles, register and log in to manage their profiles, and save favorites for quick access.

## Features

- Browse movies, TV series, and animations with rich metadata (title, description, genre, release year, rating).
- Featured content slider showcasing top picks.
- User authentication: register, login, and logout.
- User profile page displaying account information and favorite content.
- Search functionality to find movies, series, and animations.
- Responsive and accessible design with keyboard navigation support.
- Flash messages for user feedback.
- Interactive UI with hover effects and play button simulation.
- Secure password hashing and user session management.

## Technologies Used

- Backend: Python, Flask, Flask-SQLAlchemy
- Frontend: HTML5, CSS3, JavaScript, Jinja2 Templating
- Database: SQLite (default with Flask-SQLAlchemy)
- Other: Werkzeug for password hashing, Font Awesome for icons

## Project Structure

streamvision/
│
├── app.py # Main Flask application
├── models.py # Database models (User, Content, Favorite)
├── static/
│ ├── css/
│ │ └── style.css # Stylesheets
│ ├── js/
│ │ └── script.js # JavaScript for interactivity
│ └── images/ # Content images
├── templates/
│ ├── base.html # Base template with header/footer
│ ├── index.html # Home page template
│ ├── login.html # Login page template
│ ├── register.html # Registration page template
│ ├── profile.html # User profile page template
│ └── content_detail.html # Content detail page template
├── README.md # This file
└── requirements.txt # Python dependencies

## Prerequisites

- Python 3.7 or higher installed on your system.
- `pip` package manager.

## Installation and Setup

1. Create and activate a virtual environment (recommended),

On Windows:

python -m venv venv
venv\Scripts\activate

On macOS/Linux:

python3 -m venv venv
source venv/bin/activate

2. Install dependencies

pip install -r requirements.txt

If `requirements.txt` is not present, install manually:

pip install Flask Flask-SQLAlchemy Werkzeug

3. Set up the database

In your Python shell or a setup script, initialize the database:

from app import app, db
with app.app_context():
db.create_all()

This will create the necessary tables (`users`, `contents`, `favorites`).

4. Add initial content

You can add movies, series, and animations to the database either via a script or admin interface (if implemented). Make sure your images are placed in the `static/images/` folder with correct filenames.

## Running the Application

To start the Flask development server, run the following command in your project directory:

py app.py

or if `py` is not recognized, try:

python app.py

By default, the app will be accessible at:

http://127.0.0.1:5000/

Open this URL in your web browser to start using StreamVision.

## Usage

- Home Page: Browse featured content and sections for movies, series, and animations.
- Search: Use the search bar in the header to find specific content.
- Register/Login: Create an account or log in to save favorites and access your profile.
- Profile: View your account info and manage your favorite content.
- Content Detail: Click any content card to see detailed info and watch simulation.

## Accessibility & UX

- Keyboard navigable menus and forms.
- ARIA roles and labels for screen readers.
- Flash messages with auto-dismiss.
- Responsive layout for desktop and mobile.
- Visual indicators for scrollable content sections.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License.

## Github link
https://github.com/kishala2003/Group23RAD

## Contact

For questions or support, please contact:

- name : K.H.T.Pawani Kishala
  Movindu Budvin
  Pahan Hettiarachchi
  M.S.Malshika

- Email: kishalakariyawasam@gmail.com
         kmbalahapperuma@gmail.com
         sandarumalshika652@gmail.com
         41-bit-0082@kdu.ac.lk

- GitHub: [kishala2003](https://github.com/kishala2003)
          [Movindu0616](https://github.com/Movindu0616)
          [Sandaru29882](https://github.com/Sandaru29882)
          [pahan-hettiarachchi](https://github.com/pahan-hettiarachchi)


Thank you for using StreamVision! Enjoy unlimited entertainment at your fingertips.
