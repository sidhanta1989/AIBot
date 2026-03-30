# AIBot

A Python-based conversational AI chatbot with dual interface support: text-based and voice-enabled interactions.

## Project Description

AIBot is an intelligent conversational agent that leverages the ChatterBot framework to provide interactive dialogue capabilities. The project includes two main implementations:

1. **Text-Based Chatbot** (`chatbot.py`) - Command-line interface for text interactions
2. **Voice-Enabled Chatbot** (`chatbot_voice.py`) - Voice interaction with speech recognition and audio synthesis

The bot is trained on English language corpus data and responds dynamically to user queries with contextual responses. The voice variant includes audio output capabilities powered by text-to-speech technology.

## Tech Stack

- **Language**: Python 3.6+
- **Core Framework**: ChatterBot (conversational AI library)
- **Speech Recognition**: SpeechRecognition (Google Speech Recognition API)
- **Text-to-Speech**: gTTS (Google Text-to-Speech)
- **Audio Playback**: Pygame (mixer module)
- **Database**: SQLite (db.sqlite3)
- **Standard Library**: Python codec registry, collections (OrderedDict, Counter, deque, namedtuple), copy operations, serialization support via copyreg, distutils integration

## Prerequisites

- Python 3.6 or higher
- pip (Python package manager)
- Virtual environment (recommended)
- Microphone (for voice variant)
- Internet connection (for speech recognition and text-to-speech APIs)

## Installation and Setup

### 1. Clone or Download the Repository
```bash
cd AIBot
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Required Dependencies
```bash
pip install chatterbot
pip install SpeechRecognition
pip install gtts
pip install pygame
```

### 4. Prepare Training Data

The chatbot requires English language corpus data from the ChatterBot corpus. Download the corpus:
```bash
git clone https://github.com/gunthercox/chatterbot-corpus.git
```

Update the file paths in both `chatbot.py` and `chatbot_voice.py` to point to your local corpus directory:
```python
# Replace 'F:\chatbot\Chatterbot_corpus\chatterbot-corpus-master\chatterbot_corpus\data\english/'
# with your actual corpus path
```

## Usage

### Text-Based Chatbot

Run the text interface:
```bash
python chatbot.py
```

Interact with the bot by typing messages:
```
Please Ask Something: Hello
Desi_Thanos: Hello! How are you doing today?
Please Ask Something: What is AI?
Desi_Thanos: Artificial Intelligence is a fascinating field...
Please Ask Something: Bye
Desi_Thanos: Bye
```

Type "Bye" to exit the conversation.

### Voice-Enabled Chatbot

Run the voice interface:
```bash
python chatbot_voice.py
```

The bot will:
1. Listen for audio input via microphone
2. Convert speech to text using Google Speech Recognition
3. Process the query through the ChatterBot
4. Generate a response
5. Convert the response to audio using gTTS
6. Play the audio response through Pygame

Say "Bye" or "bye" to end the conversation.

## Architecture Overview

### Core Components

**chatbot.py** - Text-based implementation:
- Initializes ChatterBot instance with ListTrainer
- Loads training data from English corpus files in the specified directory
- Implements a simple while loop for continuous user interaction
- Handles exit condition when user types "Bye"
- Returns bot responses directly to console

**chatbot_voice.py** - Voice-enabled implementation:
- Extends the text chatbot with audio capabilities
- Uses `sr.Microphone()` from SpeechRecognition for audio input
- Integrates `sr.Recognizer.recognize_google()` for speech-to-text conversion
- Implements gTTS for text-to-speech synthesis
- Uses Pygame mixer for audio playback (loads and plays welcome.mp3)
- Maintains same training data loading mechanism as text variant
- Includes error handling for speech recognition failures

### Virtual Environment and Standard Library

The project includes a comprehensive Python virtual environment with the following key standard library modules:

**codecs.py** - Python Codec Registry:
- Provides encoding/decoding infrastructure for character set conversions
- Implements StreamReader, StreamWriter, and StreamReaderWriter classes for file handling
- Supports multiple encoding error handling strategies (strict, ignore, replace, xmlcharrefreplace, backslashreplace, namereplace, surrogateescape)
- Enables transparent encoding/decoding through the codecs.open() interface
- Used internally for text processing in the chatbot

**collections/__init__.py** - Specialized Container Datatypes:
- Implements specialized data structures including:
  - **OrderedDict**: Dictionary that remembers insertion order (useful for maintaining conversation history)
  - **Counter**: Dict subclass for counting hashable objects (can be used for frequency analysis of responses)
  - **deque**: Double-ended queue for fast appends and pops (useful for conversation queue management)
  - **namedtuple**: Factory function for creating tuple subclasses with named fields
  - **defaultdict**: Dict subclass with factory function for missing values
  - **ChainMap**: Dict-like class for creating single views of multiple mappings
  - **UserDict, UserList, UserString**: Wrapper classes for easier subclassing

**collections/abc.py** - Abstract Base Classes:
- Provides abstract base classes for container types
- Enables type checking and protocol validation for custom containers

**copy.py** - Object Copying Utilities:
- Implements shallow copy via `copy.copy()`
- Implements deep copy via `copy.deepcopy()`
- Handles recursive object copying and memoization
- Supports custom copying protocols through `__copy__()` and `__deepcopy__()` methods
- Essential for managing conversation state and cloning bot instances

**copyreg.py** - Pickle Extension Registry:
- Provides extensibility for the pickle serialization module
- Enables registration of custom pickling functions for extension types
- Implements pickle protocol support for serializing bot state and conversation history
- Includes helper functions like `__newobj__()` and `__newobj_ex__()` for protocol 2 and 4

**distutils/__init__.py** - Python Distribution Utilities:
- Virtualenv-specific distutils integration
- Patches build_ext for Windows library directory handling
- Customizes distutils.dist.Distribution for configuration file discovery
- Overrides sysconfig functions for correct path resolution in virtual environments
- Ensures proper compilation and installation of C extension modules

**encodings/__init__.py** - Encoding Codec Package:
- Standard Python encoding module registry
- Implements codec search and registration functions
- Supports encoding normalization and alias resolution
- Enables dynamic loading of codec modules for various character encodings
- Registers platform-specific codecs (e.g., MBCS on Windows)
- Provides the foundation for character set handling in the chatbot

### Training and Persistence

- **db.sqlite3**: SQLite database that stores learned patterns and conversation history
- **Training Data**: English corpus files from ChatterBot corpus repository
- **Trainer**: ListTrainer class for feeding conversation pairs to the bot

### Data Flow

1. Bot loads corpus files from the English language directory
2. Each file is read line-by-line and passed to the bot's train() method
3. ChatterBot builds an internal model of conversation patterns
4. User query is processed through the trained model
5. Response is generated based on learned patterns
6. (Voice variant) Response is converted to audio and played back

## Features

- **Conversational AI**: Leverages machine learning patterns from training corpus
- **Text Interface**: Simple command-line interaction with immediate responses
- **Voice Interface**: Full audio input/output support for hands-free interaction
- **Persistent Memory**: SQLite database maintains bot learning across sessions
- **Error Handling**: Voice variant includes exception handling for speech recognition failures
- **Multi-format Training**: Can train from multiple corpus files simultaneously
- **Codec Support**: Full character encoding support via Python codec registry
- **Data Structure Optimization**: Uses specialized collections for efficient conversation management
- **Object Serialization**: Supports pickling of bot state for persistence and sharing

## Configuration

**Important**: Before running the application, update the corpus path in both Python files:

```python
# Current hardcoded path (Windows example):
for files in os.listdir('F:\chatbot\Chatterbot_corpus\chatterbot-corpus-master\chatterbot_corpus\data\english/'):

