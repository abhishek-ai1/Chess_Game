# Chess Game

A complete Python-based interactive chess application featuring a graphical user interface built with Tkinter and robust chess logic powered by the python-chess library.

## Overview

This project provides a fully functional, user-friendly chess game with:
- **Visual Chess Board**: Interactive 8x8 grid with color-coded squares
- **Piece Movement**: Click-to-select and click-to-move interface
- **Full Rule Enforcement**: Complete chess rules including castling, en passant, and pawn promotion
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Docker Support**: Containerized execution with X11 display forwarding

## Quick Start

### Local Execution (Recommended for First-Time Users)

```bash
cd chess_app
pip install -r requirements.txt
python src/main.py
```

### Docker Execution

**On Linux/Mac:**
```bash
cd chess_app
docker build -t python-chess-game .
docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix python-chess-game
```

**On Windows (with VcXsrv):**
```powershell
cd chess_app
docker build -t python-chess-game .
docker run -it --rm -e DISPLAY=host.docker.internal:0.0 python-chess-game
```

## Project Structure

```
Chess_Game/
├── LICENSE               # Project license
├── README.md             # This file
└── chess_app/            # Main application directory
    ├── Dockerfile        # Docker container configuration
    ├── requirements.txt  # Python dependencies
    ├── README.md         # Detailed chess_app documentation
    ├── src/
    │   ├── __init__.py
    │   └── main.py       # Main application (GUI + game logic)
    └── tests/
        └── __init__.py   # Test directory
```

## Prerequisites

### For Local Execution
- Python 3.8 or higher
- pip package manager
- Tkinter (included with Python on Windows/Mac; Linux: `sudo apt-get install python3-tk`)

### For Docker Execution
- Docker (installed and running)
- X11 display server:
  - **Linux/Mac**: Native X11 support
  - **Windows**: [VcXsrv](https://sourceforge.net/projects/vcxsrv/) or similar X server

## System Requirements

| Component | Requirement |
|-----------|-------------|
| **OS** | Windows, macOS, or Linux |
| **Python** | 3.8+ |
| **RAM** | 512 MB minimum |
| **Display** | 1024x1024 pixels minimum |
| **Docker** | 19.03+ (for containerized deployment) |

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/abhishek-ai1/Chess_Game.git
cd Chess_Game
```

### Step 2: Install Dependencies
```bash
cd chess_app
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python src/main.py
```

## Usage

### Starting a Game
The application launches with a standard chess starting position (white pieces at bottom).

### Making Moves
1. **Click** any of your pieces to select it
2. Gray circles appear on legal move destinations
3. **Click** any gray circle to move the piece
4. **Click** an empty square to deselect

### Game End
- The window title displays the result (checkmate, stalemate, etc.)
- Click pieces to review the final position

## Features

- ✅ Full chess rule implementation
- ✅ Visual move validation
- ✅ Automatic pawn promotion
- ✅ Game state tracking
- ✅ Cross-platform compatibility
- ✅ Dockerized deployment
- ✅ Intuitive GUI

## Dependencies

- **python-chess** (1.999): Chess game logic and rule enforcement
- **tkinter**: GUI framework (system package)
- **python** (3.8+): Core language

See `chess_app/requirements.txt` for the complete dependency list.

## Troubleshooting

### Application Won't Start

**"No module named 'tkinter'"**
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# macOS
brew install python-tk@3.x

# Windows
# Tkinter included in official Python installer
```

**"No module named 'chess'"**
```bash
pip install -r requirements.txt
```

### Docker Issues

**"No display name and no $DISPLAY environment variable"**
- Ensure X11 is properly forwarded
- Linux/Mac: Check `echo $DISPLAY`
- Windows: Verify VcXsrv is running

For detailed troubleshooting, see [chess_app/README.md](chess_app/README.md#troubleshooting).

## Development

### Code Structure
- `src/main.py`: Contains `ChessApp` class with GUI and game logic
- Uses `chess.Board()` for move validation
- Tkinter Canvas for rendering

### Running Tests
```bash
cd chess_app
python -m pytest tests/
```

## Platform Support

| Platform | Local | Docker |
|----------|:-----:|:------:|
| **Windows** | ✅ | ✅* |
| **macOS** | ✅ | ✅ |
| **Linux** | ✅ | ✅ |

*Windows Docker requires VcXsrv or similar X server

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Ready to play?** Start with:
```bash
cd chess_app && pip install -r requirements.txt && python src/main.py
```
