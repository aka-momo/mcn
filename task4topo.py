from mininet.topo import Topo

# Virtual View For the Path Balancer Problem Topology
#           s3
#         /    \
#        /      \
# h1 - s1 - s4 - s2 - h2
#        \      /
#         \    /
#           s5
#####################################################

class MyTopo( Topo ):
    

    def __init__( self ):
        print "Path load balancing Topology"

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host1 = self.addHost( 'h1' )
        host2 = self.addHost( 'h2' )
        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )
        topSwitch = self.addSwitch( 's3' )
        middleSwitch = self.addSwitch( 's4' )
        bottomSwitch = self.addSwitch( 's5' )

        # Add links
        self.addLink( host1, switch1 )
        self.addLink( host2, switch2 )
        self.addLink( switch1, topSwitch )
        self.addLink( switch1, middleSwitch )
        self.addLink( switch1, bottomSwitch )
        self.addLink( switch2, topSwitch )
        self.addLink( switch2, middleSwitch )
        self.addLink( switch2, bottomSwitch )


topos = { 'mytopo': ( lambda: MyTopo() ) }
