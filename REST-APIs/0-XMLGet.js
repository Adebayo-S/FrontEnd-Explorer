const req = new XMLHttpRequest();

req.open('GET', '/api/someresource');

req.onload = function() {
    if (req.status == 200) {
        const data = JSON.parse(req.response);
        // process data
    }
}

req.send();
