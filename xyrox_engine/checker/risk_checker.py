from xyrox_engine.engine import Xyrox

engine = Xyrox()

def check_risk():
    """
        Checks command risk
    """
    print('Command could be potentially risky. Exercise caution and double-check!')
    engine.make_speech('The command you want to execute is potentially risky! should I go ahead and execute?')

    speech = engine.listen_to_speech()
    speech = speech.lower()
    return speech
