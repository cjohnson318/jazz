import sys

import parse
import utils

if __name__ == '__main__':
    device = utils.init()

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'blue-in-green.txt'
    score = parse.lead_sheet(filename)
    
    utils.quit_listener()
    for chord in score:
        utils.play(chord, device)
