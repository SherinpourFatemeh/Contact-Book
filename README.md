# Contact Book

The Python Contact Book Project provides an interactive console text-based application where users can store, retrieve, edit, and delete their contacts. User can store their contact's name, phone number, email, and address.

## Project Implementation
The primary data structure was a built-in Python dictionary, which was tasked with managing contact entries. 

# Project Structure
The project consists of the following files and directories.

```
.
├── README.md
└── main.py
```

The project structure was designed to be simple and clean.

- `README.md`: this document providing project description and documentation
- `main.py`: the main script which interacts with the user and uses ContactBook class methods to provide the desired functionality

### ContactBook Class

The core logic of the application is implemented in `contact_book` class:

- The `add_contact` method allows for new entries to be made to the 'book'. Each entry must be unique by name.
- The `update_contact` method permits updates to contact information.

- The `view_contact` method lists all contacts in the address book along with their information.
- The `delete_contact` method allows for existing contacts to be removed from the book.


The `main.py` file serves as an interface between the user and the `contact_book` class instance. It gets user inputs, calls the necessary methods and handles the application flow.


## Installation and Usage
To run the program, navigate to the project directory and run the following command:

```bash
python main.py
```