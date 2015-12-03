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
      sudo mn --topo linear,2,3 --mac --switch ovsk --controller remote      
    ```
  - Run Command

    ```
      ./pox.py mcn.firewall
    ```
  - Run In Debug Mode

    ```
      ./pox.py log.level --DEBUG mcn.firewall
    ```
----
* Task 3 : Server load balancing
  - Mininet initialization

    ```
      
    ```
  - Run Command

    ```
      
    ```
  - Run In Debug Mode

    ```
      
    ```
----
* Task 4 : Path load balancing
  - Mininet initialization

    ```
      
    ```
  - Run Command

    ```
      
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
