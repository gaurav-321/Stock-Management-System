# Stock Management System 📦

## Description ✨
The Stock Management System is a simple yet powerful tool built using Flask to manage product inventory efficiently. It offers features like adding, updating, and deleting products, along with a login feature for secure access.

## Features 🚀
- **User Authentication:** Secure user registration and login.
- **Product Management:** Add, update, and delete products easily.
- **Web-based Interface:** Manage stock through an intuitive web interface.

## Installation 🛠️
1. Clone the repository:
   ```bash
   git clone https://github.com/gag3301v/Stock-Management-System.git
   cd Stock-Management-System
   ```

2. Install dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage 📦
Here’s how you can use the system:

### Running the Application
To run the application, execute:
```bash
python app.py
```
The server will start on `127.0.0.1` at port `8080`.

### Adding a Product
Navigate to `/add_product` in your browser and fill out the form to add a new product.

## Configuration 🔧
- **Environment Variables:** No specific environment variables are required, but ensure that the database URI is correctly set in your development environment.
  
## Tests 🧪
This project includes basic unit tests for key functionalities. You can run them using:
```bash
python -m unittest discover tests/
```

## Project Structure 📁
```
Stock-Management-System/
├── app.py
├── forms.py
├── methods.py
├── models.py
├── routes.py
└── templates/
    ├── base.html
    ├── dashboard.html
    ├── login.html
    ├── register.html
    └── stock_list.html
```

## Contributing 🙌
Contributions are welcome! Please read our [CONTRIBUTING.md](https://github.com/gag3301v/Stock-Management-System/blob/main/CONTRIBUTING.md) for details on how to contribute.

## License 📄
This project is licensed under the MIT License - see the [LICENSE](https://github.com/gag3301v/Stock-Management-System/blob/main/LICENSE) file for details.

---

**Note:** This README is a template and should be adapted according to your specific project's needs.