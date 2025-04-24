# assistAIve

# assistAIve 🤖 – Your Personal AI Tool Finder

assistAIve is a friendly AI chatbot that helps users discover useful AI tools and websites based on what they want to do like building a website, editing an image, writing a blog or more. It's designed to feel simple and helpful, especially for people who aren't experts with technology.

## What It Does

- Helps users find AI tools by understanding what they type.
- Uses smart language processing (NLP) to match their input with tools.
- Supports chatting, tool suggestions, and remembering history.
- Admins can view all user chats and feedback.
- Users can send feedback and change chat themes (like pastel, dark, or classic).
- There’s a fun “🪄 Surprise Me” feature that shows a random cool AI tool.


## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Database**: MySQL
- **NLP Tools**: spaCy, Enchant, NLTK

## How to Run

1. **Clone the repository** or download the project files.
2. Make sure Python and MySQL are installed.
3. Create a MySQL database named `assistaive` and import the `ai_tools` table.
4. Install Python dependencies:
   pip install flask mysql-connector-python spacy nltk pyenchant
5. Download language models:
   python -m spacy download en_core_web_sm
6. Run the app:
   python app.py
7. Open your browser and go to `http://localhost:5000`.

## Who Is It For?

This chatbot is for:
- Students
- Beginners
- Creators
- Anyone looking for the best AI tools to get tasks done faster

## Extras

- Admin access reveals extra features like viewing feedback and chats.
- Theme switcher, feedback modal, and user profile with total chat count.
- A growing database of 100+ real AI tools.
