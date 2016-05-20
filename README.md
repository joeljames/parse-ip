## Python implementation of parsing and summarizing ip address from nginx access log file

1. Running the python script against a local nginx access file

    ```
    python3 parse_ip.py {path to log file}
    ```

2. Running the python script against a file accessable by http

    ```
    python3 parse_ip.py {url to access the file}
    ```


## Bash implementation of parsing and summarizing ip address from nginx access log file

1. Running the python script against a local nginx access file

    ```
    bin/parse_ip nginx_access.log
    ```
