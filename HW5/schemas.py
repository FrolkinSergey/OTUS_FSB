schema_list_breeds = {
        "type": "object",
        "properties":{
            "message": {"type": "object"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }


schema_any_images = {
        "type": "object",
        "properties":{
            "message": {"type": "array"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
}

schema_one_image = {
        "type": "object",
        "properties":{
            "message": {"type": "string"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
}


schema_any_brewery = {
        "type": "array",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "brewery_type": {"type": "string"},
            "address_1": {"type": "string"},
            "address_2": {"type": "string"},
            "address_3": {"type": "string"},
            "city": {"type": "string"},
            "state_province": {"type": "string"},
            "postal_code": {"type": "string"},
            "country": {"type": "string"},
            "longitude": {"type": "string"},
            "latitude": {"type": "string"},
            "phone": {"type": "string"},
            "website_url": {"type": "string"},
            "state": {"type": "string"},
            "street": {"type": "string"},
          },
        "required": ["id", "name", "brewery_type", "address_1", "address_2", "address_3", "city", "state_province",
                     "postal_code", "country", "longitude", "latitude", "phone", "website_url", "state", "street"]
}

schema_one_brewery2 = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "brewery_type": {"type": "string"},
            "address_1": {"type": "string"},
            "address_2": {"type": "null"},
            "address_3": {"type": "null"},
            "city": {"type": "string"},
            "state_province": {"type": "string"},
            "postal_code": {"type": "string"},
            "country": {"type": "string"},
            "longitude": {"type": "string"},
            "latitude": {"type": "string"},
            "phone": {"type": "string"},
            "website_url": {"type": "string"},
            "state": {"type": "string"},
            "street": {"type": "string"},
          },
        "required": ["id", "name", "brewery_type", "address_1", "address_2", "address_3", "city", "state_province",
                     "postal_code", "country", "longitude", "latitude", "phone", "website_url", "state", "street"]
}

schema_one_brewery = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "brewery_type": {"type": "string"},
            "address_1": {"type": "string"},
            "address_2": {"type": "string"},
            "address_3": {"type": "string"},
            "city": {"type": "string"},
            "state_province": {"type": "string"},
            "postal_code": {"type": "string"},
            "country": {"type": "string"},
            "longitude": {"type": "string"},
            "latitude": {"type": "string"},
            "phone": {"type": "string"},
            "website_url": {"type": "string"},
            "state": {"type": "string"},
            "street": {"type": "string"},
          },
        "required": ["id", "name", "brewery_type", "address_1", "address_2", "address_3", "city", "state_province",
                     "postal_code", "country", "longitude", "latitude", "phone", "website_url", "state", "street"]
}


schema_posts = {
        "type": "array",
        "properties":{
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["userId", "id", "title", "body"]
}


schema_posts_object = {
        "type": "object",
        "properties":{
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["userId", "id", "title", "body"]
}

schema_user = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "username": {"type": "string"},
            "email": {"type": "string"},
            "address": {"type": "object"},
            "phone": {"type": "string"},
            "website": {"type": "string"},
            "company": {"type": "object"},
        },
        "required": ["id", "name", "username", "email", "address", "phone", "website", "company"]
}
