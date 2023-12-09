# Static Discord Rich Presence Client

This repository contains a Python script for creating and managing a static Discord Rich Presence using the pypresence library.

## Features
- Asynchronous Discord Rich Presence management
- Customizable presence data
- Graceful handling of connection and disconnection

## Compatibility
- This client should work on all operating systems, but it has been specifically tested on Windows and macOS.

## Resource Efficiency
- This client is resource-efficient because it sets the presence once and only keeps the connection alive without any continuous loops.

## Requirements
- Python 3.6 or higher
- [pypresence](https://github.com/qwertyquerty/pypresence) library

## Installation
1. Clone this repository.
2. Install the required dependencies:
   ```
   pip install pypresence
   ```

## Usage
1. Obtain your Discord application's client ID and set it in `static_data.py`.
2. Set the other fields in `static_data.py` (Set them to `None` to disable them.).
3. Run the script:
   ```
   python static_drp.py
   ```

## Contributing
Feel free to fork this repository and submit pull requests.

## Acknowledgments
- [pypresence](https://github.com/qwertyquerty/pypresence) for providing the Discord Rich Presence API wrapper for Python.