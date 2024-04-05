# Private Key Importer for Phantom Wallet

This script allows you to decode a Base58 encoded private key, convert it to a numerical array format, and save it as a JSON file. This JSON file is formatted for direct import into the Phantom wallet.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python 3.x
- pip (Python package installer)


## Installation

Follow these steps to set up the environment and run the script:

1. Install Python
If you haven't installed Python, download it from the official Python website (https://www.python.org/downloads/) and follow the installation instructions for your operating system.

2. Clone the Repository
Clone this repository to your local machine using Git:

```
git clone https://github.com/yanowo/solana_decode_private_key.git
cd solana_decode_private_key
```

3. Install Dependencies
Install the required Python packages using pip:

```
pip install base58 python-dotenv
```

4. Set Up Environment Variables
Create a .env file in the root directory of the project. Add your Base58 encoded private key to this file:

```
PRIVATE_KEY=YourBase58EncodedPrivateKeyHere
```

Usage
Run the script with the following command:

```
python decode_private_key.py
```

This will decode your Base58 encoded private key, convert it into a numerical array, and save it in a file named id.json in the current directory.
