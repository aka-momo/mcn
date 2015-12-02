# mcn
----


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
