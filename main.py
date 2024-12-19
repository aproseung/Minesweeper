import screen
import play

if __name__ == '__main__':
    _screen = screen.ScreenHandler()
    _screen.create_board()
    print(f"ROI: {_screen.ROI}")

    _player = play.Player()
    x, y = _screen.cvt_board2screen(2, 3)
    _player.click(x, y)
    z, w = _screen.cvt_board2screen(2, 4)
    _player.click(z, w)