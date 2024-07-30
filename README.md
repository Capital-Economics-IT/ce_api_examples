# Capital Economics - API Examples

(c) 2024 Capital Economics Ltd.

This repository contains examples of how to use the Capital Economics API. 


## Introduction

The API provides access to a range of economic data and forecasts and is available to clients with a **valid subscription** for use of this product.

For more details about the API and Excel plugin see our [Data Capabilities page](https://www.capitaleconomics.com/data)


## Getting Started

1. **Obtain an API subscription** - To use the API you will need to have an api-user account. Please contact your account manager for more details.

2. We use [basic auth](https://en.wikipedia.org/wiki/Basic_access_authentication) to authenticate users API requests. You will need to provide your API username and password in the request headers (more details below).

3. Write your code! We have provided some examples in this repository to help you get started.


## APIs

We provide 2 main endpoints for the API:

* **Metadata** 
* **Data**

An optional `?vers=parameter` can be added to specify the version of the API you wich to use. _The latest current version will be used if no version is specified._

Each API endpoint requires **basic authentication** (see above) along with assorted query parameters to specify the data you wish to retrieve.


## Metadata API

URI `https://capitaleconomics.com/api/middletier/metadata/prod`

This endpoint provides access to our economic series metadata. 

### Query Parameters

The query parameters for the metadata endpoint are as follows:

#### skey

Series ID. This is the identifier for the series e.g. "GB_RGDPYY".
Multiple series IDs can be supplied separated by commas. This is a **required** parameter.

#### f_code

Frequency. This identifies the frequency. The valid options are "D" (daily), "W" (weekly), "M" (monthly), "Q" (quarterly), "Y" (yearly). This is an _optional_ parameter.

#### t_code

Type. The type of the data required, either "AC" for actual data, "F" for Capital Economics forecasts, or blank for both. This is an _optional_ parameter.


## Data API

URI `https://capitaleconomics.com/api/middletier/data/prod`

This endpoint provides access to our economic data and forecasts. _This is essentially time based series data._

### Query Parameters

The query parameters for the data endpoint are as follows:

#### skey 

Series ID. This is the identifier for the series e.g. "GB_RGDPYY". 
Multiple series IDs can be supplied separated by commas. This is a **required** parameter.

#### f_code

Frequency. This identifies the frequency. The valid options are "D" (daily), "W" (weekly), "M" (monthly), "Q" (quarterly), "Y" (yearly). This is a **required** parameter.

#### t_code

Type. The type of the data required, either "AC" for actual data, "F" for Capital Economics forecasts, or blank for both. This is an _optional_ parameter. 

#### start_date

Start Date. The date from which you want data to be returned. This should be in the format "YYYY-MM-DD". This is an _optional_ parameter.

#### end_date

End Date. The last date to which you want data to be returned. This should be in the format "YYYY-MM-DD". This is an _optional_ parameter.

#### series_info

Series Info. Another _optional_ parameter, if set to `TRUE` will return series metadata alongside the data, `FALSE` (the default) returns the data only.

## Code snippets

We have provided some code snippets in this repository to help you get started.

* **Python** - We have provided a Python script that demonstrates how to use the API to retrieve data.

Enjoy!