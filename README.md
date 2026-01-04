<a id="readme-top"></a>

<br />
<div align="center">
  <a href="https://github.com/Ryan-Goosen/run-on-anything">
    <img src="readme_graphics/Your paragraph text (Circle Sticker).png" alt="Logo" style="width:200px; border-radius: 50%;">
  </a>

  <h3 align="center">Run On Anything</h3>

  <p align="center">
    A Python library that lets you run your Python project on any machine with Python installed.
    <br />
    <a href="https://github.com/Ryan-Goosen/run-on-anything"><strong>Explore the docs »</strong></a>

</div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Unlicense License][license-shield]][license-url]

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project provides a Python script that runs you Python file (containing a `main` or entry point) inside a virtual environment created with a specified Python version anywhere  between 3.0 and 3.14.

It automatically installs dependencies from one of athe following (if present):
- `requirements`
- `uv.lock`
- `pyproject.toml`


Here's why:
* Avoids the "works on my machine" issue.
* Allows anyone to run your project with minimal setup.
* Simple install, its useable as a llibrary or directly from the internet.

You can install it via pip or import it directly into your project.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

### Built With

* [![Python][Python]][Python]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

These instructions will take you through the two different options you have to utilize the program inside you projects.

### Prerequisites

Python 3.0 or newer.
* Check your python version with:
  ```sh
  python --version
  ```

### Installation
#### Options 1: Clone and Install locally

1. Clone the repo
   ```sh
   git clone https://github.com/Ryan-Goosen/run-on-anything.git
   ```

2. Adding the repo to pip

   Inside of the repos directory run the following command.
   ```sh
       pip install .
   ```

3. You can now utilize the repo as a library inside of your projects. 

#### Options 2: Install directly from Github

1. Add the repo to pip

  ```sh
    pip install git+https://github.com/Ryan-Goosen/run-on-anything.git
  ```

2. You can now utilize the repo as a library inside of your project. 


## Usage

To use the library create a new .py file and import the library. Call the `run()` function, passing in:
- the file name containing you main function
- the python version to run it with

```python
from env_setup import run

run("main.py", 3.13.0)
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Working Demo
- [ ] Run the program from the run function instead of having to create a new method


<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Top contributors:

<a href="https://github.com/Ryan-Goosen/run-on-anything/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Ryan-Goosen/run-on-anything" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/Ryan-Goosen/run-on-anything](https://github.com/Ryan-Goosen/run-on-anything)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

I would like to give credit to the following people for helping me.

* [ReadMe Template](https://github.com/othneildrew/Best-README-Template) 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Ryan-Goosen/run-on-anything.svg?style=for-the-badge
[contributors-url]: https://github.com/Ryan-Goosen/run-on-anything/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Ryan-Goosen/run-on-anything.svg?style=for-the-badge
[forks-url]: https://github.com/Ryan-Goosen/run-on-anything/network/members
[stars-shield]: https://img.shields.io/github/stars/Ryan-Goosen/run-on-anything.svg?style=for-the-badge
[stars-url]: https://github.com/Ryan-Goosen/run-on-anything/stargazers
[issues-shield]: https://img.shields.io/github/issues/Ryan-Goosen/run-on-anything.svg?style=for-the-badge
[issues-url]: https://github.com/Ryan-Goosen/run-on-anything/issues
[license-shield]: https://img.shields.io/github/license/Ryan-Goosen/run-on-anything.svg?style=for-the-badge
[license-url]: https://github.com/Ryan-Goosen/run-on-anything/blob/main/LICENSE
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54

<!-- [linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555 -->