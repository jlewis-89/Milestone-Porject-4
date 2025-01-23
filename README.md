# CrystalsCakes

Crystal's Cakes is a full-stack e-commerce website built using the Django full stack as part of the Milestone 4 Project for Code Institutes Full Stack Developer Course

## Live Project
[View the Live Project here](https://crystals-cakes-4efc6d8bc1c9.herokuapp.com/)

## Repository
[View the repo here.](https://github.com/jlewis-89/Milestone-Porject-4)

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
- - **Frontend**:
  - HTML
  - CSS (Styling)
  - Javascript

- **Backend**:
  - Django (Python web framework)
  - SQLite3 (Database)

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
* Crisp-Form tags not functioning, removed crispy-forms tags in place of standard form formatting.
* Fixtures data not loading, used boutique ado template and populated with own data
* Add to cart - Issues adding items to cart and editing cart contents, product id not passed through correctly
* Favorites functionality - Could not get items to add to favorites list, required item id and not passed through in view
* Images not displaying on carousel after deployment - This was due to the hosting with AWS S3 and the way the setting.py build the url, by pre-pending {{ MEDIA_URL }} it allowed django to build the correct URL and display the images.


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
Prerequisites

A Django project
A Heroku account
An AWS account with S3 access
git and heroku CLI installed
Step 1: Prepare Your Django Project

Install Required Packages

Ensure you have the following packages in your requirements.txt:

django
gunicorn
django-storages
boto3
dj-database-url
psycopg2-binary
Install them using:

pip install -r requirements.txt
Modify settings.py

Update your settings.py to configure static files and database settings:

import dj_database_url
import os

AWS S3 Configuration
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3.S3Boto3Storage'

Static files (CSS, JavaScript, Images)
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

Database Configuration
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}
Collect Static Files

Run the command to collect static files into the static root:

python manage.py collectstatic
Step 2: Set Up AWS S3

Create an S3 Bucket

Go to your AWS Management Console.
Navigate to S3 and create a new bucket.
Set the bucket name (it should be unique) and select the appropriate region.
Set Bucket Policy

Update the bucket policy to allow public access to your static files. Replace your-bucket-name with your actual bucket name.

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::your-bucket-name/*"
        }
    ]
}
Create an IAM User for S3

Go to IAM in your AWS Management Console.
Create a new user with programmatic access.
Attach the existing policy AmazonS3FullAccess or create a custom policy with limited permissions to your bucket.
Save the Access Key ID and Secret Access Key.
Step 3: Set Up Heroku

Create a Heroku App

Create a new Heroku app in your terminal:

heroku create your-app-name
Set Environment Variables

Set the environment variables in Heroku using the following commands:

heroku config:set AWS_ACCESS_KEY_ID='your-access-key-id'
heroku config:set AWS_SECRET_ACCESS_KEY='your-secret-access-key'
heroku config:set AWS_STORAGE_BUCKET_NAME='your-bucket-name'
heroku config:set DATABASE_URL='your-database-url'
Deploy Your Project

Commit your changes and push the code to Heroku:

git add .
git commit -m "Deploying Django project to Heroku"
git push heroku master
Run Migrations

After deployment, run the following command to apply migrations:

heroku run python manage.py migrate
Open Your Application

You can now open your app in the browser:

heroku open

## Credit
- Code Institute Walkthrough Project Boutique Ado has been relied on heavily throughout the project development with numerous code snippets re-used and re-purposed.
- Images taken from Whip & Drizzle Instagram
- Footer from MDBoostrap.com - https://mdbootstrap.com/snippets/standard/mdbootstrap/2885008?view=side

## License
N/A

## Status
In Development
---