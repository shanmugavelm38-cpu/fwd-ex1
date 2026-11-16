# EX01 Developing a Simple Webserver
## Date:16-11-2026
## reg no:26008603

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
~~~
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
~~~  

## OUTPUT:

![alt text](<Screenshot 2026-11-14 160738.png>)
!alt text](<Screenshot 2026-11-14 162325.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.

