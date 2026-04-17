# v3/projects/{projectId}/weather/{weatherId}

Source: https://aps.autodesk.com/en/docs/acc/reference/http/forms-get-weather-data-for-a-project-GET/

---

Get weather data for a project

GET

# v3/projects/{projectId}/weather/{weatherId}

Returns weather data for a specific weather record associated with a project.

Weather data is returned in **metric units**:
- Temperature values (`temp`, `temperatureMin`, `temperatureMax`) are in **Celsius** - Wind speed values (`windSpeed`, `windGust`) are in **kilometers per hour (km/h)** - Precipitation values (`precipitationAccumulation`) are in **millimeters (mm)**

Weather records are created when forms capture weather conditions. Use the `weatherId` from a form to retrieve the full weather details.

## [Resource Information](#resource-information)

| Method and URI | GET https://developer.api.autodesk.com/construction/forms/v3/projects/:projectId/weather/:weatherId |
| --- | --- |
| Authentication Context | User context required |
| Required OAuth Scopes | `data:read` |
| Data Format | JSON |

### Request

## [Headers](#headers)

| Authorization*   string | Must be `Bearer <token>`, where `<token>` is a three-legged access token obtained via an [Authorization Code flow](../../oauth/how-to-docs/get-3-legged-token.md) or a [Secure Service Account (SSA) flow](../../ssa/tutorials-docs/getting-started-with-ssa-task3-generate-3-legged-access-token.md). <br>The SSA flow is designed for headless server-to-server operations. While it functions like a two-legged flow (no user interaction), it is classified as three-legged because it preserves user context. |
| --- | --- |

* Required

### Request

## [URI Parameters](#uri-parameters)

- projectIdstring The ID of the project. Use the [Data Management API](https://aps.autodesk.com/en/docs/data/v2/) to retrieve the project ID. For more information, see the [Retrieve a Project ID](https://forge.autodesk.com/en/docs/acc/v1/tutorials/getting-started/retrieve-account-and-project-id/) tutorial. You need to convert the project ID into a project ID for the Forma API by removing the “**b.**" prefix. For example, a project ID of **b.**a4be0c34a-4ab7 translates to a project ID of a4be0c34a-4ab7.
- weatherIdint The unique identifier of the weather record. Use [GET forms](https://aps.autodesk.com/en/docs/acc/v1/reference/http/forms-forms-(Deprecated/)-GET/) to retrieve the weather ID from a form’s `weatherId` field.

### Response

## [HTTP Status Code Summary](#http-status-code-summary)

| 200   OK | Weather data in metric units. |
| --- | --- |
| 400   Bad Request | The request could not be understood by the server due to malformed syntax or missing request header |
| 401   Unauthorized | The request was not accepted because it lacked valid authentication credentials |
| 403   Forbidden | The request was not accepted because the client is authenticated, but is not authorized to access the target resource |
| 404   Not Found | The weather record cannot be found |
| 429   Too Many Requests | The request could not be completed due to the rate limit of the target resource |
| 500   Internal Server Error | The request could not be completed due to an internal server error |

### Response

## [Body Structure (200)](#body-structure-200)

Expand all

| id   int | Unique identifier for the weather record. |
| --- | --- |
| summaryKey   string | A code describing the weather conditions in SCREAMING_SNAKE_CASE. Common values include: `CLEAR`, `RAIN`, `SNOW`, `SLEET`, `WIND`, `FOG`, `CLOUDY`, `PARTLY_CLOUDY`, `MOSTLY_CLEAR`, `MOSTLY_CLOUDY`, `HEAVY_RAIN`, `DRIZZLE`, `HEAVY_SNOW`, `FLURRIES`, `FREEZING_RAIN`, `THUNDERSTORMS`, `WINDY`, `BREEZY`, `FOGGY`, `HAZE`, `BLIZZARD`, `HOT`, `FRIGID`, `WINTRY_MIX`. Additional values may appear as weather condition codes evolve. |
| precipitationType   string | Type of precipitation. Possible values: `RAIN`, `SNOW`, `SLEET`, or `null` if no precipitation. |
| precipitationAccumulation   number | Amount of precipitation accumulated throughout the day, in **millimeters (mm)**. |
| hourlyWeather   array: object | Weather observations for specific hours of the day (typically 07:00, 12:00, and 16:00 local time). |
| id   int | Unique identifier for the hourly weather record. |
| summaryKey   string | A code describing the weather conditions for this hour in SCREAMING_SNAKE_CASE. Common values include: `CLEAR`, `RAIN`, `SNOW`, `SLEET`, `WIND`, `FOG`, `CLOUDY`, `PARTLY_CLOUDY`, `MOSTLY_CLEAR`, `MOSTLY_CLOUDY`, `HEAVY_RAIN`, `DRIZZLE`, `HEAVY_SNOW`, `FLURRIES`, `FREEZING_RAIN`, `THUNDERSTORMS`, `WINDY`, `BREEZY`, `FOGGY`, `HAZE`, `BLIZZARD`, `HOT`, `FRIGID`, `WINTRY_MIX`. Additional values may appear as weather condition codes evolve. |
| hour   string | The hour of day for this observation, in `HH:MM:SS` format (24-hour clock). |
| temp   number | Temperature during the specified hour, in **degrees Celsius (°C)**. |
| windSpeed   number | Average wind speed during the specified hour, in **kilometers per hour (km/h)**. |
| windBearing   int | Direction the wind is coming from, in degrees (0-360). North is 0°, East is 90°, South is 180°, West is 270°. |
| windBearingKey   string | Cardinal direction the wind is coming from. Possible values: `N`, `NE`, `E`, `SE`, `S`, `SW`, `W`, `NW`. |
| humidity   number | Relative humidity as a decimal value between 0 and 1 (e.g., 0.65 represents 65% humidity). |
| provider   enum:string | Indicates the source of the weather data. Possible values: `DARK_SKY`, `WEATHER_KIT` |
| fetchedAt   datetime: ISO 8601 | The date and time when the weather data was fetched from the weather API. |

## [Example](#example)

Weather data in metric units.

### Request

```
curl -v 'https://developer.api.autodesk.com/construction/forms/v3/projects/:projectId/weather/:weatherId' \
  -H 'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'

```

### Response

```
{
  "id": 12345,
  "summaryKey": "CLEAR",
  "precipitationType": "RAIN",
  "precipitationAccumulation": 12.7,
  "hourlyWeather": [
    {
      "id": 67890,
      "summaryKey": "PARTLY_CLOUDY",
      "hour": "12:00:00",
      "temp": 22.5,
      "windSpeed": 16.9,
      "windBearing": 225,
      "windBearingKey": "SW",
      "humidity": 0.65
    }
  ],
  "provider": "WEATHER_KIT",
  "fetchedAt": "2024-01-20T14:30:00+00:00"
}

```

Show More
