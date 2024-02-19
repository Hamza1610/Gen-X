from engine import Xyrox
from google_config import Gemini


engine = Xyrox()
def execution_info(result):
    """Give information status of command execution

    Args:
        result (str): retult content
    """
    engine.make_speech(result)
 

def risk_info(risk):
        """Return risk detail
        Args:
            rist (str): risk content
        `"""
        risk_info = Gemini(mode='gen', text=f'Tell me the risk of executing {risk} in one or two sentence only.', google_api_key=os.getenv(key='GOOGLE_API_KEY'))
        engine.make_speech(risk_info)