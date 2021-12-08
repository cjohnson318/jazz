import parse
import utils

if __name__ == '__main__':
    device = utils.init()

    score = parse.lead_sheet('autumn-leaves.txt')
    
    utils.quit_listener()
    for chord in score:
        utils.play(chord, device)
