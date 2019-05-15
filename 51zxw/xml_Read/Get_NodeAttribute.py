from xml.dom import minidom
dom = minidom.parse('Class_info.xml')

root = dom._get_documentElement()
logins=root.getElementsByTagName('login')
for i in range(2):
    username=logins[i].getAttribute('username')
    password=logins[i].getAttribute('password')
    print(username)
    print(password)