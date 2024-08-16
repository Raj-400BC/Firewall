import random
# importing random to generate random IPs
def generate_random_ip():
    return f"192.168.1.{random.randint(1, 40)}"

def checking_firewall_rule(ip, rules):
    for rule_ip, action in rules.items():  # Corrected 'item' to 'items'
        if ip == rule_ip:
            return action
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

 for _ in range(12):
  ip_address = generate_random_ip()
  action = checking_firewall_rule(ip_address, firewall_rules)
  random_number = random.randint(0, 9999)
  print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")

if __name__ == "__main__":
  main()

