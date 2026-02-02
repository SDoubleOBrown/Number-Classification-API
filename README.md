# Number Classification API

A REST API that takes a number and returns interesting mathematical properties about it.

## Features

- Checks if a number is prime
- Checks if a number is perfect
- Checks if a number is an Armstrong number
- Determines if a number is odd or even
- Calculates digit sum
- Provides fun facts about numbers

## API Endpoint
```
GET /api/classify-number?number=371
```

## Example Response
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

## Error Response
```json
{
    "number": "alphabet",
    "error": true
}
```

## Tech Stack

- Python
- Flask
- NGINX (reverse proxy)

## Live URL

http://3.16.51.62/api/classify-number?number=371
