# tldr
Socials Summarized: A quick example on how to use openAI to summarize text responses from third party socials.


## Requirements

You will need to create your own reddit app, you can do so [here](https://www.reddit.com/prefs/apps).
- Reddit Client ID
- Reddit Client Secret

You will also need an OpenAI Api Key which you can get [here](https://platform.openai.com/account/api-keys)
- OpenAI Api Key


## Running Locally

Copy the sample.env file and rename it to .env, ensure it remains in the root of this directory.
Update your new .env file with the required variables.


### Without Docker
To run without docker you can simply do the following.

*I would highly recommend using a python virtual environment when running any python project*

[https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)

```python
pip install -r requirements.txt
python main.py
```

This will start a uvicorn server running on the following port address by default [http://127.0.0.1:3000](http://127.0.0.1:3000)

Any code changes will reload the server, so you can hack away and see changes instantly

### With Docker

To run using docker use the following commands.

```python
docker build -t tldrapp .
docker run -d --name tldrappcontainer -p 3000:3000 tldrapp
```

This will start a uvicorn server running on the following port address by default [http://127.0.0.1:3000](http://127.0.0.1:3000)


## Health check

You can verify that the application is running by visiting the following url [http://127.0.0.1:3000/health](http://127.0.0.1:3000/health)

# Summarize

To summarize your configured socials, simply send a get request to [http://127.0.0.1:3000/summarize](http://127.0.0.1:3000/summarize)

The response will be a json object in the following format

```js
{
    "social name": {
        "social post title": "social post summary"
    }
}
```

Example:
```js
{
    "reddit": {
        "TIFU by deving on windows": "Mistakes were made by the user....."
    }
}
```


# Adapters

Adapters are classes that handle the fetching / parsing and summarization of their particular social media content.
They should adhere to the base Adapter interface.

## Reddit

The only adapter currently supported by this application.

You can find the adapter in src.app.adapters.Reddit.

This class was designed to fetch the first 5 "hot" posts from the "tldr" subreddit as this is a very popular text based subreddit - a good starting point on text summarization using OpenAI.

### Note

The current options are customizable to your own taste. ie. post limit, subreddit, and openai summarization model. The current values were chosen as a showcase configuration.

Token size and OpenAI limitations are not accounted for in this application, you may need to adjust your settings according to your own openAI account usage

This is not intended for production environments


# TODO

- Facebook Adapter
- Twitter Adapter
- AWS Infrasctructure
    - ECS
    - ECR
    - Example on michaeltreyvaud.com with UI