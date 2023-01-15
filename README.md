# Interview Simulator 2023 API Wrapper
I dislike Flask, but I dislike C# even more. An API wrapper for [Cohere's](https://cohere.ai) Classify AI.

Part of the [Interview Simulator](https://github.com/mariagarcia466/Interview-Sim) project done for SheHacks+ 7.

# How to run
I honestly do not know how to use Flask for debug or production, good luck

# Documentation
There's really only one route here.

## /analyze

| Parameter | Value |
|---|---|
| Type | POST |
| Media Type | `application/json` |
| Data | `text` - A paragraph/sentence to be classified. |
| Response | One word - the most likely prediction. |
