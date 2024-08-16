import random
from termcolor import colored

def generate_random_ip():
    return f"192.168.1.{random.randint(1, 20)}"

def checking_firewall_rule(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return colored(action, 'red')
    return "allow"

def main():
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.3": "block",
        "192.168.1.4": "block",
        "192.168.1.7": "block",
        "192.168.1.10": "block",
        "192.168.1.22": "block",
        "192.168.1.14": "block",
        "192.168.1.18": "block",
        "192.168.1.21": "block",
        "192.168.1.27": "block",
    }
    
    ip_count = {}
    rate_limit = 2

    for _ in range(12):
        ip_address = generate_random_ip()

        # If the IP is blocked, just continue without counting it
        if ip_address in firewall_rules:
            action = checking_firewall_rule(ip_address, firewall_rules)
            random_number = random.randint(0, 9999)
            print(colored(f"IP: {ip_address}, Action: {action}, Random: {random_number}", 'red'))
            continue
        
        # Track how many times an IP has been generated
        if ip_address in ip_count:
            ip_count[ip_address] += 1
        else:
            ip_count[ip_address] = 1
        
        # Check if the IP exceeds the rate limit
        if ip_count[ip_address] > rate_limit:
            print(colored(f"IP {ip_address} exceeded rate limit!", 'yellow'))
            
            # Remove the IP from ip_count
            del ip_count[ip_address]
            print(colored(f"Removed IP {ip_address} from count.", 'yellow'))
            
            # Generate a new IP and ensure it's not the one just removed
            new_ip = generate_random_ip()
            while new_ip in firewall_rules or new_ip in ip_count or new_ip == ip_address:
                new_ip = generate_random_ip()
            ip_count[new_ip] = 1
            print(colored(f"Added IP {new_ip} to count.", 'yellow'))
            continue

        action = checking_firewall_rule(ip_address, firewall_rules)
        random_number = random.randint(0, 9999)
        print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")

if __name__ == "__main__":
    main()
