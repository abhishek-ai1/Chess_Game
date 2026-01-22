import tkinter as tk
import chess

# Constants
SQUARE_SIZE = 80
BOARD_SIZE = SQUARE_SIZE * 8
COLORS = ["#F0D9B5", "#B58863"]  # Light, Dark squares
HIGHLIGHT_COLOR = "#BACQ44" # greenish
SELECTED_COLOR = "#F6F669" # yellow

UNICODE_PIECES = {
    'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
    'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙'
}

class ChessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Chess (Tkinter)")
        self.canvas = tk.Canvas(root, width=BOARD_SIZE, height=BOARD_SIZE)
        self.canvas.pack()

        self.board = chess.Board()
        self.selected_square = None
        self.valid_moves = []

        self.draw_board()
        self.draw_pieces()

        self.canvas.bind("<Button-1>", self.on_click)

    def draw_board(self):
        """Draws the checkerboard pattern."""
        self.canvas.delete("square") # Clear previous highlights
        for row in range(8):
            for col in range(8):
                color = COLORS[(row + col) % 2]
                
                # Coordinates
                x1 = col * SQUARE_SIZE
                y1 = row * SQUARE_SIZE
                x2 = x1 + SQUARE_SIZE
                y2 = y1 + SQUARE_SIZE

                # Check for highlighting
                square_index = chess.square(col, 7 - row)
                
                if self.selected_square == square_index:
                    color = SELECTED_COLOR
                elif square_index in [move.to_square for move in self.valid_moves]:
                     # We can draw the square differently or add a marker later
                     # For now, let's keep the board clean, we'll draw move markers on top
                     pass

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="", tags="square")

        # Draw move validation markers (dots)
        for move in self.valid_moves:
             dest_sq = move.to_square
             col = chess.square_file(dest_sq)
             row = 7 - chess.square_rank(dest_sq)
             
             x_center = col * SQUARE_SIZE + SQUARE_SIZE // 2
             y_center = row * SQUARE_SIZE + SQUARE_SIZE // 2
             radius = SQUARE_SIZE // 6
             
             self.canvas.create_oval(x_center - radius, y_center - radius, 
                                     x_center + radius, y_center + radius, 
                                     fill="gray", outline="", tags="marker")

    def draw_pieces(self):
        """Draws the pieces on the board."""
        self.canvas.delete("piece")
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                col = chess.square_file(square)
                row = 7 - chess.square_rank(square)
                
                x_center = col * SQUARE_SIZE + SQUARE_SIZE // 2
                y_center = row * SQUARE_SIZE + SQUARE_SIZE // 2
                
                symbol = UNICODE_PIECES[piece.symbol()]
                
                # Color logic: Unicode characters are monochrome usually. 
                # We can explicitly set color.
                # Standard convention: White pieces black outline? 
                # Actually, standard terminal chess just prints them.
                # Tkinter Text supports color.
                # Let's use simple Black for all and rely on the glyphs.
                # BUT: The glyphs might not be distinct enough on dark background.
                # Let's try: White pieces -> White text with Black outline (font trick?)
                # Tkinter canvas text doesn't support outline easily.
                # Let's stick to Black text for now, maybe use a larger bold font.
                
                self.canvas.create_text(x_center, y_center, text=symbol, 
                                        font=("Segoe UI Symbol", 48), tags="piece", fill="black")

    def on_click(self, event):
        col = event.x // SQUARE_SIZE
        row = event.y // SQUARE_SIZE
        
        if not (0 <= col < 8 and 0 <= row < 8):
            return

        clicked_square = chess.square(col, 7 - row)

        if self.selected_square is None:
            # Select a piece
            piece = self.board.piece_at(clicked_square)
            if piece and piece.color == self.board.turn:
                self.selected_square = clicked_square
                self.valid_moves = [m for m in self.board.legal_moves if m.from_square == clicked_square]
                self.redraw()
        else:
            # Move or Deselect
            move = chess.Move(self.selected_square, clicked_square)
            
            # Check for promotion (auto-queen)
            move_prom = chess.Move(self.selected_square, clicked_square, promotion=chess.QUEEN)
            
            target_move = None
            if move in self.valid_moves:
                target_move = move
            elif move_prom in self.valid_moves:
                target_move = move_prom

            if target_move:
                self.board.push(target_move)
                if self.board.is_game_over():
                    print("Game Over:", self.board.result())
                    self.root.title(f"Game Over: {self.board.result()}")
                
                self.selected_square = None
                self.valid_moves = []
            else:
                # If clicked valid piece of same color, change selection
                piece = self.board.piece_at(clicked_square)
                if piece and piece.color == self.board.turn:
                    self.selected_square = clicked_square
                    self.valid_moves = [m for m in self.board.legal_moves if m.from_square == clicked_square]
                else:
                    self.selected_square = None
                    self.valid_moves = []
            
            self.redraw()

    def redraw(self):
        self.canvas.delete("all")
        self.draw_board()
        self.draw_pieces()

if __name__ == "__main__":
    root = tk.Tk()
    # Center window
    root.geometry(f"{BOARD_SIZE}x{BOARD_SIZE}")
    root.resizable(False, False)
    
    app = ChessApp(root)
    root.mainloop()
