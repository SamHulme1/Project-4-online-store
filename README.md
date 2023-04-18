# Tavern
To see the live version of the site click [here!]()

![mockup-image]()

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

- To create a website were users can create, read, upadte and delete data 
- To create a full stack eccomerce application

---
### Target Audience: 

- The website targets people who enjoy drinks
- The theme of the website is based around the fantasy genre, it took inspiration form one of my previous projects when developing this site. Thus the site also targets people who enjoy the fantasy genre.

---
### Target Audience goals: 

- To be able to navigate around the site
- To be able to create, read, update and delete data
- To be able to make a purchaces on the site
---
## User Requirements and Expectations

The website features visual and written content with clear methods for the user to create, read, update and delete information. The user is given feedback from the site whenever they create, and update information on their profile, when a staff member created deletes or upadates information, they are also given clear feedback as to what they have created, updated or deleted. 

---
## Developer goals: 

- To create a website that has both front end and backend functinaloty 
- To build my knowledge of django and how it can be used to create a full stack website

---
## User Stories: 

### First-Time Users customers:

- As a first time user on the site, i need to be able to register my profile
- I need to be able to view the contents of the catalogue and find which product to purchace, 
for this site the products and the pricings are seperate so i need to be able to clearly navigate between the two the stages for adding a product are: browsing the catalogue, looking at products in differnet catagories that interest me. Then navigating to the boxes section and choosing the appropriate box for the 
products that interest me. It is up to the site owner to create the products and the catagories for these products
- I need to be able to see my orders
- I need to be able to favourite and store products that I like 

### Returning users customer:
- As a returning user i need to be able to log back into the site using my information
- I need to be able to make new purchaces 
- I need to be able to view my past orders
- view my stored favourite products

### First-Time Users Admin:
- As a first time admin, i need to be able to log into the site
- I need to be able to create new products for the store 

### Returning users Admin:
As a returning admin, I need to be able to:
- add new products to the store catalogue
- create new pricing information
- delte products and pricings 
- update products and information 

## Design Choices 

---

### Colors:

---
### Fonts

---
### Imagery

The current prouct and pricing images on the site were created using the AI art generation tool NightCafe and help to build the fantasy theme. The backaground image came from pexels, I used djangos easy thumbnails to create links to the images so that they can be clicked on and opened to be viewed at full scale. This also helps to create a consistancy across the site.

---
### Styling 

The site is designed to be responsive accross all screen sizes, different page are store behind appropriate buttons and links which have been named appropriately. I used page breakers to help divide the information on the differnet pages. I made sure that any written infomaion on the site was informative to help guide the users through the site. informative written information is also accompanied by appropriate and related images that are stored on the database


---
## WireFrames: 


---
## Features: 

### Current Features:

### Navbar
The navbar contains links to all the different pages, it features the logo, searchbar, basket and notification area. 
- The logo features as a way for the user to return to the home page. 
- On the searchbar, the users can search the site for information about either the products or the pricing boxes. 
- The basket allows the users to navigate to the basket page.
- The notification bell notifies the user when they have a notification from the site, such as when something goes wrong or is successful


### Forms
-  Forms on the site allow ordinary users to accomplish tasks such as creating a profile, making purchaces, changing profile information and modifying there basket contents. 
- For admin users, forms allow users to add products and pricings, modify information on products and pricings, and delete them. 


### Secondary navigation bar
- The second navigation bar gives users another way of navigating the products in the catalogue, whenever a adin creates a new pricing, they can update the products to have the catagory of that pricing or add new products with that catagory and then a new link is created on secondary navbar. 


### Store and pricing catalogues
- When a user searches the store or clicks on a link in the navigation bar they will be brought to either the pricings page or the products page, dependant on what they click on or search for. on these pages the user can view products or pricings that are currently on the store. They can click the view button to see relavent information on either the product or pricing. 

### Details pages
- After the user clicks the view button on either the products or the pricing boxes, they can see the details of that product or pricing, the product details include a link to all the pricings and the pricings include the feature to add to the users basket. The pricing details page also includes products names of what products are included in the box and how much the box is. Whereas the product detail tell the user which box the products are included in. On the product details page, the user can favourite products. 
- For the admin users, on these pages they can delete products or pricings from the store. 

### Basket Page
- The basket page allows the user to see what is currently in their cart, they can manipulate the data by clicking on either the increase or decrease buttons, which updates the total for their order, they can then click the checkout button to ender the checkout page

### Checkout page
- From the checkout page the users can create orders based uppon the contents of their basket, the page features a card method which the user can enter their card details for an uppon successful enter the order confirmation page. But uppon failure be redirected back to the basket page with a message displayed to them as to what went wrong with their purchace. whenever a user creates a new order, they are attatched to their profile, however, in the instance that the user has not already created a profile, the site creates a profile for the user and attatches the order to it so that they can veiw the successful orders that they have made at a later date. The information for their profile, is generated from the information that they provide in the form. 

