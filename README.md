#🖥️ Skill Extractor

## Project Overview

Skill Extractor is a simple Python program that takes a user's self-description as input and identifies the programming languages, technologies, and skills mentioned in it.
The extracted information is then displayed in a structured JSON format.

## Problem Statement

When information about a person is given as normal text, it can take time to manually identify their skills and technical knowledge.
This project tries to solve this problem by automatically searching the given text for predefined languages, technologies, and skills.

## Installation Instructions

### ⚙️ Requirements

- Python 3.13.7
- No external Python libraries are required.

The project uses Python's built-in `re` and `json` modules.

### 💻 Running the Project

1. Clone or download this repository.
2. Open the project folder.
3. Run the Python file.

### 🔎How It Works
1.The user enters a description about themselves.
2.The program converts the input into a format suitable for searching.
3.It checks the text for predefined languages, technologies, and skills.
Regular expressions (re) are used to identify the skills accurately and avoid incorrect matches.
4.The detected skills are grouped into their respective categories.
5.The final result is displayed in JSON format.

##  🧪 Example

### Input
I have experience in Python and C++ and worked on CNN models and AI/ML projects.

### Output
{
    "Languages": [
        "python",
        "c++"
    ],
    "Technology": [
        "CNN"
    ],
    "Skill": [
        "AI/ML"
    ]
}

## 📁 Project Directory

Skill-Extractor/
│
├── Skill_extractor.py
└── README.md
Skill_extractor.py contains the main Python program, while README.md contains the project documentation.

---
## 📜 License
This project is open-source and available under the [MIT License](LICENSE). Feel free to fork, modify, and use it for your own projects!

---

<p align="center">
   ☀️<b>Built by John Rufina J R</b><br>
  <sub>Still learning. Still building. This is just the beginning</sub>
</p>
