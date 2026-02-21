# Configuring your Local Server

Source: https://aps.autodesk.com/en/docs/webhooks/tutorials/configuring-your-server/

---

# Configuring your Local Server

This walkthrough shows how to test your hooks against a *localhost* server.

## [Step 1 : Configuring ngrok](#step-1-configuring-ngrok)

For Webhooks service to send notifications to your *localhost* server, you may like to use *ngrok*. You can find more information on *ngrok* at <https://ngrok.com>.

[Download ngrok](https://ngrok.com/download)

After downloading *ngrok*, you can expose your *localhost* by running command:

```
./ngrok http 5678

```

You should see output like:

```
Session Status                online
Version                       2.2.8
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://bf067e05.ngrok.io -> localhost:5678
Forwarding                    https://bf067e05.ngrok.io -> localhost:5678

```

Take note of the `*.ngrok.io` URL. In this case, it is: `http://bf067e05.ngrok.io`

## [Step 2 : Running the localhost server](#step-2-running-the-localhost-server)

Assuming our callback URL for Webhooks is going to be `http://bf067e05.ngrok.io/callback`; we need to configure `POST /callback` endpoint of `localhost:5678`.

Which means, local server *localhost* should listen to `POST` request at `/callback` path.

Here is an example of *localhost* server in `golang`:

```
package main

import (
      "fmt"
      "io/ioutil"
      "log"
      "net/http"
)

const PORT = 5678

func callbackHandler(w http.ResponseWriter, req *http.Request) {
      body, _ := ioutil.ReadAll(req.Body)
      fmt.Printf("Payload \n %s", body)
}

func main() {
      http.HandleFunc("/callback", callbackHandler)
      log.Fatal(http.ListenAndServe(fmt.Sprintf(":%v", PORT), nil))
}

```

Show More

Alternatively, you can learn more about [Sinatra](http://www.sinatrarb.com) and find a [Sinatra application here](https://github.com/github/platform-samples/tree/master/hooks/ruby/configuring-your-server).
Or, you can create *localhost* in any language or tool of your choice.

Then, run your *localhost* server.

At this stage, you should have `http://localhost:5678/callback` as `callbackUrl`.
You can use `http://bf067e05.ngrok.io/callback` in [Step 4](/en/docs/webhooks/v1/tutorials/create-a-hook-data-management) for creating a hook.
