# box-tools

## Environment

- Python 3.6.8
- CentOS Linux release 7.6.1810 (Core)

## How to use

1. Run server.
    ```sh
    python3 src/server.py
    ```
1. Run localtunnel
    ```sh
    npx localtunnel --port 80
    ```
1. Raise a box custom skill event.
    - https://app.box.com/developers/console

## References

- https://developer.box.com/reference/get-files-id-content/
- https://developer.box.com/guides/webhooks/handle/verify-signatures/#verify-with-sdk
