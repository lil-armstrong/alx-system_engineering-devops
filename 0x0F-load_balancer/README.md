# Tasks

## 0. Double the number of web servers

Requirements:

    Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
        The name of the custom HTTP header must be X-Served-By
        The value of the custom HTTP header must be the hostname of the server Nginx is running on
    Write 0-custom_http_response_header so that it configures a brand new Ubuntu machine to the requirements asked in this task
        Ignore SC2154 for shellcheck
