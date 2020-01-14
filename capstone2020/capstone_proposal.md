# Capstone Proposal
###### by Miché Lozano

### Project Name: Street Biter

## Overview
###### Project Goal: Shows coordinates with details on 'sweet spots' where you can find berry bushes and edible plants/trees around portland.


### Requirements
######  Python, HTML, CSS, JavaScript, and Django.
* Specific and attainable goals: 
    1. Create a website that shows coordinates with details on local berry bushes and edible plants around portland.
    2. Complete 1 feature of project per week: framework, database, map, users, API, Front-end  etc.
    3. Show different types of plants, information about plants, and details entered by users.

**REACH GOAL:** Allows users to update status of plants, including TOXIC plants with different colored symbols on map etc


**What are the major features of your web application:** 
* User login
* User Profile
* Navigation Bar: Home, user profile, user spots: favorites
* Users - Adding Coordinate Points or cross streets?
* Coordinates with details
    * Plant Type: (user entry) or Black berry, cloud berry, Marrion Berry, Hawethorne, Apple, uknown, etc.
    * Edible: y/n 
    * Date Added
    * Photo/ media upload 
* Display coordinate marker on a Leaflet map
* **REACH:** BLOG - Controlled by Admin, Add to favorites, Plant Facts - info resources.

**What problem is it attempting to solve?** 
* provide free food and foraging resources
* Love thy neighbor: those with an abundance can help those in need.
* creates community around a sharing economy
 
**What libraries or frameworks will you use?**
* Bootstrap
* [Leaflet](https://leafletjs.com/) API 
* Plant-APIs (more research necessary) 

## Functionality 
email using django built-in email thingy (maybe unnecessary)

Users Adding Coordinates, then leaflet map displays coordinates (very necessary)


## Data Model
* Using Django's built in user model
* Create 'Sweet Spots' for each user
* Sweet Spot fields include: 
    * Sweet Spot Title
    * Coordinates
    * Details about Sweet Spot
    * Admin Notes (in bold)
    * **REACH:** Last seen: Date, Status: Ready for Harvest, so-so, and barren. Also Toxic or Deadly (markers), Add to Favorites.


## Schedule
###### weekly 
Approximately 1 major feauture each week [4- 5 weeks]:
* Week 1: Templates and User Login, Admin, Navigation Bar
* Week 2: Set up Model - Creating Coordinate and Displaying on User Profile
* Week 3: Creating Coordinates, MAPS, APIs
* Week 4: Adding content, checking Databases and user-accounts
* Week 5: Front-end, Boot strap, sussing out details, testing.
