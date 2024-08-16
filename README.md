# Firewall Project

This repository contains my journey of understanding and building a basic firewall using Python. The goal of these projects is to explore how firewalls work, particularly focusing on IP blocking and rate limiting. As I continue learning, I plan to enhance these projects with more advanced features, such as automated IP reputation checks and improved rate limiting to prevent DDoS attacks.

## Project Structure

- **firewall_v1.py**: 
  - A basic firewall that blocks specific IPs and allows others. 
  - Generates random IP addresses and checks them against predefined firewall rules.
  - Each IP is assigned a random number to simulate different actions.

- **firewall_v2.py**: 
  - Builds on the first version by introducing rate limiting.
  - If an IP address exceeds a predefined rate limit, it's removed from the count and replaced by a new IP.
  - Uses the `termcolor` library to highlight blocked IPs in red and rate-limit messages in yellow.

## Future Enhancements

- **Automated IP Reputation Checks**: 
  - Plan to integrate APIs that automatically check the reputation of IPs and block them based on their reputation across the web.

- **Advanced Rate Limiting**: 
  - Enhance the rate-limiting logic to make it more effective and resilient against DDoS attacks.

- **Dynamic Firewall Rules**: 
  - Remove the static IP block lists and instead, dynamically update them based on real-time data.

## How to Run

1. **Install Dependencies**:
   ```bash
   pip install termcolor
