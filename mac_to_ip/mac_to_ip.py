import subprocess
import socket
import os


def mac_to_ip(device_mac_addresses, ip_address_range=None):
    """
    Find all ip addresses using provided mac addresses

    Returns a dict with a key value dict where key
        is a device identifier and value is a IP address

    :param device_mac_addresses: A key value dict where key
        is a device identifier and value is a MAC address

    :param ip_address_range: A valid nmap ip address range.
    """

    if ip_address_range is None:
        # fmt: off
        ip_address = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]  # noqa: E741 E501
        # fmt: on
        ip_address_range = ".".join(ip_address.split(".")[:-1]) + ".*"

    subprocess.call(['nmap', '-T5', '-sP', ip_address_range],
                    stdout=open(os.devnull, 'w'))

    device_ips = {}
    for device in device_mac_addresses:
        mac_address = device_mac_addresses[device]
        arp_cmd = "arp -a | grep %s | awk '{print $2}'" % mac_address
        ip_address = subprocess.Popen(
            arp_cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
        ip_address = ip_address.decode("utf-8")
        ip_address = ip_address.replace("(", "")
        ip_address = ip_address.replace(")", "")
        ip_address = ip_address.replace("\n", "")
        if ip_address == "":
            ip_address = None
        device_ips[device] = ip_address

    return device_ips
