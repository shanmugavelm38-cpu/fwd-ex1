from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<ul>
  <li>Application layer
    <ul>
      <li>HTTP / HTTPS</li>
      <li>FTP / SFTP</li>
      <li>SMTP</li>
      <li>POP3 / IMAP</li>
      <li>DNS</li>
      <li>DHCP</li>
      <li>SSH</li>
      <li>Telnet</li>
      <li>SNMP</li>
      <li>NTP</li>
    </ul>
  </li>
  <li>Transport layer
    <ul>
      <li>TCP</li>
      <li>UDP</li>
      <li>SCTP</li>
    </ul>
  </li>
  <li>Internet layer
    <ul>
      <li>IP (IPv4 / IPv6)</li>
      <li>ICMP</li>
      <li>IGMP</li>
      <li>IPsec</li>
      <li>ARP / Neighbor Discovery</li>
    </ul>
  </li>
  <li>Link layer
    <ul>
      <li>Ethernet</li>
      <li>Wi-Fi (IEEE 802.11)</li>
      <li>PPP</li>
    </ul>
  </li>
</ul>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()