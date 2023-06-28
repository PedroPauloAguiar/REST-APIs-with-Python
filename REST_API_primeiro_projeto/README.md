---
title: Project Overview
description: A first look at the project we'll build in this section.
---

# Setting up

Create a virtual environment and activate it.

python3.10 -m venv .venv
source .venv/bin/activate

Install Flask.

pip install flask

Create a file for the Flask app (I like to call it app.py) Create the Flask app.

from flask import Flask

app = Flask(**name**)

Now you can run this app using the Flask Command-Line Interface (CLI):

flask run

# Overview of your first REST API

import VideoEmbed from "@site/src/components/VideoEmbed";

<div style={{ maxWidth: "720px", margin: "3rem auto", boxShadow: "0 5px 15px 0 rgba(0, 0, 0, 0.15)" }}>
<VideoEmbed url="https://customer-zmitazl0ztnd2pvm.cloudflarestream.com/cda9c0473bdc485a36905144f13f4d3f/iframe?poster=https%3A%2F%2Fcustomer-zmitazl0ztnd2pvm.cloudflarestream.com%2Fcda9c0473bdc485a36905144f13f4d3f%2Fthumbnails%2Fthumbnail.jpg%3Ftime%3D%26height%3D600" />
</div>

In this section we'll make a simple REST API that allows us to:

- Create stores, each with a `name` and a list of stocked `items`.
- Create an item within a store, each with a `name` and a `price`.
- Retrieve a list of all stores and their items.
- Given its `name`, retrieve an individual store and all its items.
- Given a store `name`, retrieve only a list of item within it.

This is how the interaction will go!

:::tip Insomnia files
Remember to get the Insomnia files for this section or for all sections [here](/insomnia-files/)!
:::

## Create stores

Request:

```
POST /store {"name": "My Store"}
```

Response:

```
{"name": "My Store", "items": []}
```

## Create items

Request:

```
POST /store/My Store/item {"name": "Chair", "price": 175.50}
```

Response:

```
{"name": "Chair", "price": 175.50}
```

## Retrieve all stores and their items

Request:

```
GET /store
```

Response:

```
{
    "stores": [
        {
            "name": "My Store",
            "items": [
                {
                    "name": "Chair",
                    "price": 175.50
                }
            ]
        }
    ]
}
```

## Get a particular store

Request:

```
GET /store/My Store
```

Response:

```
{
    "name": "My Store",
    "items": [
        {
            "name": "Chair",
            "price": 175.50
        }
    ]
}
```

## Get only items in a store

Request:

```
GET /store/My Store/item
```

Response:

```
[
    {
        "name": "Chair",
        "price": 175.50
    }
]
```

---

title: How to create stores
description: Learn how to add data to our REST API.

---

# How to create stores in our REST API

To create a store, we'll receive JSON from our client (in our case, Insomnia, but it could be another Python app, JavaScript, or any other language or tool).

Our client will send us the name of the store they want to create, and we will add it to the database!

For this, we will use a `POST` method. `POST` is usually used to receive data from clients and either use it, or create resources with it.

In order to access the JSON body of a request, we will need to import `request` from `flask`. Your import list should now look like this:

```py
from flask import Flask, request
```

Then, create your endpoint:

```py title="app.py"
# highlight-start
from flask import Flask, request
# highlight-end

app = Flask(__name__)

stores = [{"name": "My Store", "items": [{"name": "my item", "price": 15.99}]}]


@app.get("/store")
def get_stores():
    return {"stores": stores}


# highlight-start
@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201
# highlight-end
```

Here we use `request.get_json()` to retrieve the JSON content of our request.

Then we create a new dictionary that represents our store. It has a `name` and `items` (which is an empty list).

Then we append this store to our `stores` list.

Finally we return the newly created `store`. It's empty, but it serves as a **success message**, to tell our client that we have successfully created what they wanted us to create.

:::tip Returning a status code
Every response has a status code, which tells the client if the server was successful or not. You already know at least one status code: 404. This means "Not found".

The most common status code is `200`, which means "OK". That's what Flask returns by default, such as in the `get_stores()` function.

If we want to return a different status code using Flask, we can put it as the second value returned by an endpoint function. In `create_store()`, we are returning the code `201`, which means "Created".
:::

---

title: How to create items in each store
description: A brief description of the lecture goes here.

---

# How to create items in our REST API

Next up, let's work on adding items to a store!

Here's how that's going to work:

1. The client will send us the store name where they want their new item to go.
2. They will also send us the name and price of the new item.
3. We'll go through the stores one at a time, until we find the correct one (whose name matches what the user gave us).
4. We'll append a new item dictionary to that store's `items`.

## URL parameters

There are a few ways for clients to send us data. So far, we've seen that clients can send us JSON.

But data can be included in a few other places:

- The body (as JSON, form data, plain text, or a variety of other formats).
- Inside the URL, part of it can be dynamic.
- At the end of the URL, as _query string arguments_.
- In the request headers.

For this request, the client will send us data in two of these at the same time: the body and the URL.

How does a dynamic URL look like?

Here's a couple examples:

- `/store/My Store/item`
- `/store/another-store/item`
- `/store/a/item`

In those three URLs, the "store name" was:

- `My Store`
- `another-store`
- `a`

We can use Flask to define dynamic endpoints for our routes, and then we can grab the value that the client put inside the URL.

This allows us to make URLs that make interacting with them more natural.

For example, it's nicer to make an item by going to `POST /store/My Store/item`, rather than going to `POST /add-item` and then pass in the store name in the JSON body.

To create a dynamic endpoint for our route, we do this:

```py
@app.route("/store/<string:name>/item")
```

That makes it so the route function will use a `name` parameter whose value will be what the client put in that part of the URL.

Without further ado, let's make our route for creating items within a store!

```py title="app.py"
from flask import Flask, request

app = Flask(__name__)

stores = [{"name": "My Store", "items": [{"name": "my item", "price": 15.99}]}]


@app.get("/store")
def get_stores():
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


# highlight-start
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item
    return {"message": "Store not found"}, 404
# highlight-end
```

:::tip Not the most efficient way
In this endpoint we're iterating over all stores in our list until we find the right one. This is very inefficient, but we'll look at better ways to do this kind of thing when we look at databases.

For now, focus on Flask, and don't worry about efficiency of our code!
:::

---

title: Get a specific store and its items
description: How to use Flask to return data from your REST API to your client.

---

# How to get a specific store and its items

The last thing we want to look at in our first REST API is returning data that uses some filtering.

Using URL parameters, we can select a specific store:

```py
@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404
```

And just as we did when creating an item in a store, you can use the same endpoint (with a `GET` method), to select the items in a store:

```py
@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404
```
