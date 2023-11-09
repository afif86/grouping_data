<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Project Title</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Few lines describing your project.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)


## 🧐 About <a name = "about"></a>

A webapp which groups people living at identical addresses. 
## Features
The webapp provide two ways to input the data: 
- By manual text entry through the form 
- By uploading а .csv file. 
- Using both option at the same time. 
..
The results will display on the UI and users have an option to download the results as a .txt file.
A text document where each line is a comma-separated list of names of people living at the same address. 
The names on each line is sorted alphabetically. 
The lines of the file also is sorted alphabetically.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
Python 3.9 +
Some kind of virtual environment (Optional/ Recommended)

```


### Installing

Create a virtual environment then install the requirements, (following the commands)

```
**pip install -r requirements.text**
```



## 🔧 Running the tests <a name = "tests"></a>


Execute by following command: 

```
pytest
```


## 🎈 Usage <a name="usage"></a>

Add your data through table one by one or upload a csv file and submit, the result will appear in a seconds. 

## 🚀 Deployment <a name = "deployment"></a>

Download the repo and use flask run command to run. it will port on your local host by default, to change the address run the command:( **flask run -p** _yourDesireNumber_ )



