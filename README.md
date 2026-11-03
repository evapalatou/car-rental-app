<h1 align="center">🏎 Elite Rides Car Rental 🏎</h1>

![Overview](readme/overview.png)

## Overview
Elite Rides is a web-based car rental platform designed to make finding and booking a rental car simple and convenient. The website allows visitors to browse a selection of available vehicles, explore individual car details and choose a vehicle that suits their travel needs. With a clean and responsive interface, Elite Rides aims to provide a straightforward experience across desktop, tablet and mobile devices. Registered customers can manage their reservations, view their booking history and share their experiences through testimonials. The platform also provides a contact form for enquiries, making it easy for customers to get in touch.

## Purpose
The purpose of Elite Rides is to provide a user-friendly car rental application that streamlines the vehicle browsing and reservation process for customers while allowing administrators to manage the platform efficiently. Customers can create an account, browse available cars, make reservations, manage their bookings and submit testimonials. Administrators have access to dedicated management functionality, allowing them to add, edit and remove vehicles, oversee reservations, manage customer enquiries and approve testimonials. The project brings together customer-facing features and administrative tools in one full-stack web application, providing a practical and accessible solution for managing a car rental service.

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

* [Elite Rides Car Rental](#elite-rides-car-rental)
* [User Experience Design](#user-experience-design)
    * [The Strategy Plane](#the-strategy-plane)
        * [Site Goals](#site-goals)
        * [Agile Planning](#agile-planning)
            * [Epics](#epics)
            * [User Stories](#user-stories)
    * [The Scope Plane](#the-scope-plane)
    * [The Structure Plane](#the-structure-plane)
       * [Features](#features)
       * [Future Enhancements](#future-enhancements)
    * [The Skeleton Plane](#the-skeleton-plane)
       * [Wireframes](#wireframes)
       * [Database Design](#database-design)
       * [Security](#security)
    * [The Surface Plane](#the-surface-plane)
       * [Design](#design)
       * [Color Scheme](#color-scheme)
       * [Typography](#typography)
       * [Imagery](#imagery)
   * [Technologies Used](#technologies-used)
   * [Manual Testing](#manual-testing)
       * [Fixed Bugs](#fixed-bugs)
       * [Unfixed Errors](#unfixed-errors)
   * [Deployment](#deployment)
       * [Version Control](#version-control)
       * [Heroku Deployment](#heroku-deployment)
       * [Run Locally](#run-locally)
       * [Fork Project](#fork-project)
   * [Credits](#credits)

# User Experience Design

## The Strategy Plane

### Site Goals
- Provide a fully responsive, user-friendly platform for customers to browse available rental cars.
- Allow visitors to explore individual vehicles and view their specifications, features and rental prices.
- Enable registered customers to create accounts, make reservations and manage their bookings.
- Provide secure user and administrator access with appropriate permissions.
- Allow administrators to manage vehicles, reservations, customer enquiries and testimonials through dedicated management features.
- Offer customers a convenient way to contact the business and share their experiences through testimonials.
- Create a reliable and straightforward car rental experience across desktop, tablet and mobile devices.

### Agile Planning
![Kanban Board](readme/kanban-board.png)
Elite Rides Car Rental was developed using Agile methodologies, with tasks organised and tracked through a GitHub Projects Kanban board. The project was divided into manageable user stories, allowing development to progress in small, structured steps. Each user story includes acceptance criteria to define the expected functionality and establish clear conditions for completion. GitHub Issues were used to document individual tasks, track progress and organise development work. Labels helped categorise issues and distinguish different types of work. The Kanban board provided an overview of the project's progress, with user stories moved through the relevant stages as development and testing progressed. This approach helped prioritise essential features, monitor completed work and identify outstanding tasks. For more details, you can view the [Agile Planning Board](https://github.com/users/evapalatou/projects/4) and the [project repository](https://github.com/evapalatou/car-rental-app).

### User Stories: [Car Rental Kanban Board](https://github.com/users/evapalatou/projects/4)

**Epic 1: Accounts**
- As a new user, I want to register an account so that I can book cars.
- As a site user, I want to log in and out so that my bookings stay private.
- As a site user, I want to see that I’m logged in so that I know my session state.
- As a site user, I want to reset a forgotten password so that I can get back into my account.
- As a new user, I want to be sent to the login page if I open a booking page so that restricted pages stay protected.

**Epic 2: Browse Cars and Navigate**
- As a new user, I want to browse the available cars so that I can see what’s on offer.
- As a new user, I want to view a car’s details so that I can decide if it suits me.
- As a new user, I want to filter cars by category so that I can narrow my choice.
- As a new user, I want to search for cars by make or model so that I can find a specific car quickly.
- As a new user, I want to understand what the site offers so that I can quickly reach the cars.

**Epic 3: Reservations**
- As a site user, I want to book a car for a date range so that it’s reserved for me.
- As a site user, I want to be told when my dates aren’t available so that I can choose others.
- As a site user, I want to see my bookings so that I can keep track of them.
- As a site user, I want to edit my booking so that I can change my plans.
- As a site user, I want to cancel my booking so that I don’t hold a car I don’t need.
- As a site admin, I want to approve or decline reservations so that I control the fleet.
- As a site user, I want to receive an email about my reservation so that I have a record of it.

**Epic 4: Fleet Management**
- As a site admin, I want to add a car so that the fleet stays up to date.
- As a site admin, I want to edit a car so that I can change its price or details.
- As a site admin, I want to delete a car so that unavailable cars are removed.

**Epic 5: Contact**
- As a new user, I want to send a message through a contact form so that I can ask the owner a question.
- As a site admin, I want to read the contact messages so that I can reply to them.

**Epic 6: Testimonials**
- As a site user, I want to write a testimonial so that I can share my experience.
- As a site admin, I want to approve testimonials so that I control what shows.

## The Scope Plane
At the beginning of the Elite Rides project, I identified the essential features needed to create a functional car rental platform. To manage the project scope, prioritise development and avoid scope creep within the available timeframe, I used the MoSCoW prioritisation method. This approach helped me distinguish between essential features required for the minimum viable product and additional functionality that could be considered for future development.

**Must Have**
- User registration, login and logout.
- Password recovery.
- Browse available rental cars.
- View individual car details.
- Search cars by make or model.
- Filter cars by category.
- Make a reservation by selecting rental dates.
- Check car availability and prevent overlapping reservations.
- View, edit and cancel personal reservations.
- Email notifications relating to reservations.
- Administrator access with appropriate permissions.
- Full CRUD functionality for car management.
- Administrator ability to approve or decline reservations.
- Contact form for customer enquiries.
- Administrator ability to manage contact messages.
- Customer testimonials and administrator approval.
- Responsive design for desktop, tablet and mobile devices.

**Should Have**
- A dedicated homepage introducing the car rental service.
- Clear navigation for customers and administrators.
- Informative confirmation and feedback messages.
- A straightforward and accessible user experience.

**Could Have**
- Online payment integration.
- Customer profile management.
- Automated booking reminders.
- Additional vehicle filtering options.

**Won't Have**
- Online payment processing.
- A loyalty or rewards programme.
- A live chat support system.
- A mobile application.
- Integration with external car rental or fleet management services.

## The Structure Plane
### Flow Chart
To help with the website I created a flowchart using [Draw.io](https://draw.io/)
![Flow Chart](readme/flow-chart.png)

### Features
<details>
<summary><strong>Navigation & Footer</strong></summary>
The navigation bar displays the ELITE RIDES logo and website name, which also serves as a link to the homepage. It provides access to the main sections of the website. Visitors who are not logged in can access the Register and Login options. Once logged in, customers can access their account features, including My Bookings, and the Logout option. Additional management links are available to staff users. The footer displays © 2026 Evanthia Palatou, followed by links to LinkedIn and GitHub, represented by social media icons.

![Navigation](readme/feature-1.png) 
![Footer](readme/feature-2.png) 
</details>

### Future Enhancements

## The Skeleton Plane

### Wireframes

Homepage
![Homepage Wireframe](wireframes/1-home.png)

Car List
![Car List Wireframe](wireframes/2-car_list.png)

Car Detail
![Car Detail Wireframe](wireframes/3-car_detail.png)

Booking Form
![Booking Form Wireframe](wireframes/4-booking_form.png)

My Bookings
![MyBookings Wireframe](wireframes/5-my_bookings.png)

Register
![Register Wireframe](wireframes/6-register.png)

Login
![Login Wireframe](wireframes/7-login.png)

Car List (admin)
![Car List (admin) Wireframe](wireframes/8-car_list_admin.png)

Car Form
![Car Form Wireframe](wireframes/9-car_form.png)

Reservations
![Reservations Wireframe](wireframes/10-reservations.png)

Contact Us
![Contact Us Wireframe](wireframes/11-contact.png)

Testimonials
![Testimonials Wireframe](wireframes/12-testimonials.png)

### Database Design

![ERD Diagram](readme/car-rental-erd.png)

### Security

## The Surface Plane

### Design
### Color Scheme
### Typography
### Imagery

## Technologies Used

## Manual Testing

### Fixed Bugs
### Unfixed Errors

## Deployment

### Version Control

### Heroku Deployment

### Run Locally

### Fork Project

## Credits

