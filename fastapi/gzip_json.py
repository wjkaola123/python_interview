import json
import gzip


def compress_data(data):
    # Convert to JSON
    json_data = json.dumps(data, indent=2)
    # Convert to bytes
    encoded = json_data.encode('utf-8')
    # Compress
    compressed = gzip.compress(encoded)
    return compressed


data = {
    "name": "John Smith",
    "age": 35,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "90210"
    },
    "phone": [
        {
            "type": "home",
            "number": "555-1234"
        },
        {
            "type": "work",
            "number": "555-5678",
            "extension": "123"
        }
    ],
    "email": "john.smith@example.com",
    "social_media": {
        "facebook": "https://www.facebook.com/john.smith",
        "twitter": "https://twitter.com/john_smith",
        "instagram": "https://www.instagram.com/john_smith"
    },
    "education": [
        {
            "degree": "Bachelor",
            "major": "Computer Science",
            "school": "University of California, Los Angeles",
            "graduation_year": 2010
        },
        {
            "degree": "Master",
            "major": "Business Administration",
            "school": "Stanford University",
            "graduation_year": 2015
        }
    ],
    "work_experience": [
        {
            "company": "Google",
            "position": "Software Engineer",
            "start_date": "2010-05-01",
            "end_date": "2014-04-30"
        },
        {
            "company": "Apple",
            "position": "Senior Software Engineer",
            "start_date": "2014-05-01",
            "end_date": "2018-06-30"
        },
        {
            "company": "Amazon",
            "position": "Engineering Manager",
            "start_date": "2018-07-01",
            "end_date": None
        }
    ]
}

compressed_data = compress_data(data)
print(compressed_data)


def decompress_gzip_data(input_data):
    try:
        decompressed_data = gzip.decompress(input_data)
        return decompressed_data
    except Exception as e:
        print(f"Oops! Something went wrong in the kitchen, I mean, with the decompression: {e}")
        return None


# Replace 'compressed_data' with your gzip compressed data
decompressed_data = decompress_gzip_data(compressed_data)
if decompressed_data:
    orginal_data = decompressed_data.decode(encoding='utf-8')
    json_object = json.loads(orginal_data)
    print(json_object)
