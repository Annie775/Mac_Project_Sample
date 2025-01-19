import random

def generate_random_mac():
    # Generate a random MAC address in the format 00:XX:XX:XX:XX:XX
    mac = [0x00, random.randint(0x00, 0x7f),  # Ensure it's locally administered
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: f"{x:02x}", mac))

# Example usage
random_mac = generate_random_mac()
print("Generated Random MAC Address:", random_mac)


def arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="mac_address", help="New MAC Address")
    parser.add_option("-r", "--random", action="store_true", dest="random_mac", help="Random Mac Address")
    
    (value, args) = parser.parse_args()
    if value.random_mac:
        # Generate a random MAC address
        random_mac = generate_random_mac()
        print(f"[+] Generated Random MAC Address: {random_mac}")
        if not value.interface:
            parser.error("[-] Please specify an interface with -i when using -r.")
        mac_changer(value.interface, random_mac)
        return value.interface
    elif value.interface and value.mac_address:
        mac_changer(value.interface, value.mac_address)
        return value.interface
    else:
        parser.error("[-] Please specify either -i and -m together, or -r with -i.")


    if not value.interface:
        parser.error("[-] Please specify an interface with -i")
    else: 
        if value.random_mac and value.interface:
            random_mac = generate_random_mac()
            print(f"[+] Generated Random MAC Address: {random_mac}")
            mac_changer(value.interface, random_mac)
        
        elif value.interface and value.mac_address:
            mac_changer(value.interface, value.mac_address)

        else:
            parser.error("[-] Please specify either -i and -m together, or -r with -i.")
        
        return value.interface


