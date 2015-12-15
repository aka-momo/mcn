# mcn


* Useful Links
  - [Mininet Setups](http://sdnhub.org/resources/useful-mininet-setups/)

* Task 1 : Learning Switch
  - Mininet initialization

    ```
      sudo mn --topo=single,3 --mac --controller=remote --switch=ovsk
    ```
  - Run Command

    ```
      ./pox.py mcn.l2_learning
    ```
  - Run In Debug Mode

    ```
      ./pox.py log.level --DEBUG mcn.l2_learning
    ```
----
* Task 2 : Firewall / Network virtualization
  - Mininet initialization

    ```
      sudo mn --topo linear,3,3 --mac --switch ovsk --controller remote      
    ```
  - Run Command
    - Firewall / blocked and permitted connections:
      - BLOCKED_IPS : list of ips that cannot send to any other host but can recieve.
      - PERMITTED_IPS: list of pair of ips (src, dst) that the src ip can only communicate with the specified dst ip. Communications with any other hosts in the network will be blocked.
      
      ```
        ./pox.py mcn.firewall
      ```

    - Network virtualization:
      - A host x can ping host y iff they are connected to the same switch.
      ```
        ./pox.py mcn.net_virtualization

        - you can specify number of switches and number of hosts per each switch
        - default: 3 switches and 3 hosts per each switch

        ./pox.py mcn.net_virtualization --nSwitches=3 --hostsPerSwitch=3
      ```
  - Run In Debug Mode

    ```
      ./pox.py log.level --DEBUG mcn.firewall
    ```
----
* Task 3 : Server load balancing
  - Mininet initialization

    ```
      sudo mn --arp --topo single,4 --mac --switch ovsk --controller ovsc
      mininet> h1 arp -s 10.0.0.5 00:00:00:00:00:05
      mininet> h2 python -m CGIHTTPServer &
      mininet> h3 python -m CGIHTTPServer &
      mininet> h4 python -m CGIHTTPServer &
    ```
  - Run Command

    ```
       ./pox.py mcn.trial
    ```
  - Run In Debug Mode

    ```
       ./pox.py log.level --DEBUG mcn.trial

    ```
----
* Task 4 : Path load balancing
  - Mininet initialization

    ```
      sudo mn --custom=pox/mcn/task4topo.py --topo=mytopo --controller=remote
    ```
  - Run Command

    ```
      ./pox.py mcn.task_4 openflow.discovery
    ```
  - Run In Debug Mode

    ```
      
    ```
----
* Task 5 : Path load balancing (bonus)
  - Mininet initialization

    ```
      
    ```
  - Run Command

    ```
      
    ```
  - Run In Debug Mode

    ```
      
    ```
