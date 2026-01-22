# Interactive Chess Game (Docker)

This is a Python-based interactive chess game using `tkinter` and `python-chess`, containerized with Docker.

## Project Structure
- `src/main.py`: Main game logic and UI.
- `tests/`: Directory for tests.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Container configuration.

## 1. Build the Image

Run this command in the `chess_app` directory:

```bash
docker build -t python-chess-game .
```

## 2. Run the Container

Running GUI applications from Docker requires forwarding the display to your host machine.

### For Windows (using WSL2 + VcXsrv)
1. **Install an X Server**: Download and install [VcXsrv](https://sourceforge.net/projects/vcxsrv/).
2. **Launch XLaunch** (VcXsrv): 
   - Select "Multiple windows".
   - **Important**: In "Extra settings", check **"Disable access control"**.
3. **Run Docker Command**:
   Run in PowerShell:
   ```powershell
   docker run -it --rm -e DISPLAY=host.docker.internal:0.0 -v /tmp/.X11-unix:/tmp/.X11-unix python-chess-game
   ```

### For Linux/Mac (with X11)
```bash
docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix python-chess-game
```

## 3. Run Locally (without Docker)
You can also run the game directly if you have Python installed:

```bash
pip install -r requirements.txt
python src/main.py
```
