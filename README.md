# 🧠 Sweatable – Your Multilingual AI Companion

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sweatable.streamlit.app/)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**Sweatable** is an intelligent multilingual AI companion app that breaks language barriers in AI conversations. Built with **Streamlit** and powered by **Sarvam AI**, it enables users to chat with an AI assistant in various Indian languages, creating more inclusive and culturally relevant interactions.

## 🌟 Why Sweatable?

In a diverse country like India, language plays a crucial role in comfortable communication. Sweatable addresses the gap in AI accessibility by:

- **Democratizing AI**: Making AI conversations accessible to non-English speakers
- **Cultural Sensitivity**: Understanding regional contexts and linguistic nuances
- **Real-time Translation**: Seamless conversations across language barriers
- **Emotional Connection**: Building deeper relationships through native language interaction

## ✨ Features

### 🔤 **Multilingual Support**
- Support for major Indian languages (Hindi, Tamil, Bengali, Telugu, Marathi, and more)
- Seamless language switching during conversations
- Regional dialect understanding

### 💬 **Intelligent Conversations**
- Powered by Sarvam AI's advanced language models
- Context-aware responses
- Natural language understanding across languages

### 🎭 **Enhanced User Experience**
- Realistic typing animation effects
- Character-based interaction modes
- Clean, responsive interface design
- Mobile-friendly responsive layout

### 🎨 **Modern UI/UX**
- Minimal and intuitive design
- Dark/light theme compatibility
- Smooth animations and transitions
- Accessibility-focused interface

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Sarvam AI API key ([Get one here](https://sarvam.ai/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/RajeebLochan/Sweatable.git
   cd Sweatable
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   SARVAM_API_KEY=your_sarvam_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run sweatable.py
   ```

6. **Open your browser** and navigate to `http://localhost:8501`

## 🎯 Usage Guide

### Getting Started
1. **Select Your Character**: Choose from different AI personalities
2. **Pick Your Language**: Select your preferred Indian language
3. **Start Chatting**: Type your message and hit Enter
4. **Experience Magic**: Watch the AI respond naturally in your chosen language

### Pro Tips
- Switch languages mid-conversation for bilingual interactions
- Use natural phrases and colloquialisms - the AI understands context
- Experiment with different characters for varied conversation styles
- The typing effect can be toggled in settings for faster responses

## 🏗️ Architecture

```
Sweatable/
├── sweatable.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (create this)
├── .gitignore           # Git ignore file
├── README.md            # This file
└── assets/              # Static assets (if any)
```

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **Backend**: Sarvam AI API
- **Language**: Python 3.8+
- **Deployment**: Streamlit Cloud
- **Environment Management**: python-dotenv

## 🌐 Deployment

The app is deployed on Streamlit Cloud and accessible at:
**[sweatable.streamlit.app](https://sweatable.streamlit.app/)**

### Deploy Your Own Instance

1. Fork this repository
2. Connect your GitHub account to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy the app with your Sarvam AI API key in secrets
4. Configure environment variables in Streamlit Cloud dashboard

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Contribution Ideas
- Add support for more Indian languages
- Implement voice input/output functionality
- Create more character personalities
- Improve UI/UX design
- Add conversation history persistence
- Implement advanced NLP features


## 🐛 Known Issues

- API rate limits may cause temporary delays
- Some regional dialects may need fine-tuning
- Some Mobile responsiveness can be improved

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[Sarvam AI](https://sarvam.ai/)** for providing the powerful multilingual AI backend
- **[Streamlit](https://streamlit.io/)** for the excellent framework that makes building AI apps effortless
- **Indian Language Community** for inspiration and feedback
- **Open Source Contributors** who make projects like this possible

## 👨‍💻 About the Developer

**Rajeeb Lochan** - Full Stack Developer & AI Enthusiast

- 💼 [LinkedIn](https://www.linkedin.com/in/rajeeb-lochan/)
- 🐦 [Twitter](https://x.com/rajeeb_thedev)
- 📧 Contact: [rajeebl2003@gmail.com]

Passionate about making AI accessible to everyone, regardless of their language preference. Building bridges between technology and cultural diversity.

## 🌟 Support

If you find Sweatable useful, please consider:
- ⭐ Starring this repository
- 🍴 Forking and contributing
- 📢 Sharing with friends and colleagues
- 💬 Providing feedback and suggestions

---

**Made with ❤️ for the Indian AI community**

*"Technology should speak your language, not the other way around."*
