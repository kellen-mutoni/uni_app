# Kellen's Uni Search Application

This is a web application that allows users to search for universities in specific countries and if the user chooses, he/she can filter the results by name. It uses the HipoLabs Universities API to fetch real-time data.

## Features
- Search by Country: Enter a country (e.g., "Rwanda") to see universities in that country.
- Filter Results: Refine your search by typing part of a university name (e.g., "Adventist").
- Live Data: It uses an external API, so the data is always up to date.

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/kellen-mutoni/uni_app.git

  ## Deployment
The application is running on two servers and a Load Balancer.

- Load Balancer: http://3.83.202.235
- Web Server 1: 3.95.132.116
- Web Server 2: 34.238.119.129

### How it Works
1. I deployed the code to both Web Servers using git clone.
2. I used nohup to keep the app running in the background.
3. I configured the Load Balancer using HAProxy to split the traffic between the two servers.

## API Reference
I used the HipoLabs Universities API to get the data.
- Link: http://universities.hipolabs.com/
- Credit: Thank you to the HipoLabs team for the free API.

## Author
Kellen Ashley Mutoni.