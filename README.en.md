

# VSS Playwright UI Test Project

This is a UI automation test project based on Playwright, designed for testing VSS-related functionalities. The project employs the Page Object Model design pattern and integrates with the Allure reporting framework.

## 📁 Project Structure

```
.
├── BasePage/                # Base page class, encapsulating commonly used page operation methods
├── BuildinLibrary/          # Built-in library, providing functionalities such as parameter replacement
├── Common/                  # Common module, including Allure report beautification tools
├── Config/                  # Configuration module, containing project configuration information
├── Pages/                   # Page object directory, where each page corresponds to a class
├── TestCase/                # Test case directory, containing specific test scripts
├── TestDatas/               # Test data directory, using YAML files to store test data
├── TestReport/              # Test report output directory
├── Utils/                   # Utility class directory, including YAML file reading tools
├── conftest.py              # pytest fixture configuration file
├── requirements.txt         # Project dependency file
└── run.py                   # Test execution entry file
```

## 🛠️ Technology Stack

- [Playwright](https://playwright.dev/) - Browser automation tool  
- [pytest](https://docs.pytest.org/en/latest/) - Testing framework  
- [Allure](https://docs.qameta.io/allure/) - Test reporting framework  
- [YAML](https://yaml.org/) - Test data storage format  

## 📦 Installation

1. Install dependencies  

```bash
pip install -r requirements.txt
```

2. Install Playwright browsers  

```bash
playwright install
```

## 🧪 Usage Instructions

1. Writing test cases  

Test cases are located in the `TestCase` directory and are written using the `pytest` framework.

2. Running tests  

```bash
python run.py
```

3. Viewing test reports  

Test reports are generated in the `TestReport/AllureReport` directory. You can start the report server using the following command:

```bash
allure serve TestReport/AllureResult
```

## 📝 Page Object Model

The project adopts the Page Object Model design pattern, where each page corresponds to a class that encapsulates the element locators and operation methods of the page. For example:

```python
class LoginPage(BasePage):
    def goto_login(self, url):
        self._goto_url(url)
    
    def fill_username(self, value):
        self._fill("#username", value)
    
    def fill_password(self, value):
        self._fill("#password", value)
    
    def click_login_button(self):
        self._click("#login-button")
```

## 📊 Test Data

Test data is stored in YAML format in the `TestDatas` directory and is read using the `ReadYaml` utility class.

```yaml
- username: "testuser"
  password: "testpass"
  expected_result: "success"
```

## 📎 Allure Reports

Test results generate Allure reports that include detailed test steps, screenshots, and execution information. Reports are saved in the `TestReport/AllureResult` directory.

## 📤 Contribution Guidelines

Code contributions are welcome! Please follow these steps:

1. Fork the project  
2. Create a new branch (`git checkout -b feature/new-feature`)  
3. Commit your changes (`git commit -am 'Add new feature'`)  
4. Push the branch (`git push origin feature/new-feature`)  
5. Create a Pull Request  

## 📄 License

This project uses the MIT License. Please refer to the [LICENSE](LICENSE) file for more details.