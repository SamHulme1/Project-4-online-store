# Tavern
To see the live version of the site click [here!](https://tavern-app-project.herokuapp.com/)

![mockup-image](/static/readme-images/mock-up-image.jpg)

---
## Contents

### [UX](#ux-1)
### [User Requirements and Expectations](#user-requirements-and-expectations-1) 
### [Developer goals](#developer-goals-1) 
### [User Stories](#user-stories-1)
### [Design Choices](#design-choices-1) 
### [Wireframes](#wireframes-1)
### [Features](#features-1)
### [Database](#database)
### [Technologies Used](#technologies-used-1)
### [Depolyment](#deployment) 
### [Testing](#testing-1) 
### [Bugs](#bugs-1)
### [Credits](#credits-1)
---
## UX:

### Project goals: 

- To create a website where users can create, read, update and delete data 
- To create a full stack eCommerce application
- To build a better understanding of Django

---
### Target Audience: 

- The website targets people who enjoy drinks
- The theme of the website is based on the fantasy genre, it took inspiration from one of my previous projects when developing this site. Thus the site also targets people who enjoy the fantasy genre.

---
### Target Audience goals: 

- To be able to navigate around the site
- To be able to create, read, update and delete data
- To be able to make a purchases on the site
---
## User Requirements and Expectations

The website features visual and written content with clear methods for the user to create, read, update and delete information. The user is given feedback from the site whenever they create, and update information on their profile, when a staff member created deletes or updates information, they are also given clear feedback as to what they have created, updated or deleted. 

---
## Developer goals: 

- To create a website that has both front end and backend functionality 
- To build my knowledge of Django and how it can be used to create a full-stack website

---
## User Stories: 

### First-Time Users customers:

- As a first-time user on the site, I need to be able to register my profile
- I need to be able to view the contents of the catalogue and find which product to purchase, 
for this site the products and the pricing are separate so I need to be able to navigate between the two stages for adding a product: browsing the catalogue, looking at products in different categories that interest me. Then navigate to the boxes section and choose the appropriate box for the 
products that interest me. It is up to the site owner to create the products and the categories for these products
- I need to be able to see my orders
- I need to be able to favourite and store products that I like 

### Returning users customer:
- As a returning user I need to be able to log back into the site using my information
- I need to be able to make new purchases 
- I need to be able to view my past orders
- view my stored favourite products

### First-Time Users Admin:
- As a first-time admin, I need to be able to log into the site
- I need to be able to create new products for the store 

### Returning users Admin:
As a returning admin, I need to be able to:
- add new products to the store catalogue
- create new pricing information
- delete products and pricings 
- update products and information 

## Design Choices 

---
[colour-palete](/static/readme-images/colour-palette.jpg)
### Colors:
I used the following colour palette of browns, blacks and whites across the site, I got this colour 
palette from one of the images I generated. I used a brown palette because it is a colour associated with
an old wooden tavern.

---
### Fonts
The font I used across the site was a google font called Aboreto, because I thought that it looked 
rustic which fitted the theme.
---
### Imagery

The current product and pricing images on the site were created using the AI art generation tool NightCafe and helped to build the fantasy theme. The background image came from pexels, I used Django's easy thumbnails to create links to the images so that they can be clicked on and opened to be viewed at full scale. This also helps to create consistency across the site.

---
### Styling 

The site is designed to be responsive across all screen sizes, different pages are stored behind appropriate buttons and links which have been named appropriately. I used page breakers to help divide the information into different pages. I made sure that any written information on the site was informative to help guide the users through the site. informative written information is also accompanied by appropriate and related images that are stored on the database

---
## WireFrames: 
![home-page](/static/readme-images/index-page.jpg)
![basket-page](/static/readme-images/basket-page-wireframe.jpg)
![checkout-page](/static/readme-images/checkout-page.jpg)
![favourite-page](/static/readme-images/favourites-page-lighthouse.jpg)
![myaccount-page](/static/readme-images/my-account-wireframe.jpg)
![order-history-page](/static/readme-images/orders-page-wireframe.jpg)
![pricing-and-product-details-pages](/static/readme-images/product-and-pricing-details-pages.jpg)
![product-and-pricing-forms](/static/readme-images/product-and-pricing-form.jpg)
![all-products-and-pricing-pages](/static/readme-images/products-and-pricing-pages.jpg)
![update-and-create-info-form](/static/readme-images/update_info_form.jpg)


---
## Features: 

### Current Features:

![navbar](/static/readme-images/navbar.jpg)
### Navbar
The navbar contains links to all the different pages, it features the logo, search bar, basket and notification area. 
- The logo features as a way for the user to return to the home page. 
- On the search bar, the users can search the site for information about either the products or the pricing boxes. 
- The basket allows the users to navigate to the basket page.
- The notification bell notifies the user when they have a notification from the site, such as when something goes wrong or is successful
- The notification message appears below the navbar

![forms](/static/readme-images/forms.jpg)
### Forms
- Forms on the site allow ordinary users to accomplish tasks such as creating a profile, making purchases, changing profile information and modifying their basket contents. 
- For admin users, forms allow users to add products and pricings, modify information on products and pricing, and delete them. 

![second-nav](/static/readme-images/second-nav.jpg)
### Secondary navigation bar
- The second navigation bar gives users another way of navigating the products in the catalogue, whenever an admin creates a new pricing, they can update the products to have the category of that pricing or add new products with that category and then a new link is created on the secondary navbar. 


![second-nav](/static/readme-images/store-pricing-products-catalog-pages.jpg)
### Store and pricing catalogues
- When a user searches the store or clicks on a link in the navigation bar they will be brought to either the pricing page or the products page, depending on what they click on or search for. on these pages, the user can view products or pricing that are currently in the store. They can click the view button to see relevant information on either the product or pricing. 


![detail-pages](/static/readme-images/details-pages.jpg)
![detail-pages](/static/readme-images/detais-pages-pricing.jpg)
### Details pages
- After the user clicks the view button on either the products or the pricing boxes, they can see the details of that product or pricing, the product details include a link to all the pricings and the pricings include the feature to add to the user's basket. The pricing details page also includes product names what products are included in the box and how much the box is. Whereas the product detail tells the user which boxes the products are included in. On the product details page, the user can favourite products. 
- For the admin users, on these pages, they can delete products or pricings from the store. 


![basket-page](/static/readme-images/basket.png)
### Basket Page
- The basket page allows the user to see what is currently in their cart, they can manipulate the data by clicking on either the increase or decrease buttons, which updates the total for their order, they can then click the checkout button to enter the checkout page

![checkout-page](/static/readme-images/checkout.jpg)
### Checkout page
- From the checkout page the users can create orders based on the contents of their basket, the page features a card method in which the user can enter their card details upon successfully entering the order confirmation page. But upon failure be redirected back to the basket page with a message displayed to them as to what went wrong with their purchase. whenever a user creates a new order, they are attached to their profile, however, in the instance that the user has not already created a profile, the site creates a profile for the user and attaches the order to it so that they can view the successful orders that they have made at a later date. The information for their profile is generated from the information that they provide in the form. 


![order-pages](/static/readme-images/orders.png)
### Orders page
- The orders page contains links to all the orders the user has made , providing them with the order number, how much the total was an on which date they made the order. 

![order-page-success](/static/readme-images/orders-s.jpg)
### Orders Success/Confirmation pages
- From the orders page the user can view their order details, In essence whenever a user creates an order they can return to the page created and view that order. This page contains more details on that order

![saved-products](/static/readme-images/saved-products.jpg)
### Saved products page
- This page stores all the products that the user has saved, it uses the same layout as the product catalogue page but only shows results to the user if they have favourited the product. On this page, the users can click on the products to view the product details for that product. From there they can do the same actions as on the product details page(the same page), and if they wanted to remove the product from their favourites.


![profile-page](/static/readme-images/profile.jpg)
### My profile page
- On this page, the user can manage their profile, for the ordinary user can edit or add their profile, view their orders and saved products and perform actions such as changing their emails and passwords by clicking on the appropriate buttons. 
- For the admin users, they can create new products and pricing by clicking the links to the appropriate pages, they can also edit them from this page. 

![footer](/static/readme-images/footer.jpg)
### Footer
-The footer sits at the bottom of each page, it contains external links for the user


![hero-image](/static/readme-images/hero.png)
### Hero image and home page
- On the home page the site has a hero image, on larger screens the hero contains a search bar, however on smaller screens the search bar is hidden. 


### Naming Conventions and Structure of Files 

- All the files on the site have been named with consistency and structured into their appropriate sections
- Names contain lowercase and no special characters
- Javascript variables follow the format of camelcase
- Python variables follow the format of CamelCase for classes and use underscore and lowercase to define methods and variables. All Python is indented correctly
- Separate Javascript files have been created for the different web pages, however, javascript that is used across the site has been added to the main.js file
- static files have been added to the static folder on the main project
- images uploaded by the admin are stored in the media file to prevent users from uploading static files such as javascript files to the main static folder and breaking the site
- HTML templates for Python routes are included in templates folders for each app
- Site includes a procfile for heroku deployment
- dependencies are stored in requirement.txt

---

## Database
The database was built using SQLite, The different tables on the database are as follows:
- Accounts: 
    - Allauth accounts so that the users can create and store accounts
    - Allauth also includes an Authentication and Authorisation table to store authenticated users and display which users are authenticated, this table also stores the users in the database
- Catalogue: 
    - The catalogue section store information on the products and pricing on the site, although the pricings and products table has no relation initially, A relationship is created from products to pricing via the use of forms on the create new product form. As the options for the category when creating the product come from the pricing title, if new pricing is created products can be updated and added to that category. This also means that when a product is deleted, the relevant link to that product category is deleted from the secondary navigation, and the products are related to the prices through the foreign key category. However, to create a relationship with the main navigation, I added a charfeild called catagory_name. This is set to a stringified version of the pricing title when the admin creates a product. this input is hidden on the form so that the user cannot create uncategorized products.
    - The product also has a many-to-many relationship with the user accounts so that users can favourite products. 
- Checkout:
    - The checkout models store information on the customers' orders and have a foreign key of user_info, this is so that orders can be attached to users' profiles. So that they can see which orders they have created on the site, the model Order also stores information about the user to create the order summary and stuff information such as the user's address, name and phone number. It also has integer fields to create the price total for the order, which items they had in their basket on checkout and stores their stipe payment intent number for reference to Stripe products on the Stripe site. The model also has a generator for generating a random number using uuid for the customer's order number and a save method for updating the total of the order based on the inline line items.
- The second checkout model store information on the items that the user has in their basket on checkout, it takes the foreign keys of orders and pricings to create a relationship between the two tables to get the total for each item and appear in line with the order model.
- User Profiles:
    - The user info table stores information on the user, the user has the option of creating a profile before checkout using my profile page. When they check out a profile is automatically generated using the credentials provided and stored in the user info model.
## Technologies used: 

### Languages: 

1. [HTML5](https://www.w3schools.com/html/default.asp) To create the structure and the content of the website
2. [CSS3](https://www.w3schools.com/css/) To create the style for the website and its content
3. [Javascript](https://www.w3schools.com/js/) creates the functionality for the website
4. [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) creates the backend for the website

---
### Tools and libraries:

1. [Gitpod](https://www.gitpod.io/) To create and code the site functionality
2. [Heroku](https://dashboard.heroku.com/) To host, deploy and store the site
6. [Google Fonts](https://fonts.google.com/about) To import fonts to the site
7. [Grammarly](https://app.grammarly.com/) To correct spelling, punctuation and grammar
8. [Font Awesome](https://fontawesome.com/) To create the icons used on the site
9. [Adobe Colourwheel](https://color.adobe.com/create/color-wheel) To create the colour scheme for the website
10. [Jigsaw](https://jigsaw.w3.org/css-validator/validator) To validate CSS
11. [nu Html Checker](https://validator.w3.org/) To validate HTML 
13. [Jshint](https://jshint.com/) To validate Javascript 
14. [NightCafe](https://nightcafe.studio/) To create the images used on the site
15. [Django](https://www.mongodb.com/) To create the apps and project
16. [Bootstrap](https://materializecss.com/) To create site responsiveness and styling
17. [Balsamiq](https://en.wikipedia.org/wiki/Balsamiq) To create wireframes
18. [ExtendsClass](https://extendsclass.com/python-tester.html) To validate Python
19. [django-allauth](https://django-allauth.readthedocs.io/en/latest/) 
    To allow the user to create and manage accounts 
20. [django-countries](https://pypi.org/project/django-countries/) for the country fields on the forms 
21. [easy-thumbnails](https://easy-thumbnails.readthedocs.io/en/latest/usage/)
     To render the images at set dimensions 
22. [Pillow](https://pillow.readthedocs.io/en/stable/) To allow the admins to upload images to the site
23. [strip](https://stripe.com/en-gb) To create and handle test payments on the site
24. [pexels](https://www.pexels.com/) For the background image
25. [cloudinaty](https://cloudinary.com/)To host and store the static files used on the website as I was unable to create buckets on AWS
---
## Deployment


### This site was developed using Git. Here is the development lifecycle:

1. I created a new repository by using Code Institutes template
2. In the terminal, I typed git init to initialise
3. I created all the files and folders for the project
4. For each change that I made I used the git add . and commit commands
5. I used git push to push the changes in Git to Github

### The site was then deployed using heroku to make a copy of the site:
1. head over to Github, you'll need an account to make a clone/fork of the project
2. Clone or fork the project by going to the project's repository on GitHub
3. Click on the code dropdown and select GitHub CLI local, copy the URL
4. In gitpod open the git bash command line 
5. Change the current directory to a location where you want to clone to
6. Enter the Command git clone and paste your URL then press enter
7. Install Django on the site by running the command pip3 install django==3.2
8. install dependencies using the relevant command for each one for example pip3 install stripe
9. After installation any dependencies be sure to freeze the requirements by using pip 3 freeze > requirments.txt
10. create a new Django super user on the site. 
11. run the command python3 manage.py run server to open a local server for the site
11. To use the payment section you will need to have created a Stipe account 
12. After doing so set the environment secret keys and public keys. to set up the webhook you will need to create a new webhook on Stripe, then set the URL on stripe to the URL of the project, be sure to include the /what the end of the link. set the stripe webhook key in the environment. 
##### important additions
13. Don't forget to create your db on Elephant to create and link a database
14. If you wanted to have your static files you would also need a Cloudinary account set up 


To connect your newly cloned site to Heroku you need to first
1. create a new database to host your project on Elephantsql
2. create a new app on Heroku
2. sign in to Heroku using the command heroku sign in 
3. add a remote to the app in the command line by following the steps defined by heroku, 
5. Use git add, commit and push to send your created files across to GitHub, then use
heroku push master to push the files to heroku
6. In the created app go to settings and click on reveal config vars
6. Set the vars that are stored in the environment on the settings file in gitpod
8. Back on Heroku click on deploy, automatic deploy and select your branch. Enable automatic deploys
9. If you see the message app deployed successfully well done! You have deployed your site.


## Testing 

### Testing User's Stories 

#### First Time User customer
- As a new user I can successfully create an account on the site by registering my email and creating a password, I can search the store for products, see products that I like and add them to my favourites, I can 
find the appropriate pricing boxes for those categories of products and add them to my basket, I can change the number of items in my basket and create and order and pay for my order. I can see my order history on my orders page and if I want to print take a physical receipt of the order by printing it.

### Returning users customer:
When I return to the site I can log back into my account, view my previous orders,
make orders and view the products I have favourited if they remain on the database

### First-Time Users Admin:
As a first-time admin, I can log into the site using the account created for me
from there, I can view update and delete products and pricing in the store, 
creating new pricing boxes for products and creating new products that I 
want in those boxes

### Returning users Admin:
As a returning admin, I can view the information that I had previously created, 
and add new products and prices, if I want to I can also make purchases from the site

---
### Developer goals have been met by

- I have created a website that has both front-end and backend functionality
- I have been able to build upon my knowledge of Django and Python 
---
### Site responsiveness and compatibility

The site has been tested for responsiveness on the following devices using Google Developer tools:
- Blackberry Z30
- Blackberry PlayBook
- Galaxy Note 3
- Galaxy Note 2
- Galaxy S3 
- Galaxy S8
- Galaxy S9 Plus
- Galaxy Tab S4 
- Galaxy S20 Ultra
- Galaxy Fold
- Galaxy A51
- Kindle Fire HDX
- LG Optimus L70
- Microsoft Lumia 550
- Microsoft Lumia 950
- Moto G4 
- Nexus 10, 4, 5, 5X, 6, 6P, 7, 
- Nokia Lumia 520
- Nokia N9
- Pixel 3, 4, 3 XL, 5
- Ipad mini, Ipad, Ipad Pro
- iPhone 4, SE, XR, 12 Pro
- JioPhone 2
- Ipad air, mini
- Surface Pro 7, Duo
- Nest Hub, Hub Max
- iPhone 5, SE, 6, 7, 8, X
- larger screen sizes such as 4k have also been tested
I used Bootstrap to build the basis for my site responsiveness, I have added media queries to achieve the desired responsiveness on the site and to hide elements that I only wanted to appear on larger sizes.

---
<details>
*Note some of the best practices scores appear in the amber on some of the pages
due to the amount of 3rd party influences on the site such as Stripe, Jquery etc
<summary> Lighthouse</summary>

![forms](/static/readme-images/forms-lighthouse.jpg)
![favourites-page](/static/readme-images/favourites-page-lighthouse.jpg)
![home-page](/static/readme-images/home-page-lighthouse.png)
![pricing-details](/static/readme-images/pricing-details-page-lighthouse.jpg)
![product-details](/static/readme-images/product-details-page-lighthouse.jpg)
![products](/static/readme-images/products-page-lighthouse.png)
![search-catagories](/static/readme-images/lighthouse-search.jpg)
![profile-page](/static/readme-images/profile-page-lighthouse.jpg)
![basket](/static/readme-images/lighthouse-basket.jpg)
![orders](/static/readme-images/orders-lighthouse.jpg)
![success](/static/readme-images/lighthouse-success.jpg)
![checkout](/static/readme-images/lighthouse-checkout.jpg)
</details>




### Online validators 

The final validator results:

---
### Python Validation

<details>
<summary> Python</summary>

*For those that have errors concerning the messages, I'm pretty sure that's
something to do with the validator I used, I tested a different one and didn't get any
![base-context](/static/readme-images/python-valiadion-base-context.png)
![catalogue-forms](/static/readme-images/python-valiadion-catalogue-forms.png)
![catalogue-models](/static/readme-images/python-valiadion-catalogue-models.png)
![catalogue-admin](/static/readme-images/python-validaion-catalogue-admin.png)
![checkout-apps](/static/readme-images/python-validaion-checkout-apps.png)
![checkout-urls](/static/readme-images/python-validaion-checkout-urls.png)
![home-urls](/static/readme-images/python-validaion-home-urls.png)
![home-views](/static/readme-images/python-validaion-home-views.png)
![css-validation](/static/readme-images/python-validaion-settings.png)
![user-info-form](/static/readme-images/python-validaion-user-profiles-forms.png)
![user-profiles-views](/static/readme-images/python-validaion-user-profiles-views.png)
![user-profiles-admin](/static/readme-images/python-validaion-user_profiles-admin.png)
![app-urls](/static/readme-images/python-validaion-app-urls.png)
![webhooks](/static/readme-images/python-validaion-webhook.png)
![basket-signals](/static/readme-images/python-validaion-basket-signals.png)
![basket-contexts](/static/readme-images/python-validation-basket-context.png)
![basket-urls](/static/readme-images/python-validation-basket-urls.png)
![basket-apps](/static/readme-images/python-validation-basket-apps.png)
![basket-views](/static/readme-images/python-validation-basket-view.png)
![catalogue-urls](/static/readme-images/python-validation-catalogue-urls.png)
![catalogue-views](/static/readme-images/python-validation-catalogue-view.png)
![catalgue-forms](/static/readme-images/python-validation-checkout-forms.png)
![checkout-models](/static/readme-images/python-validation-checkout-models.png)
![checkout-forms](/static/readme-images/python-validation-checkout-forms.png)
![user-profiles-models](/static/readme-images/python-validation-user-profiles-models.png)
![user-profiles-urls](/static/readme-images/python-validation-user-profiles-urls.png)
![checkout-views](/static/readme-images/python-validation-checkout-views.png)

</details>

---
### CSS Validation
![css-validation](/static/readme-images/css-validation.jpg)

### HTML Validation

<details>
<summary> HTML </summary>

![add-product](/static/readme-images/html-validaion-add-product.png)
![basket](/static/readme-images/html-validaion-basket.png)
![edit-profile](/static/readme-images/html-validaion-edit-profile.png)
![orders](/static/readme-images/html-validaion-orders.png)
![success](/static/readme-images/html-validaion-success.png)
![add-pricing](/static/readme-images/html-validation-add-pricing.png)
![catagories](/static/readme-images/html-validation-catagories.png)
![checkout](/static/readme-images/html-validation-checkout.png)
![create-profile](/static/readme-images/html-validation-create-profile.png)
![edit-pricing](/static/readme-images/html-validation-edit-pricing.png)
![edit-products](/static/readme-images/html-validation-edit-product.png)
![base-index](/static/readme-images/html-validation-index-including-base-etc.jpg)
![login](/static/readme-images/html-validation-login.jpg)
![pricing-details](/static/readme-images/html-validation-pricing-details.png)
![pricings](/static/readme-images/html-validation-pricings.png)
![product-details](/static/readme-images/html-validation-product-details.png)
![products](/static/readme-images/html-validation-products.jpg)
![saved](/static/readme-images/html-validation-saved.png)
![search](/static/readme-images/html-validation-search.png)

</details>

---
### Javascript Validation
![stripe-management](/static/readme-images/javascipt-validation-stripe-management.jpg)
![orders](/static/readme-images/javascipt-validation-orders.jpg)
![basket](/static/readme-images/javascipt-validation-basket.jpg)
![forms](/static/readme-images/js-validation-forms.png)
![profile-form](/static/readme-images/js-validation-profile-form.png)
---
### Manual Tests run on site

Below are several manual tests I've run towards the end of the development
1. Do all the nav links work?
- result: all the nav links work
2. Do the footer links open in separate tabs?
- result: all the links open in separate tabs
3. Can I create an account?
- result: I can create an account on the website, and the user appears in the db
4. Can I manipulate information on the site by changing data and or creating new data
- result: I can change, create and update information without errors, and I can view the new information
5. Can I change my password?
- result: I can change my password on the db
6. Can I change my email: 
- result: I can change my email
7. Can I create an order
- result: can create an order on the site by using a Stripe test key
8. Do my actions on the website cause errors in the console 
- results: I found errors that appeared in the code where the parts of the templates weren't being rendered due to the user being unauthenticated but were still targeted. The notification icon was also causing errors due to the button still being clickable but it had no element to remove due to the message area not existing in the DOM yet.
-Action: I put all the javascript that targeted elements behind conditional if statements to which check if the dom element is null
---

### Browser testing 

The site has been tested on Chrome, and safri

---
## Bugs 
1. Javascript decrease and increase buttons only increased the top value
Caused by: I forgot to add the index of the buttons and the elements I wanted to change so it only 
changed the first
fixed by: adding indexes to the buttons
2. navbar item names changed on each page
Caused by: incorrect naming on the main context processor
Fixed by: Changing the names to be unique
3. when migrating to the elephant database I had an error in my category forms code which caused the console
to throw the error: 
Django.db.utils.ProgrammingError: relation "catalogue_pricing" does not exist
LINE 1: ...ricing"."title", "catalogue_pricing"."title" FROM "catalogue...
fixed by: I had to contact student support for this one and they helped to find the route of the issue
4. Deployment error when deploying the site, the error said that there was no defined buildpack
fixed by: changing the heroku-22 to heroku-20 and adding a runtime file
5. Sometimes the emails from Django don't send correctly sending an error 505 response, I haven't been able to fix this however, I have left email verifications disabled in the settings so you can still create an account and sign in.
6. I noticed that on a regular account when you checkout sometimes the instances don't fill out. 

---

## Credits 


---
### Content 

- All written content for the site came from me the developer

---
### Media

- The images for the site were created using an online AI image generator [NightCafe](https://nightcafe.studio/)
- The favicon was created using [Favicon Io](https://favicon.io/favicon-converter/)
- The background image came from [Pexels](https://www.pexels.com/)
### Acknowledgements

- Other students on Slack for their support 
- Code Institute for the helpful materials and support, I used the tutorial on the checkout page and basket to help me build functionality for these apps as my project was similar to the Boutique Ado project on the course content
- I used these tutorials to help me to build the favourites section and categories section:
    [tutorial-link-1](https://www.youtube.com/watch?v=PTsljbR-Cmo)
    [tutorial-link-2](https://www.youtube.com/watch?v=1XiJvIuvqhs&t=653s)
- W3C for their library of information when I needed a quick refresher on the content I'd learnt about during the course
- W3C for content that I had previously not learnt about, mainly a more detailed review of the iexact queries used for the search functionality [W3C](https://www.w3schools.com/django/ref_lookups_iexact.php)