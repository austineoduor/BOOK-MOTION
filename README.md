# BOOK MOTION

### Contents

- [Description](#Description)
- [Environment](#Environment)
- [Further Information](#Furtherinformation)
- [Requirements](#Requirements)
- [Repo Contents](#FileContents)
- [Installation](#Installation)
- [Usage](#Usage)
- [Technologies](#Technologies)

## Description :page_facing_up:
This project aims at making digital libraries more engaging, interactive and interesting by employing software engineering techniques to build a digital learning platform that helps users access learning materials easily, get book recommendations based on the user’s historical behavior  and also interact with other users.


## Environment :computer:
The console was developed in Ubuntu 14.04LTS using python3 (version 3.4.3).

### Further information :bookmark_tabs:
For further information on python version, and documentation visit [python.org](https://www.python.org/).

## Requirements :memo:
Knowledge in python3, how to use a command line interpreter, a computer with Ubuntu 14.04, python3.

## Repo Contents :clipboard:
This repository constains the following files:

|   **File**   |   **Description**   |
| -------------- | --------------------- |
|[AUTHORS](./AUTHORS) | Contains info about authors of the project |
|[BookMotion_base.py](./models/bookmotion_base.py) | Defines LibrarifyBase class (parent class), and methods |
|[file_storage.py](./models/storage/file_storage.py) | Creates new instance of class, serializes and deserializes data |
|[BookMotion_console.py](./bookmotion_console.py) | creates object, retrieves object from file, does operations on objects, updates attributes of object and destroys object |


## Installation :hammer_and_wrench:
Clone the repository and run the console.py
```
$ git clone https://github.com/austineoduor/BOOK-MOTION.git
```

## Usage :wrench:

|   **Method**   |   **Description**   |
| -------------- | --------------------- |
|[create](./bookmotion_console.py) | Creates object of given class |
|[show](./bookmotion_console.py) | Prints the string representation of an instance based on the class name and id |
|[all](./bookmotion_console.py) | Prints all string representation of all instances based or not on the class name |
|[update](./bookmotion_console.py) | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |
|[destroy](./bookmotion_console.py)| Deletes an instance based on the class name and id (save the change into the JSON file) |
|[count](./bookmotion_console.py)| Retrieve the number of instances of a class |
|[help](./bookmotion_console.py)| Prints information about specific command |
|[quit/ EOF](./bookmotion_console.py)| Exit the program |

###### Example

```
vagrant@ubuntu-focal:~/BOOK-MOTION$ ./bookmotion_console.py
(BookMotion) create BookMotionBase
8c638c17-28f3-4de1-bda7-377f24c87a7a
(BookMotion) show BookMotionBase 8c638c17-28f3-4de1-bda7-377f24c87a7a
[BookMotionBase] (8c638c17-28f3-4de1-bda7-377f24c87a7a) {'id': '8c638c17-28f3-4de1-bda7-377f24c87a7a', 'created_at': datetime.datetime(2023, 3, 20, 19, 9, 16, 49799), 'updated_at': datetime.datetime(2023, 3, 20, 19, 9, 16, 49904)}
(BookMotion)
(BookMotion)
(BookMotion) all BookMotionBase
["[BookMotionBase] (be7f7dea-f7cb-49e0-bac0-88a40d655054) {'id': 'be7f7dea-f7cb-49e0-bac0-88a40d655054', 'created_at': datetime.datetime(2023, 3, 20, 19, 0, 37, 131434), 'updated_at': datetime.datetime(2023, 3, 20, 19, 0, 37, 131505)}", "[BookMotionBase] (8c638c17-28f3-4de1-bda7-377f24c87a7a) {'id': '8c638c17-28f3-4de1-bda7-377f24c87a7a', 'created_at': datetime.datetime(2023, 3, 20, 19, 9, 16, 49799), 'updated_at': datetime.datetime(2023, 3, 20, 19, 9, 16, 49904)}"]
(BookMotion)
(BookMotion)


```

## Technologies :gear:
python3 (3.4.3)

### Acknowledgements :raised_hands:
To all the peers that contribuited with their knowledge

### Authors :fountain_pen:
* Austine Oduor
