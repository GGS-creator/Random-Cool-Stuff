# scapy-To send custom packets TCP,UDP and ICMP send(IP(dst=IP_T)/UDP(dport=53)/Raw(load=TestUDP), verbose=0)
send(IP(dst=IP_T)/TCP(dport=22, flags=S), verbose=0); time.sleep(D)
send(IP(dst=IP_T)/TCP(dport=22, flags=0), verbose=0); time.sleep(D)
send(IP(dst=IP_T)/TCP(dport=22, flags=F), verbose=0); time.sleep(D)

# socket- To send messages to a specific ip address. 
s.connect(("ip",port))
s.send(b"hello")
s.close() you can use nc -lvnp port to listen to the sent message

# wave 
This is a built-in Python library used for working with WAV audio files (.wav).

#json
It translates JSON data into Python objects (like dictionaries and lists) using json.loads() or json.load(), and converts Python objects back into JSON text strings using json.dumps() or json.dump().