# Should be changed to your actual corpus location:
for files in os.listdir('/path/to/your/chatterbot-corpus/chatterbot_corpus/data/english/'):
```

## Notes

- The bot name is configurable via `ChatBot('Bot')` parameter
- Response quality depends on the quality and comprehensiveness of training data
- Voice variant requires internet connectivity for Google APIs
- Audio output files (welcome.mp3) are generated in the working directory
- Bot personality is set to "Desi_Thanos" for console output identification
- The virtual environment includes comprehensive standard library modules for data processing, serialization, and packaging
- Codec and encoding support enables multi-language chatbot expansion in future versions

## Troubleshooting

- **Speech Recognition Issues**: Ensure microphone is connected and permissions are granted
- **API Errors**: Check internet connection for Google Speech Recognition and Text-to-Speech
- **Corpus Not Found**: Verify corpus path is correct and files exist
- **Audio Playback**: Ensure speakers are connected and Pygame mixer is initialized
- **Encoding Errors**: Check that the Python codec registry is properly initialized for your locale
- **Virtual Environment Issues**: Ensure distutils is properly configured for your Python version

## Future Enhancements

- Configuration file for customizable corpus paths
- Support for multiple languages using codec infrastructure
- Logging and analytics tracking using collections.Counter for statistics
- Custom response personality training
- REST API interface with serialization support
- Web-based UI alternative to command-line
- Advanced conversation history management using OrderedDict and deque
- State persistence using copyreg pickle extensions
