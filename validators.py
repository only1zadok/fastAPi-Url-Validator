import socket
import ipaddress


def resolve_ips(host: str) -> set[str]:
    """
    Resolve A and AAAA records for a hostname to a set of IP strings.
    Raises ValueError if hostname cannot be resolved.
    """
    try:
        infos = socket.getaddrinfo(host, None)  # resolves A/AAAA
    except socket.gaierror as e:
        raise ValueError("Hostname could not be resolved.") from e

    ips: set[str] = set()
    for *_, sockaddr in infos:
        ip = sockaddr[0]
        ips.add(ip)
    return ips


def is_private_or_local_ip(ip: str) -> bool:
    ip_obj = ipaddress.ip_address(ip)
    return (
        ip_obj.is_private
        or ip_obj.is_loopback
        or ip_obj.is_link_local
        or ip_obj.is_reserved
        or ip_obj.is_multicast
    )


def reject_local_and_private_hosts(host: str) -> None:
    """
    Raises ValueError if host is localhost, an IP in private/local ranges,
    or resolves to any private/local IP.
    """
    host_lower = host.lower().strip()

    if host_lower in {"localhost", "localhost.localdomain"}:
        raise ValueError("Localhost URLs are not allowed.")

    # If host is an IP literal
    try:
        ip_obj = ipaddress.ip_address(host_lower)
        if is_private_or_local_ip(str(ip_obj)):
            raise ValueError("Private or local IPs are not allowed.")
        return
    except ValueError:
        # Not an IP literal, proceed to DNS resolution
        pass

    ips = resolve_ips(host_lower)
    for ip in ips:
        if is_private_or_local_ip(ip):
            raise ValueError("Hostname resolves to a private or local network address.")
