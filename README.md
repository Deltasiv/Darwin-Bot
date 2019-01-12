# Darwin_Discord_Bot

> Darwin bot written in Python using discord.py library.

![](https://img.shields.io/badge/python-3.6-blue.svg) ![](https://img.shields.io/badge/license-MIT-lightgray.svg) ![](https://img.shields.io/badge/version-0.1.4-yellow.svg) ![](https://img.shields.io/badge/build-passing-green.svg)
[![Discord PY Version](https://img.shields.io/badge/discord.py-1.0.0a-green.svg)](https://github.com/Rapptz/discord.py/tree/rewrite)
[![Version](https://img.shields.io/badge/version-0.0.1-yellow.svg)](https://github.com/Hydr43301/darwin-python/)


![Header](https://camo.githubusercontent.com/6a1779d72cfc7c201252efb1fece317edf45f87e/68747470733a2f2f63646e2e646973636f72646170702e636f6d2f6174746163686d656e74732f3532393830373032383336353831393932352f3533303732363231323336303836333734352f756e6b6e6f776e2e706e67)

---

## Table of Contents 

These are the sections on the [README.md](https://github.com/Deltasiv/Darwin-Bot/blob/master/README.md) file. 

- [Description](#description) 
- [How To Use](#usage)
- [References](#references)
- [Contributing](#contributing)
- [Installation](#installation)
- [License](#license)
- [Files Included](#files-included)
- [Author Info](#author-info)
- [Contributors](#contributors)
- [Version Info](#version-info) 
- [Help](#help)
- [Info](#info)

--- 

## Description 

Darwin is a Microbiological tool in the making that is made to be used with Biological sciences and will have features added to 
make it better Darwin was made as a substitute to using big bulk textbooks and to simply use the modern tools given to us to work 
on Microbial data. 

#### Technologies 

- [Python 3.7.1](https://www.python.org/downloads/release/python-371/) 
- [SQLite3](https://docs.python.org/3/library/sqlite3.html) 
- [Discord.py 1.0.0a](https://discordpy.readthedocs.io/en/rewrite/)

##### Other technologies are subject to be used 

--- 

## Usage

### Installation

### Clone Repository

To clone Darwin repository please use the following command. 

```bash 
git clone https://github.com/Hydr43301/darwin-python/
```

### Virtualenv

Before using Darwin we need to setup virtualenv for the libraries, we can do that with the command:
```bash
python -m virtualenv darwin-python-master
```
After that activate the environment:
```bash
source darwin-python-master/bin/activate
```
And finally install discord.py:
```bash
python3 -m pip install -U https://github.com/Rapptz/discord.py/archive/async.zip#egg=discord.py[voice]
```

#### How To Use 

After activating the virtual environment enter the directory and run:
```bash
python discord_bot.py
```

#### Using the bot 

After the bot is running and inviting the bot to your server you can use the following commands:

* Bot
  * logout - Logs the bot off from the network, [read installation notes to change the user ID and token](#installation)

* Misc
  * ping - Checks for delay
  
* Moderation
  * purge {amount} - Purge amount of messages

#### Chaging User ID and TOKEN

To change User ID and TOKEN enter discord_bot.py with your text editor of choice and edit the following values:
```python
token = 'your token here'
ownerid = 'your user id here'
```

#### Prerequistites 

You must have a Python interpreter that will run Python 3.7.1. If you don't have one [install from here](https://www.python.org/downloads/release/python-371/). 

--- 

## References 

[Back To Top](#Table-of-Contents)

--- 

## License

MIT License 

Copyright (c) [2017] [Delta Siv] 

Permission is hereby granted, free of charge, to any person obtainin g a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: 

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. 

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT, IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 

See | [LICENSE.md](https://github.com/Deltasiv/Darwin-Bot/blob/master/LICENSE) file or [MIT](https://choosealicense.com/licenses/mit/)|

[Back To The Top](#Darwin) 

--- 

## Files Included 

[discord_bot.py](#https://github.com/Deltasiv/Darwin-Bot/blob/master/discord_bot.py) 
[LICENSE](#https://github.com/Deltasiv/Darwin-Bot/blob/master/LICENSE) 
[README.md](#https://github.com/Deltasiv/Darwin-Bot/blob/master/README.md)
[bug_report.md](#https://github.com/Deltasiv/Darwin-Bot/blob/master/.github/ISSUE_TEMPLATE/bug_report.md)
[feature_request.md](#https://github.com/Deltasiv/Darwin-Bot/blob/master/.github/ISSUE_TEMPLATE/feature_request.md)
[virus.db](#https://github.com/Deltasiv/Darwin-Bot/blob/master/resources/virus.db)
[virus.db-journal](#https://github.com/Deltasiv/Darwin-Bot/blob/master/resources/virus.db-journal) 

--- 

## Author Info 


- YELLOWHATT - https://github.com/YELLOWHATT

- Hydra - https://github.com/Hydr43301

- Johk3 - https://github.com/Johk3 

---

## Contributors 

- YELLOWHATT - https://github.com/YELLOWHATT

- Hydra - https://github.com/Hydr43301

- Artistic Memes - https://github.com/ArtisticMemes

- Johk3 - https://github.com/Johk3 

Darwin, darwin-python is currently maintained by [Delta Siv](https://github.com/Deltasiv)

--- 

## Version Info 

The current stable version of Darwin is: 0.0.1. 

This repository uses semantic versioning for keeping track of versions.

--- 

[Back To The Top](#Darwin) 

## Release History

* 0.0.1
   
   * Update discord_bot.py, Add virus.db, Create README.md

## Contributing

1. Fork it (<https://github.com/Hydr43301/darwin-python/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request 

---

## Help 

If you encounter issues while running Darwin please report it to [issues](https://github.com/Hydr43301/darwin-python/issues)

--- 

## Info 

If you have any info you are willing to know contact us on our social media or email. 

Emails are located int [Help](#help) otherwise use Twitter or Discord. 

#### Thank you for giving this project a look :) 

[Back To Top](#Darwin_Discord_Bot)
