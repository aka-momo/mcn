from pox.core import core
from pox.lib.addresses import IPAddr,EthAddr,parse_cidr
from pox.lib.revent import EventContinue,EventHalt
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
import sys

#to log the output
log = core.getLogger()

#All the coming values were set automatically using the following commands 

#sudo mn --arp --topo single,4 --mac --switch ovsk --controller remote

#  mininet> h1 arp -s 10.0.0.5 00:00:00:00:00:05
#  mininet> h2 python -m CGIHTTPServer &
#  mininet> h3 python -m CGIHTTPServer &
#  mininet> h4 python -m CGIHTTPServer &



#Host/Client ip and macAddress
virtual_ip = IPAddr("10.0.0.5")
virtual_mac = EthAddr("00:00:00:00:00:05")

#List of servers linked to the switch
server = {}

#Adding Server 1 with its ip, macAddress and port
server[0] = {'ip':IPAddr("10.0.0.2"), 'mac':EthAddr("00:00:00:00:00:02"), 'outport': 2}
#Adding Server 2 with its ip, macAddress and port
server[1] = {'ip':IPAddr("10.0.0.3"), 'mac':EthAddr("00:00:00:00:00:03"), 'outport': 3}
#Adding Server 3 with its ip, macAddress and port
server[2] = {'ip':IPAddr("10.0.0.4"), 'mac':EthAddr("00:00:00:00:00:04"), 'outport': 4}

#Number of available servers to the switch
number_of_servers = len(server)

#variable for looping on servers
index = 0


def handle_sent_packet(event):
	global index
    #only if the packet is well known (ipv4 or igmp) for example
	packet = event.parsed

	msg = of.ofp_flow_mod()
    
    # match headers from an incoming packet
	msg.match = of.ofp_match.from_packet(packet)

    # to make sure destination is the Host
	if (msg.match.nw_dst != virtual_ip):
		return EventContinue


    #Select one of the servers (Switches take turn)
	index = server_index % total_servers
	selected_server_ip = server[index]['ip']
	selected_server_mac = server[index]['mac']
	selected_server_outport = server[index]['outport']

	print("***************")

    #To take the next the second server for the next time
	server_index += 1

    #msg is the request sent from the client to the Host and passed to the switch
	msg.buffer_id = event.ofp.buffer_id
    #port used to send msg 
	msg.in_port = event.port

	msg.actions.append(of.ofp_action_dl_addr(of.OFPAT_SET_DL_DST, selected_server_mac))
	msg.actions.append(of.ofp_action_nw_addr(of.OFPAT_SET_NW_DST, selected_server_ip))
	msg.actions.append(of.ofp_action_output(port = selected_server_outport))
    #send the message to the selected server
	event.connection.send(msg)

    #reverse msg is the response of the server to the client
	reverse_msg = of.ofp_flow_mod()
	reverse_msg.buffer_id = None
<<<<<<< HEAD
	
=======

>>>>>>> d57617616ab7ae1692bc2465f6eb967f2205d0bc
    #port used to send response
	reverse_msg.in_port = selected_server_outport

    # match headers of response packet
	reverse_msg.match = of.ofp_match()

    #the source is the selected server to respond to the client 
	reverse_msg.match.dl_src = selected_server_mac
	reverse_msg.match.nw_src = selected_server_ip
	reverse_msg.match.tp_src = msg.match.tp_dst

    #distination is the client sending the request
	reverse_msg.match.dl_dst = msg.match.dl_src
	reverse_msg.match.nw_dst = msg.match.nw_src
	reverse_msg.match.tp_dst = msg.match.tp_src


	reverse_msg.actions.append(of.ofp_action_dl_addr(of.OFPAT_SET_DL_SRC, virtual_mac))
	reverse_msg.actions.append(of.ofp_action_nw_addr(of.OFPAT_SET_NW_SRC, virtual_ip))
    #set out port to the same port the msg was sent through
	reverse_msg.actions.append(of.ofp_action_output(port = msg.in_port))
    #send response to the 
<<<<<<< HEAD
	msgb = of.ofp_packet_out(data = event.ofp) # send packet out by packetInevent

 	event.connection.send(msgb)
=======
>>>>>>> d57617616ab7ae1692bc2465f6eb967f2205d0bc
	event.connection.send(reverse_msg)
	return	EventHalt

def launch ():
    #add handler to the switch
	core.openflow.addListenerByName("PacketIn", handle_sent_packet)


###################################################################

    
<<<<<<< HEAD
    # Only handle IPv4 flows
=======
>>>>>>> d57617616ab7ae1692bc2465f6eb967f2205d0bc
    # if (not event.parsed.find("ipv4")):
    #     return EventContinue
    #log.debug for debugging 
    # log.debug("Broadcasting %s.%i -> %s.%i" %
    #      (packet.src, event.ofp.in_port, packet.dst, of.OFPP_ALL))
    #print packet 27 
<<<<<<< HEAD

=======
>>>>>>> d57617616ab7ae1692bc2465f6eb967f2205d0bc
