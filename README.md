# BusBladi <img width="600" alt="logo big" src="https://github.com/user-attachments/assets/ac5f5833-7a54-4d85-bfcb-c5daf764a977">


BusBladi is a web application developed for a Moroccan transport company, designed to simplify bus ticket purchasing and management. The app allows users to buy tickets, which are generated as dynamic QR code barcodes, and provides an interface for scanning and validating these codes. Additionally, BusBladi offers features for managing user profiles, tracking bus schedules, and ensuring a seamless ticketing experience.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup and Installation](#setup-and-installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Set Up Environment Variables](#set-up-environment-variables)
  - [Build and Run the Docker Containers](#build-and-run-the-docker-containers)
- [Running the Application](#running-the-application)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Pages Overview](#pages-overview)
  - [Signup Page](#signup-page)
  - [Login Page](#login-page)
  - [Home Page](#home-page)
  - [Buy Tickets Page](#buy-tickets-page)
  - [Schedules & Stops Page](#schedules--stops-page)
  - [Profile Page](#profile-page)
  - [Forgot Password Page](#forgot-password-page)
- [Demo Video](#demo-video)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication**: Sign up, login, and manage user profiles, including password reset and forgotten password recovery.
- **Email Verification**: Secure user accounts with email verification during registration.
- **Ticket Purchase**: Buy bus tickets, generated as dynamic QR code barcodes for easy verification.
- **QR Code Scanning**: Validate and delete tickets using a dedicated QR code scanning page.
- **Bus Schedules**: View and filter bus schedules and stops by city and bus route.
- **Responsive Design**: Optimized interface for various devices.
- **Integration with MongoDB Atlas**: Secure and scalable online ticket management system.
- **Dockerized Deployment**: Easily deployable setup using Docker.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Django, Python 3.12
- **Database**: MongoDB Atlas
- **Containerization**: Docker, Docker Compose

## Setup and Installation

### Prerequisites

- Docker and Docker Compose installed on your machine
- MongoDB Atlas account
- Makefile

### Clone the Repository

```bash
git clone https://github.com/belkdioui/BusBladi.git
cd BusBladi
```

### Set Up Environment Variables

Create a `.env` file in the root directory and add your MongoDB credentials:

```plaintext
# MongoDB credentials
MONGO_DB_URI='your-mongo-db-uri'
MONGO_DB_NAME='your-db-name'
MONGO_DB_USERNAME='your-username'
MONGO_DB_PASSWORD='your-password'
```
### Build and Run the Docker Containers

```bash
make
```
This will build the Docker containers and start the application on http://localhost.


## Running the Application

After running the containers, you can access the app at `http://localhost`.

## Environment Variables

The application requires the following environment variables, defined in the `.env` file:

- `MONGO_DB_URI`: URI for your MongoDB Atlas cluster
- `MONGO_DB_NAME`: Name of your MongoDB database
- `MONGO_DB_USERNAME`: Username for MongoDB authentication
- `MONGO_DB_PASSWORD`: Password for MongoDB authentication

## Usage

- **Access the web app**: Navigate to `http://localhost/` in your browser.
- **User actions**:
    - Sign up and log in to your account.
    - Buy bus tickets from the "Buy Tickets" page.
    - View and filter bus schedules and stops from the "Schedules & Stops" page.
    - Use the QR scanning page at `http://localhost/scanner/` to validate tickets.

## Pages Overview

### Signup Page

The **Signup Page** (`/signup/`) allows new users to create an account. Users need to provide their first name, last name, email, phone number, and password. Upon successful registration, a verification email is sent to the user's email address.

### Login Page

The **Login Page** (`/login/`) is where users can log in to their account using their email and password. If the account is not activated, the user will be prompted to check their email for a verification link.

### Home Page

The **Home Page** (`/home/`) displays the user's information, including their balance and the number of tickets they have. If the user has tickets, a QR code is generated for their first ticket.

### Buy Tickets Page

The **Buy Tickets Page** (`/buy-tickets/`) allows users to purchase bus tickets. Users can select the number of tickets and view the total cost before confirming their purchase. The page also updates the user's balance and ticket count after a successful transaction.

### Schedules & Stops Page

The **Schedules & Stops Page** (`/Schedules_Stops/`) provides information about bus routes, including the first and last stops. Users can select a city and bus route to view detailed schedule information.

### Profile Page

The **Profile Page** (`/profile/`) displays the user's profile information, including their phone number, email, first and last name, ticket count, balance, and avatar. Users can view and manage their account details from this page.

### Forgot Password Page

The **Forgot Password Page** (`/forgot-password/`) allows users to reset their password if they have forgotten it. Users need to provide their email address to receive a password reset link. Upon receiving the email, users can follow the instructions to set a new password and regain access to their account.

## Demo Video

Check out our demo video showcasing the BusBladi app in action: [Demo Video Link]

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