### Orders page
- The orders page contains links to all the orders the user has made , providing them with the order number, how much the total was an on which date they made the order. 

### Orders Success/Confirmation pages
- From the orders page the user can view their order details, In essance whenever a user creates an order they can return to the page created and view that order. This page contains more details on that order


### Saved products page
- This page stores all the products that the user has saved, it uses the same layout as the product catalogue page but only shows results to the user if they have favourited the product. On this page the users can click on the products to veiw the product details for that product. From their they can do the same actions as on the product details page(the same page), and if they wanted to remove the product from their favourites.

### My profile page
- On this page the user can manage their profile, for ordinay user they are able to edit or add their profile, view their orders and saved products and perform actions such as changing their emails and passwords by clicking on the appropriate buttons. 
- For the admin users, they are able to created new products and pricing from clicking the links to the approprate pages, they can also edit them from this page. 

### Footer
-The footer sits at the bottom of each page, it contains external links for the user

### Hero image
- On the home page the site has a hero image, on larger screens the hero contains a search bar, however on smaller screens the search bar is hidden. 

### Home page
- The home page contains the hero image and informatin as to what the website is all about

### Naming Conventions and Structure of Files 

- All the files on the site have been named with consistency and structured into their appropriate sections
- Names contain lowercase and no special characters
- Javascript variables follow the format of camelsCase
- Python variables follow the format of CamelCase for classes and use underscore and lowercase to define methods and variables. All python is indented correctly
- Separate Javascript files have been created for the different webpages, however, javascript that is used accross the site has been added to the main.js file
- static files have been added to static folder on the main project
- images uploaded by the admin are stored in the media file to prevent users from uploading static files such as javascript files to the main static folder and breaking the site
- html templates for python routes are included in templates folders for each app
- Site includes a procfile for heroku deployment
- dependentsies are stored in requirement.txt

---

## Database
The database was build using sqlite, The diffent table on the database are as follows:
- Accounts: 
    - Allauth accounts so that the users can create and store accounts
    - Allauth also includes a Authentication and Authroisation table to store authenticated users and display which users are authenticated, this table also store the users in the database
- Catalogue: 
    - The catalogue section store information on the products and pricings on the site, allthough the pricings and products table have no relatinon initally, A relationship is created from products to pricing via the use of forms on the create new product form. As the options for the catagory when creating the product come from the pricing title, if a new pricing is created products can be updated and added to that catagory. This also means that when a product is delted, the relatvent link to that product catagory is deleted from the secondary navigation, the products are related to the pricings through the foren key catagory. However, in order to create a realtionship with the main navigation, I added a charfeild called catagory_name. This is set to a stringified version of the pricing title when the admin creates a product. this input is hidden on the form so that the user cannot create uncatagoried products.
    - The product also has a manytomany relationship with the user accounts so that users can favourite products. 
- Checkout:
    - The checkout models store information on the customers order and have a foren key of user_info, this is so that orders can be attatched to users profiles. So that they can see which orders they have created on the site, the model Order also store information about the user in order to create the order summary and stuff information such as the users address, name and phone number. It also has interger fields to create the price total for the order, which items they had in their basket on checkout and stores their stipe payment intent number for referace to Stripe products on the Stripe site. The model also has a generator for generating a random number using uuid for the customers order number and a save method for updating the total of the order based of the inline lineitems.
- The second checkout model store information on the items that the user has in their basket on checkout, it takes the foren keys of orders and pricings to create a relationship between the two table in order to get the total for each item and appear inline with the order model.
- User Profiles:
    - The user info table stores information on the user, the user has the option of creating a profile before checkout using the my profile page. When they checkout a profile is automatically generated usng the credentials provided and stored in the user info model.
## Technologies used: 

### Languages: 

