# Capital Economics - Content API

(c) 2026 Capital Economics Ltd.

This section contains examples of how to use the Capital Economics Content API.

## Introduction

The Content API provides access to the articles and publications in the Capital Economics platform and is available to clients with a **valid subscription** for use of this product.

For more details about the APIs and Excel plugin see our [Data Capabilities page](https://www.capitaleconomics.com/data)

## Getting Started

1. **Obtain an API subscription** - To use the API you will need to have an api-user account. Please contact your account manager for more details.
2. We use generated **API keys** to authenticate users API requests. You will need to provide your api-key as a query string argument (more details below).
3. Call the API endpoint!

## Endpoint

There is one main endpoint for the Content API:

URI `https://api.capitaleconomics.com/json`

## Mandatory Query Parameter

### api-key

This will be a _32 character_ API key that you will have been provided; contact your account manager for more details. This is a **required** parameter.  For example:

`https://api.capitaleconomics.com/json?api-key=abcd...4321`

Accessing the endpoint in this way with no further query parameters will return JSON data listing all the available sub-endpoints.  For example:

```
{
  "jsonapi": {
    "version": "1.0",
    "meta": {
      "links": {
        "self": {
          "href": "http://jsonapi.org/format/1.0/"
        }
      }
    }
  },
  "data": [],
  "meta": {
    "links": {
      "me": {
        "meta": {
          "id": "ec9304d7-ca4f-402c-accd-9b2da0d0c538"
        }
      }
    }
  },
  "links": {
    "article": {
      "href": "https://api.capitaleconomics.com/json/node/article"
    },
    "file": {
      "href": "https://api.capitaleconomics.com/json/file"
    },
    "media-image": {
      "href": "https://api.capitaleconomics.com/json/media/image"
    },
    "publication": {
      "href": "https://api.capitaleconomics.com/json/node/publication"
    },
    "self": {
      "href": "https://api.capitaleconomics.com/json"
    },
    "tag-author": {
      "href": "https://api.capitaleconomics.com/json/tags/author"
    },
    "tag-blog-category": {
      "href": "https://api.capitaleconomics.com/json/tags/blog-category"
    },
    "tag-region": {
      "href": "https://api.capitaleconomics.com/json/tags/region"
    },
    "tag-topic": {
      "href": "https://api.capitaleconomics.com/json/tags/topic"
    }
  }
}
```

Note: Your api-key is ***required on every access*** made.  However, for the purposes of clarity we will omit it from these examples.

The first sub-endpoints likely to be accessed will be either `/json/node/article` or `/json/node/publication`

By default, these will return up to 50 items, sorted by most recent first.

## Optional Query Parameters

### page

The default of 50 items can be altered by using the `page` query parameter, such as:

`?page[limit]=5`

Minimum = 1, Maximum = 100, default = 50.

### offset

The offset parameter can be used to skip a number of pages:

`?page[limit]=5&page[offset]=3`

### filter

Filters allow you to reduce the amount of data returned by specifying, for example, the article title text, or a timestamp.

Example: *Title contains "Japan"*

`?filter[title][condition][path]=title&filter[title][condition][operator]=CONTAINS&filter[title][condition][value]=Japan`

Note: All three of these parts together define the filter: path, operator and value.

Example: *Published after timestamp*

`?filter[published_at][condition][path]=published_at&filter[published_at][condition][operator]=>=&filter[published_at][condition][value]=1765800223`

Here, the timestamp is a unix timestamp.

## Code snippets

We have provided some code snippets in this repository to help you get started.

* **Python** - We have provided a sample Python script that demonstrates how to use the API to retrieve data, click [here](./python/README.md) for more details

Enjoy!
