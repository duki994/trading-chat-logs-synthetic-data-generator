import tradingConfig
from tradeChatGenerator import TradingChatGenerator
import sys


num_entries = 5000
file_name_without_extension = "synthetic_trading_chats"

# sys.argv[1] is the path to the currently executing file/script
if len(sys.argv) >= 2:
    num_entries = int(sys.argv[1])
    if len(sys.argv) == 3:
        file_name = sys.argv[2]



file_name = f"{file_name_without_extension}_{num_entries}_entries.json"

tcg = TradingChatGenerator(tradingConfig.get_config())

chats = tcg.generate_trade_chat(num_entries)
tcg.save_as_json(chats, file_name)