1. [HTML5](https://www.w3schools.com/html/default.asp) To create the structure and the content of the website
2. [CSS3](https://www.w3schools.com/css/) To create the style for the website and its content
3. [Javascript](https://www.w3schools.com/js/) creates the functionality for the website
4. [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) creates the backend for the website

---
### Tools and libraries:

1. [Gitpod](https://www.gitpod.io/) To create and code the site
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
16. 
17. [Bootstrap](https://materializecss.com/) To create site responsiveness and styling
18. [Balsamiq](https://en.wikipedia.org/wiki/Balsamiq) To create wireframes
19. [ExtendsClass](https://extendsclass.com/python-tester.html) To validate Python
20. [django-allauth] To allow user to create and manage accounts 
21. [django-countries] for the country fields on the forms 
22. [easy-thumbnails] To render the images at set dimentions 
23. [Pillow] To allow the admins to upload images to the site
24. [strip] To create and handle test payments on the site
---
## Deployment


### This site was developed using Git. Here is the development lifecycle:

1. I created a new repository by using Code Institutes template
2. In the terminal, I typed git init to initialise
3. I created all the files and folders for the project
4. For each change that I made I used the git add . and commit commands
5. I used git push to push the changes in Git to Github

### The site was then deployed using heroku to make a copy of the site:
1. head over to github, you'll need an account to make a clone/fork of the project
2. Clone or fork the project by going to the projects repository on GitHub
3. Click on the code dropdown and select GitHub CLI in local, copy the URL
4. In gitpod open the git bash command line 
5. Change the current directory to a location where you want to clone to
6. Enter the Command git clone and paste your URL then press enter
7. Install django on the site by running the command pip3 install django==3.2
8. install depenanies using the relavent command for each one for example pip3 install stripe
9. After install in depenancys be sure to freeze the requirements by using pip 3 freeze > requirments.txt
10. create a new django super user on the site. 
11. run the command python3 manage.py runserver to open a local server for the site
11. In order to use the payment section you will need to have created a Stipe account 
12. After doing so set the enviroment secret keys and public keys. in order to set up the webhook you will need to create a new webhook on Stripe, then setting the url on stirpe to the url of the project, be sure to include the /wh at the end of the link. set the stripe webhook key in the enviroment. 











To connect your newly cloned site to Heroku youll need to first
1. set up an env.py file in the root, make sure to include this file in the gitignore file though
2. Add the following to the env file:
    - os.environ.setdefault("IP", "0.0.0.0")
    - os.environ.setdefault("PORT", "5000")
    - os.environ.setdefault("SECRET_KEY", "A key of your choice")
    - os.environ.setdefault("MONGO_URI", "mongodbURIlink")
    - os.environ.setdefault("MONGO_DBNAME", "your database name")
3. use the command pip freeze requirements.txt to install create file to contains dependencies
4. Create a Procfile by entering the command echo web: python app.py
5. Use git add, commit and push to send your created files across to github
6. On Heroku create a new app then select deploy from GitHub, find your repository and then click connect 
7. In the created app go to settings and click on reveal config vars
8. Set these vars to be equal to the same values you added into your env file
9. Create a new cluster in mongo db with 3 collections: users, ships and citizens
10. Get you mongoDB collection string by clicking on connect your application, this is your MONGO_URI link
11. Back on Heroku click on deploy, automatic deploy and select your branch. Enable automatic deployes
12. If you see the message app deployed sucessfully well done! You have deployed your site.





## Testing 

### Testing User's Stories 

#### First Time User



#### Returning User



---
### Developer goals have been met by

- I have created a website that has both front end and backend functionality
- I have been able to build uppon my knowledge of Django and Python 

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
#### LightHouse 
Lighthouse scores:


### Online validators 

The final validator results:

---
### Python Validation



---
### CSS Validation


### HTML Validation

---
### Javascript Validation

---
### Manual Tests run on site

Below are a number of manual tests I've run towards the end of devlopment
1. Do all the nav links work?
- result: all the nav links work
2. Do the footer links open in seperate tabs?
- result: all the links open in seperate tabs
3. Can I create an account?
- result: I can create an account on the website, the user appears in the db
4. Can I manipulate information on the site by changing data and or creating new data
- result: I can can change, create and update information without errors, i can view the new infomation
5. Can I change my password?
- result: I can change my password on the db
6. Can I change my email: 
- result: I can change my email
7. Can I create an order
- result: can can create an order on the site by using a Stripe test key


---

### Browser testing 

The site has been tested on Chrome, Firefox and Microsoft Edge 

---
## Bugs 


---
### Bugs Left in Code:


---
## Credits 

### Code

---
### Content 

- All written content for the site came from me the developer

---
### Media

- The images for the site were created using an online AI image generator [NightCafe](https://nightcafe.studio/)
- The favicon was created using [Favicon Io](https://favicon.io/favicon-converter/)
- The background image came from [Pexels]()
### Acknowledgements

- Other students on slack for their support 
- Code Institute for the helpful materials and support, I used the turorials on the checkout page and basket to help me build functionality for these apps as my project was simialr to the Boutique Ado project on the course content
- I used these tutorials to help me to build the favourites section and catagories section:
    - 
    - 
- W3C for their library of information when I needed a quick refresher on the content I'd learnt about during the course
- W3C for conent that I had previously not learnt about, mainly for the iexact queries used for the search functionaliy [W3C](https://www.w3schools.com/django/ref_lookups_iexact.php)