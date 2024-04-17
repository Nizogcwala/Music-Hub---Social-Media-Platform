
# Music Hub - Social Media Platform

A web application that aims to create a social music platform where music enthusiasts can discover new music, connect with artists, share their favorite tracks, and engage with like-minded individuals. 


## Authors

- [Sibusiso Mkhupheka](https://www.github.com/Nizogcwala)


## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## API Reference

#### Get all artists

```http
  GET /api/artists
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. API key for accessing the Spotify Web API. This key is necessary to authenticate and authorize requests to the Spotify API. Without a valid API key, access to the API endpoints will be denied. You can obtain an API key by registering your application with the Spotify Developer Dashboard. Example: YourAPIkey8932344d682c47ce80a22d1f2d68ec21
 |

#### Get artist by Id 

```http
  GET /api/artists/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. artist Id to fetch 0rlp1RP8eTEd74FVmndZ47 |

#### add(num1, num2)

Takes two numbers and returns the sum.


