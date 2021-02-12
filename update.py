import socket


domain_path = "domain.txt"
ip_path = "ip.txt"


def get_domain_ip(domain: str):
    addrs = socket.getaddrinfo(domain, '')
    for i in range(len(addrs)):
        if addrs[i][0] == 2:
            yield str(addrs[i][4][0]) + "/32"


def read_domain_file():
    with open(domain_path, 'r') as f:
        content = f.read().splitlines()
        f.close()
    return content


def write_ip_file(ip):
    with open(ip_path, 'a+') as f:
        f.write(ip)
        f.write('\n')
        f.close()
    return True


with open(ip_path, 'w') as f:
    f.close()


if __name__ == "__main__":
    for i in read_domain_file():
        for j in get_domain_ip(i):
            write_ip_file(j)
