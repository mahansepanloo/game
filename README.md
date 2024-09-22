# Project Bottle  

## Overview  
Project Bottle is a location-based social game that allows users to interact anonymously with individuals nearby based on their current location and score.  

## Features  

- **User Onboarding**: Upon registration, each user receives an initial amount of coins.  
- **Gameplay Actions**:   
  - Create a new bottle  
  - Read a new bottle  

_Note: Each bottle contains a text message._  

## Store  
The game includes a store where users can purchase various items using their coins:  

1. **Bottle Creation**: Users must buy bottles from the store. Each bottle has two components:  
   - **Message Character Length**: The number of characters a user can include in the message.  
   - **Range**: The maximum distance the bottle can travel from the user's location.  
   - Bottles are priced according to these components. For example, a bottle that holds 300 characters and can travel up to 10 kilometers may cost a specific amount.  

2. **Daily Reading Limit**: Users initially can read up to 3 bottles per day. To read more, they must purchase the relevant item from the store.  

3. **Earning Coins**: Users earn coins for each bottle they read.  

4. **Response Feature**: Initially, users cannot respond to bottles. To enable this feature, an item must be purchased from the store.  

## Anonymity  
All actions (reading, creating, and responding to bottles) are anonymous. No user should know who read or responded to their bottle or who the owner of a received bottle is.  

## Bottle Distribution  
When a user creates a new bottle, it is randomly sent to another user within the specified range. For example, if user A creates a bottle with a 10 km range, it will be sent to a randomly selected user within a 10 km radius.  

## Leaderboard  
There is an overall leaderboard that ranks users based on the number of bottles they have read.  

## Conclusion  
Project Bottle offers a unique and engaging way for users to connect and interact anonymously while exploring their surroundings.
# Project Bottle Overview and Instructions  

## Access  
The application can be accessed at the following address:  
**[http://45.139.10.8:8013](http://45.139.10.8:8013)**  

## How It Works  

### User Registration  
1. **Access the Registration Page**:  
   - Go to **[http://45.139.10.8:8013/accounts/sign](http://45.139.10.8:8013/accounts/sign)**.  
   
2. **Enter Credentials**:  
   - Input your **username** and **password**.  

3. **Random Location Assignment**:  
   - After successful registration, you will be randomly assigned to one of 10 predefined islands.  

### Sending Letters  
1. **Prepare Information**:  
   - Gather required inputs: **item_id** (the identifier for the bottle) and **text** (the content of the letter).  

2. **Input Information**:  
   - Enter **item_id** and **text**.  

3. **Validation**:  
   - The system will validate the inputs.  

4. **Sending the Letter**:  
   - If valid, the item will be deleted, and the letter will be sent to a randomly selected user.  

5. **Confirmation**:  
   - You will receive a confirmation message.  

### Receiving Letters  
1. **Access the Receiver Address**:  
   - Send a GET request to **`[http://45.139.10.8:8013/receiver]`**.  

2. **Receive the Letter**:  
   - If letters are available in your range, one reading limit will be deducted, and your score will increase.  

3. **View Sent Letters**:  
   - Check all sent letters at **`[http://45.139.10.8:8013/listsend]`**.  

4. **View Received Letters**:  
   - Access all received letters at **`[http://45.139.10.8:8013/list]`**.  

## Store Items  
In the Project Bottle store, you can purchase specific items:  

1. **Item 4**:   
   - **Description**: Enables answering letters.  
   - **Benefit**: Interactively engage by responding to letters you receive.  

2. **Item 5**:   
   - **Description**: Increases response limit.  
   - **Benefit**: Adds **3 units** to your daily response limit.
  
## Additional Information  
### Testing Area  
The application has been tested in Area 1 along the x and y axes, where each unit corresponds to 1 kilometer. This means that the distribution cycle of bottles is conducted based on geographical positions within this range, with distances measured accurately in kilometers.


## Conclusion  
Project Bottle offers a unique opportunity to connect and interact with users anonymously. Follow the instructions to register, send and receive letters, and enhance your gameplay through store purchases!

