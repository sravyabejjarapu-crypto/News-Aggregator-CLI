📰 News Aggregator CLI (Python)
A simple command-line based News Aggregator application built using Python.
This project fetches the latest news headlines from an API and allows users to filter and save results.
🚀 Features
- Fetch latest news by country 🌍
- Filter news using keywords 🔍
- Display title and description 📰
- Option to save results to CSV 📁
- Simple CLI interface 💻
🛠️ Technologies Used
- Python
- requests library
- News API
📦 Installation
1. Clone the repository:
git clone https://github.com/your-username/news-aggregator.git
2. Navigate to the project folder:
cd news-aggregator
3. Install required packages:
pip install requests pandas
🔑 Setup API Key
1. Go to https://newsapi.org
2. Sign up and get your API key
3. Replace in code:
API_KEY = "your_api_key_here"
▶️ Usage
Run the program using:
python news_aggregator.py
🧾 Example
Enter country code (us/in/gb): in
Do you want to save results to CSV? (yes/no): no
Enter keyword to filter or press enter: technology
Output:
Title: Example News Title
Description: Example description of the news
--------------------------------------------------
📁 Project Structure
news-aggregator/
│── news_aggregator.py
│── README.md
🎯 Future Improvements
- Add GUI (Tkinter / Web app)
- Add category selection (sports, tech, etc.)
- Pagination for more news
- Better UI formatting
🤝 Contributing
Feel free to fork this repo and submit pull requests.
📄 License
This project is open-source and available under the MIT License.
🙌 Acknowledgements
- NewsAPI for providing news data
- Python community
