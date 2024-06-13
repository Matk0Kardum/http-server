from Request import Request


def process_request(request):
    # Split the request information into the list
    request_lines = request.split("\r\n")
    print(f"Client's request: {request_lines}")

    # Get status, headers and the body of the request
    status = request_lines[0]
    headers = request_lines[1:request_lines.index('')]
    body = '\r\n'.join(request_lines[request_lines.index('') + 1:])

    # Return the Request object from information
    return Request(status, headers, body)
