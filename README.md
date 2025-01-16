# MSP-4-CrystalsCakes

# Crystal's Cakes - Full-Stack E-Commerce Website

Welcome to Crystal's Cakes! This is a full-stack e-commerce website built using the following technologies:

- **Frontend**:
  - HTML
  - CSS (Styling)
  - Javascript

- **Backend**:
  - Django (Python web framework)
  - SQLite3 (Database)

## Table of Contents

1. About
2. Purpose
3. Software
4. Design
5. Features
6. UI
7. UX
8. Testing
9. Deployment
10. Credit
11. License

## About

Crystal's Cakes is an online e-commerce store where you can buy baked goods and products listed in the online store, it is enabled to allow users to register browse, save items, add items to a basket and checkout, with the appropriate email confirmations

## Purpose
Crystal's Cakes is an online e-commerce store where you can buy baked goods and products listed in the online store, it is enabled to allow users to register browse, save items, add items to a basket and checkout, with appropriate alerts and email confirmations.

This project has been designed to suit the criteria laid out in the Milestone 4 Project of Code Institute and City of Bristols Marking Criteria in order to pass the final qualification.

### Project Goals
To build a functioning e-commerce website
Become familiar with the django framework
Enable user authentication
Build a product portfolio for customers and user to browse
Enable payment through stripe
Alolow users to add favorite items to a list in their user profile

### Developer Goals
Become familiar with Django as a framework
Develop skills in full stack development
Build a functioning final project
Develop skills in web development and coding

## Software
- IDE - VSCode
- Wireframing & Prototyping - Figma / Draw.io
- Data Schema - Draw.io
- Image Conversion - XnConvert

## Design

## UI
### Typography
### Navigation
Bootstrap 5 Template [link]
### Colour Scheme
### Wireframes

## UX
### User Stories

1. Visit the website at http://localhost:3000.
2. Explore the product catalog, add items to your cart, and proceed to checkout.
3. Access the admin dashboard at http://localhost:8000/admin (login required).

### Data Schema

### Features

- User authentication (signup, login, logout)
- Product catalog with search and filtering options
- Shopping cart functionality
- Checkout process
- Admin dashboard for managing products, orders, and users
- Responsive design for mobile and desktop
  
#### Django Apps
- Home
- Products
- Cart
- Profiles
- Checkout
- Media (Static Folders)


## Testing
### User Stories
### HTML
### CSS
### Javascript
### Alpha Testing
### Beta Testing
### Django Testing
 - Email verification on signup has been validated through printing the content to the development copnsole, a screenshot of the console showing the verification email has been included below:
 - ![Console Email Verification](msp4/Milestone-Project-4/Testting/Email-Verification.png)
  

## Bugs & Fixes
Numerous bugs where introduced during development as the tempalte followed was using older versions of django, crispy-forms, bootstrap, and jQuery. As I opted to use the most current version there have been numerous conflicts that have had to be addressed and resolutions found.
Crisp-Form tags not functioning, removed crispy-forms tags in place of standard form formatting.
Fixtures data not loading, used boutique ado template and populated with own data
Add to cart - Issues adding items to cart and editing cart contents, product id not passed through correctly
Favorites functionality - Could not get items to add to favorites list, required item id and not passed through in view

## Known Bugs in Deployment
- Account Details form does not render on profile
- Password Change results in a 500 status
- The product minus adds items to the cart rather than remove them
- Titles are occasionally hidden behind navbar
- Footer does not remain at bottom of page on all renders
- AllAuth templates have little styling due to heavy use of templating in newest version
- No user feedback after purchase, items remain in basket and have to be manually removed
- My Orders on profile is not updated with order

## Deployment

## Credit
- Code Institute Walkthrough Project Boutique Ado has been relied on heavily throughout the project development with numerous code snippets re-used and re-purposed.
- Images taken from Whip & Drizzle Instagram
- Footer from MDBoostrap.com - https://mdbootstrap.com/snippets/standard/mdbootstrap/2885008?view=side

## License
N/A

## Status
In Development
---