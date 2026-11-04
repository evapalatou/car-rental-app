## Code Validation
### HTML
All HTML pages were validated using the [W3C HTML Validator](https://validator.w3.org/).

| PAGE | VALIDATOR SCREENSHOT | RESULT |
|---|---|---|
| Home Page | <details><summary>Home</summary>![HTML Home](readme/testing/home.png)</details> | PASS |
| Browse Cars Page | <details><summary>Browse Cars</summary>![HTML Browse Cars](readme/testing/browse-cars.png)</details> | FAIL |
| Car Details Page | <details><summary>Car Details</summary>![HTML Car Details](readme/testing/car-details.png)</details> | PASS |
| Registration Page | <details><summary>Registration</summary>![HTML Registration](readme/testing/registration.png)</details> | FAIL |
| Login Page | <details><summary>Login</summary>![HTML Login](readme/testing/login.png)</details> | PASS |
| Testimonials Page | <details><summary>Testimonials</summary>![HTML Testimonials](readme/testing/testimonials.png)</details> | FAIL |
| Contact Page | <details><summary>Contact</summary>![HTML Contact](readme/testing/contact.png)</details> | PASS |

### CSS
CSS was validated using [Jigsaw W3](https://jigsaw.w3.org/css-validator/).

| FILE | VALIDATOR SCREENSHOT | RESULT |
|---|---|---|
| style.css | <details><summary>style.css</summary>![CSS](readme/testing/css.png)</details> | PASS |

### JAVASCRIPT
JavaScript was validated using [JSHint](https://jshint.com/).

| FILE | VALIDATOR SCREENSHOT | RESULT |
|---|---|---|
| navigation.js | <details><summary>navigation.js</summary>![CSS](readme/testing/javascript.png)</details> | PASS (4 warnings) |

### PYTHON
Python was validated using [CI Python Linter](https://pep8ci.herokuapp.com/).

| FILE | VALIDATOR SCREENSHOT | RESULT |
|---|---|---|
| cars/admin.py | <details><summary>Cars Admin</summary>![CSS](readme/testing/cars-admin.png)</details> | PASS |
| cars/apps.py | <details><summary>Cars Apps</summary>![CSS](readme/testing/cars-apps.png)</details> | PASS |
| cars/forms.py | <details><summary>Cars Forms</summary>![CSS](readme/testing/cars-forms.png)</details> | PASS |
| cars/models.py | <details><summary>Cars Models</summary>![CSS](readme/testing/cars-models.png)</details> | PASS |
| cars/views.py | <details><summary>Cars Views</summary>![CSS](readme/testing/cars-views.png)</details> | PASS |

## Lighthouse
For most of the pages Lighthouse reporting tool is not indicating Performance.

| PAGE | SCREENSHOT |
|---|---|
| Home | <details><summary>Home</summary>![CSS](readme/testing/lh-home.png)</details> | 
| Register | <details><summary>Register</summary>![CSS](readme/testing/lh-register.png)</details> | 
| Login | <details><summary>Login</summary>![CSS](readme/testing/lh-login.png)</details> | 
| Logout | <details><summary>Logout</summary>![CSS](readme/testing/lh-logout.png)</details> |
| Browse Cars | <details><summary>Browse Cars</summary>![CSS](readme/testing/lh-browse-cars.png)</details> |
| Car Details | <details><summary>Car Details</summary>![CSS](readme/testing/lh-car-details.png)</details> | 
| My Bookings | <details><summary>My Bookings</summary>![CSS](readme/testing/lh-mybookings.png)</details> | 
| Testimonials | <details><summary>Testimonials</summary>![CSS](readme/testing/lh-testimonials.png)</details> | 
| Write Testimonial | <details><summary>Write Testimonial</summary>![CSS](readme/testing/lh-write-testimonial.png)</details> | 
| Contact | <details><summary>Contact</summary>![CSS](readme/testing/lh-contacts.png)</details> | 

## Manual Testing
### Navigation & Footer
| Test Name | Steps | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| Logo Navigation | 1. Click on the ELITE RIDES logo/title. | User is redirected to the homepage. | Same as expected | ✓ Pass |
| Home Navigation | 1. Click on the Home link. | User is redirected to the homepage. | Same as expected | ✓ Pass |
| Browse Cars Navigation | 1. Click on the Browse Cars link. | User is redirected to the car listing page. | Same as expected | ✓ Pass |
| Register Navigation | 1. While logged out, click on the Register link. | User is redirected to the registration page. | Same as expected | ✓ Pass |
| Login Navigation | 1. While logged out, click on the Login link. | User is redirected to the login page. | Same as expected | ✓ Pass |
| My Bookings Navigation | 1. Log in as a customer. 2. Click on the My Bookings link. | User is redirected to their bookings page. | Same as expected | ✓ Pass |
| Logout Navigation | 1. Log in to the website. 2. Click on the Logout link. 3. Confirm logout if prompted. | User is logged out and redirected to the homepage with a confirmation message. | Same as expected | ✓ Pass |
| Footer LinkedIn Link | 1. Scroll to the footer. 2. Click on the LinkedIn icon. | User is redirected to the LinkedIn profile. | Same as expected | ✓ Pass |
| Footer GitHub Link | 1. Scroll to the footer. 2. Click on the GitHub icon. | User is redirected to the GitHub profile. | Same as expected | ✓ Pass |
