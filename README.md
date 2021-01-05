# Face Id
This is my project for graduation at college.

Project was divived two part: backends, webserver.
*   The folder "backends" contains codes regard detect face, train model, embeding image...
*   In addition, outside codes was designed for UI use "CoreUI Free Laravel Bootstrap Admin Template".

# Table of content:
* [UI](#ui)
* [Installation](#installation)
* [Usage](#usage)

## UI

| User | Admin | login |
| --- | --- | --- |
| [![CoreUI](https://github.com/hoangpdang578/graduation-project/blob/main/user-ui.png)](https://github.com/hoangpdang578/) | [![CoreUI](https://github.com/hoangpdang578/graduation-project/blob/main/admin-ui.png)](https://github.com/hoangpdang578/)| [![CoreUI](https://github.com/hoangpdang578/graduation-project/blob/main/login-ui.png)](https://github.com/hoangpdang578/)


## Installation:
```bash
# clone the repo
$ git clone https://github.com/hoangpdang578/graduation-project
```
```bash
# go into app's directory
$ cd my-project/backends/data/employees-image
```
Replace by your data.

## Usage

### Train model 
After, you replace your data into folder "employees-image". You need train new data to obtain weight + model config. Then 

```bash
python update_empoyees.py
```
### Set up app's dependencies

Install some dependencies for UI.

```bash
# go to into app's directory
$ composter install 
$ npm install
```

Install package.

```bash
$ pip install -r requirement.txt
```
Note: Version python == 3.6, core system = Ubuntu 20.04

### Run

```bash
$ sh run.sh
```

## Contributors
Thanks to @khanhfabi support for CoreUI

