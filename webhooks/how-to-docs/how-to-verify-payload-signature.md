# How to verify payload signature

Source: https://aps.autodesk.com/en/docs/webhooks/tutorials/how-to-verify-payload-signature/

---

# How to verify payload signature

## [Webhooks Documentation](#webhooks-documentation)

Check our documentation [here](/en/docs/webhooks/v1/overview/basics/) to understand how to create hooks and set up your secure token to sign your callback payload.
This page demonstrates how to verify payload signature using a simple Node JS server receiving callback from the Webhooks service.

## [Verify using Node.js](#verify-using-node-js)

Prerequisites:
* Install [Node JS](https://nodejs.org).

### Create a new server with express-js

Open your favorite command line and run `$ npm init` to initialize a new node project.
Create a file called `app.js` and add the following lines.

```
var express = require('express');

app.listen(3000, function () {
      console.log('Listening on port 3000!');
});

```

Now run you server by executing `$ node app.js`

```
$ node app.js
Listening on port 3000!

```

### Add new endpoint for callback

Create a new endpoint where you will receive webhooks notifications.

```
app.post("/callback", function(req, res){
         res.send();
});

```

### Create webhook for your server

Now you have your server running you must configure the Webhooks service to send notification to your server.

Check [here](/en/docs/webhooks/v1/tutorials/create-a-hook-data-management/) to see how to create new hooks in our Step-by-Step guide.

```
{
  "callbackUrl":"http://localhost:3000/callback",
  "scope":{
    "folder":"urn:adsk.wipprod:fs.folder:co.q2d7wQwVTJSICAdBl-REQw"
  }
}

```

Note: the above hook is using localhost as callback url and it will not be reachable from the Webhooks service.
Check how to use ngrok to open a secure tunnel to localhost [here](/en/docs/webhooks/v1/tutorials/configuring-your-server/).

### Configure server to verify signature

This example uses the Crypto library bundled with Node to calculate HMAC-SHA1 signature.

```
var bodyParser = require('body-parser');
var app = express();
var WEBHOOKS_SECRET = "<YOUR_TOKEN_HERE>";

function verifySignature(req, res, buf, encoding) {
      const signature = req.header('x-adsk-signature');
  if(!signature) { return; }

  // use utf-8 encoding by default
  const body    = buf.toString(encoding);
  const hmac    = crypto.createHmac('sha1', WEBHOOKS_SECRET);
  const calcSignature = 'sha1hash=' + hmac.update(body).digest('hex');
  req.signature_match = (calcSignature === signature);
}

app.use(bodyParser.json({
  inflate: true,
  limit: '1024kb',
  type: 'application/json',
  verify: verifySignature
}));

app.post("/callback", function(req, res){
      if(!req.signature_match) {
          return res.status(403).send('not called from webhooks service');
      }

      res.status(204).send();
});

```

Show More

### Download full example

```
var express = require('express');
var bodyParser = require('body-parser');
var crypto = require('crypto');
var app = express();
var WEBHOOKS_SECRET = "<YOUR_TOKEN_HERE>";

function verifySignature(req, res, buf, encoding) {
  const signature = req.header('x-adsk-signature');
  if(!signature) { return; }

  // use utf-8 encoding by default
  const body    = buf.toString(encoding);
  const hmac    = crypto.createHmac('sha1', WEBHOOKS_SECRET);
  const calcSignature = 'sha1hash=' + hmac.update(body).digest('hex');
  req.signature_match = (calcSignature === signature);
}

app.use(bodyParser.json({
  inflate: true,
  limit: '1024kb',
  type: 'application/json',
  verify: verifySignature
}));

app.post("/callback", function(req, res){
  if(!req.signature_match) {
    return res.status(403).send('not called from webhooks service');
  }

  res.status(204).send();

  // do whatever work needs to be done with the webhooks payload
  const body = req.body;
  console.log(body);
});

app.listen(3000, function () {
  console.log('Listening on port 3000!');
});

```

Show More
