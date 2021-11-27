<h1 align="center">Gamers Corner</h1> 
The scope for this project is to create a user centric e-commerce website using Python, Django, Postgres and Heroku.
<br/><br/>
Gamers Corner, An e-commerce website were a user can search for and purchase games for gaming consoles as well as setup a user account to allow them to view their order history and user details.
<br/><br/>

![Responsive displays]

# Table of contents
- [UX](#user-experience)
    - [User stories](#user-stories)
    - [Design](#design)
    - [Surface Plane](#surface-plane)
    - [Wireframes](#wireframes)
- [Technologies Used](#technologies-used)
    - [Languages and Frameworks](#languages-and-frameworks)
- [Database Schema](#database-schema)
- [Database and Schema](#database-and-schema)
    - [Postgres Setup](#Postgres-setup)
- [Deployment](#deployment)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Making a Local Clone](#making-a-local-clone)
    - [Heroku Deployment](#heroku-deployment)
- [Credits](#credits)
- [Content](#content)
- [Acknowledgements](#acknowledgements)

# User Experience
## User stories
 -   ### First Time Customer Goals
       1. As a First Time Customer, I want to be able to view a list of games.
       2. As a First Time Customer, I want to be able to view an induvial games details.
       3. As a First Time Customer, I want to be able to view my total purchases.
       4. As a First Time Customer, I want to be able to view the products I have selected.
       5. As a First Time Customer, I want to be able to setup a user account / registration.
 
 -   ### Returning or Frequent User Goals
       1. As a Returning User, I want to be able to log in.
       2. As a Returning User, I want to be able to log out.
       3. As a Returning User, I want to be able delete my account.
       4. As a Returning User, I want to be able add personal details.
       5. As a Returning User, I want to be able update personal details.
       6. As a Returning User, I want to be able view my order history.
 
 -   ### Frequent Administrator Goals
       1. As a Frequent Administrator, I want to be able to see all customer and user orders.
       2. As a Frequent Administrator, I want to be able to see all users.
       3. As a Frequent Administrator, I want to be able to add products to the site.
       4. As a Frequent Administrator, I want to be able to update product details.
       5. As a Frequent Administrator, I want to be able to delete products from the site.
       6. As a Frequent Administrator, I want to be able to add categories to the site.
       7. As a Frequent Administrator, I want to be able to edit category names.
       8. As a Frequent Administrator, I want to be able to delete categories.
 
 -   ### Sorting and Searching Goals
       1. Sort a list of Products, either alphabetically A-Z or Z-A.
       2. Search for a Product, either by description or by name. 
       3. Sort Products in a category.

 -   ### Purchasing and Checkout Goals
       1. Add a product to the cart.
       2. Update the induvial product quantities.
       3. Remove a product from the cart.
       4. Purchase the products in the cart.
       5. Sent confirmation email of a purchase / order.