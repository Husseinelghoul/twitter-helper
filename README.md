# Twitter Unliker

Twitter Unliker is a Python script that uses the Twitter API to unlike all tweets between a certain date range. This script is useful if you want to clean up your liked tweets and start fresh.

## Requirements
Python 3.x
Tweepy library

## Setup
1. Clone the repository:
    ```
    git clone https://github.com/your-username/twitter-unliker.git
    cd twitter-unliker
    ```
2. Install the Tweepy library:
    ```
    pip install tweepy
    ```
3. Create a Twitter API application and obtain your API keys and access tokens.
You can follow the instructions [here](https://developer.twitter.com/en/docs/apps/overview) to create a new application

3. Update the `config.ini` file with your API keys and access tokens:
```
    [Twitter]
    consumer_key = your_consumer_key
    consumer_secret = your_consumer_secret
    access_token = your_access_token
    access_token_secret = your_access_token_secret
```
4. Modify the `start_date` and `end_date` variables in `unliker.py` to your desired date range.

## Usage
To run the script, simply run the `unliker.py` file:
```
python unliker.py
```

The script will automatically unlike all tweets that were liked between the `start_date` and `end_date` specified in the `unliker.py` file.

## Credit
This script was created by Hussein ElGhoul. Special thanks to the Tweepy library for providing an easy-to-use Python wrapper for the Twitter API.

## License
This project is licensed under the MIT License.