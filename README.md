Automating BGP Status Check via REST API (MikroTik RouterOS v7+)
Task

Configure a Border Gateway Protocol (BGP) neighbor via the UI, use the APIs to verify the configuration, and automate the same to check whether the BGP neighborship is up or not.
About

This task involves simulating two MikroTik routers, configuring BGP neighbors between them using the WebFig UI, verifying the configuration using REST API endpoints, and automating BGP session status checks using Python.

The solution uses RESTful API calls to interact with MikroTik RouterOS v7+ instances and confirm whether BGP neighborship is established. A Python script was developed to query and display real-time BGP session data (name, remote ID, uptime, and session state).
Steps Taken
1. Oracle VirtualBox Installation

    Oracle VirtualBox was downloaded and installed to simulate a virtualized network environment.

2. MikroTik RouterOS Setup

    MikroTik RouterOS v7+ was downloaded and installed on two VirtualBox VMs.

    Two virtual routers (referred to as R0 and R1) were configured with similar specifications.

3. BGP Configuration using WebFig UI

BGP was configured manually using MikroTik’s WebFig interface. The UI was accessed after identifying each router's local IP address from the VirtualBox terminal.

Configuration steps:

a. Set identity (hostname) of each router
b. Create a bridge interface (used for LAN configuration)
c. Assign static IP addresses to each router
d. Configure unique Router IDs
e. Set up BGP instance and peer configuration
f. Declare LAN subnets under BGP Networks
g. Define output filters to restrict advertised prefixes to LAN only
4. Postman API Testing

    REST API endpoints were tested for both routers using Postman.

    Four GET requests were prepared:

        /rest/routing/bgp/connection (R0)

        /rest/routing/bgp/session (R0)

        /rest/routing/bgp/connection (R1)

        /rest/routing/bgp/session (R1)

    Responses confirmed successful BGP session establishment.

    Screenshots and a screen recording of the WebFig and Postman tests were taken.

5. Python Script for Session Status Verification

A Python script was written to:

    Read router IPs, a shared username, and respective passwords from a .env file

    Query each router’s BGP session API (/rest/routing/bgp/session)

    Display for each session:

        name

        remote.id

        uptime

        state (e.g., established, idle)

Libraries Used

    requests – For sending HTTP requests

    requests.auth – To perform HTTP Basic Authentication

    python-dotenv (dotenv) – To securely load environment variables from a .env file

    os – To access environment variables in the script