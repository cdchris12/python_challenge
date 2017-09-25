# Python Challenge
A simple script that connects to the IBM X-Force API and returns human
readable results about a specified IP address.

# Setup
## Dependencies
In order to use this script, no additional package installation is
required.

## Configuration File
Before you can use this script to make calls to the X-Force
Exchange API, you must create a valid configuration file. In order to
do that, you'll need to change the name of "iprep_conf.py.CHANGEME"
to "iprep_conf.py" and add your own personal API keys to the "xfex_cred"
value. To do this on a *NIX machine, the command would be:
```bash
mv iprep_conf.py.CHANGEME iprep_conf.py
```
Your API keys need to be formatted as `"<api_key>:<api_secret>"`. For
example, if your key was "123", and your secret was "qwerty", your
configuration file should read as follows:
```python
#XForce exchange
# via https://exchange.xforce.ibmcloud.com/new
# Settings -> API key
xfex_cred = "123:qwerty"
```

# Usage
This script can be called directly, `./x_force.py`, or by launching the
python interpreter and passing the name of this script as a variable
`python x_force.py`

## Arguments
This script accepts the following arguments:
1. `-i <IP_Address>` or `--ip <IP_Address>`
   - The IP address you want to use to query the Xforce API
2. `-o <File_Name>` or `--outfile <File_Name>`
   - The file name you'd like the program to save the output file as.

## Example Commands
`./x_force.py -i 8.8.8.8` to query the API for the `8.8.8.8` IP address
and print the results to the console.

`python x_force.py --ip 8.8.4.4 -o results.json` to query the API for
the `8.8.4.4` IP address and save the results in JSON format as
`results.json`.

# Acknowledgements
This project uses code from
[The CTI-Toolbox Project](https://github.com/johestephan/CTI-Toolbox),
used per the licensing terms.
